import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
DEVICE = torch.device("cpu") 

# ----------------------------
# Model (exact copy)
# ----------------------------
class SimpleCNN(nn.Module):
    def __init__(self):
        super().__init__()

        self.conv1 = nn.Conv2d(1, 16, 3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, 3, padding=1)
        self.conv3 = nn.Conv2d(32, 64, 3, padding=1)

        self.pool = nn.MaxPool2d(2, 2)
        self.adaptive_pool = nn.AdaptiveAvgPool2d((1, 1))

        self.fc1 = nn.Linear(64, 32)
        self.fc2 = nn.Linear(32, 2)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = self.pool(F.relu(self.conv3(x)))

        x = self.adaptive_pool(x)
        x = torch.flatten(x, 1)

        x = F.relu(self.fc1(x))
        x = self.fc2(x)

        return x

# ----------------------------
# Load model
# ----------------------------
model = SimpleCNN()
model.load_state_dict(torch.load("model.pth", map_location=DEVICE))
model.to(DEVICE)
model.eval()

# ----------------------------
# Routes
# ----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


@app.route("/", methods=["POST"])
def predict():
    try:
        file = request.files["file"]

        np_data = np.load(file)

        if np_data.shape != (512, 512):
            return jsonify({"error": "Invalid shape"}), 400

        tensor = torch.tensor(np_data, dtype=torch.float32)\
                    .unsqueeze(0).unsqueeze(0)

        with torch.no_grad():
            output = model(tensor)
            probs = torch.softmax(output, dim=1)

            pred = torch.argmax(probs, dim=1).item()
            prob = probs[0][1].item()

        return jsonify({
            "prediction": pred,
            "probability_class_1": prob
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500