import re
from datetime import timedelta
from googleapiclient.discovery import build

API_KEY = ''
youtube = build('youtube', 'v3', developerKey=API_KEY)
hours_pattern = re.compile(r'(\d+)H')
minutes_pattern = re.compile(r'(\d+)M')
seconds_pattern = re.compile(r'(\d+)S')

def printTime(sec, id):
    td = timedelta(seconds=sec)
    print('Video:', id, "Length:", td)

def getHours(item):
    hours = hours_pattern.search(item['contentDetails']['duration'])
    hours = int(hours.group(1)) if hours else 0
    return hours

def getMinutes(item):
    minutes = minutes_pattern.search(item['contentDetails']['duration'])
    minutes = int(minutes.group(1)) if minutes else 0
    return minutes

def getSeconds(item):
    seconds = seconds_pattern.search(item['contentDetails']['duration'])
    seconds = int(seconds.group(1)) if seconds else 0
    return seconds

def getItemDuration(duration):
    hours = hours_pattern.search(duration)
    minutes = minutes_pattern.search(duration)
    seconds = seconds_pattern.search(duration)
    hours = int(hours.group(1)) if hours else 0
    minutes = int(minutes.group(1)) if minutes else 0
    seconds = int(seconds.group(1)) if seconds else 0
    video_seconds = timedelta(
        hours=hours,
        minutes=minutes,
        seconds=seconds
    ).total_seconds()
    return video_seconds

def getDuration (item):
    duration = item['contentDetails']['duration']
    return getItemDuration(duration)

# Gets videos in playlist
pl_request = youtube.playlistItems().list(
    part='contentDetails',
    playlistId='PLjEaoINr3zgFX8ZsChQVQsuDSjEqdWMAD',
    maxResults=50
)
pl_response = pl_request.execute()

# Creates a list of all the video ids
vid_ids = []
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])
# Requests the details of all the videos
vid_request = youtube.videos().list(
    part='contentDetails',
    id=','.join(vid_ids)
)
vid_response = vid_request.execute()
tseconds = 0
tminutes = 0
thours = 0
counter = 1
for item in vid_response['items']:
    tseconds += getSeconds(item)
    tminutes += getMinutes(item)
    thours += getHours(item)
    printTime(getDuration(item), counter)
    counter += 1
tseconds += tminutes*60 + thours*3600
print('Time in Seconds:', tseconds)
printTime(tseconds, "Total")



