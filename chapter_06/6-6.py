favorite_languages = {
    "jen": "python",
    "Rob": "html",
    "chris": "rust",
    "larissa": "java",
    "ravi": "python",
}

pollees = ["Ravi", "rob", "Lauren", "noelle", "kristin"]

for poll in pollees:
    if poll.lower() in [favorite.lower() for favorite in favorite_languages]:
        print("You've already been polled!")
    else:
        print("You need to take our poll")
