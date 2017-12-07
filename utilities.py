#!/usr/bin/python3.6

import re
import time
import html
import os

from models import Topic, URL
import conf

### --------------------------- LOGIN FUNCTIONS -------------------------- ###

# html response: html response in string
def set_auth_token(html_response):
	rgx_line = '^<form class'
	rgx_token_val = '<input type="hidden" name="authenticity_token" value="(.*?)"'
	line_list = [x.strip() for x in html_response.splitlines()]
	for line in line_list:
		if(re.search(rgx_line, line)): break
	# first match of regex. hopefully the only match.
	conf.AUTH_TOKEN_VAL = re.search(rgx_token_val, line).group(1)

# fills the login form of interviewbit.
def login(session, SIGN_IN_URL):
	print(f'Logging into {SIGN_IN_URL}')
	page = session.get(SIGN_IN_URL) #needed for ze form
    # get & set login form's authentication token
	set_auth_token(page.text)
	payload = {
		conf.USERNAME_KEY   : conf.USERNAME_VAL,
		conf.PASSWORD_KEY   : conf.PASSWORD_VAL,
		conf.AUTH_TOKEN_KEY : conf.AUTH_TOKEN_VAL,
		conf.UTF8_KEY       : conf.UTF8_VAL,
		conf.BUTTON_KEY     : conf.BUTTON_VAL,
		conf.CHECK_BOX_KEY  : conf.CHECK_BOX_VAL}
	# hopefully we b logging in now.
	page = session.post(SIGN_IN_URL, data = payload)
	
	if(re.search('Log Out', page.text)): print('Login successful.')
	else:	raise SystemExit('[Login] messed up at some point.')

### -------------------------- TOPIC LINKS BELOW ------------------------- ###
# fetches all the unlocked topic names & links from 
# https://www.interviewbit.com/courses/programming/
# populates the static topics list of Topic class. 
def fetch_topics(session, MAIN_URL):
	page = session.get(MAIN_URL)
	html_response = page.text
	# expecting 16 matches from link, 17 from name, 16 from stat 
	rgx_topic_link = re.compile('"(/courses/programming/.*?/)"$', re.M)
	rgx_topic_name = re.compile('"topic-title">(.*?)</div>$', re.M)
	rgx_topic_stat = re.compile('<div class="topic-box\s*(.*?)">$', re.M)
	TOPIC_UNLOCKED = 'programming unlocked'
	
	links = rgx_topic_link.findall(html_response)
	names = rgx_topic_name.findall(html_response)
	stats = rgx_topic_stat.findall(html_response)

	for stat, name, link in zip(stats, names, links):
		if(stat == TOPIC_UNLOCKED):
			Topic.instances.append(Topic(name, link))


### ------------------------- PROBLEM LINKS BELOW ------------------------ ###
# fetches all the solved problem links from 
# https://www.interviewbit.com/courses/programming/topics/<topic name>/
# adds problem links to corresponding Topic objects. 
def fetch_problems(session):
	# Search the regex strings in html file for clarification.
	rgx_link = re.compile('<a class="locked".*?href="(.*?)">', re.S)
	rgx_stat = re.compile('<td>\n\s*(.*?)\s*</td>\n\s*</tr>', re.S)
	PROBLEM_SOLVED = 'Solved'

	for topic in Topic.instances:
		url = URL.BASE + topic.link
		print(f'Fetching: {url}')
		# get response from the server | turn it into html file as string
		page = session.get(url); page = page.text
		# get links and statuses
		links = rgx_link.findall(page)
		stats = [PROBLEM_SOLVED in x for x in rgx_stat.findall(page)]
		topic.problems = {l for s, l in zip(stats, links) if s}
		time.sleep(0.2)

### ------------------- COPIES PROBLEMS TO LOCAL BELOW ------------------- ###
# Creates a directory called 'interviewbit'.
# Creates subdirectories called <topicname> inside 'interviewbit'.
# Creates <problemname>.cpp files inside those subdirectories.
# Writes the solution codes fetched from the website into aforementioned
# cpp files.
def copy_problems(session):
	problem_count = 0
	# doensn't throw if the directory already exists 
	os.makedirs('interviewbit', exist_ok=True);  
	os.chdir('interviewbit') # go down #1
	rgx_cpp_code = re.compile('<textarea id="editor".*?>(.*?)</textarea>', re.S)
	for topic in Topic.instances:
		print(f'Fetching topic:{topic.name}')
		# make the directories in interviewbit/ without throwing
		os.makedirs(topic.name, exist_ok=True)
		os.chdir(topic.name) # go down #2
		for problem_link in topic.problems:
			url = URL.BASE + problem_link
			cpp_name = Topic.local_problem_name(problem_link)			
			print('\tproblem: {:<50}'.format(cpp_name), end = '')
			# get response from the server | turn it into html file as string
			page = session.get(url); page = page.text
			# unescapes stuff like &lt &gt | rgx.srch(x).grp(1) = first match
			cpp_code = html.unescape(rgx_cpp_code.search(page).group(1))
			problem_count += 1
			print('...done')
			# create a file & paste the code.
			with open(cpp_name, 'w') as out:
				out.write(cpp_code)
			time.sleep(0.2)
		print()
		os.chdir('..') # go up #2
	os.chdir('..') # go up #1
	print('Everything\'s done.')
	print(f'Number of solved problems:{problem_count}')
