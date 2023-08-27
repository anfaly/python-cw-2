my_name=input("enter your name")
my_age=input("enter your age")
print(f"my_name is {my_name} and i an {my_age} years old")
first_number=int(input("enter first number"))
second_number=int(input("enyer second number"))
operation=input("what is the operation (+-*/)")
if operation == '+' :
    print(first_number + second_number)
elif operation == "-" :
    print(first_number - second_number)
elif operation == "*" :
    print(first_number * second_number)
elif operation == "/" :
    print(first_number / second_number)
else :
    print('the operation is not valid')
bus_capacity = 50
people_inbus=int(input('how many people are waiting '))
waiting = int(input('how many people are waiting '))
empty_seeats = bus_capacity - people_inbus
if empty_seeats > waiting:
    print(f'there are empty seats {empty_seeats}')
elif empty_seeats <= waiting :
    print('the bus is full')
