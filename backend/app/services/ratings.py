from sqlalchemy import func
from ..db.session import session
from ..models import Review, Specialist

class RatingSystem:
    def calculate_rating(self, specialist_id):
        avg_rating = session.query(
            func.avg(Review.rating)
        ).filter_by(specialist_id=specialist_id).scalar()
        
        return round(avg_rating, 2) if avg_rating else 0.0

    def update_rating(self, specialist_id, new_rating):
        specialist = session.query(Specialist).get(specialist_id)
        specialist.rating = self.calculate_rating(specialist_id)
        session.commit()
