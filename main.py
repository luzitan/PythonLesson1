# Задача 1

# a = input()
# a = list(a)
# sum = int(a[0]) + int(a[1]) + int(a[2])
# print(sum)


# Задача 2

# s = int(input())
# x = s//6
# print(x)
# print(4*x)
# print(x)

# Задача 3

# a = input()
# a = list(a)
# if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
#     print("yes")
# else:
#     print("no")

# Задача 4

n = int(input())
m = int(input())
k = int(input())

if k % n == 0 or k % m == 0:
    if k < n*m:
        print("yes")
else:
    print("no")