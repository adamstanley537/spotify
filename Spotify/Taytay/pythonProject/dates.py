import pandas as pd

df = pd.read_csv("taytracks.csv")
df2 = pd.read_csv("taydata.csv")

df3 = pd.merge(left=df2, right=df["date"], left_index=True, right_index=True)
df3.drop(["Unnamed: 0.1","Unnamed: 0","id_x","id_y"], axis=1, inplace=True)
df3.to_csv("taydata_v2.csv")

