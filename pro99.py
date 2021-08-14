import time
import os
import shutil
def main():
    path = input("Enter the path address: ")
    days = 30
    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):
        for rootfolder, folders, files in os.walk(path):
            if seconds >= getage(rootfolder):
                removefolder(rootfolder)
                break
            else:
                for folder in folders:
                    folderpath = os.path.join(rootfolder,folder)
                    if seconds >= getage(folderpath):
                        removefolder(folderpath)
                for file in files:
                    filepath = os.path.join(rootfolder,file)
                    if seconds >= getage(filepath):
                        removefile(filepath)
    else:
        print("Path doesn't exist")
   
def removefolder(path):
    if not shutil.rmtree(path):
        print("Path removed successfully!")
    else: 
        print("Unable to delete path")    

def getage(path):
    ctime = os.stat(path).st_ctime
    return(ctime)  

def removefile(path):
    if not os.remove(path):
        print("File removed successfully!")
    else:
        print("Unable to delete file")   

main()          