from transformers import BertTokenizer, TFBertModel

btokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
bmodel = TFBertModel.from_pretrained("bert-base-uncased")

sentence = "He was idle."

encoded = btokenizer.encode_plus(
        text=sentence,
        add_special_tokens=True,
        max_length=10,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors="tf"
)

inputs = encoded["input_ids"]

outputs = bmodel(inputs)




print(outputs[0].shape)
print(outputs[1].shape)
