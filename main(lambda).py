numbers = [3,7, 9, 12]
first, second, third, fourth = numbers
sum = first + second + third + fourth
print(sum)


def smallest_number(list):
    min = list[0]
    for i in numbers:
        if i<min:
            min = i
    return min
print (smallest_number(numbers))


items = [("product 1", 12),
         ("product 2", 2),
         ("product 3", 42) ]
def sort_item(items):
    return items[0]

items.sort(key=lambda item: item[0])
print(items)

students = [
    {"name": "Jan", "age": 20},
    {"name": "Agata", "age": 27},
    {"name": "Karlina", "age": 18}
]

students.sort(key = lambda student: student["age"])
print(students[0])
