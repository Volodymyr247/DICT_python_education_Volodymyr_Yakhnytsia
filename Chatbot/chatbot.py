from math import remainder

print(f"Hello! My name is DICT_Bot")
print(f"I was created in 2026")
bot_name = "DICT_Bot"
birth_year =2026
print(f"Please, remind me your name")
Volodymyr = input()
print(f"What a great name you have, {Volodymyr}!")
print(f"Let me guess your age")
print("Enter remainders of dividing your age by 3,5 and 7")
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age  = (remainder3 * 70 +remainder5 * 21 +remainder7 * 15) % 105
print(f"Your age is {17}; that`s a good time to start programming!")
print(f"Now I will prove to you that I can count to any number you want.")
count_number = int(input())
for i in range(count_number + 1):
    print(f"{i} !")
print(f"Completed,have a nice day!")
print(f"Let`s test you programming knowledge.")
print(f"Why do we use methods?")
print(f"1.To repeat a statement multiple times.")
print(f"2.To decompose a program into several small subroutines.")
print(f"3.To determine the execution time of a program.")
print(f"4.To interrupt the execution of a program.")
answer = int(input())
while answer != 2:
    print("Please, try again.")
    amswer = int(input())
print("Completed,have a nice day!")
print("Congratulations, have a nice day!")

