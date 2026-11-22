"""Round-robin fixture generator."""


def round_robin(teams):
    """Return a single round-robin schedule as a list of rounds.

    Each round is a list of (home, away) tuples. Every pair of teams must meet
    exactly once across the schedule, and no team may appear twice in a round.
    With an even number of teams there are n - 1 rounds; with an odd number
    there are n rounds and one team sits out (has a bye) each round. Byes are
    not listed. Fewer than 2 teams returns [].
    """
    t = list(teams)
    n = len(t)
    if n < 2:
        return []
    rounds = []
    for _ in range(n - 1):
        rounds.append([(t[i], t[n - 1 - i]) for i in range(n // 2)])
        t = [t[-1]] + t[:-1]
    return rounds
