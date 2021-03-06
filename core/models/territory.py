from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from core.models.base import PerTurnModel, PieceType, \
    TerritoryType


class Territory(models.Model):
    """
    Represents an area in the game map that can be occupied.
    """
    name = models.CharField(
        max_length=50,
        null=False,
    )
    controlled_by_initial = models.ForeignKey(
        'Nation',
        on_delete=models.CASCADE,
        null=True,
        related_name='initially_controlled_territories',
    )
    variant = models.ForeignKey(
        'Variant',
        null=False,
        on_delete=models.CASCADE,
        related_name='territories',
    )
    nationality = models.ForeignKey(
        'Nation',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='national_territories',
    )
    neighbours = models.ManyToManyField(
        'self',
        symmetrical=True,
        blank=True,
    )
    shared_coasts = models.ManyToManyField(
        'self',
        symmetrical=True,
    )
    type = models.CharField(
        max_length=10,
        choices=TerritoryType.CHOICES,
        blank=False,
        null=False
    )
    supply_center = models.BooleanField(
        default=False,
    )
    initial_piece_type = models.CharField(
        max_length=50,
        null=True,
        choices=PieceType.CHOICES,
    )

    def __str__(self):
        return self.name

    def state(self, turn):
        return self.territory_states.get(turn=turn)

    def adjacent_to(self, territory):
        return territory in self.neighbours.all()

    def shares_coast_with(self, territory):
        return territory in self.shared_coasts.all()

    def get_piece(self):
        """
        Return the piece if it exists in the territory. If no piece exists
        in the territory, return `None`. If there is are two pieces in a
        territory, gets the non-retreating piece.

        Returns:
            * `PieceState` or `None` if there is no piece in the territory.
        """
        try:
            return self.pieces.get(must_retreat=False)
        except ObjectDoesNotExist:
            return None

    @property
    def is_coastal(self):
        return self.type == TerritoryType.COASTAL

    @property
    def is_sea(self):
        return self.type == TerritoryType.SEA

    @property
    def is_inland(self):
        return self.type == TerritoryType.INLAND

    @property
    def is_complex(self):
        return self.named_coasts.all().exists()


class TerritoryState(PerTurnModel):
    """
    A through model between `Turn` and `Territory`. Represents the state of
    a territory in a given turn.
    """
    territory = models.ForeignKey(
        'Territory',
        null=False,
        related_name='territory_states',
        on_delete=models.CASCADE,
    )
    controlled_by = models.ForeignKey(
        'Nation',
        on_delete=models.CASCADE,
        null=True,
        related_name='controlled_territories',
    )
    contested = models.BooleanField(
        default=False,
    )
    bounce_occurred = models.BooleanField(
        default=False,
    )

    def to_dict(self):
        territory = self.territory
        return {
            '_id': territory.id,
            'type': territory.type,
            'name': territory.name,
            'neighbour_ids': list(territory.neighbours.all().values_list('pk', flat=True)),
            'shared_coast_ids': list(territory.shared_coasts.all().values_list('pk', flat=True)),
            'supply_center': territory.supply_center,
            'nationality': getattr(territory.nationality, 'id', None),
            'controlled_by': getattr(territory.nationality, 'id', None),
            'named_coasts': [n.to_dict() for n in territory.named_coasts.all()],
            'contested': self.contested,
        }
