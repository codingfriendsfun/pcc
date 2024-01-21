# 3-10. Every Function
# a script to practice re-ordering lists

languages = ["R", "Python", "Java", "Cobol", "Ruby", "Elixir"]

print(f"Languages = {languages}")

print() # printing a blank line for readability


# add and remove entries
languages.append("C++")
print(f"Append C++:\n {languages}")
languages.insert(2, "Rust")
print(f"Insert Rust in address 2:\n {languages}")
popped = languages.pop(-2)
print(f"Pop second to last entry:\n {languages}")
print(f"Entry popped:\n {popped}")
del languages[2]
print(f"Delete address 2:\n {languages}")
languages.remove("Java")
print(f"Remove Java by value:\n {languages}")

print() # printing a blank line for readability


# sorting
print(f"Sorted, non-destructively:\n {sorted(languages)}")
languages.sort(reverse=True)
print(f"Sorted, destructively, reverse alphabetical:\n {languages}")
languages.sort()
print(f"Sorted, destructively:\n {languages}")

print() # printing a blank line for readability


# reversing
languages.reverse()
print(f"Reversed, destructively:\n {languages}")

print() # printing a blank line for readability