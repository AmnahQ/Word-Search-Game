#importing the basic trie structure
import my_trie
#used for counting letters later
from collections import Counter

#importing the dictionary we got from online
file = open("words.txt", 'r')

dictionary = []
# in order for word to be correct or even be considered:number of characters should be 4 or more

for i in file:

    if len(i) < 4:
        continue
    #we have to remove the new line because of the nature of our dictionary
    dictionary.append(i[:-1])

#initializing the trie which we have cereated in --> my_trie.py
trie = my_trie.Trie()
# then we add all the valid words to the tries like if its apple then it will go something like a->p->p and so on we are checking the prefic
# suppose we have AX.. so there is no prefix AX so we wouldnt check the whole string and stop immediatley
trie.add_to_trie(dictionary)


# Takes in a word search board and returns the set of valid words that can be made using the letters on the board No adjacency constraints - just check if the word can be formed
# using the available letters
# def solve_boggle(board, trie=trie):
#     #make all the entries of the board in lower case
#     make_lower_case(board)
    
#     #we get all the elements in the board and add it to one combined list
#     all_letters = []
#     for row in board:
#         for letter in row:
#             all_letters.append(letter)
    
#     # then we count how many alphabets appear how many times
#     board_letter_counts = Counter(all_letters)
#     # print(board_letter_counts)
    
#     #it make sure that the valid word is counted once
#     solutions = set()
    
#     # For efficiency, first extract all possible words from trie
#     all_possible_words = extract_all_words(trie.root)
    
    
#     for word in all_possible_words:
#         word_letter_counts = Counter(word)


        
#         # Check if all letters in the word can be found on the board
#         can_form = True
#         for letter, count in word_letter_counts.items():
#             if count > board_letter_counts.get(letter, 0):
#                 can_form = False
#                 break
        
#         if can_form:
#             solutions.add(word)
    
#     return solutions


def solve_word_search(board, trie):
    # Count letters on the board
    letter_counts = Counter(letter.lower() for row in board for letter in row)
    solutions = set()

    def search(node, remaining_letters):
        print(node)
        if node.complete:
            solutions.add(node.complete)
        
        for child in node.children:
            char=child.value
            if remaining_letters.get(char, 0) > 0:
                # we create the copy of the reaming letter so for different paths will have different frequencies
                updated_letters = remaining_letters.copy()
                updated_letters[char] -= 1
                search(child, updated_letters)

    search(trie.root, letter_counts)
    return solutions



# def extract_all_words(node, prefix=""):
#     words = []
    
#     if node.complete:
#         words.append(node.complete)
    
#     for child in node.children:
#         words.extend(extract_all_words(child, prefix + child.value))
    
#     return words


#this function takes all of the alphabet in the board and make it in the lower case because of case sensitivity
#also the dictionary we are using is all in lowercase 
def make_lower_case(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = board[i][j].lower()


if __name__ == "__main__":
    # An example Boggle board
    board = \
    [['a', 't'], 
     ['p', 'c']]

    # Call our solve_boggle function on the board, 
    # which returns a list of all the legal words on it
    result = solve_word_search(board,trie)
    print(result)


# # We import a file containing my version of the trie tree data 
# # structure, which will be useful for checking valid words
# import my_trie
# from collections import Counter

# # First, we grab all the valid boggle words from the dictionary
# file = open("words.txt", 'r')
# dictionary = []
# # in boggle, words must be of length >= 3
# for word in file:
#     # accounts for new line character
#     if len(word) < 4:
#         continue
#     # removes new line character
#     dictionary.append(word[:-1])

# # makes a trie out of all the words in the dictionary
# trie = my_trie.Trie()
# trie.add_to_trie(dictionary)


# # Takes in a boggle board and returns the set
# # of valid words that can be made using the letters on the board
# # No adjacency constraints - just check if the word can be formed
# # using the available letters
# def solve_boggle(board, trie=trie):
#     make_lower_case(board)
    
#     # Get all letters from the board
#     all_letters = []
#     for row in board:
#         for letter in row:
#             all_letters.append(letter)
    
#     # Count frequency of each letter on the board
#     board_letter_counts = Counter(all_letters)
    
#     # Check each dictionary word to see if it can be made from board letters
#     solutions = set()
    
#     # For efficiency, first extract all possible words from trie
#     all_possible_words = extract_all_words(trie.root)
    
#     for word in all_possible_words:
#         word_letter_counts = Counter(word)
        
#         # Check if all letters in the word can be found on the board
#         can_form = True
#         for letter, count in word_letter_counts.items():
#             if count > board_letter_counts.get(letter, 0):
#                 can_form = False
#                 break
        
#         if can_form:
#             solutions.add(word)
    
#     return solutions


# # Extract all words from the trie
# def extract_all_words(node, prefix=""):
#     words = []
    
#     if node.complete:
#         words.append(node.complete)
    
#     for child in node.children:
#         words.extend(extract_all_words(child, prefix + child.value))
    
#     return words


# # converts all the letters on the boggle board to lowercase
# # so that our input is not case sensitive
# def make_lower_case(mat):
#     for i in range(len(mat)):
#         for j in range(len(mat[i])):
#             mat[i][j] = mat[i][j].lower()


# if __name__ == "__main__":
#     # An example Boggle board
#     board = \
#     [['s', 't'], 
#      ['p', 'o']]

#     # Call our solve_boggle function on the board, 
#     # which returns a list of all the legal words on it
#     result = solve_boggle(board)
#     print(result)
