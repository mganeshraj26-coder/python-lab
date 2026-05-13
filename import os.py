import os.path
import sys

# Input filename
fname = input("Enter the filename to sort: ")

# Check if file exists
if not os.path.isfile(fname):
    print("File", fname, "doesn't exist")
    sys.exit(0)

# Open file in read mode
infile = open(fname, "r")

# Read all lines into a list
lines = infile.readlines()

# Close the input file
infile.close()

# Create empty list
lineList = []

# Remove newline characters
for line in lines:
    lineList.append(line.strip())

# Sort the list
lineList.sort()

# Display sorted lines
print("\nSorted Lines:")
for line in lineList:
    print(line)

# Optional: write sorted lines to a new file
outfile = open("sorted_" + fname, "w")

for line in lineList:
    outfile.write(line + "\n")

outfile.close()

print("\nSorted content written to file:", "sorted_" + fname)