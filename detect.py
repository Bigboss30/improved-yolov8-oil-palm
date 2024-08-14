from ultralytics import YOLO

# Load a model
model = YOLO("yolov8x-best.pt")  # load an official model

# Predict with the model
results = model.predict("Palm-Detection-4/valid/images", save=True, save_crop=True, conf=0.5)