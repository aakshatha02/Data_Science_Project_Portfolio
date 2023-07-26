# Lab-project-B
================
## *Topic* 
### Crime Analysis in Chicago City 

## *Overview*
Security has always been one of the most significant concerns. Government and security agencies are working hard to prevent crimes and protect their people. However, challenge of dealing with large amount of data has become a major issue for all organizations and therefore, a crime information system that is able to process large amount of data in a short period of time is needed. News and records indicate that there have been a large number of crimes in Chicago city. It is called as “murder capital” or “crime capital” of the U.S in 2012. Chicago had more murders in 2012 than any other city in the country. Therefore, there is a requirement to make more informed decisions and analyze crimes occurring in different region of Chicago city. Data was collected from Chicago Data Portal and will be analyzing 3 years of crime data of Chicago from 2021 - 2023. 

## *Goal*
Our project aims to investigate 
- crimes hotspots 
- crime patterns
- Dashboard count of crimes in each neighbourhood

## *Method* 

- *Data Collecting*: crime data sets from Chicago Data Portal 
  
- *Data Preprocessing*: Necessary preprocessing is done to transform raw data into uniform data, removing missing values, normalizing data, removing errors etc. 

- *Exploratory Analysis*: Data visualization (Plotting, relationships between variables)

- *Folium Package and K- means clustering*: This method is used to identify crime hotspots and crime patterns in a particular area, which can be used by the police and criminal investigators. 
 
 - *Streamlit library*: This library is used show the visualization of dashboard of crime count in each neighbour.
  
 Here are Python libraries we will be using for of our project: 

 *Data collection*: pandas, NumPy 
 
 *Data cleaning*: pandas, NumPy, sklearn

 *Exploratory data analysis*: pandas, NumPy, Matplotlib, Seaborn
 
 *Clustering*: sklearn, KMeans
 
 *FOLIUM PACKAGE*:
 Folium is a Python library used for visualizing geospatial data. It is built on top of the leaflet JavaScript library, which is one of the most popular libraries for creating interactive maps on the web. Folium allows users to create maps with various features such as markers, popups, tooltips, polygons, and heatmaps. It also supports different tile sets such as OpenStreetMap, Mapbox (Limited levels of zoom for free tiles), and Stamen etc.

Folium provides an easy-to-use interface for creating interactive maps directly from Python code. It allows users to create maps with codes and customize the maps using various options and parameters. It also provides functionality to save the maps as HTML files that can be shared and viewed in any web browser.

 ## *Data*
 Website : https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2
 
 ## *References*
https://www.researchgate.net/publication/335361962_Crime_Analysis_in_Chicago_City/link/5d77582ca6fdcc9961bcb334/download 

https://vciba.springeropen.com/articles/10.1186/s42492-021-00075-z
