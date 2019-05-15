from PIL import Image
import sys
import subprocess
import random


#reverse string to make len word can't compare with dictionary
def reversestring(message):
	return message[::-1]


#create a vigenere table
def vigenere_table():
    table = []
    for i in range(26):
        table.append([])

    for row in range(26):
        for column in range(26):
            if (row + 65) + column > 90:
                table[row].append(chr((row+65) + column - 26))
            else:
                table[row].append(chr((row+65)+column))

    return table

#use vignere table to encryption message with key
def vignere_encryption(message, key):
	table = vigenere_table()
	message = message.upper()
	key = key.upper()
	key_map = ""
	j=0
	for i in range(len(message)):
		if (ord(message[i]) >= 32 and ord(message[i]) <= 64) or (ord(message[i]) >= 91 and ord(message[i]) <= 96) or (ord(message[i]) >= 123 and ord(message[i]) <= 126):
			#parse whitespace
			key_map += message[i]
		else:
			if j < len(key):
				key_map += key[j]
				j += 1
			else:
				j = 0
				key_map += key[j]
				j += 1

    
	encrypted_message = ""

	for i in range(len(message)):
		if (ord(message[i]) >= 32 and ord(message[i]) <= 64) or (ord(message[i]) >= 91 and ord(message[i]) <= 96) or (ord(message[i]) >= 123 and ord(message[i]) <= 126):
			encrypted_message += message[i]
		else:
			row = ord(message[i])-65
			column = ord(key_map[i]) - 65
			encrypted_message += table[row][column]

	return (format(encrypted_message))
	
#count to split key and message can't fit together	
def itr_count(key, message):
    counter = 0
    result = ""

    for i in range(26):
        if key + i > 90:
            result += chr(key+(i-26))
        else:
            result += chr(key+i)
 
    for i in range(len(result)):
        if result[i] == chr(message):
            break
        else:
            counter += 1

    return counter

#decrypt message with key base on vignere table above
def vignere_decryption(message, key):
    table = vigenere_table()
    key = key.upper()
    message = message.upper()
    key_map = ""
    j=0
    for i in range(len(message)):
		if (ord(message[i]) >= 32 and ord(message[i]) <= 64) or (ord(message[i]) >= 91 and ord(message[i]) <= 96) or (ord(message[i]) >= 123 and ord(message[i]) <= 126):
			#loai dau cach
			key_map += message[i]
		else:
			if j < len(key):
				key_map += key[j]
				j += 1
			else:
				j = 0
				key_map += key[j]
				j += 1
    decrypted_message = ""

    for i in range(len(message)):
        if (ord(message[i]) >= 32 and ord(message[i]) <= 64) or (ord(message[i]) >= 91 and ord(message[i]) <= 96) or (ord(message[i]) >= 123 and ord(message[i]) <= 126):
            decrypted_message += message[i]
        else:
            decrypted_message += chr(65 + itr_count(ord(key_map[i]), ord(message[i])))

    return format(decrypted_message)
	
#add watermark	
def mark(message):
	message=message + "BLUEsteg***"
	return message

def random(message):
	message=message + chr(random.randint(32, 126))*random.randint(0,5)
	return message
	

#def readImage(image):
#convert message to binary
def tobinary(message):
	#s = ' '.join(format(ord(i), 'b') for i in message)
	#s = map(bin,bytearray(message))
	a=' '.join('{0:08b}'.format(ord(x), 'b') for x in message)
	return a.split()

#check have message in image or not by watermark of toolname
def checkmessage(message):
	if message == null:
		print "Nothing here."
	elif message[-11:] != "BLUEsteg***":
		print "Nothing here."

#encrypt message to bit red
def RGBR(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()
	#ran = random()
	#loop to enter message to pixel
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			r2 = list(bin(r))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				#print newimage
				#print b
				continue
			else:
					#print s[j]
				if r2[-1] != s[j][i]:
					r2[-1] = s[j][i]
				#print b2
				#print d
				d+=1
				i-=1
				r3 = ''.join(r2)
				r4 = int(r3,2)
				#print b4
				newimage.append((r4,g,b))
				#print newimage
				#if d==7 or s[j][i]=='b':
				#	d=0
				#	i=1
				#	j+=1
					#print s[j]
	#print newimage
	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#encrypt message to bit green
def RGBG(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	#ran = random()
	#loop to enter message to pixel
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()	
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			g2 = list(bin(g))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				#print newimage
				#print b
				continue
			else:
					#print s[j]
				if g2[-1] != s[j][i]:
					g2[-1] = s[j][i]
				#print b2
				#print d
				d+=1
				i-=1
				g3 = ''.join(g2)
				g4 = int(g3,2)
				#print b4
				newimage.append((r,g4,b))
				#print newimage
				#if d==7 or s[j][i]=='b':
				#	d=0
				#	i=1
				#	j+=1
					#print s[j]
	#print newimage
	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#encrypt message to bit blue
def RGBB(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	#r = random()
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()	
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			b2 = list(bin(b))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				continue
			else:
				if b2[-1] != s[j][i]:
					b2[-1] = s[j][i]
				d+=1
				i-=1
				b3 = ''.join(b2)
				b4 = int(b3,2)
				newimage.append((r,g,b4))
	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#encrypt for Red bit of RGBA image
def RGBAR(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			r2 = list(bin(r))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				continue
			else:
					#print s[j]
				if r2[-1] != s[j][i]:
					r2[-1] = s[j][i]
				#print b2
				#print d
				d+=1
				i-=1
				r3 = ''.join(r2)
				r4 = int(r3,2)
				newimage.append((r4,g,b))

	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#encrypt for Green bit of RGBA image
def RGBAG(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			g2 = list(bin(g))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				continue
			else:
					#print s[j]
				if g2[-1] != s[j][i]:
					g2[-1] = s[j][i]
				#print b2
				#print d
				d+=1
				i-=1
				g3 = ''.join(g2)
				g4 = int(g3,2)
				newimage.append((r,g4,b))

	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#encrypt for Blue bit of RGBA image
def RGBAB(image,s):
	img = Image.open(image)
	d=0
	i=-1
	j=0
	newimage=[]
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	if len(s) > w*h/8:
		print "Message too long for this picture"
		sys.exit()
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			b2 = list(bin(b))
			if d==8:
				d=0
				i=-1
				j+=1
			if j >= len(s):
				newimage.append((r,g,b))
				continue
			else:
				if b2[-1] != s[j][i]:
					b2[-1] = s[j][i]
				d+=1
				i-=1
				b3 = ''.join(b2)
				b4 = int(b3,2)
				newimage.append((r,g,b4))

	newim = Image.new(img.mode,img.size,"white")
	newim.putdata(newimage)
	newim.save("output.png")

#read image and decrypt Red bit
def readRGBR(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			#print b
			#print bin(b)[-1:]
			s += bin(r)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				#print c
				#print s
				#print message
				if ord(c) > 126 or ord(c)< 32:
					#print message
					#return message
					#print message
					return message
				else:
					message += c
				#print message
				d=0
				s='' 

#decrypt Green bit
def readRGBG(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			s += bin(g)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				if ord(c) > 126 or ord(c)< 32:
					return message
				else:
					message += c
				d=0
				s='' 

#decrypt blue bit
def readRGBB(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b = img.getpixel((x,y))
			s += bin(b)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				if ord(c) > 126 or ord(c)< 32:
					return message
				else:
					message += c
				d=0
				s='' 

#decrypt RGBA red
def readRGBAR(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			#print b
			#print bin(b)[-1:]
			s += bin(r)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				if ord(c) > 126 or ord(c)< 32:
					return message
				else:
					message += c
				#print message
				d=0
				s=''

#decrypt RGBA Green
def readRGBAG(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			s += bin(g)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				if ord(c) > 126 or ord(c)< 32:
					return message
				else:
					message += c
				d=0
				s='' 

#decrypt RGBA Blue
def readRGBAB(image):
	newimage=[]
	d = 0
	s = ''
	message = ''
	img=Image.open(image)
	w = img.size[0]
	h = img.size[1]
	for y in range (h):
		for x in range (w):
			r,g,b,a = img.getpixel((x,y))
			s += bin(b)[-1:]
			d += 1
			if d==8:
				c = (chr(int(s[::-1],2)))
				if ord(c) > 126 or ord(c)< 32:
					return message
				else:
					message += c
				d=0
				s='' 

#check watermark to stop service
def check(message):
	f = "Nothing here or wrong key."
	if (message[-11:]=="BLUESTEG***"):
		return message[:-11]
	else:
		return f

#print help for user
def showhelp():
	print """
	Usage: python bluestego.py [OPTIONS]
	[OPTIONS]
	-i / --image   [File location]
	-h / --help 	 [Show help]
	"""

#show 1st menu
def menu():
	print """
1. Encrypt message to image
2. Decrypt message from image
	"""

#show option menu for user
def option(image):
	menu()
	choice = input("Your choice: \n")
	if choice == 1:
		print("Color use to encrypt \n\tRed(r) \n\tGreen(g)\n\tBlue(b)\n")
		colors=raw_input("Your choice: \n")
		#print(colors)
		message = raw_input("Message: ")
		key = raw_input("Key: ")
		s = tobinary(reversestring(vignere_encryption(mark(message),key)))
		out = subprocess.check_output(['file', image])

		#encrypt
		if colors == "r":
			if 'RGBA' in out:
				RGBAR(image,s)
				print "Encrypted image: output.png"
			else:
				RGBR(image,s)
				print "Encrypted image: output.png"
		elif colors == "g":
			if 'RGBA' in out:
				RGBAG(image,s)
				print "Encrypted image: output.png"
			else:
				RGBG(image,s)
				print "Encrypted image: output.png"
		elif colors == "b":
			if 'RGBA' in out:
				RGBAB(image,s)
				print "Encrypted image: output.png"
			else:
				RGBB(image,s)
				print "Encrypted image: output.png"
		elif colors != "r" or colors != "g" or colors != "b":
				print "Please chose r,g,b"

	#decrypt
	elif choice == 2:
		print("Color to decrypt \n\tRed(r) \n\tGreen(g)\n\tBlue(b)\n")
		colors = raw_input("Your choice: \n")
		key = raw_input("Key: ")
		out = subprocess.check_output(['file', image])
		if colors == "r":
			if 'RGBA' in out:
				s=readRGBAR(image)
			else:
				s=readRGBR(image)
			mess = (vignere_decryption(reversestring(s),key))
			print check(mess)
		elif colors == "g":
			if 'RGBAG' in out:
				s=readRGBAG(image)
			else:
				s=readRGBG(image)
			#s = readImg(image)
			#print s
			mess = (vignere_decryption(reversestring(s),key))
			print check(mess)
		elif colors == "b":
			if 'RGBA' in out:
				s=readRGBAB(image)
			else:
				s=readRGBB(image)
			#s = readImg(image)
			#print s
			mess = (vignere_decryption(reversestring(s),key))
			print check(mess)
		elif colors != "r" or colors != "g" or colors != "b":
				print "Please chose r,g,b"
	elif choice != 1 or choice !=2:
		print "Wrong choice"

if __name__ == '__main__':
	if len(sys.argv) <= 1:
		showhelp()
		sys.exit()
 	else:
 		if sys.argv[1] == "--image" or sys.argv[1] == "-i" :
  			option(sys.argv[2])
  		elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
  			showhelp()
  		else:
  			print "Wrong option please try --help"
