#the main file, it will create a tmp file, which can be opened in vsplit 
from os import system
import os.path

PluginLocation = '/home/teja/.vim/plugins/tagbar2'

INFOfile = open('/home/teja/.vim/plugins/tagbar2/curr_info')
file_info = INFOfile.readline()
file_info = file_info.split("\n")[0]
file_path = "/".join(file_info.split("/")[:-1]) + "/"
file_name = file_info.split("/")[-1]

INFOfile.close()
#print "file full path = "+file_info
#print "just path = "+file_path
print "file name = "+file_name

exit = 0
#make all checks here

#search for the tags file.
tags_path = file_path
cscope_path = file_path

while tags_path != '':
	if os.path.exists(tags_path + '/tags'):
		#print "tags file found"
		break;
	else:
		tags_path = "/".join(tags_path.split("/")[:-1])
		#print tags_path

while cscope_path != '':
	if os.path.exists(cscope_path + '/cscope.out'):
		#print "cscope file found"
		break;
	else:
		cscope_path = "/".join(cscope_path.split("/")[:-1])
		#print cscope_path


#if os.path.exists(tags_path+'/tags'):
if os.path.exists(cscope_path+'/cscope.out'):
	print "all files found."
else:
	print "some files not found."
	exit = 1

# started work :)
#print "tags path = "+tags_path
#print "cscope path ="+cscope_path
#print "file path = "+file_path
# started work :)
print tags_path
print file_path
if tags_path != file_path:
	rel_file_path =  file_path.split(tags_path+'/')[1]
else:
	rel_file_path = ''
#print "file path relative to tags = "+rel_file_path

chetta_name  = "*".join(file_info.split('/'))+file_name
if exit == 0:
	#grep the function names
	os.system('grep ' + rel_file_path + file_name +' '+ tags_path + \
		'/tags > '+PluginLocation +'/chetta/' + '__'+ \
		chetta_name +'__.t2')
	#remove any old files. A max of 40 files can stay in the folder
	#TODO: send output to dev/null to make it silent
	os.system('ls '+PluginLocation+'/chetta/ -t | sed -e \'1,40d\' ' + \
		'| sed -r  \'s/__/'+ \
		'\/'.join(PluginLocation.split('/')) + \
		'\\/chetta\\/__/\'  | xargs -d \'\n\' rm') # > /dev/null 2>&1')
	os.system('ls')


#T2_FILE = open()

#TODO: cscope -L1 asdasd
