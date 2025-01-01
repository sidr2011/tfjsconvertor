from ultralytics import YOLO

# Load a pre-trained YOLO11 model
model = YOLO("yolov8n.pt") #best.pt

# Specify the source image
# source = "https://ultralytics.com/images/bus.jpg"
source = "000000_jpg.rf.1b029d4c742673020fa91367070f5f51.jpg"
# Make predictions
results = model.predict(source, save=True, imgsz=320, conf=0.5)
print("results :", results)
# Extract bounding box dimensions
boxes = results[0].boxes.xywh.cpu()
for box in boxes:
    x, y, w, h = box
    print(f"Width of Box: {w}, Height of Box: {h}")