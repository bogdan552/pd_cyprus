import pandas as pd

def chunker(df, size_from: int):
    start_index = 0
    cur_size = 0
    for i in range(0, len(df)):

        if cur_size < size_from:
            cur_size += 1
            continue

        if df["dt"].iloc[i] != df["dt"].iloc[i-1]:
            yield df[start_index:i]
            start_index = i
            cur_size = 0

        cur_size += 1
    yield df[start_index:]


chunk_size_from = int(input())
chunk_size_to = int(input())

dfs = pd.date_range(
    "2023-01-01 00:00:00",
    "2023-01-01 00:00:06",
    freq="s"
)
df = pd.DataFrame({"dt": dfs.repeat(9)})


for chunk in chunker(df, chunk_size_from):
    print(chunk)