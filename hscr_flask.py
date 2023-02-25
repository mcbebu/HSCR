import io
import torch
from flask import Flask, jsonify
from PIL import Image
import base64

app = Flask(__name__)

model_path = "best.pt"
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

# Define a route handler to make predictions
@app.route("/predict", methods=["GET"])
def predict():
    # Get the input data from the request
    # input_data = request.json["data"]
    # Convert the input image to a PIL Image object
    input_image_path = "demo.jpg"
    with open(input_image_path, "rb") as input_image:
        image_bytecode = input_image.read() 
        pil_image = Image.open(io.BytesIO(image_bytecode))
        image_bytes = str(base64.b64encode(image_bytecode))

    results = model(pil_image)

    results_string = str(results)
    results_string = " ".join(results_string.split("\n")[0].split(" ")[-2:])
    
    # Return the output data as a JSON response

    # strip the b from the image_bytes
    return jsonify({"result": results_string, "image_bytes": image_bytes[2:-1]})

@app.route("/health", methods=["GET"])
def health():
    return "OK"

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)