# n1 = 3.141596
# n2 = 10.22455
#format
# print('num 1 is {0:.3f} and num 2 is {1:.3f}'.format(n1,n2))
#using f-strings

#dictionary
# def all(dictionary):
# 	for key, val in dictionary.items():
# 		print(f'I am {key} and my position is {all}')

# def all_count(dictionary):
# 	c_position = list(dictionary.values())
# 	for i in set(c_position):
# 		num = c_position.count(i)
# 		print(f'There are {num} {i}')

# totoal_player={}
# while True:
# 	player = input('please enter your name: ')
# 	position = input('please enter your position: ')
# 	totoal_player[player]=position
# 	# print(f'I am {player} and my position is {position}')
# 	another = input('another?(y/n)')
# 	if another == 'y':
# 		continue
# 	else:
# 		break
# # all(totoal_player)
# all_count(totoal_player)


# class method& static method
class Planet:
	shape = 'round'

	def __init__(self, name, radius, gravity, system):
		self.name = name
		self.radius = radius
		self.gravity = gravity
		self.system = system

	def orbit(self):
		return f'{self.name} is orbiting in the {self.system}'

	@classmethod
	def commons(cls):
		return f'All planets are {cls.shape} because of gravity'

	@staticmethod
	def spin(speed='2000 miles per hour'):
		return f'The planet spins and spins at {speed}'
