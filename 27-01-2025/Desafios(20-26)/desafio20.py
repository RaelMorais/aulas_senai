import re

class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False

    def valid_move(self, start, end, board):
        raise NotImplementedError

class Pawn(Piece):
    def valid_move(self, start, end, board):
        sr, sc = start
        er, ec = end
        direction = 1 if self.color == 'white' else -1

        if sc == ec and er == sr + direction and board[er][ec] is None:
            return True
 
        if not self.has_moved and sc == ec and er == sr + 2 * direction and board[sr + direction][sc] is None and board[er][ec] is None:
            return True
 
        if abs(sc - ec) == 1 and er == sr + direction and board[er][ec] and board[er][ec].color != self.color:
            return True
   
        if abs(sc - ec) == 1 and er == sr + direction and board[er][ec] is None and board.en_passant_target == (er, ec):
            return True
        return False

class Rook(Piece):
    def valid_move(self, start, end, board):
        sr, sc = start
        er, ec = end
        if sr != er and sc != ec:
            return False
        step_r = 0 if sr == er else (1 if er > sr else -1)
        step_c = 0 if sc == ec else (1 if ec > sc else -1)
        r, c = sr + step_r, sc + step_c
        while r != er or c != ec:
            if board[r][c] is not None:
                return False
            r += step_r
            c += step_c
        return board[er][ec] is None or board[er][ec].color != self.color

class Knight(Piece):
    def valid_move(self, start, end, board):
        sr, sc = start
        er, ec = end
        dr, dc = abs(er - sr), abs(ec - sc)
        return (dr, dc) in [(2, 1), (1, 2)] and (board[er][ec] is None or board[er][ec].color != self.color)

class Bishop(Piece):
    def valid_move(self, start, end, board):
        sr, sc = start
        er, ec = end
        if abs(er - sr) != abs(ec - sc):
            return False
        dr = 1 if er > sr else -1
        dc = 1 if ec > sc else -1
        r, c = sr + dr, sc + dc
        while r != er and c != ec:
            if board[r][c] is not None:
                return False
            r += dr
            c += dc
        return board[er][ec] is None or board[er][ec].color != self.color

class Queen(Piece):
    def valid_move(self, start, end, board):
        return Rook(self.color).valid_move(start, end, board) or Bishop(self.color).valid_move(start, end, board)

class King(Piece):
    def valid_move(self, start, end, board):
        sr, sc = start
        er, ec = end
        dr, dc = abs(er - sr), abs(ec - sc)
        # Standard move
        if dr <= 1 and dc <= 1 and (dr > 0 or dc > 0):
            return board[er][ec] is None or board[er][ec].color != self.color
        # Castling
        if not self.has_moved and sr == er and abs(ec - sc) == 2 and not board.in_check(self.color):
            rook_col = 7 if ec > sc else 0
            rook = board[sr][rook_col]
            if isinstance(rook, Rook) and not rook.has_moved:
                step = 1 if ec > sc else -1
                for c in range(sc + step, rook_col, step):
                    if board[sr][c] is not None or board.is_square_attacked((sr, c), self.color):
                        return False
                return True
        return False

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.en_passant_target = None
        self.setup_board()

    def setup_board(self):
        for col in range(8):
            self.board[1][col] = Pawn('white')
            self.board[6][col] = Pawn('black')
        pieces = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for col, piece in enumerate(pieces):
            self.board[0][col] = piece('white')
            self.board[7][col] = piece('black')

    def move_piece(self, start, end, promote_to='queen'):
        sr, sc = start
        er, ec = end
        piece = self.board[sr][sc]
        if not piece or not piece.valid_move(start, end, self):
            print("Movimento inválido!")
            return False
   
        temp = self.board[er][ec]
        self.board[er][ec] = piece
        self.board[sr][sc] = None
        if self.in_check(piece.color):
            self.board[sr][sc] = piece
            self.board[er][ec] = temp
            print("Movimento deixa rei em xeque!")
            return False
    
        if isinstance(piece, Pawn) and end == self.en_passant_target:
            self.board[sr][ec] = None
      
        self.en_passant_target = None
        if isinstance(piece, Pawn) and abs(er - sr) == 2:
            self.en_passant_target = (sr + (1 if piece.color == 'white' else -1), sc)
        
        if isinstance(piece, King) and abs(ec - sc) == 2:
            rook_col = 7 if ec > sc else 0
            new_rook_col = 5 if ec > sc else 3
            self.board[sr][new_rook_col] = self.board[sr][rook_col]
            self.board[sr][rook_col] = None
      
        if isinstance(piece, Pawn) and er in (0, 7):
            self.board[er][ec] = {'queen': Queen, 'rook': Rook, 'bishop': Bishop, 'knight': Knight}[promote_to](piece.color)
        piece.has_moved = True
        return True

    def in_check(self, color):
        king_pos = None
        for r in range(8):
            for c in range(8):
                if isinstance(self.board[r][c], King) and self.board[r][c].color == color:
                    king_pos = (r, c)
                    break
            if king_pos:
                break
        return self.is_square_attacked(king_pos, color) if king_pos else False

    def is_square_attacked(self, pos, color):
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color != color and piece.valid_move((r, c), pos, self):
                    return True
        return False

    def is_checkmate(self, color):
        if not self.in_check(color):
            return False
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color == color:
                    for er in range(8):
                        for ec in range(8):
                            if piece.valid_move((r, c), (er, ec), self):
                                temp = self.board[er][ec]
                                self.board[er][ec] = piece
                                self.board[r][c] = None
                                in_check = self.in_check(color)
                                self.board[r][c] = piece
                                self.board[er][ec] = temp
                                if not in_check:
                                    return False
        return True

    def display(self):
        print('  a b c d e f g h')
        for r in range(7, -1, -1):
            row = f'{r + 1} '
            for c in range(8):
                piece = self.board[r][c]
                if piece is None:
                    row += '. '
                else:
                    symbol = {'Pawn': 'p', 'Rook': 'r', 'Knight': 'n', 'Bishop': 'b', 'Queen': 'q', 'King': 'k'}
                    row += symbol[piece.__class__.__name__].upper() if piece.color == 'white' else symbol[piece.__class__.__name__]
                    row += ' '
            print(row)
        print()

def algebraic_to_coords(move):
    if not re.match(r'[a-h][1-8][a-h][1-8]', move):
        return None
    sc = ord(move[0]) - ord('a')
    sr = int(move[1]) - 1
    ec = ord(move[2]) - ord('a')
    er = int(move[3]) - 1
    return (sr, sc), (er, ec)

def play_chess():
    board = Board()
    current_color = 'white'
    while True:
        board.display()
        print(f"{current_color.capitalize()}'s turn. Enter move (e.g., e2e4) or 'quit':")
        move = input().strip()
        if move.lower() == 'quit':
            break
        coords = algebraic_to_coords(move)
        if not coords:
            print("Invalid move format! Use e.g., e2e4.")
            continue
        start, end = coords
        piece = board.board[start[0]][start[1]]
        if not piece or piece.color != current_color:
            print("Invalid piece or not your turn!")
            continue
        promote_to = 'queen'
        if isinstance(piece, Pawn) and end[0] in (0, 7):
            promote_to = input("Promote to (queen/rook/bishop/knight): ").lower()
            if promote_to not in ['queen', 'rook', 'bishop', 'knight']:
                promote_to = 'queen'
        if board.move_piece(start, end, promote_to):
            if board.is_checkmate('black' if current_color == 'white' else 'white'):
                board.display()
                print(f"Checkmate! {current_color.capitalize()} wins!")
                break
            current_color = 'black' if current_color == 'white' else 'white'

if __name__ == "__main__":
    play_chess()