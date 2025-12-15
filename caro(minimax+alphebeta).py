import math

class CaroAI:
    def __init__(self, size=3):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]

    def print_board(self):
        print("\n" + "\n".join([' | '.join(row) for row in self.board]))
        print("-" * (self.size * 4 - 1))

    def is_moves_left(self):
        return any(' ' in row for row in self.board)

    def check_winner(self, player):
        # Kiểm tra hàng, cột, đường chéo (Win khi đủ size quân)
        # 1. Hàng & Cột
        for i in range(self.size):
            if all(self.board[i][j] == player for j in range(self.size)) or \
               all(self.board[j][i] == player for j in range(self.size)):
                return True
        # 2. Đường chéo
        if all(self.board[i][i] == player for i in range(self.size)) or \
           all(self.board[i][self.size-1-i] == player for i in range(self.size)):
            return True
        return False

    def evaluate(self):
        if self.check_winner('O'): return 10
        if self.check_winner('X'): return -10
        return 0

    def minimax(self, depth, is_max, alpha, beta):
        score = self.evaluate()
        if score == 10 or score == -10: return score
        if not self.is_moves_left() or depth == 0: return 0

        if is_max: # Lượt máy (O)
            best = -math.inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'O'
                        best = max(best, self.minimax(depth-1, False, alpha, beta))
                        self.board[i][j] = ' '
                        alpha = max(alpha, best)
                        if beta <= alpha: return best # Cắt tỉa Alpha
            return best
        else: # Lượt người (X)
            best = math.inf
            for i in range(self.size):
                for j in range(self.size):
                    if self.board[i][j] == ' ':
                        self.board[i][j] = 'X'
                        best = min(best, self.minimax(depth-1, True, alpha, beta))
                        self.board[i][j] = ' '
                        beta = min(beta, best)
                        if beta <= alpha: return best # Cắt tỉa Beta
            return best

    def find_best_move(self, depth_limit):
        best_val = -math.inf
        best_move = (-1, -1)
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    move_val = self.minimax(depth_limit, False, -math.inf, math.inf)
                    self.board[i][j] = ' '
                    if move_val > best_val:
                        best_move = (i, j)
                        best_val = move_val
        return best_move

# --- DEMO ---
if __name__ == "__main__":
    n = int(input("1. Nhập kích thước bàn cờ : "))
    d = int(input("2. Nhập độ khó (Độ sâu suy nghĩ): "))
    game = CaroAI(n)
    
    while game.is_moves_left() and not game.check_winner('O') and not game.check_winner('X'):
        game.print_board()
        try:
            x, y = map(int, input(f"Nhập nước đi của bạn (0-{n-1} 0-{n-1}): ").split())
            if game.board[x][y] != ' ': continue
            game.board[x][y] = 'X'
            
            if game.check_winner('X'): break
            
            print("Máy đang tính toán...")
            move = game.find_best_move(d)
            if move != (-1, -1): game.board[move[0]][move[1]] = 'O'
        except: print("Lỗi nhập liệu!")

    game.print_board()
    print("Game Over! Bạn thắng" if game.check_winner('X') else "Game Over! Máy thắng" if game.check_winner('O') else "Hòa!")