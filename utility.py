#!/usr/bin/python3.6

import re
import conf
import requests

class Topic():
	instances = []
	def __init__(self, name='', link=''):
		self.name = name
		self.link = link

	def __str__(self):
		res =  'Printing Topic:\n'
		res += f'\tname: {self.name}\n'
		res += f'\tlink: {self.link}\n'
		return res


### --------------------- UTILITY FUNCTIONS --------------------- ###

# html response: html response in string
def set_auth_token(html_response):
	rgx_line = '^<form class'
	rgx_token_val = '<input type="hidden" name="authenticity_token" value="(.*?)"'
	line_list = [x.strip() for x in html_response.splitlines()]
	for line in line_list:
		if(re.search(rgx_line, line)): break
	# first match of regex. hopefully the only match.
	conf.AUTH_TOKEN_VAL = re.search(rgx_token_val, line).group(1)

# gets one topic from a <div class="topic-box  programming unlocked"> element
# returns the index of the next line and the fetched topic object
def get_topic(line_list, index):
	div_count = 1;  index = index + 1
	while(div_count):
		line = line_list[index]
		# look for title name & link to problems 
		if(re.search('<a href', line)):
			topic_link = re.search('<a href="(.*?)"', line).group(1)
		if(re.search('topic-title', line)):	
			topic_name = re.search('"topic-title">(.*?)<', line).group(1)
		# keep track of opened and closed div elements
		if(re.search('</div>', line)):	div_count -= 1
		if(re.search('<div', line)):	div_count += 1
		index = index + 1
	return index, Topic(name=topic_name, link=topic_link)

# fetches all the topics from https://www.interviewbit.com/courses/programming/
# populates the static topics list of Topic class.
def get_topics(html_response):
	rgx_block_start = 'level">$' # regex for block start
	rgx_div_bgn = "^<div"
	rgx_div_end = "</div"
	line_list = [x.strip() for x in html_response.splitlines()]

	topic_count = 0
	for index in range(len(line_list)):
		if(re.search(rgx_block_start, line_list[index])):	topic_count += 1
		if(topic_count == 2):	break
	
	unlocked = 1
	while(unlocked):
		unlocked = 0 # will be updated this if the current topic is unlocked
		# keeps track of opened & closed div elements. | index.
		div_count = 1;		index = index + 1
		while(div_count):
			line = line_list[index]
			if(re.search('programming unlocked">$', line)):
				unlocked = 1 #this topic was unlocked, so we keep on looking
				index, topic = get_topic(line_list, index)
				Topic.instances.append(topic)
				continue
			if(re.search('</div>', line)):	div_count -= 1
			if(re.search('<div', line)):	div_count += 1
			index += 1
	# return	

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
	if(re.search(conf.NICKNAME, page.text)): print('Login successful.')
	else:	raise SystemExit('[Login]We fucked up at some point.')

def crawl_main(session, MAIN_URL):
	page = session.get(MAIN_URL)
	get_topics(page.text)
	for topic in Topic.instances:	print(topic)
	print(len(Topic.instances))