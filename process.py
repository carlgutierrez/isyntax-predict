import numpy as np
from dataCleaning import clean_code
from tokenizeProcess import tokenize_code
from keras.preprocessing.sequence import pad_sequences
from apiConfig import max_length


# feed code inside list
def process(code):
    sample = clean_code(code)
    embed_sample = tokenize_code(sample)
    if len(embed_sample[0]) < max_length:
        processed = []
        for seq in embed_sample:
            user_seq = pad_sequences([seq], maxlen=max_length)[0]
            in_seq = pad_sequences([seq[:1]], maxlen=max_length)[0]
            processed.append(np.append(user_seq, in_seq))
        processed = np.array(processed)
        return processed
    else:
        print("Try another code as it exceeds max length")
        return []
