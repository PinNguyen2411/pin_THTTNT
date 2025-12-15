class TicTacToe:
    def __init__(self, size):
        self.size = size
        self.board = [' ' for _ in range(size * size)] # Mảng 1 chiều
        self.human = 'X'
        self.ai = 'O'

    def print_board(self):
        print("\n  " + "   ".join([str(i) for i in range(self.size)])) # In số cột
        print("  " + "-" * (self.size * 4 + 1))
        for i in range(self.size):
            row = self.board[i * self.size : (i + 1) * self.size]
            print(f"{i} | " + " | ".join(row) + " |") # In số hàng
            print("  " + "-" * (self.size * 4 + 1))

    def is_winner(self, player):
        n = self.size
        b = self.board
        # Kiểm tra hàng, cột, chéo (như cũ)
        for row in range(n):
            if all(b[row * n + col] == player for col in range(n)): return True
        for col in range(n):
            if all(b[row * n + col] == player for row in range(n)): return True
        if all(b[i * n + i] == player for i in range(n)): return True
        if all(b[i * n + (n - 1 - i)] == player for i in range(n)): return True
        return False

    def is_full(self):
        return ' ' not in self.board

    def minimax(self, depth, is_maximizing, max_depth):
        if self.is_winner(self.ai): return 100 - depth
        if self.is_winner(self.human): return depth - 100
        if self.is_full(): return 0
        if depth >= max_depth: return 0

        if is_maximizing:
            best_score = -10000
            for i in range(self.size * self.size):
                if self.board[i] == ' ':
                    self.board[i] = self.ai
                    score = self.minimax(depth + 1, False, max_depth)
                    self.board[i] = ' '
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = 10000
            for i in range(self.size * self.size):
                if self.board[i] == ' ':
                    self.board[i] = self.human
                    score = self.minimax(depth + 1, True, max_depth)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def best_move(self):
        best_score = -10000
        move = -1
        current_max_depth = 9 if self.size == 3 else 3 # Giảm depth nếu bàn cờ lớn
        
        for i in range(self.size * self.size):
            if self.board[i] == ' ':
                self.board[i] = self.ai
                score = self.minimax(0, False, current_max_depth)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move

# --- PHẦN DEMO (MAIN) ĐÃ CẬP NHẬT ---
if __name__ == "__main__":
    print("\n=== DEMO MINIMAX (NHẬP HÀNG/CỘT) ===")
    
    while True:
        try:
            sz = int(input("Nhập kích thước bàn cờ (ví dụ 3): "))
            if sz < 3: print("Kích thước tối thiểu là 3!"); continue
            break
        except ValueError:
            print("Nhập số nguyên!"); continue

    game = TicTacToe(sz)
    print(f"\nBắt đầu game {sz}x{sz}. Bạn là X, Máy là O.")
    print("Lưu ý: Hàng và Cột bắt đầu từ số 0.")

    while True:
        game.print_board()
        if game.is_winner(game.human): print(" Bạn thắng!"); break
        if game.is_winner(game.ai): print(" Máy thắng!"); break
        if game.is_full(): print(" Hòa!"); break

        # --- PHẦN NHẬP LIỆU HÀNG/CỘT MỚI ---
        try:
            print(f"Đến lượt bạn:")
            r = int(input(f"   - Nhập Hàng (0-{sz-1}): "))
            c = int(input(f"   - Nhập Cột  (0-{sz-1}): "))
            
            # Kiểm tra tọa độ hợp lệ
            if r < 0 or r >= sz or c < 0 or c >= sz:
                print(f"⚠️ Tọa độ không hợp lệ! Hãy nhập từ 0 đến {sz-1}.")
                continue
            
            # Quy đổi từ (Hàng, Cột) -> Chỉ số mảng 1 chiều
            move_index = r * sz + c

            if game.board[move_index] == ' ':
                game.board[move_index] = game.human
                
                # Máy đi
                if not game.is_winner(game.human) and not game.is_full():
                    print("Máy đang tính toán...")
                    ai_move = game.best_move()
                    game.board[ai_move] = game.ai
            else:
                print("⚠️ Ô này đã có người đánh rồi!")

        except ValueError:
            print("⚠️ Vui lòng nhập số nguyên!")