import pandas as pd

def chunker(df, size_from: int, size_to: int):
    start_index = 0
    sub_size_index = 0
    cur_size = 0
    sub_size = 0
    for i in range(0, len(df)):

        if cur_size < size_from:
            cur_size += 1
            continue
        if sub_size > 0:
            sub_size += 1

        if df["dt"].iloc[i] != df["dt"].iloc[i-1]:
            if sub_size == 0:
                sub_size_index = i
            sub_size += 1

            if sub_size + cur_size >= size_to:
                yield df[start_index:sub_size_index]
                start_index = sub_size_index
                cur_size = i-sub_size_index
                sub_size = 0
            sub_size_index = i

        cur_size += 1
    if sub_size > 0:
        yield df[start_index:sub_size_index]
        start_index = sub_size_index
    yield df[start_index:]


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