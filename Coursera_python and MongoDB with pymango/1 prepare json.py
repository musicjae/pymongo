from pprint import pprint

fh = open("./Vocabulary_set.csv", "r")
wd_list = fh.readlines()

wd_list.pop(0) # delete First word

vocab_list =[]

for rawstring in wd_list:
    word, definition = rawstring.split(',',1) # maxsplit=1
    definition = definition.rstrip()
    vocab_list.append({'word':word,'definition':definition})

pprint(vocab_list)
print('\n'*3,'개수: ',len(vocab_list ))