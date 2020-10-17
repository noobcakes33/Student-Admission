import pandas as pd
import random

# creating a data frame with the columns needed
data = pd.DataFrame(
            columns=["Student_ID", "Gender", "Nationality", "PlaceofBirth", "Math_exam", "Essay_exam"]
            )

# creating random values for the columns we need
rows = []
for i in range(1000):
    rows.append(
        {
            "Student_ID": random.randint(50000, 80000),
            "Gender": random.choice(["M", "F"]),
            "Nationality": random.choice(["KU", "LEB", "UK", "US", "EGY"]),
            "PlaceofBirth": random.choice(["Kuwait", "Lebanon", "UK", "USA", "Egypt"]),
            "Math_exam": random.randint(0, 100),
            "Essay_exam": random.randint(0, 100),
        }
    )

# inserting the values into the data frame
data = data.append(rows)

# creating a new column named Total that is the sum of both exams' grades
data["Total"] = data["Math_exam"] + data["Essay_exam"]

# creating Admission column that is 1 or 0 for Accepted or Rejected
# the criteria here is the sum of both grades greater than or equals 125.
data["Admission"] = [1 if data["Total"][i] >= 125 else 0 for i in range(len(data))]

# Number of rejected and accepted admissions
print("[Rejected] ", len(data[data["Admission"] == 0]))
print("[Accepted] ", len(data[data["Admission"] == 1]))

# Exporting the data frame into a csv file.
data.to_csv("College Dataset.csv")
print("Dataset generated successfully!")
