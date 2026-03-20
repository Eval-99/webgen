import os
import shutil


def copy_recur(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)
    for item in os.listdir(source):
        if os.path.isfile(os.path.join(source, item)):
            shutil.copy(os.path.join(source, item), destination)
            print(f"Copying {os.path.join(source, item)} to {destination}")
            continue
        else:
            copy_recur(os.path.join(source, item), os.path.join(destination, item))
