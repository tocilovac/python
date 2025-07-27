from blessed import Terminal
term = Terminal()

def main():
    options = ["Get proper divisors", "Check for perfect number", "Look up the first few perfect numbers (up to 4)", "Quit"]
    selected_index = 0
    while True:
        selected_index = main_menu(options, selected_index)
        
        while True:
            if selected_index == 0:
            # --- Get a valid number input from user ---
                while True:
                    number_check = input(term.bold_cyan("Enter a number to find its proper divisors: ")).strip()
                    try:
                        number_check = int(number_check)
                        break
                    except ValueError:
                        try:
                            float_val = float(number_check)
                            if float_val.is_integer():
                                number_check = int(float_val)
                                break
                            else:
                                print("please enter a whole number, not a decimal.")
                                continue
                        except ValueError:
                            print(f"{number_check} is not a number! Try again.")
                            continue

                # --- Get and display proper divisors ---
                proper_divisors = get_proper_divisors(number_check)
                if type(proper_divisors) == str:
                    print(term.bold_cyan(proper_divisors))
                elif type(proper_divisors) == list:
                    print(term.bold_cyan(f"Proper divisors of {number_check}:"))    
                    print(term.bold_cyan(", ".join(str(n) for n in proper_divisors)))
                break

            elif selected_index == 1:
                while True:
                    number_check = input(term.bold_cyan("Enter a positive integer to check if its a perfect number: ")).strip()
                    try:
                        number_check = int(number_check)
                        break
                    except ValueError:
                        try:
                            float_val = float(number_check)
                            if float_val.is_integer():
                                number_check = int(float_val)
                                break
                            else:
                                print("please enter a whole number, not a decimal.")
                                continue
                        except ValueError:
                            print(f"{number_check} is not a number! Try again.")
                            continue
                print(term.bold_cyan(check_perfection(number_check)))
                break

            elif selected_index == 2:
                while True:
                    lim = input(term.bold_cyan("choose the limit for the number of first perfect numbers to be shown (up to 4): "))
                    try:
                        lim = int(lim)
                    except ValueError:
                        print("wrong input! Value must be between 1-4.")
                        continue
                    if 0 < lim < 5:
                        print(term.bold_cyan(f"list of first {lim} perfect numbers:"), ", ".join(str(x) for x in list_perfect_nums(lim)), sep="\n")
                        break
                    else:
                        print("wrong input! Value must be between 1-4.")
                        continue
                break

            elif selected_index == 3:
                print (term.bold_cyan("quitting program...", "Goodbye!"), sep = "\n")
                exit()
        pausing = input(term.dim +term.yellow("\nPress Enter to continue..."))
        # second menu's code insert here!!!! (Either return to main menu by repeating this while loop or end program right here.)
        options_second_lst = ["Go back to main menu", "Quit Program"]
        second_menu_selected_index = second_menu(options_second_lst, 0)
        if second_menu_selected_index == 0:
            continue
        elif second_menu_selected_index == 1:
            print (term.bold + term.cyan("quitting program...Goodbye!"))
            exit()

def second_menu(options, index):
    with term.cbreak():
        index = 0
        while True:
            print (term.clear() + term.move_yx(0, 0))
            print (term.bold_red("Choose the next action:"))
            for i, option in enumerate(options):
                if i == index:
                    print (term.bold_purple + term.reverse(option))
                else:
                    print (option)
            key = term.inkey()
            if key.name == 'KEY_UP' or key.name == 'KEY_LEFT':
                index = (index - 1) % len(options)
            elif key.name == 'KEY_DOWN' or key.name == 'KEY_RIGHT':
                index = (index + 1) % len(options)
            if key.name == 'KEY_ENTER':
                print (term.clear())
                print(term.bold_yellow(f"\nYou selected: {options[index]}"))
                return index

# --- defines parameters for the main menu ---
def main_menu(options, index):
    print (term.clear())
    with term.cbreak():
        index = 0
        while True:
            print (term.move_yx(0, 0))
            print (term.clear_eos())

            print (term.bold + term.white_on_red("*** Welcome to your number property checker ***".center(70), '\n'))
            print (term.bold_cyan("Use ↑ ↓ arrows and Enter to select:\n"))
            
            for i, option in enumerate (options):
                if i == index:
                    print (term.bold_purple + term.reverse(option))
                else:
                    print(option)
            
            key = term.inkey()
            if key.name == 'KEY_UP' or key.name == 'KEY_LEFT':
                index = (index - 1) % len(options)
            elif key.name == 'KEY_DOWN' or key.name == 'KEY_RIGHT':
                index = (index + 1) % len(options)
            elif key.name == 'KEY_ENTER':
                print (term.clear())
                print(term.bold_yellow(f"\nYou selected: {options[index]}"))
                return index

# --- Find all proper divisors of a number ---
def get_proper_divisors(n):
    divisors_lst = []
    if n < 0:
        return f"{n} must be positive"
    elif n == 0:
        return "nothing divided by something is nothing"
    elif n == 1:
        return f"{n} is only properly divided by itself"
    else:
        x = int(n / 2 + 1)
    for i in range(1, x):
        if n % i == 0:
            divisors_lst.append(i)
    if len(divisors_lst) == 1:
        return f"{n} is a prime number!"
    else:
        return divisors_lst

# --- Check if a number is perfect ---
def check_perfection(num):
    if isinstance(get_proper_divisors(num), list):
        check_lst = get_proper_divisors(num)
    else:
        return get_proper_divisors(num)
    sum = 0
    for i in range(len(check_lst)):
        sum += check_lst[i]
    if sum == num:
        return f"{num} is a perfect number"
    else:
        return f"{num} is not a perfect number"

# --- Generate list of the first 'limit' perfect numbers ---
def list_perfect_nums(limit):
    perfect_list = []
    for i in range(9000):
        if check_perfection(i) == f"{i} is a perfect number":
            perfect_list.append(i)
        if len(perfect_list) == limit:
            break
    return perfect_list[:limit]

# --- Program entry point ---
if __name__ == '__main__':
    main()