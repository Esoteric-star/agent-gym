"""Command line entry point: python3 -m gym.cli table results.csv"""
import argparse
import csv
import sys

from gym.league import build_table


def read_results(path):
    with open(path, newline="") as f:
        return [(r["home"], int(r["home_goals"]), int(r["away_goals"]), r["away"])
                for r in csv.DictReader(f)]


def render(rows):
    lines = [f"{'Pos':>3} {'Team':<20} {'P':>2} {'GD':>4} {'Pts':>3}"]
    for i, r in enumerate(rows, 1):
        lines.append(f"{i:>3} {r['team']:<20} {r['played']:>2} {r['gd']:>4} {r['points']:>3}")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(prog="gym")
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("table", help="print a league table")
    t.add_argument("csv")
    args = p.parse_args(argv)
    rows = build_table(read_results(args.csv))
    print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
