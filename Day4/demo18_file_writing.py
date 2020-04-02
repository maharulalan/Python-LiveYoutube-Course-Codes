poem = ''' Programming is fun
When the work is done
if you wanna make your work also fun:
        use Python!
'''

f = open('poem.txt', 'w') # open for 'w'riting
f.write(poem) # write text to file
f.close()
