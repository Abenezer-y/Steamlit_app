artist_id = 2
artists = [{'id': 1, 'name': 'Name_1'}, {'id': 2, 'name': 'Name_21'}]

result = [artist for artist in artists if artist["id"] == artist_id]

if result:
    print(result[0])
    
