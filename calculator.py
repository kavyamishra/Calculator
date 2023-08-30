def calculate(choice, digit_1, digit_2):
    if choice == "add":
        return digit_1 + digit_2
    elif choice == "subtract":
        if digit_1 > digit_2:
            return digit_1 - digit_2
        return digit_2 - digit_1
    elif choice == "divide":
        return digit_1 / digit_2
    elif choice == "multiply":
        return digit_1 * digit_2
    elif choice == "power":
        return digit_1**digit_2
def start():
    while True:
        print ("Choices")
        print("Exit : 0")
        print("Add : 1")
        print("Sub : 2")
        print("Divide : 3")
        print("Multiply : 4")
        print("Power : 5")
        choice = int(input("Enter your choice: ... "))
        if choice == 0:
            break
        a = int(input("Enter Digit 1 -> "))
        b = int(input("Enter Digit 2 -> "))
        if choice == 1:
            print("response -> ",calculate("add", a, b),"\n")
        if choice == 2:
            print("response -> ",calculate("subtract", a, b),"\n")
        if choice == 3:
            print("response -> ",calculate("divide", a, b),"\n")
        if choice == 4:
            print("response -> ",calculate("multiply", a, b),"\n")
        if choice == 5:
            print("response -> ",calculate("power", a, b),"\n")
        else:
            print("Enter a valid choice")
    
if __name__ == "__main__":
    start()