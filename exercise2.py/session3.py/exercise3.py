max_number=int(input('Up to which number do we need to check for?'))
for number in range(max_number):
    if(number%2==0):
        print(number)


for number in range (10,21):
    print(number)


for number in range (50,101,5):
    if(number==75):
        continue
    else:
        print(number)