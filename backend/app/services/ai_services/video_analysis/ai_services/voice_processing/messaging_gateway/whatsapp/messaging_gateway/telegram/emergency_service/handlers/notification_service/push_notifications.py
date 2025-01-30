from pywebpush import webpush
import os

def send_push_notification(subscription_info, message):
    webpush(
        subscription_info=subscription_info,
        data=message,
        vapid_private_key=os.getenv('VAPID_PRIVATE_KEY'),
        vapid_claims={"sub": "mailto:admin@example.com"}
    )
