from string import Template
name = 'world'
program ='python'
new = Template('Hello $name! This is $program.')
print(new.substitute(name= name,program=program))
