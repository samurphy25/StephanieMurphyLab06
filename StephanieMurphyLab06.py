#  stephanie murphy
#Ramzi diehs
def menu_function():
    print("Menu option:")
    print("1. Encode password")
    print("2. Decode password")
    print("3. Exit")
    print(end="\n")

# stephanie murphy
def encoder_function(digits):
    result = ""
    for num in digits:
        new_numbers = (int(num) + 3)
        if new_numbers > 9:
            new_numbers = new_numbers % 10
        result += str(new_numbers)
    return result

def decodePass(encryptedCode): #ramzi did this
    res = ""
    for i in encryptedCode:
        temp = int(i) - 3
        if temp < 1:
            temp = abs(temp % 10)
        res = res + str(temp)
    return res



if __name__ == "__main__":
    while True:
        menu_function()
        option = int(input("Choose to encode or decode your password:"))


        if option == 1:
            password = (input("Enter your 8-digit password here:"))
            encoded_pass = encoder_function(password)
            print("Your password has been encoded and stored!")
            print()


        elif option == 2:
            print(f"The encoded password is {encoded_pass}, and the original password is {decodePass(encoded_pass)}.")

        elif option == 3:
            break
