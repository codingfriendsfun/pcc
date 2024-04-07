# 10-10. Common Words

from pathlib import Path

# deal with "What folder am I working from?"
import os
cwd = os.getcwd()
index = cwd.find("chapter")
if index > 0:
    cwd = cwd[:index]
# else do nothing, assume we're in workspace root

def countWords(inputFile, word):
    file = Path(inputFile)
    try:
        fileDump = file.read_text(encoding='utf-8')
    except FileNotFoundError:
        print("Error: file not found.")
    
    wordCount = fileDump.lower().count(word)

    return wordCount


sourceDir = f'{cwd}/chapter_10/gutenberg'
    
for file in os.listdir(sourceDir):
    print(f"The file {file} contains the string 'the' (without spaces) " + 
        f"{countWords(f'{sourceDir}/{file}', 'the')} times.")
    print(f"It contains the word 'the' (with spaces) " + 
        f"{countWords(f'{sourceDir}/{file}', ' the ')} times.")
    print() # for readability
