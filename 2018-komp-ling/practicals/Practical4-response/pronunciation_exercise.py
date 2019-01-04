import sys
from sklearn.linear_model import perceptron


train_data = [] # training exmaples, e.g. feature vectors
train_labels = [] # Correct labels
words = [] # the word, correct label and pronounciation
test_data = []
count = 0

for line in open('pronunciation_data.tsv').readlines():
    if count in range(1500):
        row = line.strip().split('\t')
        vec = []
        for i in row [3].split(','):
            vec.append(int(i))
        train_data.append(vec)
        train_labels.append(int(row[0]))
     #   words.append((row[1], row[2], int(row[0])))
    else:
        row = line.strip().split('\t')
        vec = []
        for i in row[3].split(','):
            vec.append(int(i))
        test_data.append(vec)
       # labels.append(int(row[0]))
        words.append((row[1], row[2], int(row[0])))
    count += 1

net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(train_data,train_labels)

result = net.predict(test_data)

total = 0
correct = 0
for i in range(0, len(words)):
    if result[i] == words[i][2]:
      #  print('+', result[i], words[i])
        correct = correct + 1
    else:
        print('-', result[i], words[i])
    total = total + 1

print(correct)
print(total)

print(correct/total)
