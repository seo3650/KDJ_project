#facebook crawling and return post name/text
import subprocess
import re
import datetime
import os

#To run this program, You need To 'pip install' scrapy, datetime

def call_crawler(date):
	os.chdir(os.getcwd()+"\\fbcrawl-master")
	subprocess.run(["scrapy", "crawl", "fb", "-a", "email=kjune03223@gmail.com", "-a", "password=kadaejeon", "-a", "page=KaDaejeon", "-a", "date="+date, "-a", "lang=en", "-o", "crawled.csv"])
#	subprocess.run(["scrapy crawl fb -a email=\"01028233991\" -a password=\"wnsdn12\" -a page=\"KaDaejeon\" -a date=\""+date+	"\" -a lang=\"en\" -o=\"crawled.csv\""])
	return

def read_file():
	post=[]
	f=open("crawled.csv",'r',encoding='utf-8')
	line=f.readline()
	while True:
		line=f.readline()
		if "source,shared_from,date,text,reactions,likes,ahah,love,wow,sigh,grrr,comments,post_id,url" in line: continue
		if not line: break
		try:
			name=line.split('[')
			name=name[1].split(']')
			text=name[1].split("----------")
			post.append([name[0],text[0]])
		except:
			print(name)
	f.close()
	return post

def debug(post):
	print(post)

def main():
	nowdir=os.getcwd()
	date=datetime.datetime.now()
	call_crawler(date.strftime("%Y-%m-%d"))
	post=read_file()
	os.remove("crawled.csv")
	os.chdir(nowdir)
	return post


#	debug(post)
