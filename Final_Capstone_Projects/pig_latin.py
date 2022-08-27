# move the first letter to the end and add "ay" to the word before

def translater():
    word = input ("enter the word ")
    
    letters = []    
    for letter in word:
        letters.append(letter)
        
    a = letters.pop(0)
    word = letters.append(a)

    word = "".join(letters)
    word = word + "-" + "ay"
    
    print (word)  
    
translater()