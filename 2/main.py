import random

f = open('test.txt','r')
user = '#qq id#'
num_sentnece_generate = 50

# remove extra meta data
for _ in xrange(8):
    f.readline()

wordmap = {}
wordmap[''] = []
line_by_user = False
counter = 0
for line in f:
    if (counter%3 == 0):
        if user in line:
            line_by_user = True
    elif (counter%3 == 1):
        if (line_by_user is False):
            counter = counter + 1
            continue

        list = line.split()
        if (len(list) == 0 or len(list) == 1):
            line_by_user = False
            counter = counter + 1
            continue
        wordmap[''].append(list[0])
        for i in range(len(list)-1):
            if (list[i] in wordmap):
                wordmap[list[i]].append(list[i+1])
            else:
                wordmap[list[i]] = [list[i + 1]]
        if (list[len(list)-1] in wordmap):
            wordmap[list[len(list)-1]].append('\n')
        else:
            wordmap[list[len(list) - 1]] = ['\n']

        line_by_user = False

    counter = counter + 1

for i in range(num_sentnece_generate):
    str = 'User:'+': '
    word = ''
    while word != '\n':
        str = str + ' '+ word
        pos = random.randint(1, len(wordmap[word]))-1
        word = wordmap[word][pos]
    print str
