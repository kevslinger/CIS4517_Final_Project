import pandas as pd
import argparse
import glob
import os

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

def read_tweets(data_dir):
    file_list = glob.glob(os.path.join(data_dir, '*.csv'))
    df = pd.concat([pd.read_csv(file_list[i], low_memory=False) for i in range(len(file_list))], ignore_index=True)

    return df

def remove_duplicates(df, output_path):
    df.drop_duplicates(subset='id', keep=False, inplace=True)
    return df

def main(args):
    #df = read_tweets(args.data_dir)
    #df.to_csv('/Users/kevin/Desktop/test_concat_df.csv', index=False)
    df = pd.read_csv('output/combined_df.csv', low_memory=False)
    df = remove_duplicates(df, args.output_dir)
    df.to_csv('output/duplicates_dropped.csv', index=False)


if __name__ == '__main__':
    print('Hello World')
    parser = argparse.ArgumentParser(description='Clean Directory of Tweet CSV files into one CSV which removes duplicates and retweets.')
    parser.add_argument('--data_dir', default='data', type=str, help='The directory containing your CSV files to be processed.')
    parser.add_argument('--output_dir', default='output', type=str, help='The location where you would like your cleaned CSV file to be saved.')
    args = parser.parse_args()

    main(args)
