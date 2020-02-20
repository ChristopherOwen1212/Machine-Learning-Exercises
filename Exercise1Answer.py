#!/usr/bin/env python
# coding: utf-8

# # Case Study Singapore Airbnb Answer

import pandas as pd
Data = pd.read_csv("listings.csv")
print(Data)
print(Data.isna().values.any())


# # 1a. Find Minimum Value

minValue = Data.min()
print(minValue)


# # 1b. Find Maximum Value

maxValue = Data.max()
print(maxValue)


# # 2. Remove Null Value

newDataWithoutNull = Data.dropna()
print(newDataWithoutNull.isna().values.any())
print(len(newDataWithoutNull))
print(newDataWithoutNull.isna().sum())


# # 3. Replace null value to certain value

newDataFillNull = Data.fillna(10)
print(newDataFillNull.isna().values.any())
print(len(newDataFillNull))
print(newDataFillNull.isna().sum())
