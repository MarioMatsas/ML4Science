# Imports

import pandas as pd
import numpy as np


df = pd.read_csv("data/structured_routing.csv")
dd = pd.read_csv("data/data_dictionary.csv")

# Take the column roles from the dictionary
FEATURES = dd.loc[dd.role == "pre_routing_feature", "column"].tolist()
TARGETS = dd.loc[dd.role == "target", "column"].tolist()
EVAL_ONLY = dd.loc[dd.role == "evaluation_only", "column"].tolist()
IDS = dd.loc[dd.role == "identifier", "column"].tolist()

print(len(FEATURES), len(TARGETS), len(EVAL_ONLY), len(IDS))
assert len(FEATURES) == 19 # Make sure the number of features is correct
assert set(FEATURES).isdisjoint(TARGETS + EVAL_ONLY + IDS) # Make sure the features are disjoint from the other roles

TARGET = "brier_improvement" # Primary target, as per the instructions