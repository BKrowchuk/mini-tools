# user_request = youtube.channels().list(
#     part='contentDetails, statistics',
#     # forUsername='BlenderGuruOfficial'
#     id='UCOKHwx1VCdgnxwbjyb9Iu1g'
#     # id='UC4XGsrwK74aTPsG3itbljGg'
# )
# user_response = user_request.execute()
# print(user_response)


# play_request = youtube.playlists().list(
#     part='contentDetails, snippet',
#     channelId='UCOKHwx1VCdgnxwbjyb9Iu1g'
# )
# play_response = play_request.execute()
# printItems(play_response)