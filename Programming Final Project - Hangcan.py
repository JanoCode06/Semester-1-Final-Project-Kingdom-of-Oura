user_name = input("What is your name?: ")

print(f"""****************************** Expenses Tracker *******************************
Welcome to the Oura Kingdom! I see that you are new here. What is your name?
Name: {user_name}

Hello, {user_name}! You are chosen by the Queen Hermione to be sent to Hogwarts
School of Witchcraft and Wizardry, granting you a scholarship due to your
potential. An amount of 20,000 gold will be given to you as a monthly allowance.
Since you live quite far from Hogwarts, we have reserved a room for you in the
boarding house inside the campus which cost 4,000 gold monthly. To make sure
that you at least eat everyday, we have arranged the meal plan subscription
in the cafeteria for you which costs 300 gold per day. If you compute the
total default expenses which are housing, and food and drink, you still have
some allowance for other things like transportation, healthcare, leisure, and
school. But remember that you only have exactly 20,000 gold for all your
expenses monthly, so you have to make sure that you don't overspend.
Let me help you keep track of your expenses.
*******************************************************************************""")

def show_total(day, balance, expenses):

    print("\n*******************************************************************************")
    print("Day", day)
    print("Balance:", balance)
    print("Food and Drink:", expenses["foodandDrink"])
    print("Transport:", expenses["transportation"])
    print("Health:", expenses["healthcare"])-
    print("Housing:", expenses["housingandUtilities"])
    print("Leisure:", expenses["leisure"])
    print("School:", expenses["school"])

def end_month(balance, expenses, total_balance_count, total_spent):
    total_balance_count += 20000
    balance += 20000
    expenses["foodandDrink"] = 300
    balance -= 300
    total_spent += 300
    expenses["transportation"] = 0
    expenses["healthcare"] = 0
    expenses["housingandUtilities"] = 0
    expenses["leisure"] = 0
    expenses["school"] = 0
    balance -= 4000
    expenses["housingandUtilities"] += 4000
    total_spent += 4000
    return balance, expenses, total_balance_count, total_spent

def end_month_total(day, balance, expenses):
    print(f"""\nAt the end of Day {day}, you have {balance} gold left.
    Food and Drink ({expenses["foodandDrink"] / 200}%) : {expenses["foodandDrink"]}
    Transportation ({expenses["transportation"] / 200}%) : {expenses["transportation"]}
    Healthcare ({expenses["healthcare"] / 200}%) : {expenses["healthcare"]}
    Housing and Utilities ({expenses["housingandUtilities"] / 200}%) : {expenses["housingandUtilities"]}
    Leisure ({expenses["leisure"] / 200}%) : {expenses["leisure"]}
    School ({expenses["school"] / 200}%) : {expenses["school"]}""")

def expulsion_summary(total_day, total_spent, total_balance_count):

    print(f"""\nOh no!
You ate the meals without paying.
Hogwarts is no place for thieves.
The Queen is greatly disappointed.
The scholarship is now cancelled.
          
    on Day {total_day}, you quit Hogwarts. During your entire stay, Queen Hermione
has bestowed you a total of {total_balance_count}. You spent a total of {total_spent} which is {total_spent / total_balance_count * 100:.1f}%
of the total money you received. You are left with 0 gold. """)
    return total_spent

def add_expenses(balance, expenses, choice, total_spent):
    print("""\nWhat would you like to do today?
     1 - add Food and Drink expenses
     2 - add Transportation expenses
     3 - add Healthcare expenses
     4 - add Housing and Utilities expenses
     5 - add Leisure expenses
     6 - add School expenses
     7 - end the Day
     8 - end the Month
     0 - exit the program""")

    choice = int(input("Enter the number of your choice: "))


    if choice >= 1 and choice < 7:
            
            amount = int(input("Enter the amount: "))
            print("Expenses successfuly added.")
            if choice == 1:
                expenses["foodandDrink"] += amount
                balance -= amount
                total_spent += amount
            elif choice == 2:
                expenses["transportation"] += amount
                balance -= amount
                total_spent += amount
            elif choice == 3:
                expenses["healthcare"] += amount
                balance -= amount
                total_spent += amount
            elif choice == 4:
                expenses["housingandUtilities"] += amount
                balance -= amount
                total_spent += amount
            elif choice == 5:
                expenses["leisure"] += amount
                balance -= amount
                total_spent += amount
            elif choice == 6:
                expenses["school"] += amount
                balance -= amount
                total_spent += amount
    else:
        if choice == 0:
            exit()

        
    return balance, expenses, choice, total_spent

def main_program():

    expenses = {
        "foodandDrink": 300,
        "transportation": 0,
        "healthcare": 0,
        "housingandUtilities": 4000,
        "leisure": 0,
        "school": 0
    }

    current_day = 1
    day = 1
    total_day = 0
    balance = 20000 - 4000 - 300
    total_balance_count = 20000
    choice = 0
    total_spent = 4000 + 300
    
    show_total(day, balance, expenses)

    while True:
        balance, expenses, choice, total_spent = add_expenses(balance, expenses, choice, total_spent)

        if balance < 0:
            expulsion_summary(total_day, total_spent, total_balance_count)
            exit()


        if choice == 7:
            print(f"\nat the end of Day {day}, you have {balance} gold left.")
            expenses["foodandDrink"] += 300
            balance -= 300
            total_spent += 300
            day += 1
            current_day += 1
            show_total(day, balance, expenses)

        elif choice == 8:
            days_remaining = 30 - current_day
            print(f"\n. . . {days_remaining} Days have passed . . .")
            for times in range(days_remaining):
                expenses["foodandDrink"] += 300
                balance -= 300
                total_spent += 300
                day += 1
            total_day += 30

            if balance <= 0:
                    expulsion_summary(total_day, total_spent, total_balance_count)
                    exit()

            current_day = 1

            if balance > 0:
                end_month_total(day, balance, expenses)
                balance, expenses, total_balance_count, total_spent = end_month(balance, expenses, total_balance_count, total_spent)
                day += 1
                show_total(day, balance, expenses)


main_program()