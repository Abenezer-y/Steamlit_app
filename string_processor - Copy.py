# import python Moduels, 1 pandas to read the excel file and load data and datetime functionalites 
from distutils.command.config import dump_file
import pandas as pd
from datetime import date, datetime

#Reading excel file, passing the excel file path 
file_path = './data.xlsx'
raw_data = pd.read_excel(open(file_path, 'rb'), sheet_name='Sheet2')


# Listing values from each columun in the dataframe
# Bassically converting the importedd data to python list 

meta = raw_data['meta'].values # Length
titles = raw_data['title'].values # Artist, Title
views = raw_data['view'].values
likes = raw_data['like'].values
posted_date = raw_data['date'].values
channels = raw_data['channel'].values




# Creating an empty dictionary for storing validated data
processed_data = {'Channel': [], 'Artist':[], 'Title':[], 'Duration':[], 'Views':[], 'Likes':[],
                  'Post Date':[], 'Collection Date':[]}

rejected_data = {'Channel': [], 'Artist':[], 'Title':[], 'Duration':[], 'Views':[],
                 'Likes':[], 'Post Date':[], 'Collection Date':[]}


# Validation Functions 
def text_split(text, splitter_str):
    str_pos  = text.find(splitter_str)
    if str_pos != -1:
        splited_texts = text.split(splitter_str)
        return splited_texts
    else:
        return [None]

def duration(meta_text):
    dur_meta = text_split(meta_text, ' ago ')
    dur_list = text_split(dur_meta[1], ' ')
    dur_list[-2:] = []
    duration = ""
    for dur in dur_list:
        duration = duration + ' ' + dur
    return duration

def view(text):
    view_list = text_split(text, ' ')
    if view_list[0]:
        meta_text = view_list[0].replace(',', '')
        view_count = meta_text.replace(" ", '')
        return int(view_count)
    else:
        return 0   

def like(text):
    like_list = text_split(str(text), 'likes')
    if like_list[0]:
        meta_text = like_list[0].replace(',', '')
        like_count = meta_text.replace(" ", '')
        if like_count.isdigit():
            return int(like_count)
        else:
            return 0
    else:
        return 0  

def post_date(text):
    date_list = text_split(str(text), 'Premiered ')
    if date_list[0] is None: 
        return text 
    else:
        return date_list[1]
     
# to generate excel file to save processed data
# processed_data = pd.read_excel(open('./Test_processed.xlsx', 'rb'), sheet_name='data')


text = "Olirra Taarikuu - Etiyophiya - ኦልእራ ታሪኩ - ኢትዮዽያ - New Ethiopian Oromo Music 2022 (Official Video) by Nahom Records Inc 8 days ago 5 minutes, 28 seconds 4,217 views"
# Validation Process
for i in range(len(titles)):
    artist = text_split(titles[i], '-')[0]
    if artist:
        processed_data['Artist'].append(artist)
        processed_data['Duration'].append(duration(meta[i]))
        processed_data['Views'].append(view(views[i]))
        processed_data['Channel'].append(channels[i])
        processed_data['Title'].append(titles[i])
        processed_data['Likes'].append(like(likes[i]))
        processed_data['Post Date'].append(post_date(posted_date[i]))
        processed_data['Collection Date'].append(date(2022, 1, 6))
    else:
        rejected_data['Artist'].append(artist)
        rejected_data['Duration'].append(duration(meta[i]))
        rejected_data['Views'].append(view(views[i]))
        rejected_data['Channel'].append(channels[i])
        rejected_data['Title'].append(titles[i])
        rejected_data['Likes'].append(like(likes[i]))
        rejected_data['Post Date'].append(post_date(posted_date[i]))
        rejected_data['Collection Date'].append(date(2022, 1, 6))

# converting validated data to dataframe
processed_df = pd.DataFrame.from_dict(processed_data)
rejected__df = pd.DataFrame.from_dict(rejected_data)

# Saving Dataframe to Excel
processed_df.to_excel("./Test_processed.xlsx", sheet_name='data')
rejected__df.to_excel("./Test_rejected.xlsx", sheet_name='data')


# # processed_data = pd.read_excel(open('./Test_processed.xlsx', 'rb'), sheet_name='data')
# # processed_data['Post Date']= pd.to_datetime(processed_data['Post Date'])
# # print(processed_data.nunique())
# # df_2012 = processed_data.loc[((processed_data['Post Date']>=datetime(2012, 1, 1)) & (processed_data['Post Date']<=datetime(2012, 12, 31)))]
# # df_2013 = processed_data.loc[((processed_data['Post Date']>=datetime(2013, 1, 1)) & (processed_data['Post Date']<=datetime(2013, 12, 31)))]
# # df_2014 = processed_data.loc[((processed_data['Post Date']>=datetime(2014, 1, 1)) & (processed_data['Post Date']<=datetime(2014, 12, 31)))]
# # df_2015 = processed_data.loc[((processed_data['Post Date']>=datetime(2015, 1, 1)) & (processed_data['Post Date']<=datetime(2015, 12, 31)))]
# # df_2016 = processed_data.loc[((processed_data['Post Date']>=datetime(2016, 1, 1)) & (processed_data['Post Date']<=datetime(2016, 12, 31)))]
# # df_2017 = processed_data.loc[((processed_data['Post Date']>=datetime(2017, 1, 1)) & (processed_data['Post Date']<=datetime(2017, 12, 31)))]
# # df_2018 = processed_data.loc[((processed_data['Post Date']>=datetime(2018, 1, 1)) & (processed_data['Post Date']<=datetime(2018, 12, 31)))]
# # df_2019 = processed_data.loc[((processed_data['Post Date']>=datetime(2019, 1, 1)) & (processed_data['Post Date']<=datetime(2019, 12, 31)))]
# # df_2020 = processed_data.loc[((processed_data['Post Date']>=datetime(2020, 1, 1)) & (processed_data['Post Date']<=datetime(2020, 12, 31)))]
# # df_2021 = processed_data.loc[((processed_data['Post Date']>=datetime(2021, 1, 1)) & (processed_data['Post Date']<=datetime(2021, 12, 31)))]
# # df_2022 = processed_data.loc[((processed_data['Post Date']>=datetime(2022, 1, 1)) & (processed_data['Post Date']<=datetime(2022, 12, 31)))]

# # yearly_data = [df_2012, df_2013, df_2014, df_2015, df_2016, df_2017, df_2018, df_2019, df_2020, df_2021, df_2022]

# # def unique_value(df):
# #      artist_list = df.Artist.unique()
# #     #  artist_no = df.Artist.nunique()
# #      artists = pd.DataFrame({'Artists': artist_list})
# #      return artists

# # artist_count = []
# # for df in yearly_data:
# #     df_values = len(unique_value(df).values)
# #     df_vals = len(df.values)
# #     artist_count.append(df_values)
# #     artist_count.append(df_vals)

# # print(artist_count)


# # view_counts = {"Post Date": ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022'], 
# #                "Views": [df_2012['Views'].sum(), df_2013['Views'].sum(), df_2014['Views'].sum(), df_2015['Views'].sum(), df_2016['Views'].sum(), 
# #                          df_2017['Views'].sum(), df_2018['Views'].sum(), df_2019['Views'].sum(), df_2020['Views'].sum(), df_2021['Views'].sum(),
# #                          df_2022['Views'].sum(),]}
                       
# # print(unique_value(df_2017))