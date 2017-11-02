# This file is responsibile for downloading a cam rewind.
# It can be run on its own, but is also utilized in backwash.py.
import os, urllib2, json
import multiprocessing as mp

def main():
    download_cam_rewind("http://www.surfline.com/surfdata/video-rewind/video_rewind_json.cfm?id=5157&context=2017-10-30")


def build_crf_url(camera, time, date):
    return "https://camrewinds.cdn-surfline.com/" + camera + "/" + camera + "." + str(time) + "." + date + ".mp4"
    

def download_file(url, filename):
    res = urllib2.urlopen(url)
    with open("./clips/" + filename, 'wb') as f:
        f.write(res.read())


def f(camera, time, date):
    url = build_crf_url(camera, time, date)
    filename = camera + "-" + time + "-" + date + ".mp4"
    print("Downloading " + url + "...")
    download_file(url, filename)
    return filename + " --> DONE"


def download_cam_rewind(apiUrl):
    print("\n!!!!!!!!!!!!")
    print("You may want to clear out your /clips/ folder before downloading.")
    print("!!!!!!!!!!!!\n")

    # Make sure /clips/ exists
    if not os.path.exists("clips/"):
        print("Creating /clips/ directory...\n")
        os.makedirs("clips")

    print("Starting download... CTRL+C to stop.\n")

    res = urllib2.urlopen(apiUrl)
    data = json.load(res)

    video_times = data['video_times']
    camera_alias = str(data['camera_alias'])
    date = str(data['context_aware'])

    pool = mp.Pool(processes=mp.cpu_count())
    times = []

    for i in range(0, len(video_times)):
        time = str(int(video_times[i]))
        # make '700' -> '0700'
        if(len(time) == 3):
            time = "0" + time
        times.append(time)
            
    complete = [pool.apply_async(f, (camera_alias,t, date,)) for t in times]
    for c in complete:
        print(res.get())


if __name__ == "__main__":
    main()
