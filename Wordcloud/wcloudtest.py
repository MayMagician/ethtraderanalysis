import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import json
from collections import Counter
from nltk import ngrams
import spacy
from PIL import Image
import numpy as np

f = open('submissionsFrom2018.json')
# ritorno l'oggetto json come dizionario
data = json.load(f)

# prendo tutti i titoli e tutti i testi delle submissions e li metto in una variabile allText, per costruirci il wordcloud

allText = ""

for i in data["submissions"]:
    allText += str(i["title"] + " ")
    allText += str(i["text"] + " ")

#print(allText)

with open("allText.txt", "w") as f:
    f.write(allText)
f.close()

text = open("allText.txt", mode="r", encoding="utf-8").read()

#stopwords di wordcloud
#stopwords = STOPWORDS
nlp = spacy.load("en_core_web_lg")
#stopwords di spacy
stopwords = nlp.Defaults.stop_words

char_mask = np.array(Image.open("ethlogo.jpg"))  

wc = WordCloud(
    background_color = "white",
    stopwords = stopwords,
    height = 600,
    width = 400,
    mask = char_mask
)

wc.generate(text)
wc.to_file("wordcloud_output_spacy.png")

#ritorno la lista di tutte le parole nei testi
#all_words = text.split()

#a = Counter(all_words)

#most_occur = a.most_common(200)

#print("Most frequent words (200):")
print("---")
#print(most_occur)

print("---")
print("---")
print("---")
print("---")
print("---")

#b = Counter(list(ngrams(all_words, 2)))

#frequentBigrams = b.most_common(200)

#print("Most frequent bigrams (200):")
print("---")
#print(frequentBigrams)

print("---")
print("---")
print("---")
print("---")
print("---")

#c = Counter(list(ngrams(all_words, 3)))

#frequentTrigrams = c.most_common(200)

#print("Most frequent trigrams (200):")
#print("---")
#print(frequentTrigrams)
