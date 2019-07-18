'''
My solutions for Jose Portilla's Udemy MOOC

'''
def rec_sum(n):
    if n == 1:
        return 1  
    else:
       return n + rec_sum(n-1)
        
print(rec_sum(4))


def sum_func(n):
    if n // 10 == 0:
        return n 
    else:
        return n % 10 + sum_func(n//10)

print(sum_func(4321))


x = "themanran"
y = ['the','ran','man']

def word_split(phrase,list_of_words, output = None):
    if phrase == "":
        return output
    if output is None:
        output = []
    for word in list_of_words:
        if phrase.startswith(word):
            output.append(word)
            return(word_split(phrase[len(word):],list_of_words,output))

print(word_split(x,y))