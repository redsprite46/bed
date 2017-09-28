import pandas as pd

original = pd.read_csv(
    "C:/Users/ROBO-E-03/Desktop/scope/data/clasification/classify_per_sec.csv",
    index_col=0)
records = []
pre_t = 0
pre_s = ""
for index, row in original.iterrows():
    t = row["time"]
    s = row["state"]

    if index == 0:
        pre_t = t
        pre_s = s
    else:
        if t - 1 == pre_t:
            rec = [pre_t, pre_s]
            records.append(rec)
            pre_t = t
            pre_s = s
        else:
            pre_t = t
            pre_s = s

arrange = pd.DataFrame(records)
header = ["time", "state"]
arrange.columns = header
arrange.to_csv(
    "C:/Users/ROBO-E-03/Desktop/scope/data/clasification/classify_per_sec1.csv")
