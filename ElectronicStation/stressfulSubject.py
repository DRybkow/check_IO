import re

def is_stressful(subj):
    if subj.isupper():
        return True
    subj=subj.lower()
    s=re.compile(r'[a]+\W*[s]+\W*[a]+\W*[p]+\W*|[h]+\W*[e]+\W*[l]+\W*[p]+\W*|[u]+\W*[r]+\W*[g]+\W*[e]+\W*[n]+\W*[t]+\W*|.+[!]{3}$')
    mo=s.findall(subj)
    if mo==[]:
        return False
    return True

if __name__ == '__main__':
    #These "asserts" are only for self-checking and not necessarily for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print('Done! Go Check it!')