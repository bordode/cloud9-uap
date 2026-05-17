from ultralytics import YOLO

model = YOLO('yolov8n.pt')
model.train(data='ai-models/uap_detection/dataset/data.yaml', epochs=100, imgsz=640)
model.save('ai-models/uap_detection/runs/detect/train/weights/best.pt')
print("Training complete!")
