
import pandas as pd


df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bilge, YARŞİ",
        ],
        "Age": [22, 35, 21],
        "Sex": ["male", "male", "female"],
    }
)


print(df)

df.to_excel("output.xlsx", index=False)

print(df["Age"])
ages = pd.Series([22,35,21],name="Age")

max_age = df["Age"].max()
print("Age sütununun maksimum değeri:", max_age)

age_description = df["Age"].describe()
print("Age sütunu özet istatistikleri:")
print(age_description)

import matplotlib.pyplot as plt
plt.figure(figsize=(8, 6))
age_description.plot(kind="bar")

plt.title("Age Sütununun Özet İstatistikleri")
plt.ylabel("Değer")
plt.xlabel("İstatistiksel Ölçütler")
plt.show()
