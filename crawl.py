#!/usr/bin/python3.6

import conf
import utility as interviewbit
import requests


MAIN_URL = 'https://www.interviewbit.com/courses/programming/'
LOGIN_URL = 'https://www.interviewbit.com/users/sign_in/'

#raise SystemExit('We\'re done for the day')

#c = requests.Session()
#interviewbit.login(c, LOGIN_URL)

with requests.Session() as c:
	interviewbit.login(c, LOGIN_URL) # we logged in, hopefully.
	interviewbit.crawl_main(c, MAIN_URL) # topic list is generated


