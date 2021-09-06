def count():
    x=sm
    print("Суммма элементов числа",n,"=",x)
    return

n=int(input("Введите число>>"))
print(n)
s=str(n)
sm=0
for i in range(len(s)):
    sm+=int(s[i])

count()
