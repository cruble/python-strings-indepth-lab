def say_hello(name):
    return "Hi my name is {name}".format(name=name)
    # takes in a name and returns the string "Hi my name is " plus the name
    # use whichever form of interpolation is most appropriate

def replace_given_substring(str_to_replace, str_to_insert, string):
    # this function takes three parameters --
    # the first is the substring we would like to replace.
    # the second substring is what we would like to use inplace of the first
    # the third is the actual string which we want to operate on
    # the function should return the new string
    return string.replace(str_to_replace, str_to_insert)
    pass

def remove_duplicate_punctuation(string): 
    marks = ["!", "@", "#", "$", ".", "?"]
    word_list = string.split()
    for word in word_list:
        for mark in marks: 
            if word.count(mark) > 1:
                clean_word = word[:-word.count(mark)+1]
                string = string.replace(word, clean_word)
    return string 


from string import punctuation 
punct = list(set(punctuation))
punct.remove('@')
punct.remove('.')

email = "chad@chad.com"
not_email = "chad.blah"
invalid_email = "chad#^"

def validate_email_format(email):
    status = 'Yes'
    if "@" in email and ".com" in email:
        status = "Yes"
        for char in email: 
            if char in punct:
                status = "No"
    else: 
        status = 'No'
    return status     

def anonymize_credit_card_number(credit_card_number):
    end_string = credit_card_number[-4:]
    start_string = []
    anonymous = []
    for char in credit_card_number[0:-4]: 
        if char == "-" or char == " ":
            anonymous.append(char)
        else: 
            anonymous.append("X")
    return ''.join(anonymous) + end_string        
