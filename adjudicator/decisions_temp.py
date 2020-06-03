from .decisions.attack_strength import AttackStrength


class Outcomes:
    UNRESOLVED = 'unresolved'
    PATH = 'path'
    NO_PATH = 'no path'
    SUCCEEDS = 'succeeds'
    FAILS = 'fails'
    MOVES = 'moves'
    GIVEN = 'given'
    CUT = 'cut'
    LEGAL = 'legal'
    ILLEGAL = 'illegal'
    DISLODGED = 'dislodged'
    SUSTAINS = 'sustains'


def hold_support(order, *args):
    """
    Support orders which are supporting the given order to hold.

    Returns:
        * A list of `Support` instances.
    """
    legal_decisions = [Outcomes.LEGAL]
    return [s for s in order.hold_support_orders if
            s.support_decision in args and s.legal_decision in legal_decisions]


def resolve_convoy_swap(order_a, order_b):
    """
    Two orders which are both traveling by convoy can swap places.
    TODO finish docstring
    """
    orders = [order_a, order_b]
    outcomes = [resolve_single_convoy_swap(o) for o in orders]

    if all([o == Outcomes.MOVES for o in outcomes]):
        [o.set_move_decision(Outcomes.MOVES) for o in orders]

    if any([o == Outcomes.FAILS for o in outcomes]):
        [o.set_move_decision(Outcomes.FAILS) for o in orders]


def resolve_single_convoy_swap(order):
    min_attack_strength, max_attack_strength = AttackStrength(order)()

    other_attacking_pieces = order.target.other_attacking_pieces(order.piece)
    other_pieces_max_prevent = max([p.order.prevent_strength_decision()[1] for p in other_attacking_pieces], default=0)
    other_pieces_min_prevent = min([p.order.prevent_strength_decision()[0] for p in other_attacking_pieces], default=0)

    if other_attacking_pieces:
        if min_attack_strength > other_pieces_max_prevent:
            return Outcomes.MOVES
    else:
        return Outcomes.MOVES

    if other_attacking_pieces:
        if max_attack_strength <= other_pieces_min_prevent:
            return Outcomes.FAILS

    return Outcomes.UNRESOLVED