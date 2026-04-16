import pandas as pd
import matplotlib.pyplot as plt

def show_charts(data):
    df = pd.DataFrame(data)

    # Gender Pie
    df["gender"].value_counts().plot.pie(autopct='%1.1f%%')
    plt.title("Gender Distribution")
    plt.show()

    # Age Histogram
    df["age"].plot.hist()
    plt.title("Age Distribution")
    plt.show()

    # City Bar
    df["city"].value_counts().plot.bar()
    plt.title("City Distribution")
    plt.show()