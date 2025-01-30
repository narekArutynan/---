from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from .emotion_analyzer import EmotionAnalyzer
import requests
import jwt
import time

class ActionDetectEmotion(Action):
    def name(self) -> Text:
        return "action_detect_emotion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        analyzer = EmotionAnalyzer()
        message = tracker.latest_message.get('text')
        emotion = analyzer.analyze(message)
        
        dispatcher.utter_message(text=f"Я понял, что вы испытываете {emotion['label']}")
        return []

class ActionCreateZoomMeeting(Action):
    def __init__(self):
        self.api_key = os.getenv('ZOOM_API_KEY')
        self.api_secret = os.getenv('ZOOM_API_SECRET')
        self.user_id = os.getenv('ZOOM_USER_ID')

    def generate_jwt(self):
        payload = {
            "iss": self.api_key,
            "exp": int(time.time()) + 5000
        }
        return jwt.encode(payload, self.api_secret, algorithm="HS256")

    def name(self) -> Text:
        return "action_create_zoom_meeting"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        headers = {
            "Authorization": f"Bearer {self.generate_jwt()}",
            "Content-Type": "application/json"
        }

        payload = {
            "topic": "Консультация со специалистом",
            "type": 1,
            "settings": {
                "host_video": True,
                "participant_video": True
            }
        }

        response = requests.post(
            f"https://api.zoom.us/v2/users/{self.user_id}/meetings",
            json=payload,
            headers=headers
        )

        if response.status_code == 201:
            meeting_url = response.json().get("join_url")
            dispatcher.utter_message(
                text=f"Запланирована встреча со специалистом: {meeting_url}")
        else:
            dispatcher.utter_message(
                text="Извините, возникла ошибка при создании встречи")

        return []
