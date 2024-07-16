
import os
from kaggle.api.kaggle_api_extended import KaggleApi

os.environ['KAGGLE_USERNAME'] = ''
os.environ['KAGGLE_KEY'] = ''

api = KaggleApi()
api.authenticate()

competition_name = 'rossmann-store-sales'

download_path = ''

if not os.path.exists(download_path):
    os.makedirs(download_path)

file_to_download  = ['store.csv', 'train.csv', 'test.csv']

for file_name in file_to_download:
    try:
        api.competition_download_file(competition_name, file_name, path=download_path)
        print(f"File store.csv from competition {competition_name} downloaded to {download_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
