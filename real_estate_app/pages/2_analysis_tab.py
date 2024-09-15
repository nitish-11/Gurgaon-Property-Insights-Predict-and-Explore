import streamlit as st
import pickle
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title= 'Analysis Tab')

st.title('Analytics')

new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

group_df = new_df.groupby('sector').mean(numeric_only=True)[['price','price_per_sqft','built_up_area','latitude','longitude']]

st.header('Sector Price per Sqft Geomap')
fig1 = px.scatter_mapbox(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                  color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                  mapbox_style="open-street-map",width=1200,height=500,hover_name=group_df.index)

st.plotly_chart(fig1,use_container_width=True)


st.header('Features Wordcloud')

wordcloud = WordCloud(width = 800, height = 500,
                      background_color ='black',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize=(8, 8))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
plt.tight_layout(pad=0)
# Display the figure in Streamlit
st.pyplot(fig)



st.header('Area Vs Price')

property_type = st.selectbox('Select Property Type', ['overall','flat', 'house'])


if property_type == 'house':
    fig2 = px.scatter(new_df[new_df['property_type'] == 'house'],  x='built_up_area', y='price', color='bedRoom')

    st.plotly_chart(fig2, use_container_width=True)

if property_type == 'overall':
    fig3 = px.scatter(new_df,  x='built_up_area', y='price', color='bedRoom')

    st.plotly_chart(fig3, use_container_width=True)

if property_type == 'flat':
    fig4 = px.scatter(new_df[new_df['property_type'] == 'flat'],  x='built_up_area', y='price', color='bedRoom')

    st.plotly_chart(fig4, use_container_width=True)




st.header('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':

  fig_sec1 = px.pie(new_df, names='bedRoom')

  st.plotly_chart(fig_sec1, use_container_width=True)


else:

    fig_sec2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')

    st.plotly_chart(fig_sec2, use_container_width=True)



st.header('Side by Side BHK price comparsion')

fig_bhk = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig_bhk, use_container_width=True)



st.header('Side by Side Distplot for property type')

fig3 = plt.figure(figsize=(10, 4))
sns.distplot(new_df[new_df['property_type'] == 'house']['price'],label='house')
sns.distplot(new_df[new_df['property_type'] == 'flat']['price'], label='flat')
plt.legend()
st.pyplot(fig3)