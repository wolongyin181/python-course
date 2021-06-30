i=0
with open('groceries.txt','r') as file:
    file_contents = file.readlines()
    for item in file_contents:
        print(f'{i}. {item.capitalize()}')
        i=i+1
