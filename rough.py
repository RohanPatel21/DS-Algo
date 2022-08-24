string = 'shlok goswami'
sub = 'SECRET'
digits = ""
if string != None and sub in string:
	for i in string:
		if i.isdigit():
			digits = digits + i
	print("Find numbers from string:", digits)
	print(len(digits))
else:
    print("SECRET code not found")
