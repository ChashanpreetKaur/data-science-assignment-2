def band(g):
    if g <= 9:
        return "Low"
    elif g <= 14:
        return "Medium"
    else:
        return "High"

df["grade_band"] = df["grade"].apply(band)

summary = df.groupby("grade_band").agg(
    students=("grade", "count"),
    avg_absences=("absences", "mean"),
    pct_internet=("internet", "mean")
)

summary["pct_internet"] *= 100
summary.to_csv("student_bands.csv")

print(summary)
