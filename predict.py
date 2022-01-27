from nltk.tokenize.treebank import TreebankWordDetokenizer
import numpy as np
from keras.preprocessing.sequence import pad_sequences
from tokenizeProcess import nltkTokenize, javaKeywords
from dataCleaning import clean_code
from apiConfig import max_length, model, ixtow


def predict(rawCode, x):
    pred_seq = x.copy()
    in_seq = pred_seq[:, :max_length]
    prediction = list()
    prediction.extend(pred_seq[:, -1])
    for i in range(1, max_length):
        predict = model.predict(pred_seq)
        predict = np.argmax(predict, axis=1)
        prediction.extend(predict)
        if ixtow[predict[0]] == '<end>':
            break
        out_seq = pred_seq[:, -i:]
        out_seq = np.append(out_seq, predict)
        out_seq = pad_sequences([out_seq], maxlen=max_length)[0]
        pred_seq = np.array([np.append(in_seq, out_seq)])

    in_sent = []
    for i in in_seq[0]:
        if i in ixtow:
            in_sent.append(ixtow[i])
    in_sent = " ".join(in_sent)

    out_sent = []
    for i in prediction:
        if i in ixtow:
            out_sent.append(ixtow[i])
#     out_sent = " ".join(out_sent)
#     out_sent = TreebankWordDetokenizer().detokenize(out_sent)

    # Get list of <UNK>
    tokenizedList = (nltkTokenize(clean_code([rawCode])))
    unkList = []
    for x in tokenizedList[0]:
        if x not in javaKeywords:
            unkList.append(x)

    # Put the removed <UNK> in to the predictedCode
    predictedArray = out_sent
    unkNum = 0
    while '<UNK>' in predictedArray:
        unkIndex = predictedArray.index('<UNK>')
        if len(unkList) <= unkNum:
            break
        predictedArray[unkIndex] = unkList[unkNum]
        unkNum += 1

    # Remove <end>
    del predictedArray[-1]

    # return string
    out_sent = TreebankWordDetokenizer().detokenize(out_sent)

    return in_sent, out_sent
