import io
import torch
from flask import Flask, jsonify
from PIL import Image
import base64
from obs import ObsClient, Object, DeleteObjectsRequest
from dotenv import load_dotenv
import os

load_dotenv()

AK = os.environ['AK']
SK = os.environ['SK']
server = os.environ['server']
bucketName = os.environ['bucketName']
obsClient = ObsClient(access_key_id=AK, secret_access_key=SK, server=server)

app = Flask(__name__)

model_path = "best.pt"
torch.hub._validate_not_a_forked_repo=lambda a,b,c: True
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

# Define a route handler to make predictions
@app.route("/predict", methods=["GET"])
def predict():
    resp = obsClient.listObjects(bucketName)
    contents = resp['body']['contents']
    contents.sort(key=lambda x: x['lastModified'])
    image_name = contents[-1]['key']
    print(image_name)
    resp = obsClient.getObject(bucketName, image_name, loadStreamInMemory=True)
    image_buffer = resp['body']['buffer']
    image_bytes = str(base64.b64encode(image_buffer))
    pil_image = Image.open(io.BytesIO(image_buffer))
    image_bytes = str(base64.b64encode(image_buffer))

    results = model(pil_image)

    results_string = str(results)
    print(results_string)
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