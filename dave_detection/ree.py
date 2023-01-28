from transformers import AutoModelForSequenceClassification, TextClassificationPipeline

modele = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert")
pipeline = TextClassificationPipeline(model=modele, device=0)


text = "This is an example text."
prediction = pipeline("allah")
print(prediction)