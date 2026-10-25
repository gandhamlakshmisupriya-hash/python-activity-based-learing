

# University Scholarship Allocation System

students = []

n = int(input("Enter number of applicants: "))

for i in range(n):
    print("\nApplicant", i + 1)

    name = input("Enter student name: ")
    marks = float(input("Enter aggregate marks (%): "))
    s1 = float(input("Enter Subject 1 marks (%): "))
    s2 = float(input("Enter Subject 2 marks (%): "))
    s3 = float(input("Enter Subject 3 marks (%): "))
    attendance = float(input("Enter attendance (%): "))
    income = float(input("Enter annual family income (Rs.): "))

    # Validate inputs
    if not (0 <= marks <= 100 and
            0 <= s1 <= 100 and 0 <= s2 <= 100 and
            0 <= s3 <= 100 and 0 <= attendance <= 100 and
            income >= 0):
        print("Invalid details. Applicant rejected.")
        continue

    # Eligibility conditions
    if (marks >= 75 and s1 >= 40 and s2 >= 40
            and s3 >= 40 and attendance >= 75
            and income <= 200000):

        students.append({
            "name": name,
            "marks": marks,
            "attendance": attendance,
            "income": income
        })

# Ranking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
students.sort(
    key=lambda s: (
        -s["marks"],
        -s["attendance"],
        s["income"]
    )
)

print("\n=== Scholarship Results ===")

if students:
    for rank, s in enumerate(students, start=1):
        print("\nRank:", rank)
        print("Name:", s["name"])
        print("Aggregate Marks:", s["marks"], "%")
        print("Attendance:", s["attendance"], "%")
        print("Family Income: Rs.", s["income"])
else:
    print("No eligible applicants found.")

print("\nTotal Eligible Students:", len(students))
