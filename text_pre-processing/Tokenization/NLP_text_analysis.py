## important NLP functions for basic text analytics

## 1. Message Length (number of characters)
length of messages
df['message_len'] = df2['message'].apply(lambda x: len(x))

## 2. Word Count
df['word_count'] = df2['message'].apply(lambda x: len(x.split()))

## 3. Avg word length per message or text passage
def get_avg_word_len(x):
    words = x.split()
    word_len = 0
    for word in words:
        word_len = word_len + len(word)

    return word_len/len(words)

## 4. Average number of words per message
df['Avg_num_words'] = df2['word_count'].mean()


## 5. Number of sentences
##5a. Spacy method
##!pip install spacy
import spacy

## load spacy model
nlp = spacy.load('en_core_web_sm')

## function to count sents with spacy
def count_sentences(text):
  doc = nlp(text)
  return len(list(doc.sents))
  
## apply to message column
df['num_sents'] = df['message'].apply(count_sentences)


##5b. NLTK method
#!pip install nltk
## import nltk
import nltk
#nltk.download()

# function to count number of sentences per row in pandas dataframe in a new column
from nltk.tokenize import sent_tokenize

def count_sentences(text):
    return len(nltk.sent_tokenize(text))

## apply to message columns
df['sentence_count'] = df['message'].apply(count_sentences)
