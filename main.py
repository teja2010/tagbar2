#the main file, it will create a tmp file, which can be opened in vsplit 
from os import system
import os.path

PluginLocation = '/home/teja/.vim/plugins/tagbar2'

INFOfile = open('curr_info')
file_info = INFOfile.readline()
file_info = file_info.split("\n")[0]
file_path = '/home/teja/'+"/".join(file_info.split("/")[:-1]) + "/"
file_name = file_info.split("/")[-1]

INFOfile.close()
print file_info
print file_path
print file_name

print file_path + 'tags'

exit = 0
#make all checks here

#search for the tags file.
tags_path = file_path

while tags_path != '':
	if os.path.exists(tags_path + '/tags'):
		print "Tags file found"
		break;
	else:
		tags_path = "/".join(tags_path.split("/")[:-1])
		print tags_path


if os.path.exists(tags_path + '/tags'):
	print "Tags file found."
else:
	print "No tags file found."
	exit = 1

# started work :)
print tags_path
print file_path
if tags_path != file_path:
	rel_file_path =  file_path.split(tags_path+'/')[1]
else:
	rel_file_path = ''
print rel_file_path

if exit == 0:
	os.system('grep ' + rel_file_path + '/' + file_name +' '+ tags_path + '/tags > '+PluginLocation +'/chetta/' + '__'+rel_file_path+file_name+'__.t2')
	#T2_FILE = open()

#TODO: cscope -L1 asdasd
