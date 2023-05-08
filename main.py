import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyodide.http import open_url

url = (
    "https://raw.githubusercontent.com/angstvra/dataset/main/student.csv"
)
student_data = pd.read_csv(open_url(url))

def plot(data):
    col_means = student_data.loc[:, "GENERAL APPEARANCE":"Student Performance Rating"].mean().to_frame().set_axis(["Mean"], axis=1)
    col_means = col_means.sort_values(by="Mean", ascending=False)
    plt.rcParams["figure.figsize"] = (18,15)
    plt.title("Average per Column")
    fig, ax = plt.subplots()
    ax = sns.barplot(data=col_means, x=col_means.index, y="Mean")
    ax.bar_label(ax.containers[0])
    plt.xticks(rotation=45)
    display(fig, target="graph-area", append=False)

plot(student_data)