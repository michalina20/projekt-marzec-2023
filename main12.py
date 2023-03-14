# suma = 0
# for x in range(1,10):
#     if x%2==0:
#         suma +=1
#         print(x)
# print(f"Parzyste liczby {suma}")
#
# def greet(name):
#     return name
#     print(f"Hi{name}")
#     #greet nie zwraca nic trzeba dac return else zwroci none
#
# def multiply(x,y):
#     return x * y
#
#     multiply (2,3,4,5)
#
# #tuple = lista wartosci ale kazda wartosc musi miec konkretny typ
#

def fizzbuzz():
    cos = str()
    for number in range(1,100):
        if number %3==0 and number%5==0:
            cos += "fizzbuzz"


        if number %3==0:
            cos += "fizz"


        if number %5==0:
            cos += "buzz"

        else:
            cos+= str(number)

        cos+= " , "
    return cos;

print(fizzbuzz())




