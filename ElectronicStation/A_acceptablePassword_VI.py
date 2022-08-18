def is_acceptable_password(password: str) -> bool:
    s,j=0,0
    list(password).sort()
    for i in password:
        if i!=password[j-1]:
            s+=1
        j+=1
    if s<3:
        return False
    if 'password' in password.lower():
        return False
    elif len(password)>9:
        return True
    elif password.isdigit():
        return False
    elif any(i.isnumeric() for i in password):
        return len(password)>6
    return False

if __name__=="__main__":
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    print('\n\t good job!')

'''
#Best "Clear" Solution
def is_acceptable_password(password: str) -> bool:
    # c1 : length should be bigger than 6
    # c2 : contains at least one digit but it can't be all digits
    # c3 : having numbers is not required for password longer than 10
    # c4 : string should not contain word "password" in any case
    # c5 : consist of 3 different letters
    c1 = len(password) >= 6
    c2 = any(map(str.isdigit, password)) and not password.isdigit()
    c3 = len(password) >= 10
    c4 = 'password' not in password.lower()
    c5 = len(set(password)) >= 3
    return c1 and (c2 or c3) and c4 and c5

#Best "Creative" Solution

import re

def is_acceptable_password(password: str) -> bool:
    return bool(re.match(r"""
        # contains at least one digit and not digit and bigger than 6 or not less than 10
        ((?=.*\d)(?=.*\D)(?=.{7,})|(?=.{10,}))
        
        # not contain the word "password" in any case
        (?!(?i:.*password))

        # contains 3 different letters (or digits)
        (?P<x>.).*?(?!(?P=x))(?P<y>.).*?(?!(?P=x))(?!(?P=y))(.)""",
        password, re.VERBOSE))

#Best "Speedy" Solution
def is_acceptable_password(password: str) -> bool:
    return (    'password' not in password.casefold()
            and len(set(password)) > 2
            and (len(password) > 9 or (    len(password) > 6
                                       and any(ch.isdigit() for ch in password)
                                       and not password.isdigit())))


#Best "3rd party" Solution


'''