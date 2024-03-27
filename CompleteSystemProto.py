import numpy as np
import pandas as pd
import math
import string
import os
import graphviz
import re
from collections import Counter


from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.parse.corenlp import CoreNLPServer
from nltk.parse.corenlp import CoreNLPParser
from nltk.corpus import stopwords
from nltk.tree.tree import Tree

import textacy
from textacy import *

def TF(text):
  translator = str.maketrans('', '', string.punctuation)
  text = text.translate(translator)
  words = word_tokenize(text)

  porter_stemmer = PorterStemmer()
  stemmed_words = [porter_stemmer.stem(word.lower()) for word in words]
  tf_counts = Counter(stemmed_words)

  TFdict = {}
  l = len(words)
  for word, count in tf_counts.items():
    TFdict[word] = count / l
  return TFdict

def KeyPhraseSGRank(Article):
  en = textacy.load_spacy_lang("en_core_web_sm")

  doc = textacy.make_spacy_doc(Article, lang=en)

  TopPhrases = [kps for kps, weights in textacy.extract.keyterms.sgrank(doc, topn=1.0)]
  return TopPhrases

def get_first_sentences(news_article):
    # Split the news article into paragraphs
    paragraphs = [p.strip() for p in news_article.split('\n\n') if p.strip()]

    # Tokenize and collect the first sentence of each paragraph
    first_sentences = []
    for paragraph in paragraphs:
        sentences = sent_tokenize(paragraph)
        if sentences:
            first_sentences.append(sentences[0])
    return first_sentences

def Parsing(Sentence, server):
  parser = CoreNLPParser(url=server.url)
  return next(parser.raw_parse(Sentence))

def find_leftmost_S(tree):
    if isinstance(tree, str):  # Terminal node
        return None
    elif tree.label() == 'S':  # Found leftmost S node
        return tree
    else:
        for subtree in tree:
            result = find_leftmost_S(subtree)
            if result is not None:
                return result

def Pruning(tree, Label):
  if isinstance(tree, str):
    return tree
  if tree.height() > 0:
    filtered_children = [Pruning(child, Label) for child in tree if (isinstance(child, str) or child.height() > 0) and (isinstance(child, str) or child.label() != Label)]
    return Tree(tree.label(), filtered_children)
  else:
    return tree

def Extract(tree):
    words = []
    for subtree in tree:
        if isinstance(subtree, Tree):
            words.extend(Extract(subtree))
        else:
            words.append(subtree)
    return words

def low_content_words(word_list):
  stop_words = set(stopwords.words('english'))
  words = [word.lower() for word in word_list]
  filtered_li=[]
  for word in words:
    if word not in stop_words:
      filtered_li.append(word)
  #print("filtered_li: ",filtered_li)
  word_freq = Counter(filtered_li)
  total_words = len(words)
  low_content_threshold = 0.01
  low_content_words = {word for word, freq in word_freq.items() if freq >= low_content_threshold * total_words}
  return low_content_words

def Matching(TFdict, text):
  translator = str.maketrans('', '', string.punctuation)
  text = text.translate(translator)
  words = word_tokenize(text)

  porter_stemmer = PorterStemmer()
  stemmed_words = [porter_stemmer.stem(word.lower()) for word in words]

  count = 0
  for i in stemmed_words:
    if i in TFdict.keys():
      count += TFdict[i]
  return count

def SGRMatching(HeadLine, TopPhrases):
  l, Flag, itre = len(TopPhrases), 0.0, 0
  for Phrase in TopPhrases:
    if Phrase in HeadLine:
      Flag += (l - TopPhrases.index(Phrase)) / l
      itre += 1
      #print(f"{Phrase} : {TopPhrases.index(Phrase)}")
  #print(f"Cumiliative Value : {Flag / itre}")
  if itre != 0:
    return Flag / itre
  else:
    return -1

def Generate(Article):
  nltk.download()
  cleaned_article = re.sub(r'\([^)]*\)', '', Article)

  os.environ['CLASSPATH'] = 'stanford-corenlp-4.5.6'

  #TFdict = TF(Article)

  KeyPhrases = KeyPhraseSGRank(Article)


  first_sentences_list = get_first_sentences(cleaned_article)

  CompressedSentences = []
  server = CoreNLPServer()
  server.start()

  for i in first_sentences_list:
    ParsedSentence = Parsing(i, server)

    for i in ParsedSentence:
      for j in i:
        lefts = find_leftmost_S(j)
        if lefts is not None:
          LeftMostS = lefts
        else:
          LeftMostS = i
        break
    Labels = ['DT', 'TMP', 'SBAR']
    #, 'CC', 'VBZ, 'PRP'' IN',
    for i in Labels:
      Temp = Pruning(LeftMostS, i)
      LeftMostS = Temp

    word_list = Extract(Temp)

    #low_content_words_inpara=low_content_words(word_list)

    sentence = ' '.join(word_list)
    CompressedSentences.append(sentence)
  server.stop()

  ResultDict = {}
  for i in CompressedSentences:
    #ResultDict[i] = Matching(TFdict, i)
    ResultDict[i] = SGRMatching(i, KeyPhrases)
  print(ResultDict)

  max_key = max(ResultDict, key=lambda k: ResultDict[k])

  return max_key
