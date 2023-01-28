from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")

model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")
#predict a message
message = "I hate you"
segs = model.predict(message)
print(segs)