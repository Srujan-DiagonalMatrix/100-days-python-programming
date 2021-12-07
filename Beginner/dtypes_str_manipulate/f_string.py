#################################################################
# f_string: allows you to concatinate any data types.
# Instead of converting str() function every time.
#
# NOTE: you may use f or format.. both are same.
#################################################################

name = 'Srujan'
age = 35
height = 1.45
male = True

summary = f"My name is {name} and I'm {age} old. I'm {height} tall and am I male? - {male}"
summary1 = "My name is {} and I'm {} old. I'm {} tall and am I male? - {}".format(name,age,height,male)
print(summary)
print(summary1)

'''
My name is Srujan and I'm 35 old. I'm 1.45 tall and am I male? - True
'''


#Non F_string
#summ = "My name is " + name + "and I'm "+age+" old"
#print(summ)

# TypeError: can only concatenate str (not "int") to str

