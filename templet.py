import os

#This program has been inspired by cokicater.
#this is used to create folders and files no matter what is the OS system you use.
dirs =[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    "notebook",
    "saved_models",
    "src"
]

#This for loop will carete the above dir structuer
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        #The .getkeep is just to not keep the folder empety
        pass



files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"), #this to keep the soruce as a python packge
]

for file_ in files:
    with open(file_, "w") as f:
        pass