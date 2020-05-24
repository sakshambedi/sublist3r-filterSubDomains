# Importing libraries 
import argparse
import os.path
import subprocess
import platform


""" 
Purpose : Reading from a file and return the list of parsed link 
@param fileName : name of the input file name
"""
def readFromFile(fileName):
    openFile = open(fileName,"r")
    lines = openFile.readlines()
    
    # making a list to add all the elements into the list 
    webLinks = []

    for line in lines:
        eachLine = line.replace("<BR>","\n")
        webLinks.append(eachLine.strip())
    
    # for eachLink in webLinks : print(eachLink)
    
    openFile.close
    return webLinks



""" 
Purpose check if the file exist 
@param filePath  : Path of the file 
"""
def isFileThere(filePath):
    return os.path.isfile(filePath)




def performPingTest(host):
    args = "ping -c 1 "+ host
    return subprocess.call(args,True) == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # adding arguments 
    parser.add_argument("-v","--version",help= "versionNumber" ,action = "store_true")
    parser.add_argument("-i","--input", type= str, required = True, help = "Name of input text file")
    parser.add_argument("-o","--output",type = str, required = True, help ="Name of output text file")
    parser.add_argument("-p","--port",help= "port to perform testing")

    args  = vars(parser.parse_args())

    streamInputName = args["input"]
    streamOutputName = args["output"]
    streamPort = args["port"]

    # print("\nInput Stream File : " + streamInputName)
    # print("\nOutput Stream File : " + streamOutputName)


    if(isFileThere(streamInputName)): 
        sortedList = readFromFile(streamInputName)
        for hosts in sortedList:
            print(str(performPingTest(hosts)))
    else : 
        print("There is no such file in",os.getcwd()) 
        breakpoint

