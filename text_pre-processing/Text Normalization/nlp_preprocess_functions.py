## Functions to help with text pre-processing
# 1. Basic function

## load spacy
nlp = spacy.load('en_core_web_sm')
nlp.remove_pipe('ner')

## preprocessing of text
def text_preprocessing(df):
  """Function to preprocess text
  1. Targets a column called 'text' to convert any HTML entities (like &amp;, &lt;, &gt;) within the text into their corresponding characters.
  2. Creates new column 'text_cleaned': removes characters that are not letters or apostrophes, converts all to lowercase. 
  3. Creates new column 'text_lemma': creates lemma of 'text cleaned' column using spacy functions
  """
    df['text'] = df['text'].apply(lambda text: html.unescape(text))
    df['text_cleaned'] = df['text'].apply(lambda x: re.sub("[^A-Za-z']+", ' ', str(x)).lower())
    df['text_lemma'] = df['text_cleaned'].apply(lambda sent: ' '.join([i.lemma_ for i in nlp(sent)]))
    
    return df


