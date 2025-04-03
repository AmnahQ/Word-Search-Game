from tkinter import *
import random
import boggle_solver

SIZE = 4
alphabet = "AAAAAABBCCDDDEEEEEEEEEEEFFGGHHHHHIIIIIIJKLLLLMM" + \
           "NNNNNNOOOOOOOPPQRRRRRSSSSSSTTTTTTTTTUUUVVWWWXYYYZ"
TIMER_DURATION = 60  # Game time in seconds

class BoggleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Boggle Game")

        # Initialize board
        self.board = [[random.choice(alphabet) for _ in range(SIZE)] for _ in range(SIZE)]
        print("\nGenerated Boggle Board:")
        for row in self.board:
            print(" ".join(row))  # Print board for debugging
        
        # Try to generate valid words and catch potential errors
        try:
            print("\nSolving Boggle board...")
            self.valid_words = set(word.lower() for word in boggle_solver.solve_boggle(self.board))
            print("\nValid Words Found:", self.valid_words)  # Debugging line
        except Exception as e:
            print("Error in boggle_solver:", e)
            self.valid_words = set()  # Prevent crash if solver fails

        self.user_words = set()
        self.score = 0
        self.time_left = TIMER_DURATION
        
        # Track the current word being built and clicked letters
        self.current_word = ""
        self.clicked_buttons = []

        self.create_widgets()
        self.update_timer()

    def create_widgets(self):
        self.board_frame = Frame(self.root)
        self.board_frame.pack(pady=10)

        # Store references to the letter buttons
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

        # Current word display
        self.current_word_label = Label(self.root, text="Current Word: ", font=("Courier", 16))
        self.current_word_label.pack(pady=5)

        # Submit and Clear buttons
        self.button_frame = Frame(self.root)
        self.button_frame.pack(pady=5)
        
        self.submit_button = Button(self.button_frame, text="Submit Word", command=self.submit_word)
        self.submit_button.pack(side=LEFT, padx=5)
        
        self.clear_button = Button(self.button_frame, text="Clear Word", command=self.clear_current_word)
        self.clear_button.pack(side=LEFT, padx=5)

        # Game info display
        self.score_label = Label(self.root, text=f"Score: {self.score}", font=("Courier", 16))
        self.score_label.pack(pady=5)

        self.timer_label = Label(self.root, text=f"Time Left: {self.time_left}s", font=("Courier", 16), fg="red")
        self.timer_label.pack(pady=5)

        self.result_label = Label(self.root, text="", font=("Courier", 14))
        self.result_label.pack(pady=5)

        # Words found display
        self.words_frame = Frame(self.root)
        self.words_frame.pack(pady=10, fill=BOTH, expand=True)
        
        Label(self.words_frame, text="Words Found:", font=("Courier", 14)).pack(anchor=W)
        
        self.words_listbox = Listbox(self.words_frame, font=("Courier", 12), height=5)
        self.words_listbox.pack(fill=BOTH, expand=True)

        self.end_button = Button(self.root, text="End Game", command=self.end_game)
        self.end_button.pack(pady=10)

    def letter_clicked(self, row, col):
        """Handle letter button clicks to build words"""
        if self.time_left <= 0:
            return  # Don't allow clicks after game ends
            
        # Add the letter to the current word
        self.current_word += self.board[row][col]
        self.current_word_label.config(text=f"Current Word: {self.current_word}")
        
        # Highlight the clicked button
        button = self.letter_buttons[row][col]
        button.config(bg="lightblue")
        self.clicked_buttons.append(button)

    def clear_current_word(self):
        """Clear the current word being built"""
        self.current_word = ""
        self.current_word_label.config(text="Current Word: ")
        
        # Reset button colors
        for button in self.clicked_buttons:
            button.config(bg="SystemButtonFace")  # Default button color
        self.clicked_buttons = []

    def submit_word(self):
        """Submit the currently built word"""
        word = self.current_word.lower()
        
        if not word:
            return
            
        print(f"\nSubmitting Word: {word}")  # Debugging input word
        print(f"Word in valid words?: {word in self.valid_words}")

        if word in self.valid_words and word not in self.user_words and len(word) >= 3:
            self.user_words.add(word)
            self.score += self.calculate_score(word)
            self.score_label.config(text=f"Score: {self.score}")
            self.result_label.config(text=f"Correct: {word}", fg="green")
            # Add to the listbox
            self.words_listbox.insert(END, f"{word} (+{self.calculate_score(word)})")
        else:
            if word in self.user_words:
                self.result_label.config(text=f"Already found: {word}", fg="orange")
            elif len(word) < 3:
                self.result_label.config(text=f"Too short: {word}", fg="red")
            else:
                self.result_label.config(text=f"Invalid: {word}", fg="red")
                
        # Clear the current word after submission
        self.clear_current_word()

    def calculate_score(self, word):
        length = len(word)
        if length == 3 or length == 4:
            return 1
        elif length == 5:
            return 2
        elif length == 6:
            return 3
        elif length >= 7:
            return 5
        return 0

    def update_timer(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=f"Time Left: {self.time_left}s")
            self.root.after(1000, self.update_timer)
        else:
            self.end_game()

    def end_game(self):
        # Show game over message
        end_message = f"Game Over! Final Score: {self.score}"
        self.result_label.config(text=end_message, fg="blue")
        
        # Create a popup to show possible words
        popup = Toplevel(self.root)
        popup.title("Game Results")
        
        Label(popup, text=end_message, font=("Courier", 16, "bold")).pack(pady=10)
        Label(popup, text=f"You found {len(self.user_words)} words out of {len(self.valid_words)} possible words", 
              font=("Courier", 12)).pack(pady=5)
        
        # Show all possible words
        word_frame = Frame(popup)
        word_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        Label(word_frame, text="All Possible Words:", font=("Courier", 12, "bold")).pack(anchor=W)
        
        words_text = Text(word_frame, wrap=WORD, width=40, height=10)
        scrollbar = Scrollbar(word_frame, command=words_text.yview)
        words_text.config(yscrollcommand=scrollbar.set)
        
        words_text.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        # Insert words, highlighting the ones found by the user
        sorted_words = sorted(self.valid_words)
        for word in sorted_words:
            if word in self.user_words:
                words_text.insert(END, f"{word} ✓\n")
                words_text.tag_add("found", f"end-{len(word)+3}c", f"end-2c")
            else:
                words_text.insert(END, f"{word}\n")
                
        words_text.tag_config("found", foreground="green", font=("Courier", 12, "bold"))
        words_text.config(state=DISABLED)  # Make read-only
        
        # Disable game controls
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