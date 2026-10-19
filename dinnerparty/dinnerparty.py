import random

# Етап 1: Введення кількості людей та їхніх імен
num_people = int(input("Enter the number of friends joining (including you):\n"))

if num_people <= 0:
    print("\nNo one is joining for the party")
else:
    print(
        "Enter the name of every friend (including you), each on a new line:"
    )
    friends_dict = {}
    for _ in range(num_people):
        name = input()
        friends_dict[name] = 0

    # Етап 2: Введення загальної суми та початковий розподіл
    total_amount = float(input("Enter the total amount:\n"))

    split_amount = round(total_amount / num_people, 2)
    for name in friends_dict:
        friends_dict[name] = split_amount

    # Етап 3 та 4: Вибір "щасливчика" та перерахунок
    lucky_choice = input(
        'Do you want to use the "Who is lucky?" feature? Write Yes/No:\n'
    )

    if lucky_choice == "Yes":
        lucky_person = random.choice(list(friends_dict.keys()))
        print(f"\n{lucky_person} is the lucky one!")

        # Перерахунок для n - 1 людей
        split_amount_lucky = round(total_amount / (num_people - 1), 2)
        for name in friends_dict:
            if name == lucky_person:
                friends_dict[name] = 0
            else:
                friends_dict[name] = split_amount_lucky

        print(friends_dict)
    else:
        print("\nNo one is going to be lucky")
        print(friends_dict)