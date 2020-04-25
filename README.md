* Tweet Cleaner

Kevin Esslinger's final project for CIS 4517 at Temple University: Data-Intensive and Cloud Computing. 

Given a dataset of tweets in either JSONL or CSV format, you can use this repo to "clean" the tweets, which will remove duplicates and retweets.

If your dataset is in JSONL format (i.e. a bunch of JSON files which are stored as one JSON object per line), use the `json_to_csv.py` script first. Run the command:

`python3 json_to_csv.py --data_dir <your_JSONL_directory> --output_dir <output_directory>`

The default output directory is `data/`.

This will convert each JSONL file into CSV, then you can run the `main` script with command:

`python3 main.py --data_dir <your_CSV_directory> --output_dir <output_directory>`

Notice that data_dir from `main.py` should match output_dir from `json_to_csv.py`. The default data_dir for `main.py` is `data/`, which is the default output_dir for `json_to_csv.py`. The default output_dir for main.py is `output/`.
