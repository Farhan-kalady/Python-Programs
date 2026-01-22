# Write a program to insert row at a given position in pandas DataFrame.

import pandas as pd

df = pd.DataFrame({
    "Name" : ["Farhan", "Umesh", "Grikhill"],
    "Age" : [20, 21, 19]
})

print("Original DataFrame:\n")
print(df)

new_row = {"Name" : "Athul", "Age" : 23}

position = 1

df_new = pd.concat(
    [df.iloc[:position],
     pd.DataFrame([new_row]),
     df.iloc[position:]],
     ignore_index=True

)

print("After Concate Row")
print(df_new)
