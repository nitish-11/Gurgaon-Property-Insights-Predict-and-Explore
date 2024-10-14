# Gurgaon Property Insights: Predict and Explore

## Introduction
This project leverages web scraping and machine learning techniques to predict property prices in Gurgaon, providing valuable insights for buyers and sellers in the real estate market.

## Key Features
- **Data Scraping:** Collected 3,900 records from MagicBricks using Selenium and Beautiful Soup.
- **Data Analysis:** Conducted univariate and multivariate analysis, including outlier detection and missing value imputation.
- **Model Performance:** Achieved R² = 0.9025 and MAE = 0.4582 with Random Forest.
- **Interactive App:** Developed a Streamlit app hosted on AWS, featuring property rate visualization and a recommendation engine. 
  - **[Access the Interactive App Here](link_to_your_streamlit_app)**

## Functionalities



## Technologies Used
- Python, Pandas, NumPy, Selenium, Beautiful Soup, Streamlit, Plotly, AWS

## Installation and Usage
To run the application locally, clone the repository and install the required packages:
```bash
git clone <repository-url>
cd <project-directory>
pip install -r requirements.txt
streamlit run app.py
