# ordinal numbers conditional practice

ordinals = range(1,10)
st = [1]
nd = [2]
rd = [3]
for num in ordinals:
    if num in st:
        print(f"{num}st")
    elif num in nd:
        print(f"{num}nd")
    elif num in rd:
        print(f"{num}rd")   
    else:
        print(f"{num}th")