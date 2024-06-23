import os
import pickle

import numpy as np
import config
import nltk

from nltk.tokenize import word_tokenize
nltk.download('punkt')
class Model():

    def __init__(self):

        self.model = pickle.load(open(config.MODEL_FILE_PATH,'rb'))

        self.count = pickle.load(open(config.COUNT_VECTORIZER,'rb'))


    def prediction(self,input_list):

        



        def tokenization(data):
            token = word_tokenize(data)

            text = [word.lower() for word in token]

            return " ".join(text)

        #text = tokenization(text)

        #print("text::",input_list)

        #text = np.array([text])

        count_text = self.count.transform(input_list)

        #print("Count_text::",count_text)

        pred = self.model.predict(count_text)

        #print("Predicted Column:::",pred)
        #print("type of pred: ",type(pred))
        return list(pred)
    

#if __name__ == "__main__":

#    model = Model()

#    model.prediction("Daniel Abrahmsen;Chirag Gupta;CASCADIA;Extra Heavy Trucks (45,001+);906 W STERRETT ST;3C7WRNFL3LG119579;15-12-2023")