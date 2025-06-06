import time

menu_items = [
    ("1. Pad Thai", 345),
    ("2. Mongolian Beef", 400),
    ("3. Chicken Munchurian", 678),
    ("4. Chicken Shashlik", 810),
    ("5. Tiramisu", 367),
    ("6. DaalChaawal", 150),
    ("7. Cheesecake", 500),
    ("8. Feiry Pepper Chicken", 790),
    ("9. Mixed vegetables", 200),
    ("A. Biryani", 250),
    ("B. Pulau", 250),
    ("C. Pepsi", 80),
    ("D. Fanta", 80),
    ("E. 7up", 80),
    ("F. Mineral Water", 50)
]

item_map = {item[0].split('.')[0]: idx for idx, item in enumerate(menu_items)}

class FoodService:
    def __init__(self):
        self.menu = menu_items.copy()
        self.orders = [0] * len(self.menu)
        self.total_amount = 0

    def show_menu(self):
        print("-------------Menu--------------")
        for item, price in self.menu:
            print(f"{item:<35} PKR {price}")

    def add_to_cart(self):
        self.show_menu()
        while True:
            try:
                raw_choice = input("Enter item code to add to cart (or 'b' to go back): ")
                choice = str(raw_choice).strip().upper()
                if not choice:
                    print("No input detected. Try again.")
                    continue
                if choice == 'B':
                    break
                elif choice in item_map:
                    self.orders[item_map[choice]] += 1
                    print("Item added.")
                else:
                    print("Invalid choice.")
            except Exception as e:
                print(f"Input error: {e}")
                break

    def view_cart(self):
        print(time.ctime())
        print("\nYour Cart:")
        total = 0
        items_in_cart = 0
        for idx, qty in enumerate(self.orders):
            if qty > 0:
                item, price = self.menu[idx]
                item_total = price * qty
                print(f"{item:<35} x{qty:<3} = PKR {item_total}")
                total += item_total
                items_in_cart += qty
        print(f"Total Bill: PKR {total}\nTotal Items: {items_in_cart}")
        self.total_amount = total

    def place_order(self):
        self.view_cart()
        print("Order placed successfully!\n")
        self.orders = [0] * len(self.menu)

    def cancel_order(self):
        try:
            confirm = input("Are you sure you want to cancel your order? (y/n): ").lower()
            if confirm == 'y':
                self.orders = [0] * len(self.menu)
                self.total_amount = 0
                print("Order canceled.")
            else:
                print("Order not canceled.")
        except Exception as e:
            print(f"Input error: {e}")

    def cash_on_delivery(self):
        print("Please pay cash on delivery.")

    def delivery_status(self):
        try:
            print("Your food will be delivered in 45 minutes.")
            delay = input("Has your order arrived? (1 = yes, 0 = no, 2 = cancel): ")
            if delay == '1':
                print("Order received.")
            elif delay == '0':
                print("Please wait another 20-30 minutes.")
            elif delay == '2':
                self.cancel_order()
        except Exception as e:
            print(f"Input error: {e}")

class UserManager:
    def __init__(self):
        self.users = {}  # username: password

    def register_user(self):
        try:
            username = input("Enter new username: ")
            if username in self.users:
                print("Username already exists. Try logging in.")
                return None
            password = input("Enter new password: ")
            self.users[username] = password
            print("Registration successful!\n")
            return username
        except Exception as e:
            print(f"Input error: {e}")
            return None

    def login_user(self):
        attempts = 3
        while attempts > 0:
            try:
                username = input("Enter username: ")
                password = input("Enter password: ")
                if self.users.get(username) == password:
                    print("Login successful!\n")
                    return username
                else:
                    attempts -= 1
                    print(f"Incorrect credentials. {attempts} attempts left.\n")
            except Exception as e:
                print(f"Input error: {e}")
                break
        print("Too many failed attempts. Returning to main menu.\n")
        return None

class App:
    def __init__(self):
        self.user_manager = UserManager()

    def user_menu(self):
        food_service = FoodService()
        while True:
            print("\n1. View Menu")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Place Order")
            print("5. Cancel Order")
            print("6. Cash on Delivery")
            print("7. Check Delivery Status")
            print("0. Logout")
            try:
                raw_choice = input("Enter your choice: ")
                choice = str(raw_choice).strip()
                if not choice:
                    print("No input detected. Please enter a valid option.")
                    continue
                if choice == '1':
                    food_service.show_menu()
                elif choice == '2':
                    food_service.add_to_cart()
                elif choice == '3':
                    food_service.view_cart()
                elif choice == '4':
                    food_service.place_order()
                elif choice == '5':
                    food_service.cancel_order()
                elif choice == '6':
                    food_service.cash_on_delivery()
                elif choice == '7':
                    food_service.delivery_status()
                elif choice == '0':
                    print("Logging out...")
                    break
                else:
                    print("Invalid option.")
            except Exception as e:
                print(f"Input error: {e}")
                break

    def run(self):
        while True:
            print("\nWelcome to Food on Wheels")
            print("1. Register")
            print("2. Login")
            print("0. Exit")
            try:
                raw_choice = input("Enter your choice: ")
                choice = str(raw_choice).strip()
                if not choice:
                    print("No input detected. Please enter a valid option.")
                    continue
                if choice == '1':
                    user = self.user_manager.register_user()
                    if user:
                        self.user_menu()
                elif choice == '2':
                    user = self.user_manager.login_user()
                    if user:
                        self.user_menu()
                elif choice == '0':
                    print("Exiting program...")
                    break
                else:
                    print("Invalid option.")
            except Exception as e:
                print(f"Input error: {e}")
                break

if __name__ == "__main__":
    App().run()
