import pandas as pd
import glob
import os
import argparse


def main(args):
    file_list = glob.glob(os.path.join(args.data_dir, '*.jsonl'))
    for path in file_list:
        # Read in one json file. lines=True is used because each line is its own json object.
        df = pd.read_json(path, lines=True)
        # Extract the filename.
        extension = path.split('/')[-1]
        # Progress Tracker
        print("Read in file " + extension)
        # Save DataFrame as a CSV file.
        df.to_csv(os.path.join(args.output_dir,  extension[:-5] + 'csv'), index=False)
        # Delete the object to save space.
        del df

if __name__ == '__main__':
    parser = argeparse.ArgumentParser(description='Converts a dataset of json files to a dataset of CSV files. Expects the input to be of type JSONL (not JSON) and will convert that directory to csv files.')
    parser.add_argument('--data_dir', type=str, help='The directory containing your JSONL files to be processed. The jsonl files are expected to be line-by-line json objects, not one json object per file.')
    parser.add_argument('--output_dir', default='data', type=str, help='The location where you would like your converted CSV files to be saved.')
    args = parser.parse_args()
    
    main(args)
