# This file is responsibile for combining all the files in the /clips/ directory into a single .mp4.
# It can be run on its own, but is also utilized in backwash.py.
import os
from subprocess import call


def combine():
    # Delete old input.txt file
    if os.path.exists('input.txt'):
        os.remove('input.txt')

    # Create an input.txt file ffmpeg with each file listed as:
    # file '/clips/input1.mp4'
    print('Creating input.txt file...')
    with open('input.txt', 'a') as inputFile:
        # the 4 digit timestamps on the files will sort just fine
        for file in sorted(os.listdir('./clips')):
            if file.endswith('.mp4'):
                inputFile.write('file \'./clips/' + file + '\'\n')
                print('- Added' + file)

    print('Combining all clips...')
    call(['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'input.txt', '-codec', 'copy', 'combined.mp4'])
    print('\nFinished.')


if __name__ == '__main__':
    combine()
