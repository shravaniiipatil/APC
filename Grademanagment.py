print("Student Grade Management System")

students = []
grades = []

# ---- 1. Add students and grades ----
students.append("Alice")
grades.append(85)

students.append("Bob")
grades.append(90)

students.append("Charlie")
grades.append(78)

print("\nStudents and Grades after adding:")
for i in range(len(students)):
    print(students[i], "->", grades[i])

# ---- 2. Update a student's grade ----
if "Bob" in students:
    index = students.index("Bob")
    grades[index] = 95

print("\nAfter updating Bob's grade:")
for i in range(len(students)):
    print(students[i], "->", grades[i])

# ---- 3. Remove a student ----
if "Charlie" in students:
    index = students.index("Charlie")
    students.pop(index)
    grades.pop(index)

print("\nAfter removing Charlie:")
for i in range(len(students)):
    print(students[i], "->", grades[i])

# ---- 4. Calculate and display average grade ----
if len(grades) > 0:
    total = sum(grades)
    average = total / len(grades)
    print("\nAverage grade of class:", average)

# ---- 5. Display highest and lowest grades ----
if len(grades) > 0:
    highest = max(grades)
    lowest = min(grades)
    print("Highest grade in class:", highest)
    print("Lowest grade in class:", lowest)
