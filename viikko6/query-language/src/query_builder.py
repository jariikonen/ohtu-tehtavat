from copy import deepcopy
from matchers import (
    And, PlaysIn, HasAtLeast, HasFewerThan, Or
)


class QBAnd(And):
    def __init__(self, *matchers):
        self._matchers = list(matchers)

    def __str__(self):
        return f"QBAnd({self._matchers})"

    def add_matcher(self, matcher):
        self._matchers.append(matcher)
        return self


class QBOr(Or):
    def __init__(self, *matchers):
        self._matchers = list(matchers)

    def __str__(self):
        return f"QBOr({self._matchers})"


class QueryBuilder:
    def __init__(self, matcher=None):
        if not matcher:
            matcher = QBAnd()
        self._matcher = matcher

    def __str__(self):
        return f"QueryBuilder({self._matcher})"

    def oneOf(self, *matchers):
        return QueryBuilder(QBOr(*matchers))

    def playsIn(self, team):
        matcher = deepcopy(self._matcher)
        return QueryBuilder(matcher.add_matcher(PlaysIn(team)))

    def hasAtLeast(self, value, attr):
        matcher = deepcopy(self._matcher)
        return QueryBuilder(matcher.add_matcher(HasAtLeast(value, attr)))

    def hasFewerThan(self, value, attr):
        matcher = deepcopy(self._matcher)
        return QueryBuilder(matcher.add_matcher(HasFewerThan(value, attr)))

    def build(self):
        return self._matcher
