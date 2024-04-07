from pathlib import Path

files = [Path('txt1.txt'), Path('txt2.txt'), Path('txt3.txt')]

for file in files:
    try:
        words = file.read_text(encoding='utf-8')
        count1 = words.lower().count('the ')
        count2 = words.lower().count('')
        print(f'{file} has {count1} words of "the "')
        print(f'{file} has {count2} words of "the"')
    except FileNotFoundError:
        print(f'{file} not found')