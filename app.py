import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, datetime
import plotly.express as px

# Functions 

def unique_value(df):
     artist_list = df.Artist.unique()
     artists = pd.DataFrame({'Artists': artist_list})
     return artists




# UI Data
raw_data = pd.read_excel(open('./data.xlsx', 'rb'), sheet_name='Sheet1')


processed_data = pd.read_excel(open('./Test_processed.xlsx', 'rb'), sheet_name='data')
processed_data['Post Date']= pd.to_datetime(processed_data['Post Date'])

df_2012 = processed_data.loc[((processed_data['Post Date']>=datetime(2012, 1, 1)) & (processed_data['Post Date']<=datetime(2012, 12, 31)))]
df_2013 = processed_data.loc[((processed_data['Post Date']>=datetime(2013, 1, 1)) & (processed_data['Post Date']<=datetime(2013, 12, 31)))]
df_2014 = processed_data.loc[((processed_data['Post Date']>=datetime(2014, 1, 1)) & (processed_data['Post Date']<=datetime(2014, 12, 31)))]
df_2015 = processed_data.loc[((processed_data['Post Date']>=datetime(2015, 1, 1)) & (processed_data['Post Date']<=datetime(2015, 12, 31)))]
df_2016 = processed_data.loc[((processed_data['Post Date']>=datetime(2016, 1, 1)) & (processed_data['Post Date']<=datetime(2016, 12, 31)))]
df_2017 = processed_data.loc[((processed_data['Post Date']>=datetime(2017, 1, 1)) & (processed_data['Post Date']<=datetime(2017, 12, 31)))]
df_2018 = processed_data.loc[((processed_data['Post Date']>=datetime(2018, 1, 1)) & (processed_data['Post Date']<=datetime(2018, 12, 31)))]
df_2019 = processed_data.loc[((processed_data['Post Date']>=datetime(2019, 1, 1)) & (processed_data['Post Date']<=datetime(2019, 12, 31)))]
df_2020 = processed_data.loc[((processed_data['Post Date']>=datetime(2020, 1, 1)) & (processed_data['Post Date']<=datetime(2020, 12, 31)))]
df_2021 = processed_data.loc[((processed_data['Post Date']>=datetime(2021, 1, 1)) & (processed_data['Post Date']<=datetime(2021, 12, 31)))]
df_2022 = processed_data.loc[((processed_data['Post Date']>=datetime(2022, 1, 1)) & (processed_data['Post Date']<=datetime(2022, 12, 31)))]


view_counts = {"Post Date": ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], 
               "Views": [df_2012['Views'].sum(), df_2013['Views'].sum(), df_2014['Views'].sum(), df_2015['Views'].sum(), df_2016['Views'].sum(), 
                         df_2017['Views'].sum(), df_2018['Views'].sum(), df_2019['Views'].sum(), df_2020['Views'].sum(), df_2021['Views'].sum(),
                         df_2022['Views'].sum(),]}

all_df = pd.DataFrame(view_counts)
# "All": all_df, 

# Dictionary of dataframes to be served 
data_dic = {"2012": df_2012, "2013": df_2013, "2014": df_2014, "2015": df_2015, "2016": df_2016, "2017": df_2017,
            "2018": df_2018, "2019": df_2019, "2020": df_2020,  "2021": df_2021, "2022": df_2022,}



chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])

# Ploty figers to be served
fig = px.bar(x=["a", "b", "c"], y=[1, 3, 2])
# fig.write_html('first_figure.html', auto_open=True)




## UI 

c1 = st.container()
c1.title('Ethiopian Music ON YouTube')
c1.dataframe(processed_data)

c1.header("Artists hosted per year")
year = c1.selectbox('Which Years data do you want to review',
                     ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'), key='artist')
search_data = data_dic[year]
c1.dataframe(unique_value(search_data))

container = st.container()
container.header("Period vs the number of views per channel")
option = container.selectbox('Which Years data do you want to review',
                     ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'), key='channel')
col3, col4 = container.columns(2)


posted_date = data_dic[option] 
# posted_date = posted_date.rename(columns={'Post Date':'index'}).set_index('index')
with col3:
     # container.line_chart(posted_date)
     per = px.line(posted_date, x="Post Date", y="Views", color="Channel")
     container.plotly_chart(per, use_container_width=True)
     
with col4:
     with container.expander("See Data"):
          st.dataframe(data_dic[option])

col5, col6 = st.columns(2)

with col5:
     st.header("Period vs the number of new artists being hosted on the channel")
     st.plotly_chart(fig, use_container_width=True)

with col6:
     st.header("Data Period and New Artists")
     st.dataframe(processed_data)


col5, col6 = st.columns(2)

with col5:
     st.header("Period vs user interaction (likes and comments)")
     st.line_chart(chart_data)

with col6:
     st.header("Data Period and Interaction")
     st.dataframe(processed_data)