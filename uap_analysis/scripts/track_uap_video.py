
import cv2
import numpy as np

def track_uap_video(video_path):
    '''Track UAP in a video using OpenCV's CSRT tracker.'''
    cap = cv2.VideoCapture(video_path)
    
    # Read first frame
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read video.")
        return
    
    # Select ROI (Region of Interest) for UAP
    bbox = cv2.selectROI("Select UAP", frame, False)
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        success, bbox = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        cv2.imshow("UAP Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    track_uap_video("data/raw/pentagon_uap_videos/tic_tac_flir.mp4")
