import re


file = open("text.txt",'r') #opens the file with the coded text
file_output = open("dec_out_digits.txt",'w') #output file

def txt_split(a,b): #split text for equal parts
	d = dict()
	y = 0
	for i in range (0, (len(a)/b)):
		code = a[y: y + b]
		y = y + 1
		d[code] = d.get(code,0)+1 #count same values
	lst = list() # list for showing the most popular values
	for a,b in sorted(d.items()):
		lst.append( (b,a) )
	lst.sort(reverse=True) #sort the list
	return lst

def symbol_counter(a): #count number of symbols in decoded text
	count = 0
	for i in a:
		count = count + 1
	return count

def output(lst): #write the output file
	for a,b in lst[:100]:
		b = int(b)
		dec_plus = (2.3+b-18.4)/48
		dec_mult = (2.3*b-18.4)/48
		file_output.write(str(b)+','+str(a)+','+str(dec_plus)+','+str(dec_mult)+'\n')

#init the txt file and prepare to read
text = file.read()
text = text.split('\n')

symbol_numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,20]

for i in text: #count symbols in raw txt file
	print 'number of symbols: ', symbol_counter(i)

for num in symbol_numbers: #count symbol patterns in raw txt file
	for i in text:
		digits = re.sub('[^0-9]', '', str(text))
		lst = txt_split(digits,num)
	output(lst)

print '---------------------------------------------------------\nThe output file is generated'