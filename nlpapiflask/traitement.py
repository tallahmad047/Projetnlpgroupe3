## for data
import json
import pandas as pd
import numpy as np
## for plotting
import matplotlib.pyplot as plt
#import seaborn as sns
## for processing
import re
import urllib.request
import nltk
## for bag-of-words
from sklearn import feature_extraction, metrics, feature_selection, model_selection, naive_bayes, pipeline, manifold, preprocessing
## for explainer
from lime import lime_text
## for bert language model
#import transformers
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np
from imblearn.over_sampling import SMOTE
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
train = pd.read_csv("Train.csv")
#test=pd.read_csv("Test.csv")

#cleaning texts
wn = WordNetLemmatizer()
label_encoder = LabelEncoder()

def text_preprocessing(review):
    review = re.sub('[^a-zA-Z]', ' ', review)
    review = review.lower()
    review = review.split()
    review = [wn.lemmatize(word) for word in review if not word in chichewa]
    review = ' '.join(review)
    return review
chichewa = ['i', 'ine', 'wanga', 'inenso', 'ife', 'athu', 'athu', 'tokha', 'inu', 'ndinu','iwe ukhoza', 'wako','wekha','nokha','iye','wake','iyemwini','icho','ndi','zake','lokha','iwo','awo','iwowo','chiyani','amene', 'uyu', 'uyo', 'awa', "ndili", 'ndi', 'ali','anali','khalani','akhala','kukhala',' Khalani nawo','wakhala','anali','chitani','amachita','kuchita', 'a', 'an', 'pulogalamu ya', 'ndi', 'koma', 'ngati', 'kapena', 'chifukwa', 'monga', 'mpaka', 'pamene', 'wa', 'pa ',' by','chifukwa' 'ndi','pafupi','kutsutsana','pakati','kupyola','nthawi', 'nthawi','kale','pambuyo','pamwamba', 'pansipa', 'kuti', 'kuchokera', 'mmwamba', 'pansi', 'mu', 'kunja', 'kuyatsa', 'kuchoka', 'kutha', 'kachiwiri', 'kupitilira','kenako',' kamodzi','apa','apo','liti','pati','bwanji','onse','aliyense','onse','aliyense', 'ochepa', 'zambiri', 'ambiri', 'ena', 'otero', 'ayi', 'kapena', 'osati', 'okha', 'eni', 'omwewo', 'kotero',' kuposa','nawonso',' kwambiri','angathe','ndidzatero','basi','musatero', 'musachite',' muyenera', 'muyenera kukhala','tsopano', 'sali', 'sindinathe','​​sanachite','satero','analibe', 'sanatero','sanachite','sindinatero','ayi','si', 'ma', 'sizingatheke','mwina','sayenera', 'osowa','osafunikira', 'shan' , 'nenani', 'sayenera', 'sanali', 'anapambana', 'sangachite', 'sanakonde', 'sangatero']

#test['Text'] = test['Text'].apply(text_preprocessing)
vectorizer = TfidfVectorizer()

def prepation():
   train['Text'] = train['Text'].apply(text_preprocessing)
   Y = vectorizer.fit_transform(train['Text']).toarray()
   pd.DataFrame(Y, columns=vectorizer.get_feature_names_out())
   Z=train['Label']
   label_encoder.fit_transform(Z)

def traitement (text):
    text=text_preprocessing(text)
    X = vectorizer.transform([text]).toarray()
    X = pd.DataFrame(X, columns=vectorizer.get_feature_names_out())
    
    json_data = {
    "input_data": {
        "columns": list(range(X.shape[1])),
        "index": list(range(X.shape[0])),
        "data": X.values.tolist(),
    },
    "params": {},
    }
    body = str.encode(json.dumps(json_data))
    
    return body
def decode(body):
    value= body.decode('utf-8')
    result_list = json.loads(value)
    #cleaned_str = body.strip("[]")
    #value = int(cleaned_str)
    print(result_list[0])
    
    body = label_encoder.inverse_transform(result_list)
    return body