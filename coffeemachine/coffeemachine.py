class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"

    def process_input(self, user_input):
        if self.state == "choosing_action":
            if user_input == "buy":
                self.state = "choosing_coffee"
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu:")
            elif user_input == "fill":
                self.state = "filling_water"
                print("Write how many ml of water do you want to add:")
            elif user_input == "take":
                print(f"I gave you {self.money}")
                self.money = 0
                self.print_action_prompt()
            elif user_input == "remaining":
                self.print_state()
                self.print_action_prompt()
            elif user_input == "exit":
                return False
            else:
                self.print_action_prompt()

        elif self.state == "choosing_coffee":
            if user_input == "back":
                self.state = "choosing_action"
                self.print_action_prompt()
            else:
                try:
                    choice = int(user_input)
                    self.make_coffee(choice)
                except ValueError:
                    pass
                self.state = "choosing_action"
                self.print_action_prompt()

        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
            print("Write how many ml of milk do you want to add:")

        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
            print("Write how many grams of coffee beans do you want to add:")

        elif self.state == "filling_beans":
            self.coffee_beans += int(user_input)
            self.state = "filling_cups"
            print("Write how many disposable cups of coffee do you want to add:")

        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "choosing_action"
            self.print_action_prompt()

        return True

    def print_state(self):
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money\n")

    def print_action_prompt(self):
        print("Write action (buy, fill, take, remaining, exit):")

    def make_coffee(self, choice):
        recipes = {
            1: [250, 0, 16, 4],
            2: [350, 75, 20, 7],
            3: [200, 100, 12, 6]
        }

        if choice not in recipes:
            return

        water_need, milk_need, beans_need, cost = recipes[choice]

        if self.water < water_need:
            print("Sorry, not enough water!")
        elif self.milk < milk_need:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < beans_need:
            print("Sorry, not enough coffee beans!")
        elif self.cups < 1:
            print("Sorry, not enough cups!")
        else:
            print("I have enough resources, making you a coffee!")
            self.water -= water_need
            self.milk -= milk_need
            self.coffee_beans -= beans_need
            self.cups -= 1
            self.money += cost


if __name__ == "__main__":
    machine = CoffeeMachine()
    machine.print_action_prompt()

    while True:
        user_input = input("> ")
        running = machine.process_input(user_input)
        if not running:
            break