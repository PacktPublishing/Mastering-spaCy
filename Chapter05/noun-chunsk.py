import spacy
nlp = spacy.load("en_core_web_md")

doc = nlp("My beautiful and cute dog jumped over the fence")
print(list(doc.noun_chunks))

sentences = nlp("I purchased a science fiction book last week. I loved everything related to this fragrance: light, floral and feminine... I purchased a bottle of wine.")

key = nlp("perfume")

for sent in sentences.sents:
    nchunks = [nchunk.text for nchunk in sent.noun_chunks]
    nchunk_doc = nlp(" ".join(nchunks))
    print(nchunk_doc.similarity(key))
