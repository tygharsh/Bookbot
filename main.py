def main():
	bookPath = "books/frankenstein.txt"
	text = get_book_text(bookPath)
	print(countWords(text))

def get_book_text(path):
	with open(path) as f:
		return f.read()

def countWords(text):
	count = len(text.split())
	return count

main()
