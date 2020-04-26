import pandas as pd
import argparse
import glob
import os
import time

# Do we want to remove all RTs?
# Definitely want to filter by Tweet ID -- keep a set of unique Tweet IDs
# Probably just append all the CSVs together since they have the same attributes.
# do NOT drop any attributes
# Does Dragut just want us to keep it in JSON? No, can be CSV
# Is storing in a dataframe the most efficient option?

# STEPS FOR THIS PROJECT
# STEP 1: Define the steps you will take to clean
#   e.g. Step 1.) Remove all duplicate keys from your data.
#        Step 2.) Remove RTs (potentially tweets that specifically start with the text "RT")
#        Step 3.) Remove RTs (potentially using the retweet attributes? Not sure if those will help or not.)
# STEP 2: SAVE your dataset at each step of the process
#   e.g. "Here is my raw dataset <link>
#        "After removing duplicate tweet_ids, my dataset became <link>
#        "Then, I removed retweets by removing tweets that started with RT. Here is my new dataset <link>"
# DO NOT DELETE OR REMOVE ANY DATA/ATTRIBUTES
# STEP 3: Write a report (sample given in step 2), documenting each step you took to clean the data.

# Read a directory for all CSV files, and concatenate them into one DataFrame
# NOTE: Your computer might not be able to handle this!! That's why it's commented out in main.
# If you dataset is very small, consdier commenting out the loop in main function and concatenating.
def read_tweets(data_dir):
    file_list = glob.glob(os.path.join(data_dir, '*.csv'))
    df = pd.concat([pd.read_csv(file_list[i], low_memory=False) for i in range(len(file_list))], ignore_index=True)

    return df

def remove_duplicates(df):
    df.drop_duplicates(subset='id', keep='first', ignore_index=True, inplace=True)
    return df

def remove_RT(df):
    is_RT = df[df['full_text'].str.startswith("RT ")]
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
