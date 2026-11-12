#ماشین حساب خط فرمان

def show_menu():
    print("\n" + "=" *35)
    print("simple calculator")
    print("1.add (+)")
    print("2.subtraction (-)")
    print("3.multiply (*)")
    print("4.divide (/)")
    print("5.exit")
    print("=" *35)

def get_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("please enter a number")

def calculate(choice , a ,b):
    if choice == "1":
        return a+b , "add"
    elif choice == "2":
        return a-b ,"subtract"
    elif choice == "3":
        return a*b ,"multiply"
    elif choice == "4":
        if b == 0 :
            return None
        return a/b, "divide"
    return None,None

def format_num(n):
    if n==int(n):
        return str(int(n))
    return str(n)

def main():
    print("welcome!")

    while True:
        show_menu()
        choice = input("chooce between 1_5:").strip()

        if choice =="5":
            print("bye")
            return

        if choice not in ("1","2","3","4"):
            print("invalid num . please choose 1-5")
            continue

        num1= get_num("first number:")
        num2= get_num("second number:")

        result, op_name= calculate(choice , num1, num2)

        if choice == "4" and num2==0:
            print("Error, cant devide to 0")
            continue

        print(f"\n result {op_name}:{format_num(num1)}, {format_num(num2)} = " f"{format_num(result)}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n app stop!")