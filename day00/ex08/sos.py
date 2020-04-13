import sys

def morse(text):
    MORSE_CODE_DICT = {'A': '.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ':' / '}
    morsed = []
    for char in text:
        code = MORSE_CODE_DICT.get(char.upper())
        morsed.append(code)
    print(' '.join(morsed))


if len(sys.argv) > 1:    
    for item in sys.argv[1:]:
        if not (item.isalnum() or item.isspace):
            print("ERROR")
            exit(1)

separator = ' '
joined = separator.join(sys.argv[1:])
morse(joined)
