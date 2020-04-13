def text_analyzer(text=''):
    """ Count and print in a text:
    -upper letters
    -lower letters
    -punctuation marks
    -spaces
    """
    punctuation = ".?!,;:\«»()[]/'"
    upper_nbr = sum(1 for c in text if c.isupper())
    lower_nbr = sum(1 for c in text if c.islower())
    punct_nbr = sum(1 for c in text if c in punctuation)
    spaces_nbr = sum(1 for c in text if c == ' ')

    print("-", upper_nbr, "uper", "letter" if upper_nbr == 1 else "letters", "\n\n-",\
    lower_nbr, "lower", "letter" if lower_nbr == 1 else "letters", "\n\n-",\
    punct_nbr, "punctuation", "mark" if punct_nbr == 1 else "marks", "\n\n-",\
    spaces_nbr, "space" if spaces_nbr == 1 else "spacess", "\n\n")
