from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analisar_sentimento(texto):
    if texto.strip() == "":
        return {"label": "NEUTRO", "score": 0}

    resultado = classifier(texto[:512])[0]
    return resultado