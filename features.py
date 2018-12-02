import pandas as pd
import numpy as np
import csv

keep_col = ['age','state','sex','rural','year_of_birth','injury_treatment_type','illness_type','symptoms_pertaining_illness','diagnosed_for','regular_treatment_source','drinking_water_source','is_water_filter','water_filteration','toilet_used','is_toilet_shared','cooking_fuel','is_refrigerator','is_bicycle','is_scooter','is_car','is_tractor','is_water_pump','cart','healthscheme_1','wt']
print(len(keep_col))

f=pd.read_csv("train.csv")
df1=f[f['sex']==1]
df2=f[f['sex']==2]

df1 = df1[keep_col].drop(['sex'],axis=1)
df2 = df2[keep_col].drop(['sex'],axis=1)
# df1.drop(['sex'],axis=1)
# df2.drop(['sex'],axis=1)

df1.to_csv("male.csv", index=False)
df2.to_csv("female.csv", index=False)

df1 = f[f['state']==5]
df2 = f[f['state']==8]
df3 = f[f['state']==9]
df4 = f[f['state']==10]
df5 = f[f['state']==18]
df6 = f[f['state']==20]
df7 = f[f['state']==21]
df8 = f[f['state']==22]
df9 = f[f['state']==23]

df1 = df1[keep_col].drop(['state'],axis=1)
df2 = df2[keep_col].drop(['state'],axis=1)
df3 = df3[keep_col].drop(['state'],axis=1)
df4 = df4[keep_col].drop(['state'],axis=1)
df5 = df5[keep_col].drop(['state'],axis=1)
df6 = df6[keep_col].drop(['state'],axis=1)
df7 = df7[keep_col].drop(['state'],axis=1)
df8 = df8[keep_col].drop(['state'],axis=1)
df9 = df9[keep_col].drop(['state'],axis=1)


df1.to_csv("Uttarakhand.csv", index=False)
df2.to_csv("Rajasthan.csv", index=False)
df3.to_csv("UP.csv", index=False)
df4.to_csv("Bihar.csv", index=False)
df5.to_csv("Assam.csv", index=False)
df6.to_csv("Jharkhand.csv", index=False)
df7.to_csv("Orissa.csv", index=False)
df8.to_csv("Chhattisgarh.csv", index=False)
df9.to_csv("MP.csv", index=False)
