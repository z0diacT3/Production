from pathlib import Path
from subprocess import call
import csv

x = ""
temp_path = Path("c:\\Temp")

if not temp_path.exists():
    temp_path.mkdir()
    print("""
    #################################################################################
    # C:\\Temp created! myrobocopy.txt should be placed in c:\\temp before continuing #
    #################################################################################
    """)


def get_x_days():
    if choice == "o":
        xi = input("MAXimum file AGE - exclude files older than x days/date(YYYYMMDD): x = ")
        return xi
    else:
        xi = input("MINimum file AGE - exclude files newer than x days/date(YYYYMMDD): x = ")
        return xi


def get_retry():
    rr = input("Enter the Robocopy retry times:  ")
    return rr


def process_robocopy_a(def_rr):
    try:
        file = open("C:\\temp\\myrobocopy.txt")
        for line in file:
            if line == "\n":
                quit()
            else:
                path = line.split(",")
                source = path[0]
                destination = path[1].split("\n")
                print(f" Copying files from Source: \"{source}\" to Destination: \"{destination[0]}\"")
                call(f"robocopy \"{source}\" \"{destination[0]}\" /E /Z /R:{def_rr} /TEE /LOG+:c:\\temp\\myrobocopyLOG.txt")
        file.close()
    except IOError:
        print("*** C:\\temp\\myrobocopy.txt NOT FOUND! ***")
    except IndexError:
        print("End of file reached or not a valid entry in c:\\temp\myrobocopy.txt")


def process_robocopy_o(days, def_rr):
    try:
        file = open("C:\\temp\\myrobocopy.txt")
        for line in file:
            if line == "\n":
                quit()
            else:
                path = line.split(",")
                source = path[0]
                destination = path[1].split("\n")
                print(f" Copying files from Source: \"{source}\" to Destination: \"{destination[0]}\"")
                call(f"robocopy \"{source}\" \"{destination[0]}\" /MAXAGE:{days} /E /Z /R:{def_rr} /TEE /LOG+:c:\\temp\\myrobocopyLOG.txt")
        file.close()
    except IOError:
        print("*** C:\\temp\\myrobocopy.txt NOT FOUND! ***")
    except IndexError:
        print("End of file reached or not a valid entry in c:\\temp\myrobocopy.txt")


def process_robocopy_n(days, def_rr):
    try:
        file = open("C:\\temp\\myrobocopy.txt")
        for line in file:
            if line == "\n":
                quit()
            else:
                path = line.split(",")
                source = path[0]
                destination = path[1].split("\n")
                print(f" Copying files from Source: \"{source}\" to Destination: \"{destination[0]}\"")
                call(f"robocopy \"{source}\" \"{destination[0]}\" /MINAGE:{days} /E /Z /R:{def_rr} /TEE /LOG+:c:\\temp\\myrobocopyLOG.txt")
        file.close()
    except IOError:
        print("*** C:\\temp\\myrobocopy.txt NOT FOUND! ***")
    except IndexError:
        print("End of file reached or not a valid entry in c:\\temp\myrobocopy.txt")


choice = input("Copy [A]ll files; Exclude files [O]lder than; or Exclude files [N]ewer than x days:\nA, O or N: ").lower()

if choice == "a":
    rr = get_retry()
    process_robocopy_a(rr)
elif choice == "o":
    rr = get_retry()
    x = get_x_days()
    print(f"Copying ALL files EXCLUDING files older than {x[0:4]}-{x[4:6]}-{x[6:]} days")
    process_robocopy_o(x, rr)
elif choice == "n":
    rr = get_retry()
    x = get_x_days()
    print(f"Copying ALL files EXCLUDING files newer than {x[0:4]}-{x[4:6]}-{x[6:]} days")
    process_robocopy_n(x, rr)
else:
    print("Not a valid option")