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
    lines = [f"{'Pos':>3} {'Team':<20} {'P':>2} {'GD':>4} {'Pts':>3} {'Form':>5}"]
    for i, r in enumerate(rows, 1):
        lines.append(f"{i:>3} {r['team']:<20} {r['played']:>2} {r['gd']:>4} {r['points']:>3} {r['form']:>5}")
    return "\n".join(lines)


def main(argv=None):
    p = argparse.ArgumentParser(prog="gym")
    sub = p.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("table", help="print a league table")
    t.add_argument("csv")
    t.add_argument("--top", type=int, required=False, help="print only top N teams")
    args = p.parse_args(argv)
    rows = build_table(read_results(args.csv))
    if args.top is not None and args.top < 1:
        p.error("--top must be >= 1")
    if args.top is not None:
        rows = rows[:args.top]
    print(render(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
