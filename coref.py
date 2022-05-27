import spacy
nlp = spacy.load('en')

import neuralcoref
neuralcoref.add_to_pipe(nlp)
