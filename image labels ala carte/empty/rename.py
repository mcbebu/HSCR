import os

directory = os.getcwd()  # replace with the path to your directory

# loop through the files in the directory
def rename_files():
    counter =1 
    for filename in os.listdir(directory):
        print(filename) 
        # check if the file is a regular file (not a directory or special file)
        if os.path.isfile(os.path.join(directory, filename)):
            # add the prefix to the filename
            new_filename = "empty"+ str(counter) + '.jpg'
            # rename the file
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
        counter += 1
if __name__ == "__main__":
    rename_files()