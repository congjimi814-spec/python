# match-case匹配(结构或内容都可以)
# case1:
a1 = int(input("请输入一个整数:"))
match a1:
    case 1:
        print("你输入的是1")
    case 2:
        print("你输入的是2")
    case _:
        print("你输入的不是1也不是2")

# case2四则运算:
num1 = int(input("请输入第一个整数:"))
num2 = int(input("请输入第二个整数:"))
operator = input("请输入运算符(+, -, *, /):")

match operator:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"{num1} / {num2} = {num1 / num2}")
        else:
            print("错误：除数不能为0")
    case _:
        print("错误：无效的运算符")