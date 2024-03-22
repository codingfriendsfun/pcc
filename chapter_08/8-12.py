

##while toppings != 'q':
  ##  topping = input("What topping would you like on your sandwich? 'q' to quit ")
    ##if topping == 'q':
      ##  break
    ##else:
      ##  toppings.append(topping)
##write a function that accepts a list of items a person wants on a sandwich

def make_sandwich(*ingredients):
    print ("making a sandwich: ")
    for ingredient in ingredients:
        print(f"Adding topping - {ingredient}")

make_sandwich('lettuce', 'tomato', 'bacon')
make_sandwich('lettuce', 'tomato', 'bacon', 'chicken', 'ranch')
make_sandwich('chicken', 'parmesian', 'tomato sauce')

##needs work was supposed to print multiple lines?