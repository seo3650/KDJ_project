# -*- coding: utf-8 -*-
import notification.notification as notification
import score.score as score
import crawler as crawler
from time import sleep
import re


while True:
    contents = crawler.main()
    print(contents)
    contents = score.main(contents)
    print(contents)
    notification.notification(contents)
    sleep(10)
