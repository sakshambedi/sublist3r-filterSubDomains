#import sys.stdout
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
    AllCorrectedDomains  = wwwHost(webLinks)

    for items in AllCorrectedDomains :
        print (items)
    openFile.close


def wwwHost(tempList):
    newLinkList = []
    eachNewLink = "name"
    for eachLink in tempList:
        if "www." not in eachLink:
            eachNewLink = "www." + eachLink
        newLinkList.append(eachNewLink)
    return newLinkList

def main():
    # fileName = input("Enter the name of File : ")
    readFromFile("skiptheDishes.txt")

# @staticmethod
if __name__ == "__main__":
    main()