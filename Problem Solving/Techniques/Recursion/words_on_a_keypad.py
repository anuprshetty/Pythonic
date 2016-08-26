# Words on a keypad
# Reference: https://www.youtube.com/watch?v=tWnHbSHwNmA

def populate_words(number, digit_index, digit_letters_mapping, word, words):
	# base condition
	if digit_index >= len(number):
		words.append(word)
		return

	digit = int(number[digit_index])
	digit_letters = digit_letters_mapping[digit]
	for digit_letter in digit_letters:
		word += digit_letter
		populate_words(number, digit_index + 1, digit_letters_mapping, word, words)
		word = word[:-1]


def keypad_words(number):
	words = []
	word = ""
	digit_index = 0
	digit_letters_mapping = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
	populate_words(number, digit_index, digit_letters_mapping, word, words)

	return words


words = keypad_words('23')

print(words)
