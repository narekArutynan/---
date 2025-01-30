from transformers import pipeline

class EmotionAnalyzer:
    def __init__(self):
        self.model = pipeline(
            "text-classification",
            model="bhadresh-savani/distilbert-base-uncased-emotion",
            return_all_scores=True
        )
    
    def analyze(self, text: str) -> Dict[str, Any]:
        results = self.model(text)[0]
        return sorted(results, key=lambda x: x['score'], reverse=True)[0]
