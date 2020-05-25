# Importing libraries 
import argparse
import os.path
import subprocess


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
        if "www" not in webLinks:
            webLinks
    
    # for eachLink in webLinks : print(eachLink)
    
    openFile.close
    return webLinks



""" 
Purpose check if the file exist 
@param filePath  : Path of the file 
"""
def isFileThere(filePath):
    return os.path.isfile(filePath)



"""
Purpose : Perform ping testing to a given sublink from the fetched links using sublist3r
          If port not specified default = 22
@param : list of all the host and return the list of filtered Hosts 
"""
def performPingTest(host, port = 22):
    args = "telnet "+ host + port
    return subprocess.call(args,shell=True) == 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # adding arguments 
    parser.add_argument("-v","--version",help= "versionNumber" ,action = "store_true")
    parser.add_argument("-i","--input", type= str, required = True, help = "Name of input text file")
    parser.add_argument("-o","--output",type = str, required = True, help ="Name of output text file")
    parser.add_argument("-p","--port",type= int ,help= "port to perform testing")

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

