userinp = raw_input("Enter a string")

#Break the string to print in two lines
def lcdValprint(string):
	new_string1 = ""
	new_string2 =""
	print "lenght of string is "
	print (len(string)) 
	if (len(string)>16):
		#display the first 16 characters in line 1
		new_string1 = new_string1 + string[:15]
		#display the second 16 characters in line2
		print "String 1 is: "
		print new_string1
		

		new_string2 = new_string2+ string[16:]
		print "String 2 is"
		print new_string2

	else:
		print string 


lcdValprint(userinp)
 


        
        