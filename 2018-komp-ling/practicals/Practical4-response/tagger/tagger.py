import sys


model = open(sys.argv[1])
input = open(sys.argv[2])


def form_extr(input):
    pos = 'empty'
    # for each of the lines of input
    vocab = pos_extr(model)
    for line in input:
        # if there is no tab character, skip the line
        if '\t' not in line:
            print(line)
        row = line.strip().split('\t')
        # if there are not 10 cells, skip the line
        if len(row) != 10:
            continue
        # take one form
        form = row[1]
        for key,val in vocab.items():
            if form == key:
                pos = vocab[key]
        if pos == 'empty':
            pos = vocab["-"]

        print('%s\t%s\t%s\t%s' % (row[0], form, "-", pos))

def pos_extr(model):
    vocab = {}  # dict to store words and tags
    for line in model:
        # if there is no tab character, skip the line
        if '\t' not in line:
            continue
        # make a list of the cells in the row
        row = line.strip().split('\t')
        # if there are not 4 cells, skip the line
        if len(row) != 4:
            continue
        # the form is the value of the 3rd cell, pos tag - 2nd cell
        form = row[3]
        pos = row[2]
        # make a dict of forms and their pos - the most frequent are mentioned first
        if form not in vocab:
            vocab[form] = pos
        elif form in vocab:
            pass
    return vocab


form_extr(input)


model.close()
input.close()
