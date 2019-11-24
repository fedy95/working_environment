import os.path
import shutil
from shutil import make_archive
from random import choice
import string

textFilesDir = "text"
binaryFilesDir = "binary"

# Utility Functions
def GenerateRandomText(length=10*1024*1024, chars=string.ascii_letters + string.digits):
    return ''.join([choice(chars) for i in range(length)])

def GetDirSize(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

# Main Functions
def CreateTextFiles(textFilesDir):
    print("Text File creation started.")
    print("Creating TextFiles directory..")
    os.makedirs(textFilesDir)

    print("Creating TextFiles...")
    dirByteSize = GetDirSize(textFilesDir)
    FileCount = 1

    while(dirByteSize < (1024*1024*1024)):
        file = open("{0}/random{1}.txt".format(textFilesDir,FileCount),"w+")
        randomText = GenerateRandomText()
        file.write(randomText)
        file.close()
        FileCount += 1
        dirByteSize = GetDirSize(textFilesDir)
        print("TextFiles Directory Size {0}MB".format(dirByteSize/1024/1024))

    print("Created TextFiles succesfully.")

def CreateBinaryFiles(binaryFilesDir):
    print("Binary File creation started.")
    print("Creating BinaryFiles directory..")
    os.makedirs(binaryFilesDir)

    print("Creating BinaryFiles...")
    dirByteSize = GetDirSize(binaryFilesDir)
    FileCount = 1

    while(dirByteSize < (1024*1024*1024)):
        print("Populating {0}/randombinary{1}".format(binaryFilesDir,FileCount))
        file = open("{0}/randombinary{1}".format(binaryFilesDir,FileCount),"wb")
        file.write(os.urandom(1024*1024*1024))
        file.close()
        print("Finished {0}/randombinary{1}".format(binaryFilesDir,FileCount))

        print("Binary Files compression started..")
        print("Compressing {0}/randombinary{1}".format(binaryFilesDir,FileCount))
        shutil.make_archive("{0}/randombinary{1}".format(binaryFilesDir,FileCount), 'zip', binaryFilesDir, "randombinary{0}".format(FileCount))
        print("Compressed {0}/randombinary{1} successfully.".format(binaryFilesDir,FileCount))

        if (FileCount != 1):
            os.remove("{0}/randombinary{1}".format(binaryFilesDir,FileCount))

        FileCount += 1
        dirByteSize = GetDirSize(binaryFilesDir)
        print("BinaryFiles Directory Size {0}MB".format(dirByteSize/1024/1024))

    print("Created BinaryFiles succesfully.")

def CreateLabFiles():
    binaryFilesDirExists = os.path.exists(binaryFilesDir)
    if binaryFilesDirExists:
        print("Binary File creation skipped, BinaryFiles directory already exists.")
    else:
        CreateBinaryFiles(binaryFilesDir)

    textFilesDirExists = os.path.exists(textFilesDir)
    if textFilesDirExists:
        print("Text File creation skipped, TextFiles directory already exists.")
    else:
        CreateTextFiles(textFilesDir)

CreateLabFiles()
