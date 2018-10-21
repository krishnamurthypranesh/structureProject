This is a module to create a structure for a data science project.
Run structureProject.py to set up the directories for your data science project.

This is the structure used in creating the project setup

| Data -> contains the datasets used in the project
|
|src ->
|       |data           -> contains the scripts used to clean, wrangle and
|                            prepare the datasets for modelling
|       |scripts        ->
|                    | train   -> contains the scripts for training the model
|                    | test    -> contains the scripts for testing the model
|       |visualizations -> contains the scripts for creating visualizations
|
|README.txt -> the readme file for the project
|requirements.txt -> the requirements for the project


The structureProject.py file contains the following functions:
  -> structureProject(path = os.getcwd(), initializeRequirements = False,
                      initializeReadme = False):
      -> The path is the directory in which the project will be situated.
      -> The initializeReadme argument initializes the README file with the text
          provided by the user on prompt.
      -> The initializerequirements argument initializes the requirements.txt
          file with the text provided by the user on prompt.
