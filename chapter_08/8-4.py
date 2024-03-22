def make_shirt(size="large", text="I love Python."):
    """

    :param size:  (Default value = "large")
    :param text:  (Default value = "I love Python.")

    """
    print(f"printing a {size} with {text} printed on it")


isActive = True

while isActive == True:
    iSize = input("What is your size? ")
    iText = input("What do you want on the shirt? ")
    make_shirt(iSize, iText)
    goAgain = input("Would you like to go again? Type 'no' to stop. ")
    if goAgain == "no":
        break

make_shirt()
