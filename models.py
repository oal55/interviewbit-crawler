class URL():
	BASE  = 'https://www.interviewbit.com'
	LOGIN = BASE + '/users/sign_in/'
	MAIN  = BASE + '/courses/programming/'


class Topic():
	instances = []

	# name: Topic name in interview bit. E.g. Two Pointers, Arrays etc.
	# link: relative url of the page from URL.BASE
	# problems[i] is the relative url of the problem from URL.BASE 
	def __init__(self, name='', link=''):
		self.name = name
		self.link = link
		self.problems = []

	# prettifies the instance
	def __str__(self):
		res =  'Printing Topic:\n'
		res += f'\tname: {self.name}\n'
		res += f'\tlink: {self.link}\n'
		res += f'\tSolved problems:\n'
		for p in self.problems:
			res += f'\t  {p}\n'
		return res

	def local_path(self):
		return self.name

	# problem: element of instances[i].problems 
	# returns
	#	  /problems/largest-coprime-divisor/
	@staticmethod
	def local_problem_name(problem):
		parts = problem.split('/')
		return parts[-2] + '.cpp'