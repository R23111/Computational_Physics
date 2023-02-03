import numpy as np


def polar_to_scalar(mode, x=0, y=0):

    if(mode == 3):
        real = x * np.cos(y)
        imag = x * np.sin(y)
        return(f"{real} + j {imag}")

    print("x*e^(iy)\n")

    x = float(input("x = "))
    y = float(input("y = "))

    real = x * np.cos(y)
    imag = x * np.sin(y)

    if(mode == 1):
        print(f"{real} + j {imag}")

    if(mode == 2):
        return complex(real, imag)


def scalar_to_polar(mode, x=0, y=0):
    if(mode == 3):
        mod = np.sqrt(x**2 + y**2)
        ang = np.arctan(y/x)
        return f"{mod} * e^(i* {ang})"

    print("x + i * y\n")

    x = float(input("x = "))
    y = float(input("y = "))

    mod = np.sqrt(x**2 + y**2)
    ang = np.arctan(y/x)

    if(mode == 1):
        print(f"{mod} * e^(i * {ang}")
    if(mode == 2):
        return [mod, ang]


def complex_sum():
    num_type = int(input("Tipo do num1:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        num1 = polar_to_scalar(mode=2)
    elif(num_type == 2):
        print("x + j * y\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = complex(x, y)

    num_type = int(input("Tipo do num2:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        num2 = polar_to_scalar(mode=2)
    elif(num_type == 2):
        print("\nx + j * y\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = complex(x, y)

    result = num1 + num2

    print(
        f"Forma complexa: {result.real} + i {result.imag}\nForma polar: {scalar_to_polar(mode=3,x=result.real, y=result.imag)}")


def complex_sub():
    num_type = int(input("Tipo do num1:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        num1 = polar_to_scalar(mode=2)
    elif(num_type == 2):
        print("x + j * y\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = complex(x, y)

    num_type = int(input("Tipo do num2:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        num2 = polar_to_scalar(mode=2)
    elif(num_type == 2):
        print("\nx + i * y\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = complex(x, y)

    sub = num1 - num2

    print(
        f"Forma complexa: {sub.real} + i {sub.imag}\nForma polar: {scalar_to_polar(mode=3,x=sub.real, y=sub.imag)}")


def complex_mult():
    num_type = int(input("Tipo do num1:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        print("x * e^(i*y)\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = [x, y]
    elif(num_type == 2):
        num1 = scalar_to_polar(mode=2)

    num_type = int(input("Tipo do num2:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        print("x * e^(i*y)\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = [x, y]
    elif(num_type == 2):
        num2 = scalar_to_polar(mode=2)

    res_mod = num1[0] * num2[0]
    res_ang = num1[1] + num2[1]

    print(
        f"Forma complexa: {polar_to_scalar(mode=3, x=res_mod, y=res_ang)}\nForma polar: {res_mod} * e^(i * {res_ang})")


def complex_div():
    num_type = int(input("Tipo do num1:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        print("x * e^(i*y)\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num1 = [x, y]

    elif(num_type == 2):
        num1 = scalar_to_polar(mode=2)

    num_type = int(input("Tipo do num2:\n[1]polar\n[2]complex\n>> "))
    if(num_type == 1):
        print("x * e^(i*y)\n")
        x = float(input("x = "))
        y = float(input("y = "))
        num2 = [x, y]
    elif(num_type == 2):
        num2 = scalar_to_polar(mode=2)

    res_mod = num1[0] / num2[0]
    res_ang = num1[1] - num2[1]

    print(
        f"Forma complexa: {polar_to_scalar(mode=3, x=res_mod, y=res_ang)}\nForma polar: {res_mod} * e^(i * {res_ang})")


def main():
    while True:
        op = int(input(
            "Tipo de operação:\n[1]polar -> escalar\n[2]escalar -> polar\n[3]Soma\n[4]Subtração\n[5]Multiplicação\n[6]Divisão\n>> "))
        if(op > 0 or op < 7 and type(op) == int):
            break

    if op == 1:
        polar_to_scalar(mode=1)
    elif op == 2:
        scalar_to_polar(mode=1)
    elif op == 3:
        complex_sum()
    elif op == 4:
        complex_sub()
    elif op == 5:
        complex_mult()
    elif op == 6:
        complex_div()

if __name__ == "__main__":
    main()