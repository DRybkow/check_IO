def caps_lock(text: str) -> str:

    t=text.split('a')
    j=0
    l=''
    for i in t:
        if j%2==1:
            k=i.upper()
            l+=k
        else:
            l+=i
        j+=1
    return l
 
    # return ''.join(c.upper() if i % 2 else c for i, c in enumerate(text.split('a')))



if __name__ == "__main__":
    print("Example:")
    print(caps_lock("Why are you asking me that?"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("Coding complete? Click 'Check' to earn cool rewards!")