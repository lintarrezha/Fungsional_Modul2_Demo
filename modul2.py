import random

# Fungsi untuk mengenerate posisi awal bidak dan goals secara acak
def generate_positions(board_size):
    for _ in range(3):  # Maksimal 3 percobaan
        piece_position = (random.randint(0, board_size - 1),
                          random.randint(0, board_size - 1))
        goal_position = (random.randint(0, board_size - 1),
                         random.randint(0, board_size - 1))
        if piece_position != goal_position:
            return piece_position, goal_position
    raise Exception(
        "Gagal menghasilkan posisi yang berbeda setelah 3 percobaan.")

# Fungsi untuk membuat papan permainan
def create_board(board_size, piece_position, goal_position):
    board = [[' - ' for _ in range(board_size)] for _ in range(board_size)]
    row, col = piece_position
    board[row][col] = ' A '
    row, col = goal_position
    board[row][col] = ' O '
    return board

# Fungsi untuk menampilkan papan permainan
def display_board(board):
    for row in board:
        print(" ".join(row))

# Fungsi untuk memeriksa apakah permainan selesai atau belum
def is_game_over(piece_position, goal_position):
    return piece_position == goal_position

# Fungsi untuk memindahkan bidak
def move_piece(board, piece_position, move):
    new_position = list(piece_position)
    if move == 'w':
        new_position[0] -= 1
    elif move == 's':
        new_position[0] += 1
    elif move == 'a':
        new_position[1] -= 1
    elif move == 'd':
        new_position[1] += 1

    if 0 <= new_position[0] < len(board) and 0 <= new_position[1] < len(board[0]):
        board[piece_position[0]][piece_position[1]] = ' - '
        board[new_position[0]][new_position[1]] = ' A '
        return tuple(new_position)
    return piece_position


if __name__ == '__main__':
    board_size = int(input("Masukkan lebar papan: "))
    max_attempts = 3
    attempts = 0

    piece_position, goal_position = generate_positions(board_size)
    board = create_board(board_size, piece_position, goal_position)
    display_board(board)

    while attempts < max_attempts:
        moves = input("Apakah Anda ingin mengacak papan lagi? (y/n): ")
        if moves.lower() == 'y':
            piece_position, goal_position = generate_positions(board_size)
            board = create_board(board_size, piece_position, goal_position)
            display_board(board)
            attempts += 1
        else:
            break

    if attempts == max_attempts:
        print("Anda telah mencoba maksimal 3 kali. Permainan dimulai.")
    
    moves = input("Masukkan perintah (contoh: aaww): ")
    for move in moves:
        piece_position = move_piece(board, piece_position, move)
        display_board(board)
        if is_game_over(piece_position, goal_position):
            print("Anda menang!")
            break
    else:
        print("Kalah. Anda tidak mencapai tujuan.")

