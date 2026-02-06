import tkinter as tk
from tkinter import messagebox

# Main Tic Tac Toe Game Class
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)  # Disable resizing

        self.current_player = "X"
        self.board = [""] * 9  # 3x3 board as a list

        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(
                self.root,
                text="",
                font=("Arial", 24, "bold"),
                width=5,
                height=2,
                command=lambda i=i: self.make_move(i)
            )
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

        # Restart button
        restart_btn = tk.Button(
            self.root,
            text="Restart",
            font=("Arial", 14),
            command=self.reset_game
        )
        restart_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def make_move(self, index):
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.disable_buttons()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check if the current player has won
        win_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in win_combinations:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def disable_buttons(self):
        for btn in self.buttons:
            btn.config(state="disabled")

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        for btn in self.buttons:
            btn.config(text="", state="normal")


# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()