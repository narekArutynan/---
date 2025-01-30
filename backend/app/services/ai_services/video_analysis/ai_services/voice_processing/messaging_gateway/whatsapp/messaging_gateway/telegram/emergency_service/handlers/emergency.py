from fastapi import APIRouter
from ..services.notifications import send_notifications

router = APIRouter()

@router.post("/emergency")
async def handle_emergency(user_id: str):
    specialist = find_available_specialist()
    meeting = create_urgent_meeting(user_id, specialist.id)
    send_notifications(user_id, specialist.id, meeting.id)
    return {"status": "success", "meeting_id": meeting.id}
