import random

# available moves and score counters
moves = ['stone', 'paper', 'scissors']
player_score = 0
computer_score = 0
ties = 0
rounds = 0


def winner(user, comp):
    if user == comp:
        return 'tie'
    if (user == 'stone' and comp == 'scissors') or (user == 'paper' and comp == 'stone') or (user == 'scissors' and comp == 'paper'):
        return 'player'
    return 'computer'


while True:
    print('\nstone, paper, scissors')
    print('1. Play round')
    print('2. Show score')
    print('3. Reset score')
    print('4. Quit')
    choice = input('Choose option: ').strip()

    if choice == '1':
        user = input('Enter stone, paper, or scissors: ').lower().strip()
        if user not in moves:
            print('Invalid choice, try again.')
            continue
        comp = random.choice(moves)
        print(f'computer chose: {comp}')
        result = winner(user, comp)
        if result == 'player':
            print('You win this round!')
            player_score += 1
        elif result == 'computer':
            print('Computer wins this round!')
            computer_score += 1
        else:
            print('This round is a tie!')
            ties += 1
        rounds += 1
    elif choice == '2':
        print(f"\nScore -> you:{player_score} | computer:{computer_score} | ties:{ties} | rounds:{rounds}")
    elif choice == '3':
        player_score = computer_score = ties = rounds = 0
        print('Score reset.')
    elif choice == '4':
        print('Thanks for playing!')
        break
    else:
        print('Invalid option, try again.')