#facebook crawling and return post name/text
import time
import subprocess
import re
import datetime
import os

def call_crawler(date):
	os.chdir(os.getcwd()+"\\fbcrawl-master")
	subprocess.run(["scrapy", "crawl", "fb", "-a", "email=kjune03223@gmail.com", "-a", "password=kadaejeon", "-a", "page=KaDaejeon", "-a", "date="+date, "-a", "lang=en", "-o", "crawled.csv"])
#	subprocess.run(["scrapy crawl fb -a email=\"01028233991\" -a password=\"wnsdn12\" -a page=\"KaDaejeon\" -a date=\""+date+	"\" -a lang=\"en\" -o=\"crawled.csv\""])
	return

def read_file():
	post=[]
	f=open(os.getcwd()+"\\fbcrawl-master\\crawled.csv",'r',encoding='utf-8')
	line=f.readline()
	while True:
		line=f.readline()
		if not line: break
		pattern=re.compile("\[[^]+\])([^]+)-+ #[^]+https://talkyou",re.DOTALL)
		tmp=line.match(pattern)
		name=tmp.group(1)
		text=tmp.group(2)
		post.append([name,text])
	f.close()
	return post

def debug(post):
	print(post)

if __name__=="__main__":
#	while True:
	nowdir=os.getcwd()
	date=datetime.datetime.now()
	call_crawler(date.strftime("%Y-%m-%d"))
	os.remove("crawled.csv")
	os.chdir(nowdir)
	print(os.getcwd())
	post=read_file()
	debug(post)
#		time.sleep(360)
