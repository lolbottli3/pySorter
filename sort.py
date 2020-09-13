import os
import shutil

def sort_print(text, endin="\n"):
    print("[SORTER]: " + text, end=endin)
def sort_input(text):
    return input("[SORTER]: " + text)
sort_print("Starting up...")
q = sort_input("Do you want to sort files in the current directory? ")
if q.lower() == "n" or q.lower() == "no":
    cwd = sort_input("Give me the directory you want to sort files in! ")
else:
    cwd = os.getcwd()

print(cwd)
files = os.listdir(cwd)
for file in files:
    srca = cwd + "\ ".strip(" ") + str(file)
    """if os.path.isdir(srca):
        os.replace(srca,cwd + "\ ".strip(" ") + folders + "\ ".strip(" ") + str(file))"""
    if os.path.isfile(srca):
        dsta = cwd  + "\ ".strip(" ") + str(file).split(".")[1] + "\ ".strip(" ")
        dstb = cwd  + "\ ".strip(" ") + str(file).split(".")[1] + "\ ".strip(" ") + str(file)
        if not os.path.exists(dsta):
            os.makedirs(dsta)
        shutil.move(srca,dstb)
    else:
        Ff = cwd  + "\ ".strip(" ") + "Folders" + "\ ".strip(" ")
        dstb = cwd  + "\ ".strip(" ") + "Folders" + "\ ".strip(" ") + str(file)
        if not os.path.exists(Ff):
            os.makedirs(Ff)
        shutil.move(srca,dstb)

