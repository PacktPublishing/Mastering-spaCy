#!/usr/bin/env python3

import spacy
from spacy import displacy
from pathlib import Path
nlp = spacy.load("en_core_web_md")

doc = nlp("I'm a butterfly.")
svg = displacy.render(doc, style="dep", jupyter=False)
filename = "butterfly.svg"
output_path = Path(filename)
output_path.open("w", encoding="utf-8").write(svg)

