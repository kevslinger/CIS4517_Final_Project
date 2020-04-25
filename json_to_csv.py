import pandas as pd
import glob
import os



def main():
    base_path = '/Users/kevin/Desktop/New Classes/Cloud Computing/'
    #file_list = glob.glob(os.path.join(base_path, 'Corona Tweet Json/', '*.jsonl'))
    file_list = [os.path.join(base_path, 'Corona Tweet Json/', 'corona_tweets_' + str(x) + '.jsonl') for x in [19, 20, 21, 22, 23, 24, 25, 26, 27]]
    for path in file_list:
        df = pd.read_json(path, lines=True)
        extension = path.split('/')[-1]
        print("Read in file " + extension)
        df.to_csv(os.path.join(base_path, 'FINAL_PROJECT', 'data', extension[:-5] + 'csv'), index=False)
        del df

if __name__ == '__main__':
    main()
