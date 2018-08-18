

#############################################################################################
################################# Packeges info and calling #########################
#############################################################################################
# Keras is an open source neural network library written in python.
# import 

# pickle module serializing python oject structure to byte stream.
import pickle

###################################
###### Creating Functions #########
###################################


# function for loading the file.

def load_file (filename):
	file = open(filename,"rb")    # r-- read,b-- binary mode
	img = pickle.load(file)
	file.close()
	return (img)


# __new__ Handles object creation
#  __init__ handles object initialisation.


# class ClassName(object):
# 	"""docstring for ClassName"""
# 	def __init__(self, arg):
# 		super(ClassName, self).__init__()
# 		self.arg = arg
		

