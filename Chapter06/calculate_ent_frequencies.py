from collections import Counter 
import spacy 
nlp  = spacy.load("en_core_web_md") 

corpus = open("data/atis_utterances.txt", "r").read().split("\n") 


all_ent_labels = [] 
for sentence in corpus: 
    doc = nlp(sentence.strip()) 
    ents = doc.ents 
    all_ent_labels += [ent.label_ for ent in ents] 

c = Counter(all_ent_labels) 
print(c) 
