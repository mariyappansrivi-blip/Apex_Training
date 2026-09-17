choice = 2

while choice <= 3:

    if choice == 1:
        r = 5
        area = int(3.14 * r * r)
        print("Area of Circle =", area)

    elif choice == 2:
        l = 10
        b = 5
        area = l * b
        print("Area of Rectangle =", area)

    elif choice == 3:
        s = 4
        area = s * s
        print("Area of Square =", area)

    break