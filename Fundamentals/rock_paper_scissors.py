from random import randint


moves = ['rock', 'paper','scissors']

  #rules : rock > sscissors, scissors > paper, ppaper > rock

while True:
    computer = moves [randint(0,2)]
    user = input("rock, paper, scissors? or quit? ").lower()
    if user == "quit":
        print("Game has ended.")
        break
    elif user == computer:
        print('It\'s a tie')
    elif user == 'rock':
         if computer == 'paper':
          print('You loose!', computer, 'beats', user)
         else:
             print("You win!", user, "beats", computer)
    elif user == 'paper':
         if computer == 'scissors':
            print('You loose!', computer, 'beats', user)
         else:
            print("You win!", user, "beats", computer)

    elif user == 'scissors':
         if computer == 'rock':
            print('You loose!', computer, 'beats', user)
         else:
            print("You win!", user, "beats", computer)
    else:
        print('Check your spelling.')