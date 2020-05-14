# make a software that reads the unique words from a file. File name will be inputted by the user with location. The
# Program will generate a output file in a different folder and the output file name include input file name without
# the location information.
#
#     program sudo logic
#     read words
#     save each word
#     write in new file

import os

word1 = []

# taking the file name with dir location from the user
inputFileName = input("File Name with Directory: ")

# creating the output file name with directory
outputFileName = f"GeneratedFiles/uniqueWords{os.path.basename(inputFileName).capitalize()}"

with open(f"{inputFileName}", "r") as sampleFile:
    for line in sampleFile:
        for word in line.split():
            if word in word1:
                continue
            else:
                word1 += [word]

with open(f"{outputFileName}", "w") as uniqueWords:
    for word in word1:
        uniqueWords.write(word.capitalize().strip(".,"))
        uniqueWords.write("\n")
