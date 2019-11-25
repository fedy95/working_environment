import os.path
import shutil
import string
from random import choice

binaryFilesDir = "binary"
textFilesDir = "text"

# Utility Functions
def GenerateRandomText(length=10*1024*1024, chars=string.ascii_letters + string.digits):
    return ''.join(["0" for i in range(length)])
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
 
    while(dirByteSize < (1030*1024*1024)):
        print("Populating {0}/random{1}.txt".format(textFilesDir,FileCount))
        file = open("{0}/random{1}.txt".format(textFilesDir,FileCount),"w+")
        randomText = GenerateRandomText()
        file.write(randomText)
        file.close()
        print("Finished {0}/random{1}.txt".format(textFilesDir,FileCount))
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
 
    while(dirByteSize < (1030*1024*1024)):
        print("Populating {0}/multi_binary{1}".format(binaryFilesDir,FileCount))
        file = open("{0}/multi_binary{1}".format(binaryFilesDir,FileCount),"wb")
        file.write(os.urandom(10*1024*1024))
        file.close()
        print("Finished {0}/multi_binary{1}".format(binaryFilesDir,FileCount))
 
        FileCount += 1
        dirByteSize = GetDirSize(binaryFilesDir)
        print("BinaryFiles Directory Size {0}MB".format(dirByteSize/1024/1024))
 
    print("BinaryFiles Directory compression started..")
    shutil.make_archive("multi_binary", 'zip', binaryFilesDir)
    shutil.move("multi_binary.zip", "{0}/multi_binary.zip".format(binaryFilesDir))
    print("BinaryFiles Directory compression completed.")
 
    print("BinaryFiles Cleanup started..")
    for i in range(1, FileCount):
        os.remove("{0}/multi_binary{1}".format(binaryFilesDir,i))
    print("BinaryFiles Cleanup completed..")
 
    print("Created BinaryFiles succesfully.")
 
def CreateBinaryFile(binaryFilesDir):
    print("Single Binary File creation started.")
 
    print("Creating Single BinaryFile...")
    print("Populating {0}/single_binary".format(binaryFilesDir))
    file = open("{0}/single_binary".format(binaryFilesDir),"wb")
    file.write(os.urandom(1030*1024*1024))
    file.close()
    print("Finished {0}/single_binary".format(binaryFilesDir))
 
    print("Single BinaryFile compression started..")
    print("Compressing {0}/single_binary".format(binaryFilesDir))
    shutil.make_archive("{0}/single_binary".format(binaryFilesDir), 'zip', binaryFilesDir, "single_binary")
    print("Compressed {0}/single_binary successfully.".format(binaryFilesDir))
 
    print("Single BinaryFile Cleanup started..")
    os.remove("{0}/single_binary".format(binaryFilesDir))
    print("Single BinaryFile Cleanup completed..")
 
    print("Created Single BinaryFile succesfully.")
 
def CreateLabFiles():
    binaryFilesDirExists = os.path.exists(binaryFilesDir)
    if binaryFilesDirExists:
        print("Binary File creation skipped, BinaryFiles directory already exists.")
    else:
        CreateBinaryFiles(binaryFilesDir)
        CreateBinaryFile(binaryFilesDir)
 
    textFilesDirExists = os.path.exists(textFilesDir)
    if textFilesDirExists:
        print("Text File creation skipped, TextFiles directory already exists.")
    else:
        CreateTextFiles(textFilesDir)
 
CreateLabFiles()
