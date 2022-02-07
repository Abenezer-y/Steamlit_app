# import python Moduels, 1 pandas to read the excel file and load data and datetime functionalites 
import pandas as pd
from datetime import date, datetime

#Reading excel file, passing the excel file path 
file_path = './data.xlsx'
raw_data = pd.read_excel(open(file_path, 'rb'), sheet_name='Sheet1')


# Listing values from each columun in the dataframe
# Bassically converting the importedd data to python list 

meta = raw_data['Meta'].values # Length
titles = raw_data['Title'].values # Artist, Title
views = raw_data['Views_as_of_Jan 6,2022'].values
likes = raw_data['Likes'].values
posted_date = raw_data['Posted Date'].values
channels = raw_data['Channel'].values




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
    if type(text) == str:
        date_list = text_split(str(text), 'Premiered ')
        return date_list[1]
    else:
        return text
     
# to generate excel file to save processed data
processed_data = pd.read_excel(open('./Test_processed.xlsx', 'rb'), sheet_name='data')
