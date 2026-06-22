from urlextract import URLExtract

extract = URLExtract()

def fetch_stats(selected_user, df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    # Number of messages
    num_messages = df.shape[0]

    # Number of words
    words = []
    for message in df['message']:
        words.extend(message.split())

    # Media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Links
    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)


def most_busy_users(df):
    x = df['user'].value_counts().head()

    percent_df = (
        round((df['user'].value_counts() / df.shape[0]) * 100, 2)
        .reset_index()
    )

    return x, percent_df