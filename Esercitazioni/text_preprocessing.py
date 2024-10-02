#!/usr/bin/env python

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def main():
    
    # download delle risorse necessarie
    nltk.download('punkt_tab')
    nltk.download('stopwords')
    
    # leggiamo il testo dal prompt
    print("Inserisci il testo >>> ",end='')
    text = input()
    
    # tokenizziamo il testo con word_tokenize
    tokens = word_tokenize(text, language="italian")
    
    print(f"Token:\n{tokens}")
    
    # filtriamo i token dalle stopwords
    filtered = [word for word in tokens if word.lower() not in stopwords.words("italian")]
    
    print(f"Eliminazione delle stopword:\n{filtered}")
    
    # Stemming con il Porter Stemmer
    # stemmer = nltk.PorterStemmer(): NON VA BENE PERCHE' IN INGLESE
    stemmer = nltk.SnowballStemmer("italian")
    
    stems = [stemmer.stem(t) for t in filtered]
    
    print(f"Stemming:\n{stems}")
    

if __name__ == "__main__":
    main()