import random

print('🎮 Welcome to Rock Paper and Scissor 🎮\n')
print('Now understand the rules of the game...\n')
print('🪨 Rock Vs 📄 Paper -> 📄 Paper wins')
print('🪨 Rock Vs ✂️ Scissor -> 🪨 Rock wins')
print('📄 Paper Vs ✂️ Scissor -> ✂️ Scissor wins')

Emoji = {1: '🪨 Rock', 2: '📄 Paper', 3: '✂️ Scissor'}

# Initialize scores and game counter
user_score = 0
computer_score = 0
game_count = 0

while True:
    print("\nEnter your choice \n 1 - 🪨 Rock \n 2 - 📄 Paper \n 3 - ✂️ Scissor \n")
    
    # User input and validation
    choice = int(input("Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice: "))
    
    choice_name = Emoji[choice]
    print("\nYour choice is:", choice_name)
    print("Now it's the computer's turn...")
    
    # Computer's random choice
    comp_choice = random.randint(1, 3)
    comp_choice_name = Emoji[comp_choice]
    
    print("Computer's choice is:", comp_choice_name)
    print(f"{choice_name} Vs {comp_choice_name}")
    
    # Determine the winner of the current round
    if choice == comp_choice:
        res = "Draw!!"
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 1):
        res = '📄 Paper'
    elif (choice == 1 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        res = '🪨 Rock'
    elif (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 2):
        res = '✂️ Scissor'
    
    # Update scores and print round result
    if res == 'Draw!!':
        print("\n<== 🤝 It's a tie ==>")
    elif res == choice_name:
        print("\n<== 🎉 You win this round! 🏆 ==>")
        user_score += 1
    else:
        print("\n<== 😢 Computer wins this round! ==>")
        computer_score += 1
    
    # Increment game count
    game_count += 1
    
    # Check if the minimum of 5 games is reached
    if game_count >= 5:
        print(f"\nGame {game_count} completed!")
        print(f"Your score: {user_score}")
        print(f"Computer's score: {computer_score}")
        
        # Declare the overall winner
        if user_score > computer_score:
            print("\n<== 🎉 Congratulations! You are the overall winner! 🏆 ==>")
        elif user_score < computer_score:
            print("\n<== 😢 Computer is the overall winner! Better luck next time! ==>")
        else:
            print("\n<== 🤝 It's an overall tie! Great game! ==>")
        
        # Ask if the user wants to continue playing
        print("\nDo you want to play more games? (Y/N)")
        ans = input().lower()
        if ans == 'n':
            break
        else:
            # Reset scores and game counter if the user continues
            user_score = 0
            computer_score = 0
            game_count = 0

print("\n🙏 Thanks for playing! See you next time! 🎮")
