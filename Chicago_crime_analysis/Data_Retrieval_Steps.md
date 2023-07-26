## Data Retrieval step for Chicago Crime Data Set and Chicago Boundaries - Neighborhoods

============================================================================================

### Data Retrieval step for Chicago Crime Data Set

#### Step 1:

Open the below link.

https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2

#### Step 2:

Click on "View Data" and select "Filter".
Filter the dataset based on "Date" and select the operation "is after"  01/01/2021.(Which means it will provide the dataset from Jan 01 2021 till present)

#### Step 3:

Select "Export" and tap on either CSV or CSV for Excel.

#### Step 4:
Required dataset is now exported and rename it to "Crimes_-_2001_to_Present_4.csv".

#### Step 5:

Create a folder "Data" under your cloned repository or "Data" under the project folder and upload the downloaded dataset there.

#### Step 6:

Now it is ready to be read by the python code.

### Data Retrieval step for Chicago Boundaries - Neighborhoods

#### Step 1:

Open the below link.

https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Neighborhoods/bbvz-uum9

#### Step 2:

Select "Export" and tap on GeoJSON.

#### Step 3:

Save it under the folder "Data" which was created in the Step 2 of Data Retrieval step for Chicago Crime Data Set.

#### Step 4:

This data is now ready to be used by streamlit_app.py


