#!/usr/bin/python3.6
import utilities as interviewbit
import requests
from models import URL

with requests.Session() as c:
	interviewbit.login(c, URL.LOGIN)
	interviewbit.fetch_topics(c, URL.MAIN) # Topic list is generated
	interviewbit.fetch_problems(c) # Problem lists in each topic is generated
	interviewbit.copy_problems(c) # problems are copied to .cpp files
