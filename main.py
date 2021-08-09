import random


def get_input():
    while True:
        user_input = input("Enter your choice : ")
        if user_input in ["rock", "paper", "scissor"]:
            break
        print("Enter a valid CHOICE")
    return user_input


def rock_paper_scissor():
    user_point = 0
    computer_point = 0

    max_points = int(input("Enter the maximum point : "))
    while user_point+computer_point < max_points:
        computer_choice = random.choice(["rock", "paper", "scissor"])
        user_input = get_input()
        print(f"Computer Choice : {computer_choice}")

        conditions = [computer_choice == "scissor" and user_input == "rock", computer_choice == "rock" and user_input == "paper", computer_choice == "paper" and user_input == "scissor"]
        if any(conditions):
            print("User wins")
            user_point += 1
        elif user_input == computer_choice:
            pass
        else:
            print("Computer Wins")
            computer_point += 1
        # print(computer_choice)

    return computer_point, user_point


c, u = rock_paper_scissor()
print(f"Computer : {c}\nUser : {u}")
print("Computer Wins" if c > u else "User wins")
