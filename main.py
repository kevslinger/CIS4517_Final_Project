import pandas as pd
import argparse
import glob
import os
import time


# Read a directory for all CSV files, and concatenate them into one DataFrame
# NOTE: Your computer might not be able to handle this!! That's why it's commented out in main.
# If you dataset is very small, consdier commenting out the loop in main function and concatenating.
def read_tweets(data_dir):
    file_list = glob.glob(os.path.join(data_dir, '*.csv'))
    df = pd.concat([pd.read_csv(file_list[i], low_memory=False) for i in range(len(file_list))], ignore_index=True)

    return df

# Remove lines in the dataFrame with the same tweet ID
def remove_duplicates(df):
    df.drop_duplicates(subset='id', keep='first', ignore_index=True, inplace=True)
    return df

# Remove lines in the dataFrame that start with text "RT @" 
def remove_RT(df):
    df['full_text'].fillna('', inplace=True)
    is_RT = df[df['full_text'].str.startswith("RT @")]
    df.drop(is_RT.index, axis=0, inplace=True)
    return df

    
def main(args):
    # If you have a small dataset, consider uncommenting these two lines
    # If you do, you need to change the df.to_csv lines that use path.split.
    #df = read_tweets(args.data_dir)
    #df.to_csv(os.path.join(args.output_dir, 'concatenated_df.csv'), index=False)
    # Since our dataset is not very small, we will iteratively apply the cleaning process
    # To each CSV file.
    for path in glob.glob(os.path.join(args.data_dir, '*.csv')):
        # Read in one csv at a time and then remove duplicate Tweet IDs, then remove Retweets, and
        # save the CSV at each step to record progress.
        df = pd.read_csv(path)
        print("Read in " + path.split('/')[-1])
        df = remove_duplicates(df)
        df.to_csv(os.path.join(args.output_dir, "deduped_" + path.split('/')[-1]), index=False)
        print("Wrote " + path.split('/')[-1])
        df = remove_RT(df)
        df.to_csv(os.path.join(args.output_dir, "removed_RT_" + path.split('/')[-1]), index=False)
        del df

if __name__ == '__main__':
    print('Hello World')
    parser = argparse.ArgumentParser(description='Clean Directory of Tweet CSV files into one CSV which removes duplicates and retweets.')
    parser.add_argument('--data_dir', default='data', type=str, help='The directory containing your CSV files to be processed.')
    parser.add_argument('--output_dir', default='output', type=str, help='The location where you would like your cleaned CSV file to be saved.')
    args = parser.parse_args()

    main(args)
