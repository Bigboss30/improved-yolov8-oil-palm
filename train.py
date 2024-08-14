# from roboflow import Roboflow
# rf = Roboflow(api_key="co9myt0hE5EWNqiV2iT4")
# project = rf.workspace("my-thesis-workspace").project("palm-detection")
# version = project.version(4)
# dataset = version.download("yolov8")
import torch
from ultralytics import YOLO

if __name__ == '__main__':
    # Load a model
    # model = YOLO("yolov8n.yaml")  # build a new model from YAML
    model = YOLO("yolov8x-best.pt")  # load a pretrained model (recommended for training)
    # model = YOLO("runs/detect/train2/weights/last.pt")  # load a pretrained model (recommended for training)
    # model = YOLO("yolov8n.yaml").load("yolov8n.pt")  # build from YAML and transfer weights

    # freezing logic
    freeze = [f"model.{x}." for x in range(19)]
    for k, v in model.named_parameters():
        v.requires_grad = True  # train all layers
        if any(x in k for x in freeze):
            print(f"freezing {k}")
            v.requires_grad = False

    for k , v in model.named_parameters():
        print(k, v.requires_grad)
        
    # layers = list(model.model.modules())
    # print(f"MODEL LAYERS -> {len(layers)}")
    
    # for i, layer in enumerate(model.model.modules()):
    #     print(f'Layer {i}: {layer}')
    
    # for i, (name, param) in enumerate(model.named_parameters()):
    #     print(i, name)
    
    # Train the model
    results = model.train(data="Palm-Detection-4/data.yaml", epochs=100, imgsz=640,  batch=2)
    # results = model.train(resume=True)