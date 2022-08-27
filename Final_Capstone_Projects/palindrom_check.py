def check():
    
    word = input ("enter your word")
    
    letters = []
    for letter in word:
        
        letters.append(letter)
        
    new_word = "".join(letters[::-1]) 
    
    if new_word == word: print("this is a palindrom word")
    else: print("this is not a palindrom word")       

check()