import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data = pd.read_csv('fossil-fuel-primary-energy.csv')  # Replace 'your_dataset.csv' with the actual filename

# Streamlit app
st.title('Interactive Fossil Fuel Map')

# Sidebar filters
entity_filter = st.sidebar.multiselect('Select Entity(s)', data['Entity'].unique())
year_filter = st.sidebar.slider('Select Year(s)', min_value=data['Year'].min(), max_value=data['Year'].max(),
                               value=(data['Year'].min(), data['Year'].max()), step=1)

# Filter the data
filtered_data = data[(data['Entity'].isin(entity_filter)) & (data['Year'] >= year_filter[0]) & (data['Year'] <= year_filter[1])]

# Create an interactive world map using Plotly Express
fig = px.choropleth(filtered_data,
                    locations='Entity',
                    locationmode='country names',
                    color='Fossil fuels (TWh)',
                    animation_frame='Year',
                    color_continuous_scale='Viridis',
                    title='Fossil Fuel Consumption by Entity Over Time',
                    labels={'Fossil Fuel': 'Fossil Fuel Consumption'},
                    projection='natural earth',  # Choose a projection suitable for global view
                    )

# Show the map
st.plotly_chart(fig)