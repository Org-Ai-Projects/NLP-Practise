# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 00:22:40 2021

@author: shaik
"""

import nltk

from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

paragraph = """Barack Obama served as the 44th President of the United States from 2009 to 2017. Before his presidency, he served in the Illinois Senate (1997–2004) and the United States Senate (2005–2008).

It was during his campaign for the United States Senate that he first made a speech that received nationwide attention; he gave the keynote address at the 2004 Democratic National Convention. and stated "there is not a liberal America and a conservative America—there is the United States of America". Obama began to run for president just three years after that speech. In response to a political controversy involving race during the primary campaign, he delivered his "A More Perfect Union" speech, which was widely seen as a critical point in the campaign.

Obama won election to the presidency in 2009 and re-election in 2013. Among the hundreds of speeches he has delivered since then include six speeches before Congress (including four State of the Union addresses), two victory speeches, a speech to the Islamic world in Egypt early in his first term, and a speech following the shooting of Congresswoman Gabby Giffords.

On January 10, 2017, We Are The Change We Seek,[1] a collection of Barack Obama's greatest speeches selected and introduced by columnist E.J. Dionne and MSNBC host Joy-Ann Reid was published by Bloomsbury Publishing."""
               

sentences = nltk.sent_tokenize(paragraph)
lemmatizer = WordNetLemmatizer()

#Lemmatization

for i in range(len(sentences)):
    words = nltk.word_tokenize(sentences[i])
    words = [lemmatizer.lemmatize(word) for word in words if word not in set(stopwords.words("english"))]
    sentences[i] = " ".join(words)
print("completed")
