from pathlib import Path

import matplotlib.pyplot as plt
import polars as pl


def reader(lines: list[str]):
    return [list(map(int, line.strip().split(","))) for line in lines]


def fin_max_area(data, ax=None):
    n = len(data)
    mi, mj = 0, 0
    max_area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = abs((data[i][0] - data[j][0] + 1) * (data[i][1] - data[j][1] + 1))
            if area > max_area:
                max_area = area
                mi, mj = i, j

    if ax:
        print(ax)
        ax.scatter([data[mi][0], data[mj][0]], [data[mi][1], data[mj][1]])
    print(max_area)
    return max_area


def part1(input_file):
    with open(input_file, "r") as f:
        data = reader(f.readlines())
        fin_max_area(data)


def sercher(df: pl.DataFrame, singularity: pl.DataFrame):
    dfs = (
        df.join(singularity, how="cross", suffix="_s")
        .with_columns(
            (
                ((pl.col("x") - pl.col("x_s")).abs() + 1)
                * ((pl.col("y") - pl.col("y_s")).abs() + 1)
            ).alias("a")
        )
        .with_row_index(name="idx")
        .join(df, how="cross", suffix="_a")
    )
    max_area = 0
    x, y = 0, 0
    for (c,), df in dfs.group_by("idx"):
        df = df.with_columns(
            pl.min_horizontal(pl.col("x"), pl.col("x_s")).alias("l"),
            pl.max_horizontal(pl.col("x"), pl.col("x_s")).alias("r"),
            pl.min_horizontal(pl.col("y"), pl.col("y_s")).alias("b"),
            pl.max_horizontal(pl.col("y"), pl.col("y_s")).alias("h"),
        )
        df_inner = df.filter(
            (pl.col("x_a").is_between(pl.col("l"), pl.col("r"), "none"))
            & (pl.col("y_a").is_between(pl.col("b"), pl.col("h"), "none"))
        )
        if df_inner.height == 0:
            area = df.get_column("a")[0]
            if area > max_area:
                max_area = area
                x = df.get_column("x")[0]
                y = df.get_column("y")[0]

    return max_area, x, y


def part2(input_file: Path):
    with open(input_file, "r") as f:
        df = pl.read_csv(f, has_header=False, new_columns=["x", "y"])
        mean_x = df.get_column("x").mean()
        mean_y = df.get_column("y").mean()
        df = df.with_columns(
            ((pl.col("x") - mean_x) ** 2 + (pl.col("y") - mean_y) ** 2).alias("r2")
        )
        singularities = df.sort("r2").head(2).sort("y")

        top_him_y = singularities.filter(pl.col("y") == pl.col("y").max())
        bot_him_y = singularities.filter(pl.col("y") == pl.col("y").min())

        top_him = df.filter(pl.col("y") >= top_him_y.get_column("y")[0])
        bot_him = df.filter(pl.col("y") <= bot_him_y.get_column("y")[0])

        tm, tx, ty = sercher(top_him, top_him_y)
        bm, bx, by = sercher(bot_him, bot_him_y)

        result = max(tm, bm)
        print(f"{result=}")

        fig, ax = plt.subplots()

        ax.plot(top_him["x"], top_him["y"], label="top")
        ax.scatter(tx, ty)
        ax.plot(bot_him["x"], bot_him["y"], label="bot")
        ax.scatter(bx, by)
        ax.legend()

        plt.savefig(input_file.with_suffix(".png"), dpi=400)
        plt.clf()
        plt.cla()


if __name__ == "__main__":
    print("Test Case")
    input_file = Path(__file__).parent / "input.test.txt"
    part1(input_file)
    # Today part 2 is customized for result case
    # part2(input_file)

    print("\n\nResult")
    input_file = Path(__file__).parent / "input.txt"
    part1(input_file)
    part2(input_file)
