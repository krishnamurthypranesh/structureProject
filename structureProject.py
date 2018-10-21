# This file contains the code for creating the folder structure for the data
# science project.
import os
import sys

def structureProject(path = os.getcwd(), initializeRequirements = False, \
    initializeReadme = False):
    directories_list = ["Data", "src", "src/data", "src/scripts", "src/visualizations"]

    if initializeReadme:
        directories_list.append("README.txt")

    if initializeRequirements:
        directories_list.append("requirements.txt")    


    paths = [(path + "/" + i) for i in directories_list]

    if initializeReadme or initializeRequirements:
        if initializeReadme:
            try:
                with open("README.txt", "w") as readme:
                    print("Enter the content for the README:")
                    readmeContent = sys.stdin.readlines()
                    for line in readmeContent:
                        print(line, file = readme)
            except IOError as ioerr:
                print("Unable to create and initialize README")
                with open("errorLog.txt", "w") as errorFile:
                    print(ioerr, file = errorFile)
            except Exception as err:
                print("Process failed. Encountered the following error while " + \
                        "creating and initializing README " + str(err))
                with open("errorLog.txt", "w") as errorFile:
                    print(err, file = errorFile)
        elif initializeRequirements:
            try:
                with open("requirements.txt", "w") as requirements:
                    print("Enter the content for the requirements:")
                    requirementsContent = sys.stdin.readlines()
                    for line in requirementsContent:
                        print(line, file = requirements)
            except IOError as ioerr:
                print("Unable to create and initialize requirements")
                with open("errorLog.txt", "w") as errorFile:
                    print(err, file = errorFile)
            except Exception as err:
                print("Process failed. Encountered the following error while " + \
                        "creating and initializing requirements " + str(err))
                with open("errorLog.txt", "w") as errorFile:
                    print(err, file = errorFile)
                    
    try:
        for path in paths:
            os.makedirs(path)
            print("Successfully created " + path)
    except Exception as err:
        print("err")
        with open("errorLog.txt", "w") as errorFile:
            print(err, file = errorFile)
