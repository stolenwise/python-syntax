def print_upper_words(word):
    """Print out each words on a separate line, but in all uppercase

        print_upper_words(["This", "is", "going", "well"])
        THIS
        IS
        GOING
        WELL
        """

    for word in words:
        print(word.upper())



def print_upper_words2(words):
    """Print each word on a separate line, uppercased, if it starts with E or e

    print_upper_words(["errand", "Erin", "Alex"])
    """

    for word in words:
            if word.startswith("e") or word.startswith("E"):
                print(word.upper())

def print_upper_words3(words, must_start_with):
    """Print out each word on a separate line, uppercased, if it starts with one of the following
     
     print_upper_words(["errand", "Erin", "Alex", "nothing"],
     must_start_with=["A","E"])
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break




    # this should print "HELLO", "HEY", "YO", and "YES"

# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                    must_start_with={"h", "y"})