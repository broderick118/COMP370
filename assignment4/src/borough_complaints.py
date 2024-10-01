import os.path
from argparse import ArgumentParser
import csv

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--filename", help="Name of file", required=True)
    parser.add_argument("-s", "--startdate", help="Start date", required=True)
    parser.add_argument("-e", "--enddate", help="End date", required=True)
    parser.add_argument("-o", "--output", help="Name of output file", required=False)

    args = parser.parse_args()
    filename = args.filename
    startdate = args.startdate
    enddate = args.enddate
    output = args.output



if (__name__ == "__main__"):
    main()