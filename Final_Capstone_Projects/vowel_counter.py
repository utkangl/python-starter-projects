# find the vowels in a text then display them

vowel_letters = ["a" , "e" , "i" , "o" , "u" ]
input_letters = []

def split_the_text():

    text = input("enter your text")

    for letter in text:
        
        input_letters.append(letter)

    return (input_letters)

split_the_text()

def finder():
    report = []
    for vowel in vowel_letters:

        if vowel in input_letters:
            report.append(vowel)
    
    print(report)
        
finder()