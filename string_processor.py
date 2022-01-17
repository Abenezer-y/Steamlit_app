# import 
import pandas as pd
from datetime import date

#Reading scrapped raw data
raw_data = pd.read_excel(open('./data.xlsx', 'rb'), sheet_name='Sheet1')

# Listing values from each columun 
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


# def spliter(raw_data, split_text):

    
#     artists = []
#     titles = []
#     posted = []
#     duration = []
#     views = []

#     index_counter = 0
#     rejected_rows  = {''[]}

#     for pt_title in title_list[:15]:
#         dash_pos  = pt_title.find('-')
#         pt_title_list = pt_title.split('-')
#         split_count = len(pt_title_list)

#         title = pt_title

#         if (dash_pos > 3 and split_count == 2):
#             artist = pt_title_list[0]

#     for pt_title in title_list[:15]:
#         dash_pos  = pt_title.find('-')
#         pt_title_list = pt_title.split('-')
#         split_count = len(pt_title_list)            
#         if split_count == 2:
#             meta_text = meta_text_list[1]
#             meta_text_list = meta_text.split('ago')
#             posted_on = meta_text_list[0] + 'ago'

#             meta_text = meta_text_list[1]

#             if len(meta_text.split('seconds')) == 2:
#                 meta_text_list = meta_text.split('seconds')
#                 length = meta_text_list[0] + 'seconds'
#             elif len(meta_text.split('second')) == 2:
#                 meta_text_list = meta_text.split('second')
#                 length = meta_text_list[0] + 'second'
#             elif  len(meta_text.split('minutes')) == 2:
#                 meta_text_list = meta_text.split('minutes')
#                 length = meta_text_list[0] + 'minutes'
#             else:
#                 rejected_rows.append(index_counter)
#             meta_text_list = meta_text_list[1].split('views')
#             meta_text = meta_text_list[0].replace(',', '')
#             view_count = meta_text.replace(" ", '')
#             view_count = int(view_count)

#                 artists.append(artist)
#                 titles.append(title)
#                 posted.append(posted_on)
#                 duration.append(length)
#                 views.append(view_count)

#         else:
#             rejected_rows.append(video_index[index_counter])

#         index_counter = index_counter + 1

#     rejected_data = raw_data.iloc[rejected_rows]
#     data = {"Artist": artists, "Title": titles, "Posted_as_of_Nov_03": posted, "Length": duration, "Views_as_of_Nov_03": views}
#     processed_data = pd.DataFrame.from_dict(data)
#     return processed_data, rejected_data

# # data = spliter(raw_data=raw_data, split_text='Hope Music Ethiopia')

# # data[0].to_excel("./processed_Data/Test_processed.xlsx", sheet_name='Hope_Entertainment Detail')  
# # data[1].to_excel("./processed_Data/Test_rejected.xlsx", sheet_name='Hope_Entertainment Detail')  



# titles = data['Title'].values

# for title in titles[:15]:
#     dash_pos  = title.find('-')
#     title_texts = title.split(' - ')
#     if dash_pos > 3:
#         if title_texts[0] == "Ethiopia":
#             artist = title_texts[1]
#             music_title = title_texts[1]
#         else:
#             artist = title_texts[0]
#             music_title = title_texts[1]
#         dic = {'artist':artist, 'title':music_title}
#         print(dic)
