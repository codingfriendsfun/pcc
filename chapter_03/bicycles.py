bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # 1st element
print(bicycles[0].title()) # can be combined with methods for the contained 
    # data type.
print(bicycles[1]) # 2nd element
print(bicycles[3]) # 4th element
print(bicycles[-1]) # count backwards from end

# can be interpolated with f-strings
message = f"My first bicycle was a {bicycles[0].title()}." 

print(message)
