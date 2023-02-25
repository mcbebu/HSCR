# HSCR
We are trying to solve a critical problem faced by Ninjavan's sorting center. Currently, the facility might experience delays and potential losses due to clogs caused by high influx of goods, coupled with a disorganised sorting process that makes it difficult to locate items. Our solution involves organising the warehouse to ensure efficient pallet placement, and implementing computer vision with AI to detect vacant spaces. This will provide decision makers with real-time information to facilitate transport of goods to either the sorting hub or backlog facility. By streamlining the sorting process, we can help Ninjavan save time, money, and provide a better experience for their customers.

## solution
Object detection of pallet and empty boxed out spaces
Dashboard for warehouse manager to monitor the congestion
Alerts/update to drivers app

## Assumption
Fixed position of camera (top-down)
2 classes: Empty and Occupied by pallet
The staff will place the objects in the right places
Images are streamed to OBS (HuaWei Cloud)/S3 (AWS)

# create virtual environment and install dependencies
python -m venv venv
venv\scripts\activate
pip install -r yolov5/requirements.txt