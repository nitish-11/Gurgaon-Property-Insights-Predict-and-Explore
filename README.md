# Gurgaon Property Insights: Predict and Explore

## Introduction
This project leverages web scraping and machine learning techniques to predict property prices in Gurgaon, providing valuable insights for buyers and sellers in the real estate market.

## Key Features
- **Data Scraping:** Collected 3,900 records from MagicBricks using Selenium and Beautiful Soup.
- **Data Analysis:** Conducted univariate and multivariate analysis, including outlier detection and missing value imputation and applied feature selection method.
- **Model Performance:** Achieved R² = 0.896 and MAE = 0.045 with Random Forest.
-  **Recommendation System**: Implemented a cosine similarity-based recommendation engine that suggests properties based on price details, nearest locations, and top facilities.
- **Interactive App:** Developed a Streamlit app hosted on AWS, featuring property rate visualization and a recommendation engine. 
  - **[Access the Interactive App Here](link_to_your_streamlit_app)**

## Functionalities

**Data Analysis:**
- Price per sqft analysis done via Interactive Map  
  <img src="images/geomap.png" alt="Price per Sqft Interactive Map" width="500" />
- Pie chart analysis of the bedroom share per sector  
  <img src="images/bhk_pie_chart.png" alt="Pie chart Analysis of the Bedroom share per sector" width="300" />

**Recommendation System:**
- Utilizes cosine similarity to provide tailored suggestions based on weighted criteria specified by the user.  
  <img src="images/recommend.png" alt="Recommendation Engine" width="300" />

**Proximity-Based Searching:**
- Recommends nearby societies based on user-defined proximity distance.  
  <img src="images/location_and_radius.png" alt="Proximity Engine" width="300" />

  
## Technologies Used
- Python, Pandas, NumPy, Selenium, Beautiful Soup, Streamlit, Plotly, AWS

## Installation and Usage
To run the application locally, clone the repository and install the required packages:
```bash
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
streamlit run app.py
