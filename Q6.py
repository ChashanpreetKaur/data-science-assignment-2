crime = pd.read_csv("crime.csv")

crime["risk"] = crime["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime"
)

result = crime.groupby("risk")["PctUnemployed"].mean()

for k, v in result.items():
    print(f"{k}: {round(v,2)}")
