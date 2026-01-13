# a = int(input("Enter a number: "))
# print(a)
# print(float(a))
# print(bool(a))
# # print(list(a))
# # print(set(a))
# print(str(a))
# # print(tuple(a))
# # print(dict(a))


# b = input("Enter a word: ")
# print(b)
# print(float(b))
# print(bool(b))
# print(list(b))
# print(set(b))
# print(str(b))
# print(tuple(b))
# print(dict(b))


#   APPEND  #

# x = [1, 2, 3, 4, 5]
# print(x)
# x.append(6)
# print(x)
# # x.append(6, 7)  #error


# #   REMOVE  #
# x.remove(1)
# print(x)
# # x.remove(3, 5)  #error


# #   POP   #
# x.pop()
# print(x)


# #   REVERSE   #
# x.reverse()
# print(x)


# #   INSERT   #
# x.insert(1,6)
# print(x)


# #   EXTEND   #
# y = [10,20,30]
# x.extend(y)
# print(x)


# #   SORT    #

# x.sort()
# print(x)


#   METHOD   #
# c = "sonal"
# c.upper()       #Does not work because String is immutable
# print(c.upper())    #It works only of the printing instance.

# d = "SONAL"
# d.lower()       #Does not work because String is immutable
# print(d.lower())    #It works only of the printing instance.


# e = d.find("O")
# print(e)

# f = "      SONAL1 "
# print(f.isupper())
# print(f.islower())
# print(f.isalpha())
# f.split()
# print(f.split())
# print(f)
# print(f.strip())


# g = {1 : "Prabhas", 2 : "Thalapaty", 3 : "Nirahua"}
# print(g[1])
# g[1] = "Dino"
# print(g)


# h = (1,1,3,2,5,3,7,9,6,4,3,2,3,4,2,2,21,1,2,3,3,2,22,1,1,22,2,2,2)
# print(h.count(1))
# print(h.index(1))


#   Statement   #
#   IF Statement
x = int(input("Enter a number: "))
if (x%2 == 0) :{
    print("The number is even")
}
else: { 
    print("The number is odd")
}