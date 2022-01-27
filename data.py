import pandas as pd

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
# df_2013.style
# df_2013.style.format("{:,.0f}")
# df_2013.style.hide_index()
view_counts = {"Post Date": ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], 
               "Views": [df_2012['Views'].sum(), df_2013['Views'].sum(), df_2014['Views'].sum(), df_2015['Views'].sum(), df_2016['Views'].sum(), 
                         df_2017['Views'].sum(), df_2018['Views'].sum(), df_2019['Views'].sum(), df_2020['Views'].sum(), df_2021['Views'].sum(),
                         df_2022['Views'].sum(),]}

all_df = pd.DataFrame(view_counts)
# "All": all_df, 
columuns = ["Post Date", 'Channel', 'Artist', 'Title', 'Duration', 'Views', 'Likes']
# Dictionary of dataframes to be served 
data_dic = {"2012": df_2012[columuns], "2013": df_2013[columuns], "2014": df_2014[columuns], 
            "2015": df_2015[columuns], "2016": df_2016[columuns], "2017": df_2017[columuns],
            "2018": df_2018[columuns], "2019": df_2019[columuns], "2020": df_2020[columuns],  
            "2021": df_2021[columuns], "2022": df_2022[columuns],}