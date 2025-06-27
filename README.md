# Used Vehicles Analysis Report - USA
  
This project is an interactive web application built with Streamlit, which performs an exploratory data analysis (EDA) of used vehicle listings in the United States. The app allows users to explore histograms, scatter plots, and apply filters to the dataset in a practical and intuitive way.
  
## Features:
  
- Filtering by brand, fuel type, and year range  
- Histogram visualization for prices and mileage  
- Generation of scatter plots with selectable variables  
- Display of filtered data table  
- Download of filtered data as a `.csv` file  
  
## Project Structure:  
  
.  
├── README.md  
├── vehicles_us.py # Main Streamlit app code  
├── vehicles_us.csv # Dataset  
├── requirement.txt # Required libraries  
├── notebooks/  
│ └── EDA.ipynb # Exploratory Data Analysis notebook  
└── streamlit/  
└── config.toml # Configuration for Render  
  
## Online Application  
    
Access the application here:    
https://projeto-sprint5-danielamorim.onrender.com  
  
To deploy this project on Render:  
  
1. Push the repository to GitHub  
2. Go to Render and create a new Web Service  
3. Connect your repository to the service  
4. Set the following commands:  
  
- **Build Command**:  
  `pip install --upgrade pip && pip install -r requirement.txt`
  
- **Start Command**:  
  `streamlit run vehicles_us.py`
  
## Requirements Fulfilled  
  
- Text header  
- At least one histogram  
- At least one scatter plot  
- At least one button or checkbox  
- Application accessible via browser  
- Required file structure:  
.  
├── README.md  
├── vehicles_us.py  
├── vehicles_us.csv  
├── requirement.txt  
├── notebooks/  
│ └── EDA.ipynb  
└── streamlit/  
└── config.toml  
  
## Data Source:  
  
The dataset `vehicles_us.csv` contains information about used vehicles for sale in the United States, including price, brand, fuel type, mileage, and year of manufacture.  
  
## Contact  
  
**Daniel Amorim**  
Data Analysis  
Bachelor in Advertising, Marketing and Public Relations  
[LinkedIn Profile](https://www.linkedin.com/in/danieloamorim)










