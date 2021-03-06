from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, views, exceptions
from rest_framework.response import Response

from core import models
from core.models.base import GameStatus
from service import serializers
from service.permissions import IsAuthenticated


# NOTE this could possibly be replaced by using options
def get_game_filter_choices():
    return {
        'game_statuses': models.base.GameStatus.CHOICES,
        'nation_choice_modes': models.base.NationChoiceMode.CHOICES,
        'deadlines': models.base.DeadlineFrequency.CHOICES,
        'variants': [(v.id, str(v)) for v in models.Variant.objects.all()],
    }


class GameFilterChoicesView(views.APIView):

    def get(self, request, format=None):
        return Response(get_game_filter_choices())


class BaseMixin:

    game_key = 'game'

    def get_game(self):
        return get_object_or_404(
            models.Game.objects,
            id=self.kwargs[self.game_key],
            status=GameStatus.ACTIVE,
            participants=self.request.user.id,
        )

    def get_user_nation_state(self):
        game = self.get_game()
        return get_object_or_404(
            models.NationState.objects,
            turn=game.get_current_turn(),
            user=self.request.user.id,
        )


class ListGames(generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = [
        'name',
        'created_by__username'
    ]
    filterset_fields = [
        'variant',
        'status',
        'num_players',
        'nation_choice_mode',
        'order_deadline',
        'retreat_deadline',
        'build_deadline',
    ]
    ordering_fields = [
        'created_at',
        'initialized_at'
    ]


class CreateGameView(generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.CreateGameSerializer

    def create(self, request, *args, **kwargs):
        defaults = {'variant': 1, 'num_players': 7}
        request.data.update(defaults)
        return super().create(request, *args, **kwargs)


class GameStateView(BaseMixin, generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GameStateSerializer
    queryset = models.Game.objects.all()
    game_key = 'pk'


class ToggleJoinGame(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.GameSerializer
    queryset = models.Game.objects.all()

    def check_object_permissions(self, request, obj):
        if request.user not in obj.participants.all():
            if obj.participants.count() >= obj.num_players:
                raise exceptions.PermissionDenied(
                    detail='Game is already full.'
                )
            if obj.status != GameStatus.PENDING:
                raise exceptions.PermissionDenied(
                    detail='Game is not pending.'
                )


class CreateOrderView(BaseMixin, generics.CreateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['nation_state'] = self.get_user_nation_state()
        return context

    def perform_create(self, serializer):
        """
        Delete existing order before creating new order.
        """
        models.Order.objects.filter(
            source=serializer.validated_data['source'],
            turn=serializer.validated_data['turn'],
            nation=serializer.validated_data['nation'],
        ).delete()
        super().perform_create(serializer)


class ListOrdersView(BaseMixin, generics.ListAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        game = get_object_or_404(
            models.Game.objects,
            id=self.kwargs['game'],
        )
        user_nation_state = models.NationState.objects.filter(
            turn=game.get_current_turn(),
            user=self.request.user.id,
        ).first()
        if not user_nation_state:
            return models.Order.objects.none()
        return models.Order.objects.filter(
            turn=user_nation_state.turn,
            nation=user_nation_state.nation,
        )


class RetrievePrivateNationStateView(BaseMixin, generics.RetrieveAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PrivateNationStateSerializer

    def get_object(self):
        game = get_object_or_404(
            models.Game.objects,
            id=self.kwargs['game'],
        )
        return models.NationState.objects.filter(
            turn=game.get_current_turn(),
            user=self.request.user.id,
        ).first()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if not instance:
            return Response({})
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class DestroyOrderView(BaseMixin, generics.DestroyAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.OrderSerializer
    queryset = models.Order.objects.all()

    def check_object_permissions(self, request, obj):
        user_nation_state = self.get_user_nation_state()
        if obj.nation != user_nation_state.nation:
            raise exceptions.PermissionDenied(
                detail='Order does not belong to this user.'
            )


class ToggleFinalizeOrdersView(generics.UpdateAPIView):

    permission_classes = [IsAuthenticated]
    serializer_class = serializers.PublicNationStateSerializer
    queryset = models.NationState.objects.filter(
        turn__game__status=GameStatus.ACTIVE
    )

    def check_object_permissions(self, request, obj):
        if request.user != obj.user:
            raise exceptions.PermissionDenied(
                detail='Cannot finalize orders for other nation.'
            )
