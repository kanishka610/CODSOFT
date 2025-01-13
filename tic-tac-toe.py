import tkinter as tk
import math


root = tk.Tk()
root.title("Tic-Tac-Toe")


board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'O'  # Human starts as 'O'
game_over = False


# Function to handle a button click (human move)
def human_move(row, col, button):
    global current_player, game_over
    if board[row][col] == ' ' and not game_over:
        board[row][col] = 'O'
        button.config(text='O', state='disabled', disabledforeground='blue') 
        if check_winner(board):
            display_winner("You win! 🎉")
        elif is_full(board):
            display_winner("It's a draw!")
        else:
            current_player = 'X'  
            root.after(500, ai_move) 


# Check if the current player has won
def check_winner(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True
    return False


# Check if the board is full
def is_full(board):
    return all(cell != ' ' for row in board for cell in row)


# Display the winner message
def display_winner(message):
    global game_over
    game_over = True
    label.config(text=message)


# AI's move using Minimax Algorithm
def ai_move():
    global current_player
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        row, col = best_move
        board[row][col] = 'X'
        buttons[row][col].config(text='X', state='disabled', disabledforeground='red')  
        if check_winner(board):
            display_winner("AI wins! 🤖")
        elif is_full(board):
            display_winner("It's a draw!")
        else:
            current_player = 'O'  


# Minimax Algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    score = evaluate(board)
    if score != 0 or is_full(board):
        return score

    if is_maximizing:  
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:  
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


# Evaluate the board for Minimax
def evaluate(board):
    winner = check_winner(board)
    if winner:
        if current_player == 'X':
            return 1  
        else:
            return -1  
    return 0  


# Function to restart the game
def restart_game():
    global board, current_player, game_over
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'O'  
    game_over = False 
    label.config(text="Your turn!")  
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state='normal')  


# Create the game board
buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=' ', font=('normal', 40), width=5, height=2,
                                  command=lambda row=i, col=j: human_move(row, col, buttons[row][col]))
        buttons[i][j].grid(row=i, column=j)

# Display message label at the top
label = tk.Label(root, text="Your turn!", font=('normal', 20))
label.grid(row=3, column=0, columnspan=3)

# Restart button
restart_button = tk.Button(root, text="Restart Game", font=('normal', 15), command=restart_game)
restart_button.grid(row=4, column=0, columnspan=3)

# Start the game
root.mainloop()
