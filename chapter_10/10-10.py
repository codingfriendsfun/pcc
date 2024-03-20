from pathlib import Path

path = Path('chapter_10/shakespeare.txt')
contents = path.read_text(encoding='utf-8')

title = "The Complete Works of William Shakespeare"

words = contents.lower()
the_count = words.count('the ')
print(f"{title} uses the word 'the' approximately {the_count} times.")