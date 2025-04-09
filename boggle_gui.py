from tkinter import *
import random

SIZE = 4
alphabet = "AAAAAABBCCDDDEEEEEEEEEEEFFGGHHHHHIIIIIIJKLLLLMMNNNNNNOOOOOOOPPQRRRRRSSSSSSTTTTTTTTTUUUVVWWWXYYYZ"
TIMER_DURATION = 60  # Game time in seconds

class BoggleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Search Game")

        # Initialize board
        self.board = [[random.choice(alphabet) for _ in range(SIZE)] for _ in range(SIZE)]

        self.user_words = set()
        self.score = 0
        self.time_left = TIMER_DURATION
        self.current_word = ""
        self.clicked_buttons = []

        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        self.board_frame = Frame(self.root)
        self.board_frame.pack(pady=10)

        self.letter_buttons = []
        for i in range(SIZE):
            row_buttons = []
            for j in range(SIZE):
                button = Button(self.board_frame, 
                                text=self.board[i][j], 
                                font=("Courier", 18), 
                                width=4, 
                                height=2,
                                command=lambda r=i, c=j: self.letter_clicked(r, c))
                button.grid(row=i, column=j, padx=2, pady=2)
                row_buttons.append(button)
            self.letter_buttons.append(row_buttons)

        self.current_word_label = Label(self.root, text="Current Word: ", font=("Courier", 16))
        self.current_word_label.pack(pady=5)

        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=5)

        self.submit_button = Button(self.button_frame, text="Submit Word", command=self.submit_word)
        self.submit_button.pack(side=LEFT, padx=5)

        self.clear_button = Button(self.button_frame, text="Clear Word", command=self.clear_current_word)
        self.clear_button.pack(side=LEFT, padx=5)

        self.score_label = Label(self.root, text=f"Score: {self.score}", font=("Courier", 16))
        self.score_label.pack(pady=5)

        self.timer_label = Label(self.root, text=f"Time Left: {self.time_left}s", font=("Courier", 16), fg="red")
        self.timer_label.pack(pady=5)

        self.result_label = Label(self.root, text="", font=("Courier", 14))
        self.result_label.pack(pady=5)

        self.words_frame = Frame(self.root)
        self.words_frame.pack(pady=10, fill=BOTH, expand=True)

        Label(self.words_frame, text="Words Found:", font=("Courier", 14)).pack(anchor=W)

        self.words_listbox = Listbox(self.words_frame, font=("Courier", 12), height=5)
        self.words_listbox.pack(fill=BOTH, expand=True)

        self.end_button = Button(self.root, text="End Game", command=self.end_game)
        self.end_button.pack(pady=10)

    def letter_clicked(self, row, col):
        if self.time_left <= 0:
            return
        self.current_word += self.board[row][col]
        self.current_word_label.config(text=f"Current Word: {self.current_word}")
        button = self.letter_buttons[row][col]
        button.config(bg="lightblue")
        self.clicked_buttons.append(button)

    def clear_current_word(self):
        self.current_word = ""
        self.current_word_label.config(text="Current Word: ")
        for button in self.clicked_buttons:
            button.config(bg="SystemButtonFace")
        self.clicked_buttons = []

    def submit_word(self):
        word = self.current_word.lower()
        if not word:
            return
        if word not in self.user_words and len(word) >= 3:
            self.user_words.add(word)
            self.words_listbox.insert(END, word)
            self.result_label.config(text=f"Submitted: {word}", fg="black")
        else:
            self.result_label.config(text=f"Already submitted or too short.", fg="gray")
        self.clear_current_word()

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        end_message = f"Game Over! Final Words: {len(self.user_words)}"
        self.result_label.config(text=end_message, fg="blue")
        for row in self.letter_buttons:
            for button in row:
                button.config(state=DISABLED)
        self.submit_button.config(state=DISABLED)
        self.clear_button.config(state=DISABLED)
        self.end_button.config(state=DISABLED)

if __name__ == "__main__":
    root = Tk()
    game = BoggleGame(root)
    root.mainloop()
