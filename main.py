# -*- coding: utf-8 -*-
import notification.notification as notification
import score.score as score
import crawler as crawler
from time import sleep
import re

option = notification.main("initial", "")

while True:

    print("option: " + option)
    contents = crawler.main()
    print(contents)
    scores = []
    for article in contents:
        signal = score.score_with_word(article[0], article[1], option)
        scores.append(signal) #?
        if signal:
            notification.main("notify", article[0])
    print(scores)
    #notification.main("notify")
    sleep(10)
