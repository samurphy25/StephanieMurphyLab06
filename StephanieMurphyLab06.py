#  stephanie murphy
def menu_function():
    print("Menu option:")
    print("1. Encode password")
    print("2. Decode password")
    print("3. Exit")
    print(end="\n")


def encoder_function(digits):
    result = ""
    for num in digits:
        new_numbers = str((int(num) + 3))
        result += new_numbers
    return result


if __name__ == "__main__":
    while True:
        menu_function()
        option = int(input("Choose to encode or decode your password:"))
        print(end="\n")

        if option == 1:
            password = (input("Enter your 8-digit password here:"))
            print(encoder_function(password))
            print(end="\n")

        elif option == 2:
            pass

        elif option == 3:
            break
