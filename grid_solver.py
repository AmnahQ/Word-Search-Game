import my_trie
from collections import Counter

#getting all words from dictionary
file = open("words - old.txt", 'r')
dictionary = []
# words must be of length >= 3
for word in file:
    # accounts for new line character
    if len(word) < 4:
        continue
    # and removes new line character
    dictionary.append(word[:-1])

# putting all words in the dictionary in a trie
trie = my_trie.Trie()
trie.trie_add(dictionary)


#this takes the board and makes the set of all wordss that are valid
def solve_board(board, trie=trie):
    make_lower_case(board)
    
    # Get all letters from the board
    all_letters = []
    for row in board:
        for letter in row:
            all_letters.append(letter)
    
    # Count frequency of each letter on the board
    board_letter_counts = Counter(all_letters)
    
    # Check each dictionary word to see if it can be made from board letters
    solutions = set()
    
    # For efficiency, first extract all possible words from trie
    all_possible_words = extract_all_words(trie.root)
    
    for word in all_possible_words:
        word_letter_counts = Counter(word)
        
        # Check if all letters in the word can be found on the board
        can_form = True
        for letter, count in word_letter_counts.items():
            if count > board_letter_counts.get(letter, 0):
                can_form = False
                break
        
        if can_form:
            solutions.add(word)
    
    return solutions


# Extract all words from the trie
def extract_all_words(node, prefix=""):
    words = []
    
    if node.complete:
        words.append(node.complete)
    
    for child in node.children:
        words.extend(extract_all_words(child, prefix + child.value))
    
    return words

#convertign to lower case so that there is no inconsistency
def make_lower_case(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j] = mat[i][j].lower()


if __name__ == "__main__":
    # An example  board
    board = \
    [['s', 't'], 
     ['p', 'o']]

    result = solve_board(board)
    print(result)
