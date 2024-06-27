import time as t
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_accounts_file():
    if not os.path.exists("acc.txt"):
        print("Creating accounts file...")
        with open("acc.txt", "w") as f:
            f.close()

def load_accounts():
    accounts = []
    if os.path.exists("acc.txt"):
        with open("acc.txt", "r") as f:
            for line in f:
                pin, balance, name = line.strip().split(', ')
                account = {"pin": int(pin), "balance": float(balance), "name": name}
                accounts.append(account)
    return accounts

def save_accounts(accounts):
    with open("acc.txt", "w") as f:
        for account in accounts:
            f.write(f"{account['pin']}, {account['balance']}, {account['name']}\n")

def main_menu():
    print("\n1: Balance Inquiry")
    print("2: Withdrawal")
    print("3: Deposit")
    print("4: Change PIN")
    print("5: Logout")

def atm_menu(account):
    print(f"\nWelcome {account['name']}")
    while True:
        main_menu()
        choice = int(input("Choose an option: "))
        if choice == 5:
            if input("Are you sure to logout? (Y/N): ").lower() == 'y':
                print("Logging out...")
                t.sleep(1)
                clear_console()
                break
        elif choice in (1, 2, 3, 4):
            perform_action(choice, account)
        else:
            print("Invalid choice. Try again.")

def perform_action(choice, account):
    if choice == 1:
        print(f"Your balance is: {account['balance']}")
    elif choice == 2:
        withdraw(account)
    elif choice == 3:
        deposit(account)
    elif choice == 4:
        change_pin(account)

def withdraw(account):
    amount = float(input("Enter amount to withdraw: "))
    if amount > account['balance']:
        print("Insufficient funds. Try again.")
    else:
        account['balance'] -= amount
        print(f"Withdrew {amount}. New balance is {account['balance']}")

def deposit(account):
    amount = float(input("Enter amount to deposit: "))
    account['balance'] += amount
    print(f"Deposited {amount}. New balance is {account['balance']}")

def change_pin(account):
    new_pin = int(input("Enter new PIN: "))
    account['pin'] = new_pin
    print("PIN changed successfully.")

def login(accounts):
    num_of_tries = 5
    while num_of_tries > 0:
        input_pin = int(input("Please enter your 4-digit pin to login into your account: "))
        for account in accounts:
            if account['pin'] == input_pin:
                return account
        num_of_tries -= 1
        print(f"Incorrect PIN. {num_of_tries} tries left.")
    print("Too many incorrect tries. Exiting...")
    return None

def main():
    clear_console()
    create_accounts_file()
    accounts = load_accounts()

    account = login(accounts)
    if account:
        atm_menu(account)
        save_accounts(accounts)
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()


