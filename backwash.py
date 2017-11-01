# This file utilizes download.py and combine.py to
# 1) Download clips from a cam rewind
# 2) Combine them into a single .mp4
# It also provides a bunch of conveniences for the user like:
# - TODO: Clearing clips folder
# - TODO: Only downloading a select time frame
# - TODO: Only combining a select time frame

import sys

from download import download_cam_rewind
from combine import combine

def main():
    if len(sys.argv) == 3:
        spot_id = sys.argv[1]
        date = sys.argv[2]

        print("Spot ID: " + spot_id)
        print("Date: " + date)
        print("\nRunning download.py and combine.py...\n")

        download_cam_rewind("http://www.surfline.com/surfdata/video-rewind/video_rewind_json.cfm?id=" + spot_id + "&context=" + date)

        combine()
        
    else:
        print("Error: incorrect input.")
        print("Format: \"python backwash.py [SPOT_ID] [YEAR-MM-DD]\"")
        print("Example: \"python backwash.py 5157 2017-10-30\"")


if __name__ == "__main__":
    main()
