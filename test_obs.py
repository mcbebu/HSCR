from obs import ObsClient, Object, DeleteObjectsRequest
import base64
import datetime
from dotenv import load_dotenv
import os

AK = os.environ['AK']
SK = os.environ['SK']
server = os.environ['server']
bucketName = os.environ['bucketName']
objectKey = 'my-obs-object-key-demo'
obsClient = ObsClient(access_key_id=AK, secret_access_key=SK, server=server)
# bucketClient = obsClient.bucketClient(bucketName)
# resp = bucketClient.putFile("test-image.jpg", "demo.jpg")
# print(resp)

resp = obsClient.listObjects(bucketName)
contents = resp['body']['contents']
contents.sort(key=lambda x: x['lastModified'])
print(contents)
image_name = contents[-1]['key']
print(image_name)
# resp = obsClient.getObject(bucketName, image_name, loadStreamInMemory=True)
# image_buffer = resp['body']['buffer']
# image_bytes = str(base64.b64encode(image_buffer))
# print(image_bytes)
