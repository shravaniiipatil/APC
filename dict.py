student = {
    "name": "Shravani",
    "age": 19,
    "course": "CSE"
}
print("Dictionary:", student)

print("Name:", student["name"])

student["grade"] = "A"
print("After adding grade:", student)

student["age"] = 20
print("After updating age:", student)

del student["course"]
print("After removing course:", student)

print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

for key, value in student.items():
    print(key, ":", value)
