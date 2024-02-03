# modify favorite_languages.py

favorite_languages = {
      'jen': ['python', 'rust'],
      'sarah': ['c'],
      'edward': ['rust', 'go'],
      'phil': ['python', 'haskell'],
      }

invitees = ["jen", "bill", "erik"]

for iname in invitees:
    if iname in favorite_languages:
        print(f"Thanks for taking the poll, {iname.title()}!")
    else:
        print(f"{iname.title()}, please take the poll.")
    