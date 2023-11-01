#!/usr/bin/python3
class SingletonClass():
  '''
  the class creates 1 instance object
  '''


  def __new__(cls):
    '''
    method checks if an instance is already created, if not creates one
    '''

    print(vars(cls))
    if not hasattr(cls, 'instance'):
      cls.instance = super(SingletonClass, cls).__new__(cls)
      print("creating a new instance")
      
    return cls.instance


s1 = SingletonClass()
cls_attributes = vars(SingletonClass)
print(cls_attributes)
s1.value = 42

s2 = SingletonClass()
print(s2.value)

if s1 is not s2:
  print(True)
else:
  print(False)