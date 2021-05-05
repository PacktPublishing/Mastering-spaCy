import json

with open("data/corona.json") as f:
    data = json.loads(f.read())


TRAIN_DATA = []

for (text, annot) in data:
    new_anno = []
    for anno in annot["entities"]:
        st, end, label = anno
        new_anno.append((st, end, label))
    TRAIN_DATA.append((text, {"entities": new_anno}))


labels = ['Pathogen', 'MedicalCondition', 'Medicine']

import random
import spacy

from spacy.training import Example





nlp = spacy.blank("en")
ner = nlp.add_pipe("ner") 


print(ner)
print(nlp.meta)


for ent in labels:
   ner.add_label(ent)

print(ner.labels)


epochs = 25

other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

with nlp.disable_pipes(*other_pipes):

  optimizer = nlp.begin_training()

  for i in range(100):
    random.shuffle(TRAIN_DATA)
    for text, annotation in TRAIN_DATA:
        doc = nlp.make_doc(text)
        example = Example.from_dict(doc, annotation)
        nlp.update([example], sgd=optimizer)



doc = nlp("One of the bacterial diseases with the highest disease burden is tuberculosis, caused by Mycobacterium tuberculosis bacteria, which kills about 2 million people a year.")
doc2 = nlp("Pathogenic bacteria contribute to other globally important diseases, such as pneumonia, which can be caused by bacteria such as Streptococcus and Pseudomonas, and foodborne illnesses, which can be caused by bacteria such as Shigella, Campylobacter, and Salmonella. Pathogenic bacteria also cause infections such as tetanus, typhoid fever, diphtheria, syphilis, and leprosy. Pathogenic bacteria are also the cause of high infant mortality rates in developing countries.")


print(doc.ents)
print(doc)

from spacy import displacy
displacy.serve(doc2, style="ent")


