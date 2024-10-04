import pandas as pd
import os.path
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="name of file", required=True)
    parser.add_argument("-o", "--output", help="output file name")
    parser.add_argument("-p", "--print", help="print head of output y/n", action="store_true")
    
    args = parser.parse_args()
    filename = args.input
    print = args.print
    output = args.output
    do_operations(filename, print, output)

def do_operations(filename, output, print):
    dirname = os.path.dirname(__name__)[:-3] + "data/"
    df = pd.read_csv(dirname + filename, usecols=[5,6], names=["complaint_type", "descriptor"])

    if print:
        print(df.head())
    elif output != None:
        df.to_csv(dirname + output)
    else :
        df.to_csv(dirname + "csv_filtered.csv")

if __name__ == "main":
    main()