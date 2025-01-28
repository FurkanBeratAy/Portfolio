def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner(board):
    for i in range(3):
        if board[i][0]==board[i][1]== board[i][2]!= " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
        if board[0][0] == board[1][1] == board[2][2] != " ":
            return board [0][2]
        
        if all(cell != " " for row in board for cell in row):
            return"Draw"
        
        return None
def play():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X","O"]
    current_players = 0 

    print("Welcome to Tic Tac Toe Game")
    print_board(board)


    while True:
        print(f"Player {players[current_players]}'s turn")
        try:
            row = int(input("Enter the row (0,1,2): "))
            col= int(input("Enter the column (0,1,2): "))
        except ValueError:
            print("invalid")

        if 0<= row <= 2 and 0<= col <= 2 and board[row][col]== ' ':
            board[row][col]=players[current_players]
            print_board(board)

            winner = check_winner(board)
            if winner:
                if winner == "draw":
                    print("Its a draw")
                else:
                    print(f"Player{winner}wins!")
                break
            current_players = 1 -current_players
        else:
            print("Invalid")

play()