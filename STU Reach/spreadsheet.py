import pandas as pd



sheet_id='1jeCvpLOfHAD95QHsegAYCWrGVpjWXNs_cXn7TifZJaQ'

df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")

print(df)


for index, row in df.iterrows():
    email = row['Email']
    interest = row['Interest']
    topic = row['Topic']
    print(email,interest,topic)

    if interest == 'Teach':
        # Iterate through the data again to find 'Learn' matches with matching topics
        for index,row1 in df.iterrows():
            other_email = row1['Email']
            other_interest = row1['Interest']
            other_topic = row1['Topic']
            print(other_email,other_interest,other_topic)
            # Check if the other entry has an interest in 'Learn'
            if other_interest == 'Learn':
                # Check if the topics match
                if topic.lower() == other_topic.lower():
                    # Send email to 'email' and 'other_email'
                    # You can add your email sending logic here
                    print(f"Send email to {email} and {other_email} for matching topic: {topic}")
    # Check if interest matches 'Teach'
#    if (interest.lower() == 'teach')