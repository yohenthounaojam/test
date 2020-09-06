import pandas as pd
import numpy as np
import os
import csv
from datetime import datetime

dire = '/Users/renee/Downloads/release_2019_07_08/2017_02_27_ITS1/201702271017/general/csv/'
os.chdir(dire)
# print(os.listdir())
with open("accel_pedal.csv", 'r') as f:
    wines = list(csv.reader(f, delimiter=","))

# print(wines[0:17])

# print(datetime.fromisoformat("2017-02-27T10:17:30+08:00"))

from numpy import genfromtxt
my_data = genfromtxt('brake_pedal.csv', delimiter=',', dtype=str)
# print(my_data[0,0:3])
# print(len(my_data))

# files = os.listdir()
# print(files)
# print(len(files))
# count=0
# for i in files:
#      if (i==".ipynb_checkpoints"):
#           continue
     # remove = len(i) - 7
     # old_name = i
     # new_name = old_name.replace('-','_')[:remove]
     # #saving folder name for sensor data - level 2
     # folder_name_2 = new_name.replace("_","")
     # #saving folder name for sensor data - level 1   
     # remove-=5  
     # folder_name_1 = new_name[:remove].__add__("ITS1")
     # folder_name_1 = i.__add__(".eaf")
     # print(folder_name_1)
     # os.rename(i,folder_name_1)
     # count+=1



# print("Count: "+str(count))


def translate_index_to_timestamp(session_id, index, fps_rate=3):#Change to FPS ---------------------
  """
  Tanslate the index to timestamp (approximate)
  Args:
    session_id (str): Session ID of the video.mp4
    index (): index of the image frame.

  Returns:
    float: converted timestamp
  """
  import os #remove ------------------
  from datetime import datetime, timedelta # remove ----------------------
  # Following formula gets timming of video from index for 3FPS.  
  # Note that this is not the Unix timestamp
  video_time_from_index = ((1/fps_rate)/2)+(index-1)*(1/fps_rate)
  # Sensor data and video data do not start at the same ISO timestamp
  # Video file names contain the ISO timestamp of the start of the video
  HDD_VIDEO_PATH = "/Users/renee/Downloads/release_2019_07_08/2017_02_27_ITS1/{0}/camera/center"      
  # Needs to removed ^ -----------------------------
  video_file_name = os.listdir(HDD_VIDEO_PATH.format(session_id))[0]
  start_of_video = datetime.fromisoformat(video_file_name[0:10:]+" "+(video_file_name[11:19:]).replace("-",":"))
  # Converting the video_time_from_index to ISO timestamp
  print("heloo")
  print(start_of_video)
  timestamp = start_of_video + timedelta(seconds=video_time_from_index)
  # Now retrieving the sensor data's starting ISO timestamp
  sensor_data = genfromtxt('brake_pedal.csv', delimiter=',', dtype=str, skip_header=155000)
  return timestamp 

print(translate_index_to_timestamp("201702271017",100))