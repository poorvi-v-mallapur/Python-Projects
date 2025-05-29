import gradio as gr
from torchvision import models, transforms
from PIL import Image
import torch
import requests

# Load pretrained model
model = models.resnet18(pretrained=True)
model.eval()

# Image transformations for the model
transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Get class labels
LABELS_URL = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
response = requests.get(LABELS_URL)
labels = response.text.strip().split("\n")

# Define prediction function
def classify_image(image):
    image = transform(image).unsqueeze(0)
    with torch.no_grad():
        predictions = model(image)
    predicted_class = predictions.argmax(1).item()
    return labels[predicted_class]

# Gradio UI
interface = gr.Interface(
    fn=classify_image,
    inputs=gr.Image(type="pil"),
    outputs="label",
    title="Image Classifier",
    description="Upload an image and I will tell you what I think it is!"
)

interface.launch()