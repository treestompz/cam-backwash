# This file is responsibile for downloading a cam rewind.
# It can be run on its own, but is also utilized in backwash.py.
import os
import json
import urllib.request
import multiprocessing as mp


HEADERS = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}


def build_crf_url(camera, time, date):
    return f'https://camrewinds.cdn-surfline.com/{camera}/{camera}.{time}.{date}.mp4'


def download_file(camera, time, date):
    url = build_crf_url(camera, time, date)
    filename = f'{camera}-{time}-{date}.mp4'
    print('Download %s...' % url)
    res = urllib.request.urlopen(url)
    with open('./clips/' + filename, 'wb') as f:
        f.write(res.read())
    return filename + ' --> DONE'


def download_cam_rewind(apiUrl):
    print('!!! You may want to clear out your clips/ folder before downloading.')
    if not os.path.exists('clips/'):
        print('Creating /clips/ directory...\n')
        os.makedirs('clips')

    print('Starting download... CTRL+C to stop.\n')
    request = urllib.request.Request(apiUrl, None, HEADERS)
    res = urllib.request.urlopen(request)
    data = json.load(res)
    video_times = data['video_times']
    camera_alias = str(data['camera_alias'])
    date = str(data['context_aware'])

    times = []
    for video_time in video_times:
        time = str(int(video_time))
        if len(time) == 3:
            time = '0' + time # '700' -> '0700'
        times.append(time)

    pool = mp.Pool(processes=mp.cpu_count())
    complete = [pool.apply_async(download_file, (camera_alias, time, date)) for time in times]
    for c in complete:
        print(c.get())
