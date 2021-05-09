import spacy

nlp = spacy.load("en_core_web_md")


with open("data/utterances.txt", "r") as utterances:
    for utterance in utterances:
        utterance = utterance.strip()
        doc = nlp(utterance)
        ents = doc.ents
        if ents:
            for ent in ents:
                if ent.label_ == "GPE":
                    print(ent.text, "\t", utterance)
