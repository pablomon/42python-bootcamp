import sys

def text_analyzer(text):    
    '''
    This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
    '''
    chars = len(text)
    if (chars is 0):
        inputText = input("What is the text to analyse?\n")
        text_analyzer(inputText)
        return

    uppers = len([u for u in text if u.isupper()])
    lowers = len([u for u in text if u.islower()])
    spaces = len([u for u in text if u.isspace()])
    nums = len([u for u in text if u.isnumeric()])
    puncts = chars - uppers - lowers - spaces - nums
    print("The text contains {} characters:\n".format(chars))
    print("- {} upper letters\n".format(uppers))    
    print("- {} lower letters\n".format(lowers))    
    print("- {} punctuation marks\n".format(puncts))    
    print("- {} spaces".format(spaces))