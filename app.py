import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, datetime
import plotly.express as px

# Functions 

def unique_value(df):
     artist_list = df.Artist.unique()
     view_count = []
     counts = []
     for artist in artist_list:
          filtered_df = df.loc[(df['Artist']==artist)]
          count = len(filtered_df['Artist'].values)
          _count = filtered_df["Views"].sum()
          view_count.append(_count)
          counts.append(count)
     artists = pd.DataFrame({'Artists': artist_list, "Views": view_count, "Freq.": counts})
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
c1.title('Ethiopian Music on Youtube')
c1.subheader("""
In this section, 
Ethiopian musics hosted by different channels, mostly 
proffessional recording lables and online streaming channels, are used to build artists information, 
mainly artist's name, total views(on YouTube) and their debut data will be collected. From this we will 
build artists full information from other platforms""")

col1, col2 = c1.columns(2)
with col1:
     c2 = st.container()
     c2.header("Artists hosted per year")
     year = c2.selectbox('Which Years data do you want to review',
                         ('2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'), key='artist')
     c2.subheader("For Year: {1}, Total Count of Posts: {0} Unique Artist Count {2}".format(len(data_dic[year].values), year, len(unique_value(data_dic[year])['Artists'].values)))
     c2.dataframe(unique_value(data_dic[year]))
with col2:
     
     channels_fig = px.pie(data_dic[year], values='Views', names='Channel', title='Total Number of posts catagorized by the channel that hosted the Videos')
     st.plotly_chart(channels_fig, use_container_width=False)

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