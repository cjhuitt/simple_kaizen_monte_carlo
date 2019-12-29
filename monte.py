import collections
import random
from argparse import ArgumentParser
from statistics import stdev


class Run:
    def __init__(self):
        self.extra_years = random.choice([0, 1, 2, 3, 4])
        self.weeks = random.choice([46, 47, 48, 49, 50, 51, 52])
        self.hours = random.triangular(30.0, 80.0, 40.0)
        self.improvement = random.triangular(0.005, 0.02, 0.01)
        self.margin = random.triangular(0.5, 1.0, 0.8)
        self.discount = random.choice([1.0, 0.9, 0.8, 0.7, 0.6])
        self.first_year = self.weeks * self.hours * self.improvement * self.margin
        self.yearly_discount = self.first_year * self.discount
        self.total = self.first_year
        for i in range(0, self.extra_years):
            self.total += max(0.0, self.first_year - (self.yearly_discount * i))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("runs", type=int, default=5000, nargs="?")
    args = parser.parse_args()
    results = {}
    raw = []
    avg = 0.0
    for i in range(0,args.runs):
        run = Run()
        total = round(run.total)
        raw.append(total)
        avg += total / args.runs
        if total in results:
            results[total] = results[total] + 1
        else:
            results[total] = 1

    print("total hours, ratio")
    #for hours, times in sorted(results):
    for hours, times in collections.OrderedDict(sorted(results.items())).items():
        #print(result)
        print(hours, ",", times/args.runs)

    print()
    print("avg:", avg)
    print("stdev:", stdev(raw))
