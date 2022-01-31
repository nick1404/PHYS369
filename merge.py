import pandas as pd

lega_c = pd.read_csv("legac.csv")
gz = pd.read_csv('gz2_hart16.csv')

ra1 = lega_c['ra'].round(decimals=4)
ra2 = gz['ra'].round(decimals=4)

dec1 = lega_c['dec'].round(decimals=4)
dec2 = gz['dec'].round(decimals=4)

ra_merged = pd.concat([ra1, ra2], axis=0)
no_unique_ra = ra_merged.unique().shape  # about 19,450 galaxies match

dec_merged = pd.concat([dec1, dec2], axis=0)
no_unique_dec = dec_merged.unique().shape  # 42,257 galaxies match
