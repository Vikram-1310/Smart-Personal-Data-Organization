import pandas as pd

def analyze_data(data):
    df = pd.DataFrame(data)

    print("\n--- Data Analysis ---")
    print("\nAverage Age:", df["age"].mean())
    print("\nGender Count:", df["gender"].value_counts())
    print("\nCity Count:", df["city"].value_counts())

    all_interests = df["interests"].explode()
    print("\nTop Interests:", all_interests.value_counts().head())