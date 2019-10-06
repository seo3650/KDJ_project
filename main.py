# -*- coding: utf-8 -*-
import notification.notification as notification
import score.score as score
import crawler as crawler
from time import sleep
import re


while True:
    contents = crawler.main()
    print(contents)
    scores = []
    for article in contents:
        scores.append(score.score_with_word(article[0], article[1], 'loss'))
    print(scores)
    notification.notification(scores)
    sleep(10)
