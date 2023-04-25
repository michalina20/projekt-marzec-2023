import time

numbers = [1, 2, 3, 4, 5]
def numberss():
    for number in numbers:
     print(number)
     time.sleep(1)

numberss()



import time

def count_down(n):
    time.sleep(1)
    if n == 1:
        print(n)
    else:
        print(n)
        count_down(n-1)

count_down(5)

# desired output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

print(list(zip(names, ages)))


Numbers = [1, 1, 2, 3, 4]
uniques = set(Numbers)
print(uniques)