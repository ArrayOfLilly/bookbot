def main():
	filepath = "books/frankenstein.txt"
	
	file_contents = read_file(filepath)
	word_count = count_words(file_contents)
	letter_count = count_letters(file_contents)
	print_report(filepath, word_count, letter_count)
	

def read_file(path):
	with open(path) as f:
		file_contents = f.read()
	return file_contents


def count_words(text):
	word_count = 0
	for word in text.split():
		word_count += 1
	return word_count


def count_letters(text):
	text = text.lower()
	letter_count = {}

	for c in text:
		if c in letter_count:
			letter_count[c] += 1
		else:
			letter_count[c] = 1
	return letter_count


def print_report(file, word_count, letters):
	print()
	print(f"--- Begin report of {file} ---")
	print(f"{word_count} words found in the document")
	print()
	for c in sorted(letters, key=letters.get, reverse=True):
		if c.isalpha():
			print(f"The '{c}' character was found {letters[c]} times")
	print()



main()
