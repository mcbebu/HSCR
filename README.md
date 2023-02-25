# HSCR
We are trying to solve a critical problem faced by Ninjavan's sorting center. Currently, the facility might experience delays and potential losses due to clogs caused by high influx of goods, coupled with a disorganised sorting process that makes it difficult to locate items. Our solution involves organising the warehouse to ensure efficient pallet placement, and implementing computer vision with AI to detect vacant spaces. This will provide decision makers with real-time information to facilitate transport of goods to either the sorting hub or backlog facility. By streamlining the sorting process, we can help Ninjavan save time, money, and provide a better experience for their customers.

## solution
- detect one box 
- detect empty and object
- then scale to whole pict
- find the boxes in the new image first
- then  identify the vacancy in the box

# create virtual environment and install dependencies

## windows
python -m venv venv
venv\scripts\activate
pip install -r yolov5/requirements.txt

## macs
python -m venv venv
source venv/bin/activate
pip install -r yolov5/requirements.txt