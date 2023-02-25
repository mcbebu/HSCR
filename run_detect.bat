@echo off
setlocal enabledelayedexpansion

set "directory=.\yolov5\runs\train"
set "latestFolder="
set "latestNumber=0"

for /d %%a in ("%directory%\*") do (
  set "folderName=%%~na"
  set "folderNumber=!folderName:*exp=!"
  if !folderNumber! gtr !latestNumber! (
    set "latestFolder=%%a"
    set "latestNumber=!folderNumber!"
  )
)

python yolov5\detect.py --weights "%latestFolder%\weights\best.pt" --img 640 --conf 0.1 --source 0
