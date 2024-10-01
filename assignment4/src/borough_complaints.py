import os.path
from argparse import ArgumentParser
import pandas as pd # type: ignore

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


def process_csv (filename, startdate, enddate, output):
    filepath = os.path.dirname(__file__)[:-3] + "data/" + filename
    dataframe = pd.read_csv(filepath)

if (__name__ == "__main__"):
    main()