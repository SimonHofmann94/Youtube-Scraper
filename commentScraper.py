import csv
from googleapiclient.discovery import build

# Set up YouTube Data API
api_key = 'Your-API-KEY'
youtube = build('youtube', 'v3', developerKey=api_key)

# Get trending videos
response = youtube.videos().list(
    part='snippet',
    chart='mostPopular',
    regionCode='US',  # You can change the region as needed
).execute()

videos = response['items']

# Create CSV file to store comments
csv_filename = 'youtube_comments.csv'
csv_file = open(csv_filename, 'w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Video ID', 'Comment'])

# Fetch comments for the first two pages for each video
for video in videos:
    video_id = video['id']
    video_title = video['snippet']['title']

    # Fetch top-level comments
    top_level_comments_response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        textFormat='plainText',
        maxResults=100,
    ).execute()

    while 'items' in top_level_comments_response:
        comments = top_level_comments_response['items']
        for comment in comments:
            comment_text = comment['snippet']['topLevelComment']['snippet']['textDisplay']
            csv_writer.writerow([video_id, comment_text])

        # Check for pagination
        if 'nextPageToken' in top_level_comments_response:
            next_page_token = top_level_comments_response['nextPageToken']
            top_level_comments_response = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                maxResults=100,
                pageToken=next_page_token,
            ).execute()
        else:
            break

# Close CSV file
csv_file.close()

print(f'Comments from the first two pages scraped and stored in {csv_filename}')
