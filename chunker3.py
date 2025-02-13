import pandas as pd
import numpy as np

def chunker(df, size_from: int, size_to: int):
    dt = df["dt"].values
    split_indexes = np.concatenate(([0], np.nonzero(np.diff(dt))[0] + 1, [len(dt)]))


    cur_size = 0
    chunk_start = 0
    for i in range(1, len(split_indexes)):
        group_start = split_indexes[i-1]
        group_end = split_indexes[i]
        group_size = group_end - group_start
        cur_size += group_size

        if cur_size < size_from:
            continue

        if cur_size > size_to:
            yield df[chunk_start:group_start]
            chunk_start = group_start
            cur_size = group_size


    yield df[chunk_start:]


chunk_size_from = int(input())
chunk_size_to = int(input())

dfs = pd.date_range(
    "2023-01-01 00:00:00",
    "2023-01-01 00:00:06",
    freq="s"
)
df = pd.DataFrame({"dt": dfs.repeat(9)})


for chunk in chunker(df, chunk_size_from, chunk_size_to):
    print(chunk)