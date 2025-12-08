import operator
from collections import Counter
from functools import reduce
from pathlib import Path

import polars as pl


class DSU:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))

    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        self.parents[self.find(i)] = self.find(j)

    def get_parents(self):
        return [self.find(i) for i in range(self.n)]


def part1(input_file, limit_join: int, top_k: int):
    with open(input_file, "r") as f:
        data = pl.scan_csv(
            f, separator=",", has_header=False, new_columns=["x", "y", "z"]
        ).with_row_index(name="c")

        df = (
            data.join(data, how="cross", suffix="2")
            .filter(pl.col("c") > pl.col("c2"))
            .with_columns(
                (
                    (pl.col("x") - pl.col("x2")) ** 2
                    + (pl.col("y") - pl.col("y2")) ** 2
                    + (pl.col("z") - pl.col("z2")) ** 2
                ).alias("d")
            )
            .sort("d")
            .head(limit_join)
            .collect()
        )

        dsu = DSU(data.collect().height)

        for c, c2 in df.select("c", "c2").iter_rows():
            dsu.union(c, c2)

        parents = dsu.get_parents()

        top_k_cluster = sorted((v for k, v in Counter(parents).items()), reverse=True)[
            :top_k
        ]
        print(reduce(operator.mul, top_k_cluster))


class DSUV2:
    def __init__(self, n):
        self.n = n
        self.parents = list(range(n))
        self.groups = n

    def find(self, i):
        if self.parents[i] == i:
            return i
        else:
            self.parents[i] = self.find(self.parents[i])
            return self.parents[i]

    def union(self, i, j):
        if self.find(i) == self.find(j):
            return False
        self.parents[self.find(i)] = self.find(j)
        self.groups -= 1
        return self.groups == 1

    def get_parents(self):
        return [self.find(i) for i in range(self.n)]


def part2(input_file):
    with open(input_file, "r") as f:
        data = pl.scan_csv(
            f, separator=",", has_header=False, new_columns=["x", "y", "z"]
        ).with_row_index(name="c")

        df = (
            data.join(data, how="cross", suffix="2")
            .filter(pl.col("c") > pl.col("c2"))
            .with_columns(
                (
                    (pl.col("x") - pl.col("x2")) ** 2
                    + (pl.col("y") - pl.col("y2")) ** 2
                    + (pl.col("z") - pl.col("z2")) ** 2
                ).alias("d")
            )
            .sort("d")
            .collect()
        )

        dsu = DSUV2(data.collect().height)

        for c, c2, x, x2 in df.select("c", "c2", "x", "x2").iter_rows():
            if dsu.union(c, c2):
                print(x * x2)
                return


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file, 10, 3)
    part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file, 1000, 3)
    part2(input_file)
