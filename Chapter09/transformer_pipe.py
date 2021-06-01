from transformers import pipeline

nlp = pipeline("sentiment-analysis")


sent1 = "I hate you so much right now."
sent2 = "I love fresh air and exercising."

result1 = nlp(sent1)
result2 = nlp(sent2)


print(result1)
print(result2)
