
def reverse(s):
    if len(s) == 1:
        return s  
    else:
        return(s[-1] + reverse(s[:-1]))
    pass

x = "hello"

print(x[:-1])

print(reverse(x))
print(reverse('hello world'))