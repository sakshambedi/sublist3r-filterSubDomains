# Importing libraries 
import argparse
import os.path


def readFromFile(fileName):
    # Assinging variables 
    webLinks = []
    
    openFile = open(fileName,"r")
    while line := openFile.readline():
        tempList = []    
        if "<BR>" in line: 
            templist = line.split("<BR>")
            webLinks.extend(templist)
        else :
            webLinks.append(line.strip())
    # AllCorrectedDomains  = wwwHost(webLinks)
    # for items in AllCorrectedDomains :
    #     print (items)
    openFile.close
    return webLinks


def wwwHost(tempList):
    newLinkList = []
    eachNewLink = None
    for eachLink in tempList:
        if "www." not in eachLink:
            eachNewLink = "www." + eachLink
        newLinkList.append(eachNewLink)
    return newLinkList



""" 
Purpose check if the file exist 
@param filePath  : Path of the file 
"""
def isFileThere(filePath):
    return os.path.isfile(filePath)


def manageOutputFile(outputFileName, resolvedDomainList):
    outputFile = open(outputFileName,"w+")

    for eachHost in resolvedDomainList :
        outputFile.write(str(eachHost) + "\n")


"""
Purpose : Perform ping testing to a given sublink from the fetched links using sublist3r
          If port not specified default = 22
@param : list of all the host and return the list of filtered Hosts 
"""
def performPingTest(host):
    return os.system("ping -c 2 " + str(host) ) == 0



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    # adding arguments 
    parser.add_argument("-i","--input", type= str, required = True, help = "Name of input text file")
    parser.add_argument("-o","--output",type = str, required = True, help ="Name of output text file")


    args  = vars(parser.parse_args())

    streamInputName = args["input"]
    streamOutputName = args["output"]

    # print("\nInput Stream File : " + streamInputName)
    # print("\nOutput Stream File : " + streamOutputName)
    resolvedDomainList = [] 

    if(isFileThere(streamInputName)): 
        sortedList = readFromFile(streamInputName)
        for host in sortedList:
            if(performPingTest(host)):
                resolvedDomainList.append(host)
                print("Adding new domain \n")
        manageOutputFile(streamOutputName, resolvedDomainList)
        print("Resolved to all responding sub-domains added to list " + str(streamOutputName) + " in " + os.getcwd())
    else :
        print("There is no such file in",os.getcwd()) 
       

