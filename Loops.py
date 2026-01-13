#       For LOOP        #

# x = int(input("Enter the number for which you want the table of: "))
# # for i in range(1, 11):
# #     # print(x , "x", i, "=", x*i)
# #     print(f"{x} x {i} = {x*i}")

# for i in range(10, 0, -1):
#     print(f"{x} x {i} = {x*i}")


#       While LOOP      #

# y = int(input("Enter the number"))
# while y <= 10:
#     if(y % 2 == 0):
#         print("y")
#     else:
#         continue

# z = 0
# productE = 1
# productO = 1
# for i in range(1, 10):
#     if(z % 2 == 0):
#         productE *= i
#         print(productE)
#     else:
#         continue
# print("Even product = ", productE)
# while z <= 10:
#     if(z % 2 != 0):
#         productO *= i
#         print(productO)
#     else:
#         continue
# print("Odd product = ", productO)


# for i in range(1, 11):
#     if(i % 2 == 0):
#         print(i)
#         continue


# x = 5
# for i in range (x, 0, -1):
#     print(i*"* ")

# x = int(input("Enter a number"))
# revNo = 0
# while x > 0:
#     temp = x % 10
#     revNo = 10 * revNo + temp
#     x = x // 10
# print(revNo)


# length = 5
# for i in range (1,length+1):
#     print("*   "* length)



# x = int(input("Enter a number which is more than 5 digits"))
# y = int(input("Enter a number you want to find the count of"))
# res = 0

# while (x > 0):
#     temp = x % 10
#     if (temp == y):
#         res += 1
#     x = x // 10
# print(res)

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = len(x)
lm = max(x)
slm = x[-2]
print(lm)
print(slm)