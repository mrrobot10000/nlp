# -*- coding: utf-8 -*-
"""NLP lab.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1q3lx3FeDinwioSeY9FECr7QazIfual1m
"""

#week-1
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text= " hello everyone, welcome to nlp lab. we are doing tokenization program. "
print(word_tokenize(text))

import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
text= " hello everyone. welcome to nlp lab. we are doing tokenization program. "
print(sent_tokenize(text))

#week-2
import string
print(string.punctuation)

import string
print(len(string.punctuation))

import string
count=0
strar="abc@+#!"
stra=string.punctuation
for char in strar:
  if char in stra:
    count=count+1
print(count)

test_str="another test file1*"
print(test_str)
res=" "
for i in range(len(test_str)):
  if (test_str[i].isalpha()):
    res=res+test_str[i]
print(str(res))

text="thi is a test text to count words"
word_count=1
for i in range(1,len(text)):
    if text[i]==' ' and text[i-1]!=' ':
      word_count=word_count+1
print(word_count)

#week-3
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence=  " the quick brown fox jumps over the lazy dog. "
tokens = word_tokenize(sentence)
tag = pos_tag(tokens)
for t,t1  in tag:
  print(t,t1)

import spacy
nlp = spacy.load("en_core_web_sm")
interrogative_sentence = "What is the weather like today?"
declarative_sentence = "The weather is sunny."
doc = nlp(interrogative_sentence)
for token in doc:
  print(token.text, token.pos_)



#week-4
import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
synonyms = []
for syn in wordnet.synsets("good"):
  for lemma in syn.lemmas():
    synonyms.append(lemma.name())
print(synonyms)

import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
antonyms = []
for syn in wordnet.synsets("good"):
  for l in syn.lemmas():
    if l.antonyms():
      antonyms.append(l.antonyms()[0].name())
print(antonyms)

import nltk
from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["running", "jumps", "happily"]
stems = [ps.stem(word) for word in words]
print(stems)

from stemming.porter2 import stem
words = ["running", "jumps", "happily"]
stems = [stem(word) for word in words]
print(stems)

pip install stemming

import nltk
from nltk.stem import SnowballStemmer
snowball_stemmer = SnowballStemmer("english")
words = ["running", "jumps", "killing","foxes","quickly"]
stems = [snowball_stemmer.stem(word) for word in words]
print(stems)

from nltk.stem import RegexpStemmer
custom_word = '^dis'
regex_stemmer = RegexpStemmer(custom_word)

word = 'disgrace'

stemmed_word = regex_stemmer.stem(word)
print(stemmed_word)

from nltk.stem import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
words = ["running", "jumps", "happily","foxes"]
stems = [lancaster_stemmer.stem(word) for word in words]
print(stems)

#week - 5

def past_tense(verb):
    irregular_verbs = {"run":"ran","go":" went","be":"was/were","see":"saw","take":"took","buy":"bought"}
    if verb in irregular_verbs:
        return irregular_verbs[verb]
    elif verb.endswitch('e'):
        return verb + 'd'
    else:
        return verb + 'ed'
print(past_tense('run'))

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def rule_based_sentiment_analysis(sentence):
    positive_words = ["good", "great", "excellent", "fantastic", "awesome", "wonderful", "superb"]
    negative_words = ["bad", "poor", "terrible", "awful", "horrible", "hate", "disappoint"]

    pos_count = 0
    neg_count = 0

    for word in sentence.split():
        if word in positive_words:
            pos_count += 1
        elif word in negative_words:
            neg_count += 1

    if pos_count > neg_count:
        return "positive"
    elif pos_count < neg_count:
        return "negative"
    else:
        return "neutral"

def ml_based_sentiment_analysis(sentence, model, vectorizer):
    sentence_vector = vectorizer.transform([sentence])
    prediction = model.predict(sentence_vector)
    return prediction[0]  # Return the first element of the prediction array

def hybrid_sentiment_analysis(sentence, model, vectorizer):
    rule_based_prediction = rule_based_sentiment_analysis(sentence)

    if rule_based_prediction == "neutral":
        return ml_based_sentiment_analysis(sentence, model, vectorizer)
    return rule_based_prediction

# Training data
train_sentences = ["the food is excellent", "i hate waiting in line", "it is ok",
                   "this is the worst movie ever", "i love this movie"]
train_labels = ["positive", "negative", "neutral", "negative", "positive"]

# Vectorization and model training
vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_sentences)
model = LogisticRegression()
model.fit(train_vectors, train_labels)

# Test sentence
test_sentence = "the movie was good but the ending was terrible"

# Get the result from hybrid sentiment analysis
result_type = hybrid_sentiment_analysis(test_sentence, model, vectorizer)
print(result_type)

def present_tense(verb):
    if verb.endswitch('y') and verb[-2] not in 'aeiou':
        return verb[:-1] + 'ies'
    elif verb.endswith(('o','ch','s','x','z')):
        return verb + 'es'
    elif verb == "be":
        return "is"
    else:
        return verb + 's'
print(present_tense('run'))


def future_tense(verb):
    if verb.endswith('e'):
        return verb + 's'
print(future_tense('run'))

def conjugate(verb,tense):
    if tense == 'past':
        return past_tense(verb)
    elif tense == 'present':
        return present_tense(verb)
    elif tense == 'future':
        return future_tense(verb)
    elif tense == 'condinuous':
        return "am/is/are" + verb + "ing"  if verb !="be"else "being"
    elif tense == 'perfect':
        return "has/have" + past_tense(verb)
    elif tense == 'past perfect':
        return "had" + past_tense(verb)
    else:
        return verb
print(conjugate("run","past"))
print(conjugate("walk","present"))
print(conjugate("be","future"))
print(conjugate("see","condinuous"))
print(conjugate("take","perfect"))
print(conjugate("buy","past perfect"))

def present_tense(verb):
    if verb.endswith('y') and verb[-2] not in 'aeiou':
        return verb[:-1] + 'ies'
    elif verb.endswith(('o', 'ch', 's', 'x', 'z')):
        return verb + 'es'
    elif verb == "be":
        return "is"
    else:
        return verb + 's'

def past_tense(verb):
    if verb.endswith('e'):
        return verb + 'd'
    else:
        return verb + 'ed'

def future_tense(verb):
    return "will " + verb  # A simple way to express future tense

def conjugate(verb, tense):
    if tense == 'past':
        return past_tense(verb)
    elif tense == 'present':
        return present_tense(verb)
    elif tense == 'future':
        return future_tense(verb)
    elif tense == 'continuous':
        return "am/is/are " + verb + "ing" if verb != "be" else "being"
    elif tense == 'perfect':
        return "has/have " + past_tense(verb)
    elif tense == 'past perfect':
        return "had " + past_tense(verb)
    else:
        return verb

# Test cases
print(present_tense('run'))          # Expected output: "runs"
print(future_tense('run'))           # Expected output: "will run"
print(conjugate("run", "past"))      # Expected output: "ran"
print(conjugate("walk", "present"))   # Expected output: "walks"
print(conjugate("be", "future"))      # Expected output: "will be"
print(conjugate("see", "continuous")) # Expected output: "am/is/are seeing"
print(conjugate("take", "perfect"))   # Expected output: "has/have taken"
print(conjugate("buy", "past perfect")) # Expected output: "had bought"



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def rule_based_sentiment_analysis(sentence):
    positive_words = ["good","great","excellent","fantastic","awesome","wonderful","superb"]
    negative_words = ["bad","poor","terrible","awful","horrible","hate","disappoint"]

    pos_count=0
    neg_count=0

    for word in sentence.lower().split():
        if word in positive_words:
            pos_count+=1
        elif word in negative_words:
            neg_count+=1

    if pos_count > neg_count:
        return "positive"
    elif pos_count < neg_count:
        return "negative"
    else:
        return "neutral"

def ml_based_sentiment_analysis(sentence,model,vectorizer):
    sentence_vector = vectorizer.transform([sentence])
    Prediction = model.predict(sentence_vector)
    return Prediction[0]

def hybrid_sentiment_analysis(sentence,model,vectorizer):
    rule_based_prediction = rule_based_sentiment_analysis(sentence)

    if rule_based_prediction == "neutral":
        return ml_based_sentiment_analysis(sentence,model,vectorizer)
    return rule_based_prediction

train_sentences =["the food is excellent","i hate waiting in line","it is ok", "this is worst movie ever"," i love this movie"]
train_labels =["positive","negative","neutral","negative","positive"]

vectorizer = CountVectorizer()
train_vectors = vectorizer.fit_transform(train_sentences)
model = LogisticRegression()
model.fit(train_vectors,train_labels)

test_sentence = "the movie was good but the ending was terrible"

result_type = hybrid_sentiment_analysis(test_sentence,model,vectorizer)
print(result_type)

#week -6
import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

# Initialize stemmer and lemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# List of words to process
words = ['running', 'flies', 'leaves', 'better', 'studying']

# Print header
print(f"{'Word':<12} {'Stemmed':<12} {'Lemmatized':<12}")
print('=' * 36)

# Process each word
for word in words:
    stemmed = stemmer.stem(word)
    lemmas = lemmatizer.lemmatize(word, pos='v')  # Using 'v' for verb lemmatization
    print(f"{word:<12} {stemmed:<12} {lemmas:<12}")

import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words=['running','flies','leaves','better','studying']
print(f"{'Word':<12} {'lemma(noun)': <12} {'lemma(verb)': <12} {'lemma(adj)': <12}")
print('_'*70)
for word in words:
  print(f"{word:<12} {lemmatizer.lemmatize(word,pos='n'):<12} {lemmatizer.lemmatize(word,pos='v'):<12} {lemmatizer.lemmatize(word,pos='a'):<12}")

pip install svgling

import nltk
from nltk import CFG
from nltk.tree import tree
from IPython.display import display
grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V PP
PP -> P NP
Det -> 'the'
N -> 'cat' | 'mat'
V -> 'sat'
P -> 'on'
""")
parser= nltk.ChartParser(grammar)
sent = 'the cat sat on the mat'.split()
for tree in parser.parse(sent):
  display(tree)

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
print(stopwords.words('english'))

import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
stop_words=set(stopwords.words('english'))
filename="""
In 2023, the company reported a revenue of $1 million, which was an increase of 15% compared to 2022. There were 50 new employees hired, and the team worked on 10 major projects throughout the year. Despite some challenges, the overall growth was promising, and many believed that with continued effort, they could achieve even greater success in the upcoming years."""
token=word_tokenize(filename)
text1=[w for w in token if not w.lower() in stop_words]
text2=[char for char in text1 if char.isalpha()]
print(text2)

#week-7

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
print(stop_words)

print(stopwords.words('english'))

import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
sent="""oh ,my!dear.I don't think that it is possible.I'll try it regardless such a marvellouss feat_one of such magnanimous proportions_obviously doe not come easy."""
sent_tokenize=word_tokenize(sent)
sent1=[w for w in sent_tokenize if not w.lower()in stop_words ]
sent2=[char for char in sent1 if char.isalpha()]
print(sent2)

##week-8
#write a program to find the distance b/w two string intersection and union


def jaccard_similarity(a, b):
    a_set = set(a.split())
    b_set = set(b.split())
    intersection = a_set.intersection(b_set)
    union = a_set.union(b_set)
    return len(intersection) / len(union) if len(union) > 0 else 0

def jaccard_distance(a, b):
    return 1 - jaccard_similarity(a, b)
a = "apple banana"
b = "grape orange"

similarity = jaccard_similarity(a, b)
distance = jaccard_distance(a, b)

print(f"Similarity: {similarity}")
print(f"Distance: {distance}")

#write a program to find jaccard distance b/w two string and provide the correct words from libriy
import nltk
from nltk.metrics.distance import jaccard_distance
from nltk.util import ngrams
from nltk.corpus import words
nltk.download('words')
incorrect_words={'reeady','laghteer','wiindoew'}
correct_words=words.words()
for word in incorrect_words:
  temp=[(jaccard_distance(set(ngrams(word,2)),set(ngrams(w,2))),w)
   for w in correct_words if w[0]==word[0]]
  print(sorted(temp,key=lambda val: val[0])[0][1])

#write a  program to b/w two list .strings jaccard distance
import nltk
from nltk.metrics import jaccard_distance
from nltk.util import ngrams
nltk.download('punkt')
l1 = ['good', 'bite', 'height']
l2 = ['google', 'kite', 'light']
def calculate_jaccard_distance(word1, word2):
    ngrams_word1 = set(ngrams(word1, 2))
    ngrams_word2 = set(ngrams(word2, 2))
    return jaccard_distance(ngrams_word1, ngrams_word2)
for i in range(len(l1)):
    word1 = l1[i]
    word2 = l2[i]
    distance = calculate_jaccard_distance(word1, word2)
    print(f"Distance between '{word1}' and '{word2}' is {distance:.4f}")

#week-9

import nltk
from nltk.util import ngrams
sentence="hello everyone welcome to nlp class for studying language processing"
x=ngrams(sentence.split(),2)
for bigram in x:
  print(bigram)
print("==========================")
x=ngrams(sentence.split(),3)
for trigram in x:
  print(trigram)

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

text = """
Break the rules and take some free time to draw a conclusion.
Keep in mind that you need to get ready for the challenge ahead.
Life is full of unexpected twists and turns, so be prepared.
Take a deep breath, stay focused, and keep moving forward.
Don't let fear hold you back; face it head-on.
Believe in yourself and your abilities.
Stay positive, even in difficult times.
Keep learning, growing and pushing boundaries.
Surround yourself with supportive people.
Stay true to your values and principles.
"""

# Tokenize the text and filter out stopwords
tokens = word_tokenize(text.lower())
stop_words = set(stopwords.words('english'))
tokens = [token for token in tokens if token.isalpha() and token not in stop_words]

# Bigram extraction
bigram_measures = BigramAssocMeasures()
bigram_finder = BigramCollocationFinder.from_words(tokens)
bigram_finder.apply_freq_filter(2)

print("Bigram collocations:")
for bigram in bigram_finder.nbest(bigram_measures.pmi, 10):
    print(bigram)

# Trigram extraction
trigram_measures = TrigramAssocMeasures()
trigram_finder = TrigramCollocationFinder.from_words(tokens)
trigram_finder.apply_freq_filter(2)

print("\nTrigram collocations:")
for trigram in trigram_finder.nbest(trigram_measures.pmi, 10):
    print(trigram)

Bigram collocations:
('keep', 'learning')
('take', 'deep')
('stay', 'positive')
('moving', 'forward')
('free', 'time')
('face', 'head')
('hold', 'back')
('believe', 'abilities')
('stay', 'true')
('rules', 'take')

Trigram collocations:
('stay', 'true', 'values')
('keep', 'moving', 'forward')
('take', 'deep', 'breath')
('stay', 'positive', 'even')
('keep', 'learning', 'growing')
('you', 'need', 'get')
('believe', 'yourself', 'abilities')
('life', 'full', 'unexpected')
('face', 'it', 'head')
('moving', 'forward', 'don')