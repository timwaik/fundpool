import sys
import os
import moneyApp_user as User_Class

class App(object):
    """docstring for App."""


    def __init__(self):
        super(App, self).__init__()
        self.user_list = {}
        self.group_transaction_list = {}
        self.user_count = 0
        self.startup()

    def startup(self):
        while True:
            while True:
                print("\nWelcome to the money manager! Select what you want to do:\n")
                print("\t[1]\t Create New User")
                print("\t[2]\t Edit Existing User Name")
                print("\t[3]\t Delete User")
                print("\t[4]\t New Expense")
                print("\t[5]\t Add Money")
                print("\t[6]\t View Users")
                print("\t[7]\t Save Group")
                print("\t[8]\t Load Group")
                print("\t[9]\t Delete Saved Group")
                print("\t[0]\t Quit")
                print("\nType in corresponding number, then [enter] to continue")
                try:
                    choice = int(input())
                    break
                except ValueError:
                    print("Unacceptable input! Try again")
                    enter = input("Press [enter] to continue:")

            if choice == 1:
                print("Creating new user")
                self.new_user()


            elif choice == 2:
                if len(self.user_list) > 0:
                    print("\nEditing a users name")
                    self.edit_user()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 3:
                if len(self.user_list) > 0:
                    print("\nDeleting a user")
                    self.delete_user()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 4:
                if len(self.user_list) > 0:
                    print("\nCreating new expense")
                    self.new_expense()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 5:
                if len(self.user_list) > 0:
                    print("\nAdding money to pool..")
                    self.new_income()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 6:
                if len(self.user_list) > 0:
                    self.view_users()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 7:
                if len(self.user_list) > 0:
                    self.save_group()
                else:
                    print("No users available! Add a user first")
                    enter = input("Press [enter] to continue:")

            elif choice == 8:
                self.load_group()

            elif choice == 9:
                self.delete_group()

            elif choice == 0:
                sys.exit("Goodbye!")

            else:
                print("Unacceptable input! Try again")
                enter = input("Press [enter] to continue:")

###############################################################################

    def new_user(self):

        new_user_name = input("Name of the new user? : ")

        if new_user_name.strip() == "":
            print("You didn't type anything!")
            enter = input("Press [enter] to continue:")
        elif new_user_name.lower() not in self.user_list:

            while True:
                try:
                    new_user_balance = int(input("How much money are you putting in? : "))
                    break
                except ValueError:
                    print("You didn't add a valid number!")
            self.user_list[new_user_name.lower()] = User_Class.User(new_user_balance)
            print("\nUser \"", new_user_name, "\" created!")
            enter = input("Press [enter] to continue:")

        else:
            print("User already exists!")
            enter = input("Press [enter] to continue:")

###############################################################################

    def edit_user(self):
        while True:
            print("Which user to edit?:\n")
            for x in self.user_list.keys():
                print("\t- ", x)
            user_to_edit = input("\nEnter user here: ")
            if user_to_edit in self.user_list:
                print("Editing ", user_to_edit)
                while True:
                    new_user_name = input("Enter user's new name: ")
                    if new_user_name.lower() in self.user_list:
                        print("Username already exists! Try another one bro")
                    else:
                        self.user_list[new_user_name.lower()] = self.user_list.pop(user_to_edit)
                        break
                print("User ", user_to_edit, " changed to ", new_user_name.lower(), "!")
                enter = input("Press [enter] to continue:")
                break
            else:
                print("User not found! Try again")

###############################################################################

    def delete_user(self):
        while True:
            print("Which user do you want to delete?")
            for x in self.user_list.keys():
                print("\t- ", x)
            user_to_delete = input("\nEnter user here: ")
            if user_to_delete.lower() in self.user_list:
                while True:
                    print("Are you sure you want to delete \"", user_to_delete.lower(), "\"?")
                    yes_or_no = input("[Y]es, delete, or [N]o, don't delete\n")
                    if yes_or_no.lower() == "y":
                        self.user_list.pop(user_to_delete.lower())
                        print("\nUser deleted!")
                        enter = input("Press [enter] to continue:")
                        break
                    elif yes_or_no.lower() == "n":
                        print("\nUser remains in the group!")
                        enter = input("Press [enter] to continue:")
                        break
                    else:
                        print("Invalid input, try again!")
                break
            else:
                print("User doesn't exist!\n")




###############################################################################

    def new_expense(self):
        print("\nType in the name of your expense:")
        expense_name = input()
        while True:
            print("\nHow much is this expense?")
            try:
                expense_amount = int(input())
                break
            except ValueError:
                print("You didn't add a valid number!")

        while True:
            print("\nIs this a [G]roup expense or [S]elect few?")
            income_choice = input()

            if income_choice.lower() == "g":
                print("\nGroup expense selected!")
                individual_expense = (expense_amount/len(self.user_list))
                for x, y in self.user_list.items():
                    y.substract(individual_expense)
                print("Expense recording completed!")
                enter = input("Press [enter] to continue:")
                break

            elif income_choice.lower() == "s":
                print("\nSelect few!")
                while True:
                    print("How many users are sharing this expense?")
                    print("You can enter a maximum of ", len(self.user_list), " users")
                    try:
                        number_of_users_paying = int(input())
                        if number_of_users_paying > len(self.user_list):
                            print("You can't have more people paying than there are users!\n")
                        else:
                            print(number_of_users_paying, " users are sharing this!")
                            break
                    except ValueError:
                        print("Invalid input! Try again")

                expense_amount = (expense_amount/number_of_users_paying)

                users_paying_count = 0
                list_of_users_in = []
                list_of_users_out = []
                for x in self.user_list:
                    list_of_users_in.append(x)
                list_of_users_out = []
                while True:
                    print("\nWho's paying for this expense?")
                    for x in list_of_users_in:
                        print("\t-", x)
                    user_adding_money = input()
                    if user_adding_money in list_of_users_in:
                        print(user_adding_money, " is paying for this!")
                        users_paying_count += 1
                        list_of_users_in.remove(user_adding_money)
                        list_of_users_out.append(user_adding_money)
                    else:
                        print("User not found! Try again")
                    if users_paying_count == number_of_users_paying:
                        break
                for x in list_of_users_out:
                    self.user_list[x].substract(expense_amount)
                print("\nExpense recording completed!")
                enter = input("Press [enter] to continue:")
                break
            else:
                print("Wrong input, try again!")

###############################################################################

    def new_income(self):
        print("[G]roup or [I]ndividual income?")
        income_choice = input()

        if income_choice.lower() == "g":
            print("Group income!")
            while True:
                print("How much is everyone chipping in? (per person)")
                try:
                    money_added = int(input())
                    break
                except ValueError:
                    print("Invalid input! Try again")
            for x, y in self.user_list.items():
                y.addition(money_added)
            print("Fund pool updated!")
            enter = input("Press [enter] to continue:")
        elif income_choice.lower() == "i":
            print("Individual income!")
            while True:
                print("Who's putting in money?")
                for x in self.user_list:
                    print("\t-", x)
                user_adding_money = input()
                if user_adding_money in self.user_list:
                    print(user_adding_money, " is adding money!")
                    break
                else:
                    print("User not found! Try again")
            while True:
                print("How much are they chipping in?")
                try:
                    money_added = int(input())
                    break
                except ValueError:
                    print("Invalid input! Try again")
            self.user_list[user_adding_money].addition(money_added)
            print("Individual pool updated!")
            enter = input("Press [enter] to continue:")

###############################################################################

    def view_users(self):
        total_money_pool = 0
        print("\nHere is a list of all the users found:\n")
        print("Username\t\tAmount of money in pool")
        for x, y in self.user_list.items():
            print(x, end= "\t\t\t")
            print(y.view_balance())
            total_money_pool += y.view_balance()
        print("\nTotal amount of funds in the pool : ", total_money_pool)
        enter = input("\nPress [enter] to continue:")

###############################################################################

    def save_group(self):
        print("Save this group name as?")
        group_name = input("Enter chosen group name here: ")
        print("Saving group...")
        group_name = group_name + ".dat"
        os.chdir(os.getcwd() + "\\Loads")
        write_file = open(group_name, "w")
        for x, y in self.user_list.items():
            write_file.write(x + "\n")
            write_file.write(str(y.view_balance()) + "\n")
        print("Group saved successfully!")
        os.chdir("..")
        write_file.close()
        enter = input("Press [enter] to continue:")

###############################################################################

    def load_group(self):
        while True:
            print("If your current group is unsaved, all data will be lost with a new load")
            print("Are you sure you want to continue?")
            yes_or_no = input("Enter [Y]es, continue, or [N]o, go back\n")
            if yes_or_no.lower() == "y":
                while True:
                    print("Loading available groups:\n")
                    os.chdir(os.getcwd() + "\\Loads")
                    for entry in os.listdir():
                        if ".dat" in entry:
                            entry = entry[:-4]
                            print("\t-", entry)
                    group_name = input("\nEnter which group to load: ")
                    print("Loading group \"", group_name, "\"")
                    group_name = group_name + ".dat"
                    try:
                        read_file = open(group_name, "r")
                        break
                    except FileNotFoundError:
                        print("This group doesn't exist!")
                        os.chdir("..")
                self.user_list.clear()
                while True:
                    user_name = read_file.readline().strip()
                    user_balance = read_file.readline().strip()
                    if user_name == "":
                        print("Group loaded successfully!")
                        read_file.close()
                        os.chdir("..")
                        enter = input("Press [enter] to continue:")
                        break
                    else:
                        self.user_list[user_name] = User_Class.User(int(user_balance))
                break
            elif yes_or_no.lower() == "n":
                print("Cancelling load, returning to main menu..")
                enter = input("Press [enter] to continue:")
                break
            else:
                print("Invalid input, type again")

###############################################################################

    def delete_group(self):
        print("You're about to delete a group")
        print("\nAvailable loads:\n")
        os.chdir(os.getcwd() + "\\Loads")
        for entry in os.listdir():
            if ".dat" in entry:
                entry = entry[:-4]
                print("\t-", entry)
        group_name = input("\nEnter which group to delete: ")
        while True:
            print("Are you sure you want to delete group \"", group_name, "\"? Action is irreversible.")
            yes_or_no = input("Enter [Y]es, delete group, or [N]o, go back\n")
            if yes_or_no.lower() == "y":
                print("Deleting group \"", group_name, "\"")
                group_name = group_name + ".dat"
                try:
                    os.remove(group_name)
                    print("This group was deleted!")
                    os.chdir("..")
                    enter = input("Press [enter] to continue:")
                    break
                except FileNotFoundError:
                    print("This group doesn't exist! No group was deleted")
                    os.chdir("..")
                    enter = input("Press [enter] to continue:")
                    break
            elif yes_or_no.lower() == "n":
                print("Cancelling action, returning to main menu")
                os.chdir("..")
                enter = input("Press [enter] to continue:")
                break
            else:
                print("Invalid option, try again")

#Running the app
new_instance = App()
