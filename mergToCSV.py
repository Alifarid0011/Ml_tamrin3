import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

ListOfTrainFiles = [name for name in sorted(list(os.listdir("Train"))) if ".txt" in name]
print("List of file names:")
print(ListOfTrainFiles)
print(f"cont of files: {len(ListOfTrainFiles)}")


def dataset(test=False, list_files=ListOfTrainFiles):
    data = []
    for fileName in list_files:
        if test:
            with open(f"Test/{fileName}") as file:
                file = file.read()
                file = file.replace(".", "0")
                file = file.replace("#", "9")
                file = file.replace("@", "6")
                file = file.replace("o", "4")

        else:
            with open(f"Train/{fileName}") as file:
                file = file.read()
                file = file.replace(".", "0")
                file = file.replace("#", "9")
        file = file.split("\n")
        char_dataframe = pd.DataFrame(list(map(int, str(row))) for row in file)
        sum_column = char_dataframe.sum(axis=0)
        sum_row = char_dataframe.sum(axis=1)
        data.append(list(sum_column) + list(sum_row) + list(fileName[0]))
    return data


columns = [f"SOC-{x}" for x in range(1, 8)] + [f"SOR-{x}" for x in range(1, 10)] + ["Label"]
df = pd.DataFrame(dataset(), columns=columns)
df.to_csv("Train.csv", index=False)

ListOfTestFiles = [name for name in sorted(list(os.listdir("Test"))) if ".txt" in name]
print("List of file names:")
print(ListOfTrainFiles)
print(f"cont of files: {len(ListOfTrainFiles)}")

df_test = pd.DataFrame(dataset(test=True, list_files=ListOfTestFiles), columns=columns)
df_test.to_csv("Test.csv", index=False)
