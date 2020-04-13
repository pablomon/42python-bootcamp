
def kata(dictionary):
    if type(dictionary) is dict:
        for x, y in dictionary.items():
            s = "{} was created by {}".format(x, y)
            print(s)
    else:
        print("Error. Only dictionaries")

languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

kata(languages)