import pandas as pd
from plot import plotstart

raw = pd.read_csv("/Users/nickmisiiuk/dev/PHYS369/data/legac+gz.csv")

# remove high magnitude galaxies and reduce uncertainty
low_mag = raw[(raw["ip_mag"] <= 22) & (raw["zp_mag"] <= 22)]

gal_smooth = low_mag[low_mag["type"] == "S"]

gal_feat = low_mag[low_mag["type"] == "F"]

print(raw["fast_lmass"].describe())