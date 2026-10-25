import random

import random

# Step 1: Input the number of people and their names
num_people = int(input("Enter the number of friends joining (including you):\n"))

if num_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends_dict = {}
    for _ in range(num_people):
        name = input()
        friends_dict[name] = 0

    # Step 2: Input the total amount and initial split
    total_amount = float(input("Enter the total amount:\n"))

    split_amount = round(total_amount / num_people, 2)
    for name in friends_dict:
        friends_dict[name] = split_amount

    # Step 3 & 4: Lucky person feature and recalculation
    lucky_choice = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if lucky_choice == "Yes":
        # Handle the edge case if only 1 person is joining
        if num_people == 1:
            lucky_person = list(friends_dict.keys())[0]
            print(f"{lucky_person} is the lucky one!")
            print(friends_dict)
        else:
            lucky_person = random.choice(list(friends_dict.keys()))
            print(f"{lucky_person} is the lucky one!")

            # Recalculate for n - 1 people
            split_amount_lucky = round(total_amount / (num_people - 1), 2)
            for name in friends_dict:
                if name == lucky_person:
                    friends_dict[name] = 0
                else:
                    friends_dict[name] = split_amount_lucky

            print(friends_dict)
    else:
        print("No one is going to be lucky")
        print(friends_dict)