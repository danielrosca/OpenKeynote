import os.path
import sys
from UI import UserInterface
from FileHandling import FileHandler
from DatabaseHandling import DatabaseHandler
from pathlib import Path
# TODO Path away from string.
# OpenKeynote
# Copyright Mathias Sønderskov Nielsen 2019


def main():
    if len(sys.argv) > 1:
        path = sys.argv[-1]
    else:
        path = Path("MYKEYNOTEFILE.TXT")  # My default testing file. if exists.
    filehandler = FileHandler()
    databasehandler = DatabaseHandler()
    if os.path.isfile(path):
        mainui = UserInterface(filehandler=filehandler, databasehandler=databasehandler, path=path)
    else:
        mainui = UserInterface(filehandler=filehandler, databasehandler=databasehandler)


if __name__ == '__main__':
    main()
