#Walking Directories 
import os

def walk(dirname):
    for name in os.listdir(dirname):
        path=os.path.join(dirname, name)


        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            walk(path)

#The ouput should be equivalent to    '$ls -R'

