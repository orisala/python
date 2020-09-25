is_correct_choice = False 

while not is_correct_choice:
    choice = input("Guess a key ")

    if choice == 'r' :
        print("You win!")
        is_correct_choice = True
        