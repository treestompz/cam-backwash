# This file is responsibile for combining all the files in the /clips/ directory into a single .mp4.
# It can be run on its own, but is also utilized in backwash.py.
import os
from subprocess import call


def main():
    combine()


def combine():
    # Delete old input.txt file
    if os.path.exists("input.txt"):
        os.remove("input.txt")

    print("Creating input.txt file...")

    clipFiles = os.listdir("./clips")
    counter = 0

    # Create an input.txt file ffmpeg with each file listed as:
    # file '/clips/input1.mp4'

    with open("input.txt", "a") as inputFile:
        for file in os.listdir("./clips"):
            if(file.endswith(".mp4")):
                counter += 1
                inputFile.write("file \'./clips/" + file + "\'\n")
                print("- Added" + file)

    print("Combining all clips...")

    # use the concat demuxer
    # ffmpeg -f concat -i input.txt -codec copy output.mp4
    call(["ffmpeg", "-f", "concat", "-safe", "0", "-i", "input.txt", "-codec", "copy", "combined.mp4"])

    print("\nFinished.")


if __name__ == "__main__":
    main()
