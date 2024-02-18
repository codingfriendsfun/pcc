# 7-10. Dream Vacation

results = {}

while True:
    name = input("What's your name?  (type 'end' to show results):")

    if name == 'end':
        if not results:
            print("You must enter at least one data point.")
            continue
        else:
            break
    
    place = input("If you could visit one place in the world, " + 
        "where would it be? ")
    
    results[name] = place

for result in results:
    print(f"{result} answered {results[result]}.")
    