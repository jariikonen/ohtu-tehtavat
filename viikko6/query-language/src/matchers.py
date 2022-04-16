class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def __repr__(self):
        return f"And({self._matchers})"
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def __repr__(self):
        return f"PlayesIn({self._team})"

    def matches(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def __repr__(self):
        return f"HasAtLeast({self._value, self._attr})"

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def __repr__(self):
        return f"All({self._matchers})"

    def matches(self, player):
        if player:
            return True


class Not:
    def __init__(self, matcher):
        self._matcher = matcher

    def __repr__(self):
        return f"Not({self._matcher})"

    def matches(self, player):
        if self._matcher.matches(player):
            return False
        else:
            return True


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def __repr__(self):
        return f"HasFewerThan({self._value, self._attr})"

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def __repr__(self):
        return f"Or({self._matchers})"

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True
        return False
