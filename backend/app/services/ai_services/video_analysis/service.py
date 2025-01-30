from fer import FER
import cv2

class VideoAnalyzer:
    def __init__(self):
        self.detector = FER(mtcnn=True)
    
    def analyze(self, video_path: str):
        cap = cv2.VideoCapture(video_path)
        emotions = []
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
                
            result = self.detector.detect_emotions(frame)
            if result:
                emotions.append(max(result[0]['emotions'], 
                                 key=result[0]['emotions'].get))
        
        cap.release()
        return max(set(emotions), key=emotions.count)
