from transformers import AutoModelForSequenceClassification, AutoTokenizer, TextClassificationPipeline
rand_insults = ['send me pussy picture', 'send me sexy picture', 'send me a dick picture']
model = AutoModelForSequenceClassification.from_pretrained("unitary/toxic-bert",problem_type="multi_label_classification")
tokenizer = AutoTokenizer.from_pretrained("unitary/toxic-bert")
for i in rand_insults:
    pipeline = TextClassificationPipeline(model=model, tokenizer=tokenizer, device=0)
    text = i
    prediction = pipeline(text, top_k=10)
    # print(prediction['score'])
    # if float(prediction['score']) >= 0.3:
    #     print(f'{prediction}\n')
    for emotion in prediction:
        if float(emotion['score']) >= 0.3:
            print(emotion)
    input()