def multiplication_table(x):
    mas = [[0] * x for i in range(x)]
    return mas
x = int(input('ввести число'))
table = multiplication_table(x)

print (table)

def multiplication_table(x):
    mas = [[0] * x for i in range(x)]
    for n in range(x):
        for j in range(x):
            mas[n][j] = (n + 1) * (j + 1)
    return mas


def multiplicationTable(size):
    return [[(x + 1) * (y + 1) for y in range(size)] for x in range(size)]

#next
def greet(name):
    name = name.title().capitalize()
    return f'Hello {name}!'

#next
def capitals(word):
    inds = []
    i = 0
    for l in word:
        if l.isupper():
            inds.append(i)
        i += 1
    return inds

def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            uppers.append(i)
    return uppers