with open('files/write.txt','w') as write_file:
	write_file.write('Hey there ninjias, python is awesome')
	
#'a' is amend
with open('files/write.txt' , 'a') as write_file:
	write_file.write('\n I love it so much, I dream in python')

quotes = [
	'\n I can resist everything except temptation',
	'\n We are all in the gutter, but some of us are looking at the stars',
	'\n Always forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a')as write_files:
	write_files.writelines(quotes)