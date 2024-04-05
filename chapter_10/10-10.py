from pathlib import Path

def common_words(file_name, word):
    """
    Count the occurrence of a chosen word in a file
    """
    path = Path(f'text_files/{file_name}')

    try:
        contents = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        pass

    else:
        return contents.lower().count(word)


total_count = 0
file_list = ['alice.txt', 'four_years.txt']

#Count the word "the" in each file using our common_words() fumction
#Add the count to total_sum
for file in file_list:
    total_count += int(common_words(file, 'the '))

print(total_count)
