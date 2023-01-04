import boto3
H = boto3.session.Session("kalvin")


s3 = H.client('s3')
s3.upload_file('Hi Bro','abkalvin17','love_you_bot_uhh.txt')
