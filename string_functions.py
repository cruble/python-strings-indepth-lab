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
    # should make sure there are no special characters (i.e. *,~,#,$,%,&,(,),`,",',:,;,/,>,<)
    # make sure the email contains an @ symbol and a .com
    # return True if format passes tests, return False otherwise


def anonymize_credit_card_number(credit_card_number):
    # should replace all characters except the last 4 with 'X'
    # return the anonymized credit card number as a string
    # the credit card may have characters that are not numbers (i.e. spaces and dashes, which we would want to keep)
    # i.e. 1234-5678-90-1234 -> XXXX-XXXX-XX-1234
    pass

print(say_hello("chad"))