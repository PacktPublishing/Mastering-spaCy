import spacy
nlp = spacy.load("en_core_web_md")
doc = nlp("You went there afskfsd.")

for token in doc:
    print(token.is_oov, token.has_vector)
