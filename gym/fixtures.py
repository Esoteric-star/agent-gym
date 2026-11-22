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
    if n % 2 == 1:
        t = t + [None]
        n += 1
    rounds = []
    for _ in range(n - 1):
        round_matches = []
        for i in range(n // 2):
            home = t[i]
            away = t[n - 1 - i]
            if home is not None and away is not None:
                round_matches.append((home, away))
        rounds.append(round_matches)
        t = [t[0]] + t[-1:] + t[1:-1]
    return rounds
