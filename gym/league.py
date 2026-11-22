"""Football league table."""


def build_table(results):
    """Build a league table from match results.

    `results` is a list of (home, home_goals, away_goals, away) tuples.
    Win = 3 points, draw = 1, loss = 0.

    Return a list of dicts with keys: team, played, won, drawn, lost,
    gf, ga, gd, points; sorted by points desc, then goal difference desc,
    then goals for desc, then team name ascending.
    """
    table = {}

    def row(team):
        return table.setdefault(team, {"team": team, "played": 0, "won": 0,
                                       "drawn": 0, "lost": 0, "gf": 0,
                                       "ga": 0, "gd": 0, "points": 0})

    for home, hg, ag, away in results:
        h, a = row(home), row(away)
        for r, f, against in ((h, hg, ag), (a, ag, hg)):
            r["played"] += 1
            r["gf"] += f
            r["ga"] += against
            r["gd"] = r["gf"] - r["ga"]
            if f > against:
                r["won"] += 1
                r["points"] += 3
            elif f == against:
                r["drawn"] += 1
                r["points"] += 1
            else:
                r["lost"] += 1
    return sorted(table.values(), key=lambda r: r["points"], reverse=True)
