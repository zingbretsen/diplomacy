from core.adjudicator.exceptions import IllegalOrderException

UNRESOLVED = 'unresolved'
PATH = 'path'
NO_PATH = 'no path'

SUCCEEDS = 'succeeds'
FAILS = 'fails'
MOVES = 'moves'
GIVEN = 'given'

LEGAL = 'legal'
ILLEGAL = 'illegal'


class ConvoyChain:
    """
    Represents a chain of one or more fleet paths which are attempting to
    convoy an army from a source to a destination.
    """

    def __init__(self, fleets):
        self.fleets = fleets
        self.result = UNRESOLVED


class Decision:

    def __call__(self):
        """
        Return the result of the decision if resolved. Otherwise attempt
        resolve the decision and then return the result
        """
        if self.result != UNRESOLVED:
            return self.result
        self.result = self._resolve()
        return self.result


# MoveDecision base class
class MoveLegal(Decision):
    """
    For each piece ordered to move, the decision whether the move is legal.
    """

    def __init__(self, move):
        self.move = move
        self.result = UNRESOLVED
        self.error_code = None

    def _resolve(self):
        # TODO unittest
        piece = self.move.source.piece

        if piece.nation != self.move.nation:
            self.error_code = 'M001'
            return ILLEGAL

        if not self.move.via_convoy:
            if not self.move.source.adjacent_to(self.move.target):
                self.error_code = 'M002'
                return ILLEGAL

        if not self.move.source.piece.can_reach(self.move.target):
            self.error_code = 'M003'
            return ILLEGAL
        return LEGAL


class StrengthDecision(Decision):

    def _resolve(self):
        if self._minimum() == self._maximum():
            return self._minimum()
        return UNRESOLVED


class Move(Decision):
    """
    For each piece ordered to move, the decision whether the move is
    successful.
    """
    def __init__(self, move):
        self.move = move
        self.result = UNRESOLVED

    def _resolve(self):
        return UNRESOLVED


class Path(Decision):
    """
    For each piece ordered to move, the decision whether there is a path from
    the source to the destination. This decision will result in `path` or
    `no_path`. When the move is without any convoy, the decision always results
    in 'path'.
    """
    def __init__(self, move):
        self.move = move
        self.result = UNRESOLVED

    def _resolve(self):

        if not self.move.via_convoy:
            return PATH

        if not self.move.convoy_chains:
            return NO_PATH

        if any([c.result == SUCCEEDS for c in self.move.convoy_chains]):
            return PATH

        if all([c.result == FAILS for c in self.move.convoy_chains]):
            return NO_PATH

        return UNRESOLVED


class PreventStrength(Decision):
    """
    A numerical decision for each unit ordered to move. It is the strength to
    prevent other units to move to the area where it is ordered to move. A
    decision that results in a value equal or greater than zero.
    """
    def __init__(self, move):
        self.move = move
        self.result = UNRESOLVED

    def _minimum(self):
        if self.move.path_decision() in [NO_PATH, UNRESOLVED]:
            return 0
        if self.move.is_head_to_head():
            opposing_move = self.move.target.piece.move
            if opposing_move.move_decision() in [MOVES, UNRESOLVED]:
                return 0
        return 1 + len(self.move.move_support(GIVEN))

    def _maximum(self):
        if self.move.path_decision() == NO_PATH:
            return 0
        if self.move.is_head_to_head():
            opposing_move = self.move.target.piece.move
            if opposing_move.move_decision() == MOVES:
                return 0
        return 1 + len(self.move.move_support(GIVEN, UNRESOLVED))


class DefendStrength(Decision):
    """
    For each piece ordered to move in a head to head battle, the strength to
    defend its own territory from the other piece of the head to head battle. A
    decision that results in a value equal or greater than zero.
    """
    def __init__(self, move):
        self.move = move
        self.result = UNRESOLVED

    def _minimum(self):
        return 1 + len(self.move.move_support(GIVEN))

    def _maximum(self):
        return 1 + len(self.move.move_support(GIVEN, UNRESOLVED))


class HoldStrength(Decision):
    """
    For each territory on the board the strength to prevent that other pieces
    move to that territory. A decision that results in a value equal or greater
    than zero.
    """
    def __init__(self, territory):
        self.territory = territory
        self.result = UNRESOLVED

    def _minimum(self):
        piece = self.territory.piece

        if not piece:
            return 0

        if piece.order.is_move:
            if piece.order.move_decision() == FAILS:
                return 1
            return 0

        return 1 + len(piece.order.hold_support(GIVEN))

    def _maximum(self):
        piece = self.territory.piece

        if not piece:
            return 0

        if piece.order.is_move:
            if piece.order.move_decision() == MOVES:
                return 0
            return 1

        return 1 + len(piece.order.hold_support(GIVEN, UNRESOLVED))
