import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt

try:
    titanic_train = pd.read_csv("data/titanic_train.csv")
except FileNotFoundError:
    print("Data not found")
    pass
else:
    print(titanic_train.shape)
    print(titanic_train.head(5))

    categorical = titanic_train.dtypes[titanic_train.dtypes == "object"].index
    print(categorical)

    print(titanic_train[categorical].describe())

    print(titanic_train["Ticket"][0:15])

    print(titanic_train["Ticket"].describe())

    new_Pclass = pd.Categorical(titanic_train["Pclass"],
                                ordered=True)
    new_Pclass = new_Pclass.rename_categories(["Class1", "Class2", "Class3"])

    new_Pclass.describe()

    titanic_train["Pclass"] = new_Pclass

    print(titanic_train["Cabin"].unique())

    char_cabin = titanic_train["Cabin"].astype(str)  # Convert data to str

    new_Cabin = np.array([cabin[0] for cabin in char_cabin])  # Take first letter

    new_Cabin = pd.Categorical(new_Cabin)

    new_Cabin.describe()

    titanic_train["Cabin"] = new_Cabin

    dummy_vector = pd.Series([1, None, 3, None, 7, 8])

    print(dummy_vector.isnull())
    print(titanic_train["Age"].describe())

    missing = np.where(titanic_train["Age"].isnull() == True)
    print(missing)

    print(len(missing[0]))

    titanic_train.hist(column='Age',
                       figsize=(9, 6),
                       bins=20)
    plt.show()

    new_age_var = np.where(titanic_train["Age"].isnull(),  # Logical check
                           28,  # Value if check is true
                           titanic_train["Age"])  # Value if check is false

    titanic_train["Age"] = new_age_var

    print(titanic_train["Age"].describe())

    titanic_train.hist(column='Age',  # Column to plot
                       figsize=(9, 6),  # Plot size
                       bins=20)  # Number of histogram bins
    plt.show()