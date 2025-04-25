class TrieNode:
	#attributes of trie
	def __init__(self, value):
		self.value = value
		self.children = []
		self.complete = None

	#node child added here
	def add(self, child):
		self.children.append(child)

	#returns the value of the child if it exists
	def get_child(self, value):
		for child in self.children:
			if child.value == value:
				return child
		return None

	#prints value
	def __str__(self):
		return str(self.value)


class Trie:
	
	#root is empty string 
	def __init__(self, list_words=None):
		self.root = TrieNode('')

		# Adds the words in the list to the trie
		if list_words != None:
			self.trie_add(list_words)


	# Add function
	def trie_add(self, list_words): 
	
		for word in list_words:

			current_node = self.root

			# If child not found then add the letter as child
			for letter in list(word):
				next_node = current_node.get_child(letter)
				if next_node == None:
					next_node = TrieNode(letter)
					current_node.add(next_node)
				current_node = next_node

			# This is a flag in Trie to see if word is complete
			current_node.complete = word