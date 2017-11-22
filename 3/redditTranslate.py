import praw
import pdb
import re
import os
import time

from googletrans import Translator

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("uwaterloo")
translator = Translator()

for comment in subreddit.stream.comments():

    try:
        detection = translator.detect(comment.body)
    except:
        continue
    if (len(comment.body)>7):
        detection = translator.detect(comment.body)
        if  (detection.lang=='zh-CN') and (detection.confidence>0.5):
            result = translator.translate(comment.body).text
            with open("replyLog.txt", "a") as f:
                f.write(result+"\n")
            translationBot_reply = 'English Translation:' + result + '\n*****\n *I am a chinese translation bot*'
            try:
                comment.reply(translationBot_reply)
            except:
                time.sleep(600)