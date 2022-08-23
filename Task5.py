a = int(input("Введіть значення a: "))
b = int(input("Введіть значення b: "))
c = int(input("Введіть значення c: "))
if a >= b:
    print("all done, try again")
else:
    while a < b:
        print(a,b)
        a = a + c