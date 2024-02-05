sampleString = "Hi"
sampleList = ["Hi", "Hello", "Aloha", "Greetings"]
searcher = "WowZA"

print (sampleString == "hi")
print (sampleString.lower() == "hi")
print( 1 == 1)
print( 1 < 2)
print( 1 > 2)
print( 1 >= 1)
print( 1 <= 1)

print (1 == 2 or 1 <= 2 )
print (1 == 2 and 1 >= 2  + "\n" )

for sample in sampleList:
    print("Is it WowZa?")
    print(sample.lower() == searcher)
if searcher not in sampleList:
        print("Nooo there is no WOWZA anymore")

