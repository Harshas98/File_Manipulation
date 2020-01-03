import os
    

def createFolderorFile():
    directory = input("Enter the directory path to create a folder or file: ")
    os.chdir(directory)
    folderFile = input("Which one u want to create Folder or File ?\n").lower()
    try:
        print("Folder or File in "+directory+" are")
        for i in os.listdir():
            print(i)
        if(folderFile == "folder"):
            folder = input("Enter your Folder name:")
            if(folder in os.listdir()):
                print("Folder already exists ")
            os.makedirs(folder)
        else:
            file = input("Enter the file name: ")
            if(file in os.listdir()):
                print("File already exists ")
            os.mknod(file)
        print("SUCCESSFULLY CREATED!!\n\n")
    except:
        print("The folder or file exits in these directory try some other directory\n\n")
        createFolderorFile()




def deleteFolder():
    directory = input("Enter the directory path where the file you want to delete is located: ")
    os.chdir(directory)
    folderFile = ("Folder or File ?\n")
    print("The Folders present " + directory +" are ")
    for i in os.listdir():
        print(i)
    try:
        if(folderFile == "folder"):
            folder = input("enter the folder you want to delete :" )
            os.removedirs(folder)
        else:
            file = input("enter the file to delete : ")
            os.removedirs(file)
        print("SUCCESSFULLY DELETED!!")
    except:
        print("File doesn't exists Please enter a valid directory or file ")
        deleteFolder()
        



def showfilesofCurrentpath():
    directory = input("Enter the directory to show the files:")
    os.chdir(directory)
    for filesFolder in os.listdir():
        print(filesFolder)
    print("\n\n")



def renamethefileFolder():
    directory = input("Enter the directory path where the file is located u wanna change :")
    os.chdir(directory)
    folderFile = input("Which one u wanna change Folder or File ?").lower()
    for i in os.listdir():
        print(i)
    try:
        if(folderFile == "folder"):
            folder = input("Enter the folder to rename: ")
            newFolder = input("Enter the new folder name to be replaced : ")
            os.rename(folder,newFolder)
        else:
            file = input("Enter the file name u wanna rename :")
            newFile = input("Enter the new file name you wanna replace :")
            os.rename(file,newFile)
        print("SUCCESSFULLY RENAMED!!\n\n")
    except:
        print("The folder or file does not exits in these directory try some other directory \n\n")
        renamethefileFolder()



def sizeofFile():
    directory = input("Enter the directory where your file is located ? ")
    os.chdir(directory)
    folderFile = input("Folder or File ?").lower()
    try:
        if(folderFile == "folder"):
            folder = input("Enter the folder to know the size :")
            size = os.stat(folder).st_size
            print("The size of the foledr is ",size/1024,"KB")
        else:
            file = input("Enter the file name :")
            size = os.stat(file).st_size
            print("The size of the file is ",size/1024,"KB\n\n")
    except:
        print("File or Folder doesn't exists please re-enter the directory\n\n")
        sizeofFile()


def osName():
    print("The os name is ",os.uname().nodename)



while(1):
    print("Select any option\n\n1.create a folder\n2.delete a folder\n3.list the file of current working path\n4.rename the file\n5.file size\n6.know the OS\n7.Exit\n\n")
    choice = int(input("Enter your choice: "))
    if(choice == 1):
        createFolderorFile()
    elif(choice == 2):
        deleteFolder()
    elif(choice == 3):
        showfilesofCurrentpath()
    elif(choice == 4):
        renamethefileFolder()
    elif(choice == 5):
        sizeofFile()
    elif(choice == 6):
        osName()
    elif(choice == 7):
        break
