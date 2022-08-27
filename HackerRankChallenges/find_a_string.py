x = 0

while (x <= 1):
    
    includer_word = input("please enter the word to search in")
    search_word = input("please enter the world whick progra is gonna find şn the inculder word")
    end = input("please press 5 for end the program and press enter to keep searching")
    
    if (search_word in includer_word):
        print("yes")
        
    elif(search_word not in includer_word):
        print("no")
        
    elif(search_word == 5 or includer_word==5):
        break
        