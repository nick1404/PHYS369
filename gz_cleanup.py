from matplotlib import pyplot as plt
import pandas as pd

gz = pd.read_csv("/Users/nickmisiiuk/dev/PHYS369/data/gz_candels.csv")

data = gz[["ID", "RA", "Dec", "clean_smooth",
           "clean_featured", "clean_clumpy", "clean_spiral"]]

clumpy_not_featured = (data["clean_clumpy"] == True) & (
    data["clean_featured"] == False)

spiral_not_featured = (data["clean_spiral"] == True) & (
    data["clean_featured"] == False)

featured = data["clean_featured"] == True

df_non_smooth = pd.concat([data[spiral_not_featured],
                           data[clumpy_not_featured], data[featured]])

df_non_smooth.drop(["clean_smooth", "clean_featured",
                   "clean_clumpy", "clean_spiral"], axis=1, inplace=True)
df_non_smooth["type"] = "F"

df_smooth = data[data["clean_smooth"] == 1]

df_smooth.drop(["clean_smooth", "clean_featured",
                "clean_clumpy", "clean_spiral"], axis=1, inplace=True)

df_smooth["type"] = "S"

df = pd.concat([df_smooth, df_non_smooth])

df.to_csv("/Users/nickmisiiuk/dev/PHYS369/data/gz_final.csv",)
