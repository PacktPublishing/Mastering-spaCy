from transformers import pipeline

nlp = pipeline("question-answering")

res = nlp({
    'question': 'What is the name of this book ?',
    'context': "I'll publish my new book Mastering spaCy soon."
})

print(res)
