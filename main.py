
def main():
    global board
    board = ["*"] * 9
    print_board()
    players = select_player()
    print("Player 1: "+players[0])
    print("Player 2: "+players[1])


def print_board():
    print(board[0] + " " + board[1] + " " + board[2])
    print(board[3] + " " + board[4] + " " + board[5])
    print(board[6] + " " + board[7] + " " + board[8])

def select_player():
    players = []
    while True:
        player = str(input("Please, choose one option X or O : "))
        if player=='X' or player=='O':
            players.append(player)
            if player=='X':
                players.append("O")
            else:
                players.append("X")
            break
    return players

def play_game():
    print("Play a game")

main()