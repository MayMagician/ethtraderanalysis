import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import json
from collections import Counter
from nltk import ngrams
import re
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
from PIL import Image
import numpy as np

f = open('submissionsFrom2018.json')
# ritorno l'oggetto json come dizionario
data = json.load(f)

nlp = spacy.blank("en")
nlp.max_length = 75000000
#aggiungo le due pipes che mi servono
nlp.add_pipe('sentencizer')
nlp.add_pipe('spacytextblob')
#stopwords di spacy
stopwords = nlp.Defaults.stop_words

positiveCounterTotal = 0
negativeCounterTotal = 0
polarityCounterTotal = 0
totalSubjectivityTotal = 0
countTotal = 0

for i in data["submissions"]:
    phrase = nlp(i["title"])
    polarityCounterTotal = polarityCounterTotal + phrase._.polarity
    if phrase._.polarity > 0:
        positiveCounterTotal = positiveCounterTotal + 1
    elif phrase._.polarity < 0:
        negativeCounterTotal = negativeCounterTotal +1
    totalSubjectivityTotal = totalSubjectivityTotal + phrase._.subjectivity
    countTotal = countTotal + 1

positiveCounter2018 = 0
negativeCounter2018 = 0
polarityCounter2018 = 0
totalSubjectivity2018 = 0
count2018 = 0
positiveCounter2019 = 0
negativeCounter2019 = 0
polarityCounter2019 = 0
totalSubjectivity2019 = 0
count2019 = 0
positiveCounter2020 = 0
negativeCounter2020 = 0
polarityCounter2020 = 0
totalSubjectivity2020 = 0
count2020 = 0
positiveCounter2021 = 0
negativeCounter2021 = 0
polarityCounter2021 = 0
totalSubjectivity2021 = 0
count2021 = 0
positiveCounter2022 = 0
negativeCounter2022 = 0
polarityCounter2022 = 0
totalSubjectivity2022 = 0
count2022 = 0

for i in data["submissions"]:
    if re.search("\A2018", i["time"]) is not None:
        phrase = nlp(i["title"])
        polarityCounter2018 = polarityCounter2018 + phrase._.polarity
        if phrase._.polarity > 0:
            positiveCounter2018 = positiveCounter2018 + 1
        elif phrase._.polarity < 0:
            negativeCounter2018 = negativeCounter2018 + 1
        totalSubjectivity2018 = totalSubjectivity2018 + phrase._.subjectivity
        count2018 = count2018 + 1
    if re.search("\A2019", i["time"]) is not None:
        phrase = nlp(i["title"])
        polarityCounter2019 = polarityCounter2019 + phrase._.polarity
        if phrase._.polarity > 0:
            positiveCounter2019 = positiveCounter2019 + 1
        elif phrase._.polarity < 0:
            negativeCounter2019 = negativeCounter2019 + 1
        totalSubjectivity2019 = totalSubjectivity2019 + phrase._.subjectivity
        count2019 = count2019 + 1
    if re.search("\A2020", i["time"]) is not None:
        phrase = nlp(i["title"])
        polarityCounter2020 = polarityCounter2020 + phrase._.polarity
        if phrase._.polarity > 0:
            positiveCounter2020 = positiveCounter2020 + 1
        elif phrase._.polarity < 0:
            negativeCounter2020 = negativeCounter2020 + 1
        totalSubjectivity2020 = totalSubjectivity2020 + phrase._.subjectivity
        count2020 = count2020 + 1
    if re.search("\A2021", i["time"]) is not None:
        phrase = nlp(i["title"])
        polarityCounter2021 = polarityCounter2021 + phrase._.polarity
        if phrase._.polarity > 0:
            positiveCounter2021 = positiveCounter2021 + 1
        elif phrase._.polarity < 0:
            negativeCounter2021 = negativeCounter2021 + 1
        totalSubjectivity2021 = totalSubjectivity2021 + phrase._.subjectivity
        count2021 = count2021 + 1
    if re.search("\A2022", i["time"]) is not None:
        phrase = nlp(i["title"])
        polarityCounter2022 = polarityCounter2022 + phrase._.polarity
        if phrase._.polarity > 0:
            positiveCounter2022 = positiveCounter2022 + 1
        elif phrase._.polarity < 0:
            negativeCounter2022 = negativeCounter2022 + 1
        totalSubjectivity2022 = totalSubjectivity2022 + phrase._.subjectivity
        count2022 = count2022 + 1

print("Year 2018:")
print("Positive counter:", positiveCounter2018)
print("Negative counter:", negativeCounter2018)
print("Medium polarity:", polarityCounter2018/count2018)
print("Medium subjectivity:", totalSubjectivity2018/count2018)
print("---")
print("Year 2019:")
print("Positive counter:", positiveCounter2019)
print("Negative counter:", negativeCounter2019)
print("Medium polarity:", polarityCounter2019/count2019)
print("Medium subjectivity:", totalSubjectivity2019/count2019)
print("---")
print("Year 2020:")
print("Positive counter:", positiveCounter2020)
print("Negative counter:", negativeCounter2020)
print("Medium polarity:", polarityCounter2020/count2020)
print("Medium subjectivity:", totalSubjectivity2020/count2020)
print("---")
print("Year 2021:")
print("Positive counter:", positiveCounter2021)
print("Negative counter:", negativeCounter2021)
print("Medium polarity:", polarityCounter2021/count2021)
print("Medium subjectivity:", totalSubjectivity2021/count2021)
print("---")
print("Year 2022:")
print("Positive counter:", positiveCounter2022)
print("Negative counter:", negativeCounter2022)
print("Medium polarity:", polarityCounter2022/count2022)
print("Medium subjectivity:", totalSubjectivity2022/count2022)
print("---")
print("Total:")
print("Positive counter:", positiveCounterTotal)
print("Negative counter:", negativeCounterTotal)
print("Medium polarity:", polarityCounterTotal/countTotal)
print("Medium subjectivity:", totalSubjectivityTotal/countTotal)