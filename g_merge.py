import pandas as pd
from query import query

lc = pd.read_csv("legac.csv")
gz = query("gz2_hart16", ["S"], columns=['dr7objid', 'ra', 'dec', 'gz2_class', 't01_smooth_or_features_a01_smooth_debiased', 't03_bar_a06_bar_debiased'])

dp=2

lc['ra'] = lc['ra'].apply(lambda x: round(x, dp))
gz['ra'] = gz['ra'].apply(lambda x: round(x, dp))
lc['dec'] = lc['dec'].apply(lambda x: round(x, dp))
gz['dec'] = gz['dec'].apply(lambda x: round(x, dp))

merge = gz.merge(lc, on=["ra","dec"])

merge.drop('Unnamed: 0', 1) ## Supposed to drop an unnamed column that appears (due to the merging of two datasets with indices... doesn't seem to do anything)

merge.to_csv("merge.csv", index=False)