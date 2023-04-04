students = [
  {"name" : "tomek", "age": 20},
  {"name" : "karolina", "age": 18}
]

students.sort(key=lambda stud:stud['age'])
print(students)

filtered = [stud for stud in students if stud['age']==18]
print(filtered)