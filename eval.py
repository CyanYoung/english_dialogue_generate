import pickle as pk

from nltk.translate.bleu_score import corpus_bleu

from generate import predict


path_sent1 = 'feat/sent1_test.pkl'
path_label = 'feat/label_test.pkl'
with open(path_sent1, 'rb') as f:
    sent1s = pk.load(f)
with open(path_label, 'rb') as f:
    labels = pk.load(f)


def test(name, sent1s, labels):
    labels = [[label.split()] for label in labels]
    preds = list()
    for i, sent1 in enumerate(sent1s):
        pred = predict(sent1, name, 'sample')
        preds.append(pred.split())
    print('\n%s %s %.2f\n' % (name, 'bleu:', corpus_bleu(labels[:10], preds)))


if __name__ == '__main__':
    test('s2s', sent1s, labels)
    test('att', sent1s, labels)
