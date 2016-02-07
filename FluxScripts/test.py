import re

txt = open("bulbstate.txt", "r+")
statelist = txt.readlines()
state = re.sub('\n', '', statelist[0])
print state