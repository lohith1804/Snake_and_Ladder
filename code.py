import random
def dice_roll():
    #Generating random numbers between 1-6 after rolling a dice
    return random.randint(1,6)

def play_turn(player,pos,snakes,ladders):
    flag=0
    # which player turn
    print(f"{player}'s turn:")
    input("Press Enter to roll the dice...")
    dice=dice_roll()
    print(f"{player} rolled a {dice}!")

    # Update the position
    nochange=pos
    pos+=dice
    
    if pos>100:
        pos=nochange  # Nochange in position if greater than 100

    # Check for snakes or ladders in the players position
    if pos in snakes:
        print(f"Player {player} landed on a snake and get back to {snakes[pos]}.")
        pos=snakes[pos]
    elif pos in ladders:
        print(f"Player {player} climbed a ladder to {ladders[pos]}.")
        pos=ladders[pos]
        flag=1

    print(f"{player} is now on square {pos}.")
    print("-----------------------------------")

    if dice == 6:
        print(f"{player} rolled a 6! They get another turn!")
        pos = play_turn(player, pos, snakes, ladders)
    elif flag==1:
        print(f"{player} climbed ladder! They get another turn!")
        pos = play_turn(player, pos, snakes, ladders)

    return pos

def display_board(snakes, ladders, player_positions, players):
    #Displays the 10x10 board with snakes, ladders, and players.
    board = [["" for _ in range(10)] for _ in range(10)]
    
    # Generating a 10x10 matric representing Snake and ladders board
    num=100
    for i in range(10):
        for j in range(10):
            board[i][j]=str(num)
            num-=1
        if i % 2 != 0:
            board[i].reverse()

    # Representing the snakes and ladders on the board
    for start, end in snakes.items():
        for i in range(10):
            for j in range(10):
                if board[i][j]==str(start):
                    board[i][j]=f"S{end}"
    for start, end in ladders.items():
        for i in range(10):
            for j in range(10):
                if board[i][j]==str(start):
                    board[i][j]=f"L{end}"

    #Representing the position of the players
    for i, position in enumerate(player_positions):
        for r in range(10):
            for c in range(10):
                if board[r][c]==str(position):
                    board[r][c]+=f"({players[i]})"

    # Printing the board
    for row in board:
        print("\t".join(row))

def main():
    """Main function to play the Snake and Ladders game."""
    print("Snake and Ladders!")

    # positions of snakes and ladders
    snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75}
    ladders = {4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 96}

    
    no_of_player = int(input("Enter the number of players (2-5): "))
    if no_of_player < 2 or no_of_player > 5:
        print("Invalid number of players! Please enter between 2 and 5.")
        return
    #generating the names of players as A, B, C.....
    players = [chr(65 + i) for i in range(no_of_player)]
    #Players position at initial stage
    player_pos = [0] * no_of_player

    # Main game loop
    while True:
        display_board(snakes, ladders, player_pos, players)
        for i, position in enumerate(player_pos):
            player_name = players[i]
            player_pos[i] = play_turn(player_name, position, snakes, ladders)

            # Checking for win condition
            if player_pos[i] == 100:
                print(f"Congratulations! {player_name} wins the game!")
                return

if __name__ == "__main__":
    main()
