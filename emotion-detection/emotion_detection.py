from transformers import pipeline


class ED_Model:

    def __init__(self):
        self.classifier = pipeline("text-classification", "cointegrated/rubert-tiny2-cedr-emotion-detection")

    def detect_emotion(self, text):
        emotion = self.classifier(text, return_all_scores=True)
        return emotion[0]
