import pandas as pd # type: ignore
import os.path
from argparse import ArgumentParser

def main():
    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="name of file", required=True)
    
    args = parser.parse_args()
    filename = args.input
    df = count_unique(filename)
    print (df)

def count_unique(filename):
    filepath = os.path.dirname(__file__)[:-3] + "data/" + filename
    df = pd.read_csv(filepath, names=["complaint_type", "descriptor"])
    return df.groupby("descriptor")["complaint_type"].nunique()
    #print (df)
'''
    df = pd.
    with open (filepath, 'r') as data:
        chunks = pd.read_csv(data, names=["complaint_type", "descriptor"], iterator=True, chunksize=1000)
        for chunk in chunks:
            chunk = chunk.groupby('descriptor')['complaint_type'].nunique()
            pd.concat(df,chunk)
'''
if __name__ == '__main__':
    main()