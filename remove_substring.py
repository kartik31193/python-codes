#remove string from string if matches

def r(s1,s2):
    if s2 in s1:
        s1= s1.replace(s2,"")
    print(s1)
    return len(s1)

print(r("xxyzrfvvoe","xyz"))
