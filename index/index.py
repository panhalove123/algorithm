
# EX1

# text=input("Enter your text: ")
# for cha in text:
#     print(cha)


# text=input("Enter your text: ")
# for i in range(len(text)):
#     print(text[i])


# Ex2

# text=input("Enter your text: ")
# for i in range(len(text)):
#     print(i)

# Ex3 

# text = input("Enter your text: ")
# index = 0
# isfound = False
# while index < len(text):
#     if text[index].isupper():
#         isfound = True
#     index += 1
# if isfound:
#     print("Yes")
# else:
#     print("No")

# EX4

# text = "3 4 5 6"
# Total=0
# for cha in text:
#     if cha != " ":
#         print(cha)
#         Total += int(cha)
# print(Total)


#Ex5


# text = "454639"
# count_odd = 0
# count_even = 0
# for i in range(len(text)):
#     total = int(text[i])
#     if total % 2 == 0:
#         count_odd += 1
#     if total % 2 == 1:
#         count_even += 1
# print("Count of even :", count_even)
# print("Count of odd :", count_odd)
# print("sum all number:",count_even+count_odd)
# print("Reverse",text[::-1])


# Ex6 - Number

# num=int(input("Enter number: "))
# if num % 2 == 0:
#     print("Even number")
# else:
#     print("Odd number")



# Ex7

# Ex7 - number
# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20


# isfound=False
# while not isfound:
#     number=int(input("Enter number: "))
#     if number<=20 and number>=10:
#         print("countinue")
#         isfound=True
#     else:
#         print("out of range")
#         isfound=False


# Ex8

# text = "9394884039"
# index = -1
# count_8 = 0
# i = 0
# while i < len(text):
#     if text[i] == "8":
#         count_8 += 1
#         index = i
#         index=len(text)
#     i += 1
# print(count_8)  
# print(index)   


# Ex9
# We have string = "3 4 5 6"
# Q1 - Remove space and keep result = "3456"
# Q2 - Multiple each letter by 2 result = "6 8 10 12"


# string = "3 4 5 6"
# result = " "
# total = " "
# i = 0
# while i < len(string):
#     cha = string[i]
#     if cha != " ":
#         result += cha
#         total += str(int(cha) * 2) + " "
#     i += 1
# print(result)  
# print(total)  


# Ex10
# print("Please enter your number : ")
# bigest_number = 0
# smailest_number = 0
# for i in range(5):
#     number = int(input("Enter number : "))
#     if bigest_number == 0 and smailest_number == 0:
#         bigest_number = number
#         smailest_number = number
#     else:
#         if number > bigest_number:
#             bigest_number = number
#         if number < smailest_number:
#             smailest_number = number
# print("Bigest number : ", bigest_number)
# print("Smaillest number : ", smailest_number)

