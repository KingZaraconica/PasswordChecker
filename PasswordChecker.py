import sys

def print_welcome() -> str:
    print("""Welcome to the Password Checker
        Please choose an action:
            1: Create a password (Reccomended for first use)
            2: Check password strength
            3: Cancel
            4: Previous passwords""")

def password_requirement() -> str:
    print("""To create a strong password, please ensure it meets the following
          requirements
        A: Contains 8 or more characters
        B: Contains both uppercase and lowercase letters
        C: Contains a number (0-9)
        D: Contains a symbol (!@#)""")

def password_checker(value: str) -> str:
    """
    Checks the strength of the input password
    """
    strength = 0
    fail = "Missing one or more of the requirements"
    test_pass = "Strong password"
    if len(value) >= 8:
        strength += 1
    if any(char.isupper() for char in value):
        strength += 1
    if any(char.islower() for char in value):
        strength += 1
    if any(char.isdigit() for char in value):
        strength += 1
    if any(not char.isalnum() for char in value):
        strength += 1
    if strength < 5:
        return fail
    else:
        return test_pass

def menu() -> str:
    print("""
Please select an option:
          1: Try again
          2: Return to menu
          3: Quit
""")
    
def main() -> "None":
    print_welcome()
    run = True
    passwords: list[str] = [""]
    menu_select = int(sys.stdin.readline().rstrip())
    selection = 0
    while run:
        if selection == 3:
            run = False
            break
        if menu_select == 1:
            selection = 1
            while selection == 1:
                password_requirement()
                password = sys.stdin.readline().rstrip()
                answer = password_checker(password)
                print(answer)
                if passwords[0] == '':
                    passwords[0] = password
                else:
                    passwords.append(password)
                menu()
                selection = int(sys.stdin.readline().rstrip())
                if selection == 2:
                    print_welcome()
                    menu_select = int(sys.stdin.readline().rstrip())
                    break
                if selection == 3:
                    print("Goodbye")
                    run = False
                    break
        elif menu_select == 2:
            selection = 1
            while selection == 1:
                print("Please input your password")
                user_input = sys.stdin.readline().rstrip()
                answer = password_checker(user_input)
                print(answer)
                if passwords[0] == '':
                    passwords[0] = user_input
                else:
                    passwords.append(user_input)
                menu()
                selection = int(sys.stdin.readline().rstrip())
                if selection == 2:
                    print_welcome()
                    menu_select = int(sys.stdin.readline().rstrip())
                    break
                elif selection == 3:
                    print("Goodbye")
                    run = False
                    break
        elif menu_select == 3:
            print("Goodbye")
            run = False
            break
        elif menu_select == 4:
            if passwords == "":
              print("No previous passwords")
            else:
              print(passwords)
            print_welcome()
            menu_select = int(sys.stdin.readline().rstrip())
main()