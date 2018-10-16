
def main():
    board = ["*"] * 9
    players = select_players(board)
    start_game(players, board)

def print_board(board):
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])

def select_players(board):
	players = []
	while True:
		player = (str(input("Please, choose one option X or O : "))).upper()
		if player=='X' or player=='O':
			players.append(player)
			players.append("X" if player=="O" else "O")
			break
	print("Player 1: "+players[0])
	print("Player 2: "+players[1])
	return players

def start_game(players, board):
	print("Starting the game...")
	count=1
	player=0
	while True:
		position = input("Player "+players[player]+" ,Please, type a number between 1 and 9: ")
		if is_the_input_valid(position, board) == False:
			continue
		board[int(position)-1] = players[player]
		if has_won(players[player], board):
			print_board(board)
			print("Winner "+players[player]+" !!!")
			break
		if count==9:
			break
		count=count+1
		player = get_next_player(player)
		print_board(board)

def is_the_input_valid(position, board):
	if position.isdigit() == False:
		return False
	position = int(position)
	return position>=1 and position<=9 and board[position-1]!="X" and board[position-1]!="O"

def get_next_player(player):
	return 1 if player == 0 else 0

def has_won(player, board):
	return is_horizontal_alike(player, board) or is_vertical_alike(player, board) or is_diagonal_alike(player, board)

def is_horizontal_alike(player, board):
	if player==board[0]==board[1]==board[2]:
		return True
	if player==board[3]==board[4]==board[5]:
		return True
	if player==board[6]==board[7]==board[8]:
		return True
	return False

def is_vertical_alike(player, board):
	if player==board[0]==board[3]==board[6]:
		return True
	if player==board[1]==board[4]==board[7]:
		return True
	if player==board[2]==board[6]==board[8]:
		return True
	return False

def is_diagonal_alike(player, board):
	if player==board[0]==board[4]==board[8]:
		return True
	if player==board[2]==board[4]==board[6]:
		return True
	return False

"""
ToDo:
1. Play again the computer
2. CHeck if clear the console every time when the user play
3. Ask to play again as soon as the game finished
"""

if __name__ == "__main__":
	main()