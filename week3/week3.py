import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def heatmap():
    data = sns.load_dataset("flights")
    data = data.pivot("month", "year", "passengers")
    sns.heatmap(data=data, annot=True, fmt="d", cmap="YlGnBu")

    plt.show()
    data.info()


def lineplot():
    data = sns.load_dataset("flights")

    sns.lineplot(data=data, x="year", y="passengers")

    plt.show()


def swarmplot():
    data = sns.load_dataset("iris")

    sns.swarmplot(x="species", y="petal_length", data=data)  # spişiz

    plt.show()


def countplot():
    data = sns.load_dataset("titanic")

    # Bar plot
    sns.countplot(data=data, x="class")

    plt.show()


def scatterplot():
    data = sns.load_dataset("tips")

    # Scatter plot
    sns.scatterplot(data=data, x="total_bill", y="tip")
    plt.show()


def FacetGrid1():
    data = sns.load_dataset("titanic")

    g = sns.FacetGrid(data, col="sex")

    g.map(sns.histplot, "age")
    plt.show()


def clustermap():
    iris = sns.load_dataset("iris")

    g = sns.clustermap(iris.drop("species", axis=1), cmap="coolwarm", standard_scale=1)

    plt.show()


def histplot():
    data = sns.load_dataset("iris")

    sns.histplot(data=data, x="sepal_length")
    plt.show()


def violinplot():
    data = sns.load_dataset("tips")

    sns.violinplot(x="day", y="total_bill", data=data)
    plt.show()


def jointGrid():
    sns.set_theme(style="white")

    df = sns.load_dataset("penguins")

    g = sns.JointGrid(data=df, x="body_mass_g", y="bill_depth_mm", space=0)
    g.plot_joint(sns.kdeplot,
                 fill=True, clip=((2200, 6800), (10, 25)),
                 thresh=0, levels=100, cmap="rocket")
    g.plot_marginals(sns.histplot, color="#03051A", alpha=1, bins=25)
    plt.show()


def FacetGrid2():
    data = pd.DataFrame({
        'age_group': np.repeat(['18-30', '31-45', '46-60', '61+'], 100),
        'feedback_rating': np.random.randint(1, 6, 400)
    })

    g = sns.FacetGrid(data, col="age_group", margin_titles=True)

    g.map(sns.histplot, "feedback_rating")
    plt.show()


GrapList = [heatmap,
            lineplot,
            swarmplot,
            countplot,
            scatterplot,
            FacetGrid1,
            clustermap,
            histplot,
            violinplot,
            jointGrid,
            FacetGrid2]

for grap in GrapList:
    grap()
