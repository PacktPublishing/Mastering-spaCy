from transformers import BertTokenizer

btokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
sentence = "He lived characteristically idle and romantic."
sentence = "[CLS] " + sentence + " [SEP]"
tokens = btokenizer.tokenize(sentence)

print(tokens)

ids = btokenizer.convert_tokens_to_ids(tokens)
print(ids)

