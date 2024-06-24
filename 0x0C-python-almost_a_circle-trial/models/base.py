#!/usr/bin/python3
	"""
 defines a base model class
	"""
 class Base:
	"""
 represents the base model
	"""
	__nb_objects  = 0 #class variable shared by all instances of the class
 
 	def __init__(self, id=None):
      if  id is not None :
          self.id  = id
      else:
          Base.__nb_objects += 1
          self.id = Base.__nb_objects
          
          
if  __name__ == "__main__":
    b


