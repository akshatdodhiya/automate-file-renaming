import os
from time import sleep


def process_output():
    """
    Function that prints a simple progress bar to make output more attractive
    """
    print("Processing......", end="")
    for i in range(10):  # Printing a simple progress bar using for loop
        sleep(0.2)
        print("." * i, end="")

    print("\nDone processing :)\n")


def arrange(folder, file, ext):
    """
    This function will rename the files present in a specific directory
    except some files that are present in parameter 'file'

    :param folder: The path from which files should be handled
    :param file: The file in which the names of exception files are written with extension
    :param ext: The extension of the files which are to be handled [without dot (.) before it]
    """

    try:
        if os.path.exists(folder):  # Checking whether the path provided exists or not
            os.chdir(folder)  # Changing the current directory to the path provided
            extension = "." + ext  # Adding dot(.) to the extension
            j = 0  # Variable to be set as name of the files

            names_of_files = os.listdir()  # Storing names of all the files present in the current working directory
            print("This folder contains", len(names_of_files), "files")  # Printing total number of files

            for i in range(len(names_of_files)):  # Running for loop the number of times total files are present in cwd
                f = open(file)  # Opening the file in which exception file's names are written

                if names_of_files[i].lower() not in f.read().lower() and names_of_files[i] != file:
                    # Condition for checking whether a file is exception file or not
                    split = os.path.splitext(names_of_files[i])
                    # Splitting the name and the extension of that file and storing it in list

                    if extension == split[1]:  # comparing the extension of the file with the extension provided
                        os.rename(names_of_files[i], str(j) + extension)  # Renaming the file in chronological order
                        j += 1  # Incrementing the variable

                    if extension != split[1]:
                        os.rename(names_of_files[i], names_of_files[i].capitalize())  # Capitalizing the first letter
                        # of the file

                f.close()  # Closing the file to read it again in next iteration

        else:  # Condition to be executed when the path provided doesn't exists
            print("The Path you have provided does not exists :(")
            exit()  # Exiting the program if the path is invalid

    except Exception as e:
        print(e)  # Printing the error message

    else:
        print("Task Completed Successfully... :)")  # Printing final message


if __name__ == '__main__':
    directory = input("Enter the Path of the Folder in which you want to Organize files\n")
    # Taking input of the path in which files are to be handled

    exception_file = input("Enter the name of the file with extension in which the names of the "
                           "files are written whose name should not be changed\n")
    # Taking name of the file in which names of exception files are written

    file_extension = input("Enter the extension of the files whose names you want to change\n")
    # Input of extension of files who are to be renamed

    process_output()  # Calling a method to show simple progress bar

    arrange(directory, exception_file, file_extension)  # Calling the method which renames the files
    # More details are in the Docstring of the function
