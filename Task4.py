def bigger(a, b, c):
    if a > b:
        print("Great!")
    elif a == b:
        if c < b:
            print("Oh, no!")
        else:
            print("Very well!")
    else:
        print("'sad smile'")

a = (input("Введіть значення a: "))
b = (input("Введіть значення b: "))
c = (input("Введіть значення c: "))
bigger(a, b, c)