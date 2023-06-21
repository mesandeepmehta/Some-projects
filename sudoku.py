import tkinter as tk

class SudokuGame:
    def __init__(self):
        self.board = [[0] * 9 for _ in range(9)]
        self.root = tk.Tk()
        self.root.title("Sudoku")
        self.create_widgets()
        self.draw_board()

    def create_widgets(self):
        self.canvas = tk.Canvas(self.root, width=450, height=450)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.click_handler)
        self.solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        self.solve_button.pack()

    def draw_board(self):
        self.canvas.delete("all")

        # Draw grid lines
        for i in range(10):
            if i % 3 == 0:
                self.canvas.create_line(50 * i, 0, 50 * i, 450, width=2)
                self.canvas.create_line(0, 50 * i, 450, 50 * i, width=2)
            else:
                self.canvas.create_line(50 * i, 0, 50 * i, 450)
                self.canvas.create_line(0, 50 * i, 450, 50 * i)

        # Draw numbers
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != 0:
                    self.canvas.create_text(
                        25 + 50 * j,
                        25 + 50 * i,
                        text=str(self.board[i][j]),
                        font=("Arial", 20),
                    )

    def click_handler(self, event):
        row = event.y // 50
        col = event.x // 50
        self.canvas.delete("selected")

        if self.board[row][col] != 0:
            return

        self.canvas.create_rectangle(
            col * 50,
            row * 50,
            (col + 1) * 50,
            (row + 1) * 50,
            fill="light blue",
            outline="black",
            tags="selected",
        )

    def solve(self):
        if self.solve_sudoku():
            self.draw_board()

    def is_valid(self, row, col, num):
        # Check if the number already exists in the row
        for i in range(9):
            if self.board[row][i] == num:
                return False

        # Check if the number already exists in the column
        for i in range(9):
            if self.board[i][col] == num:
                return False

        # Check if the number already exists in the 3x3 grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[i + start_row][j + start_col] == num:
                    return False

        return True

    def solve_sudoku(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(row, col, num):
                            self.board[row][col] = num
                            if self.solve_sudoku():
                                return True
                            self.board[row][col] = 0
                    return False
        return True

def main():
    game = SudokuGame()
    game.root.mainloop()

if __name__ == "__main__":
    main()
