import sys


if len(sys.argv) > 1:
    instream = open(sys.argv[1])
else:
    instream = sys.stdin


def count_w_fr(table):
    vocab = {}  # dict to store frequency list
    words = {}
    tags = {}
    all = 0
    # for each of the lines of input
    for line in sys.stdin.readlines():
        # if there is no tab character, skip the line
        if '\t' not in line:
            continue
        # make a list of the cells in the row
        row = line.split('\t')
        # if there are not 10 cells, skip the line
        if len(row) != 10:
            continue
        # the form is the value of the second cell, pos tag - 4th cell
        form = row[1]
        pos = row[3]
        # calculate tag occurances
        if pos not in tags:
            tags[pos] = 0
        tags[pos] += 1
        all += 1
        # calculate form occurrences with different pos tags
        if form not in vocab:
            words[form] = 0
            vocab[form] = {}
            if pos not in vocab[form]:
                vocab[form][pos] = 0
            vocab[form][pos] += 1
        elif form in vocab:
            if pos not in vocab[form]:
                vocab[form][pos] = 0
            vocab[form][pos] += 1
        # calculate form occurrences regardless its pos tag
        words[form] += 1

    for t in tags:
            print('%04.2f\t%d\t%s\t-' % ((float(tags[t]) / float(all)), tags[t], t,))
    for w in vocab:
        for p in vocab[w]:
            print('%04.2f\t%d\t%s\t%s' % ((float(vocab[w][p]) / float(words[w])), vocab[w][p], p, w))

print('# P\tcount\ttag\tform')
print(count_w_fr(instream))
