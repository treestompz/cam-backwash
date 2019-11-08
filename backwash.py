# This file utilizes download.py and combine.py to:
# - Download clips from a cam rewind
# - Combine them into a single .mp4
import sys
from download import download_cam_rewind
from combine import combine


def main():
    if len(sys.argv) != 3:
        print('Error: incorrect input.')
        print('Format: \'python backwash.py [SPOT_ID] [YEAR-MM-DD]\'')
        print('Example: \'python backwash.py 5157 2017-10-30\'')
        return

    spot_id = sys.argv[1]
    date = sys.argv[2]
    print('Spot ID: %s' % spot_id)
    print('Date: %s' % date)
    print('\nRunning download.py and combine.py...\n')
    url = f'http://www.surfline.com/surfdata/video-rewind/video_rewind_json.cfm?id={spot_id}&context={date}'
    download_cam_rewind(url)
    combine()


if __name__ == '__main__':
    main()
