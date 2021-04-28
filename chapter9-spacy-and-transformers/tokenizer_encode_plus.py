from transformers import BertTokenizer

btokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
sentence = "He lived characteristically idle and romantic."

encoded = btokenizer.encode_plus(
        text=sentence,
        add_special_tokens=True,
        max_length=12,
        pad_to_max_length=True,
        return_tensors="tf"
)

token_ids = encoded["input_ids"]

print(token_ids)
