f= open('poem.txt','r') 
for line in f.readlines():
	print line
f.close()
