Morse = {'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..',' ':'/'}
code=[]
#convert upper case to lower case
#if not a letter, tell an error

#input=input('What do you want to translate?')

#input=input.lower()

input='ap3le'

for letter in input:
    if letter in Morse.keys():
        continue
    else:
        input=input('What do you want to translate?')

#for letter in input:
    #code.append(Morse[letter])

#for a in code:
    #print(a,end=" ")