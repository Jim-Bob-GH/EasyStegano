from PIL import Image

def convertText(text, mode):
	slim = ""
	for x in range(0,len(text)):
		if mode == "hex":
			let = hex(ord(text[x]))
		elif mode == "bin":
			let = bin(ord(text[x]))
		let = let[+2:]
		slim += let + "."
	return slim

def readFile(selected):
	box = ""
	with open(selected, "rb") as f:
		byte = f.read(1)
		while byte != b"":
			byte = f.read(1)
			new = str(byte)
			box += new[+2:-1]
	return box

def encodeImage(pic, message, opic, mul=1):
	img = Image.open(pic)
	pixels = img.load()
	width, height = img.size
	print("Selected image: ", pic)
	print("Width: ", width, "  Height: ",height)
	#print("Adding: ", message)
	
	val = 0; changes = []
	for m in range(len(message)):
		if str(message[m]) == "a":
			val = 10
		elif str(message[m]) == "b":
			val = 11
		elif str(message[m]) == "c":
			val = 12
		elif str(message[m]) == "d":
			val = 13
		elif str(message[m]) == "e":
			val = 14
		elif str(message[m]) == "f":
			val = 15
		elif str(message[m]) == ".":
			val = -5
		else:
			val = message[m]
		test = int(val) -10; test = str(test)   # UGLY
		changes.append(test)
	#print(changes)

	if len(changes) < width*height:
		step = 0
		for w in range(width):
			for h in range(height):
				if step < len(changes)-1:
					#print(w, h, pixels[w,h], changes[step])
					colors = pixels[w,h]
					new = colors[0]
					new -= (int(changes[step]))*mul
					pixels[w,h] = (new,colors[1],colors[2])
					step+=1
		img.save(opic)
		print("Using ", len(changes), " of ", width*height)
	else:
		print("Operation canceled.. Message is bigger than available storage.  ", len(changes), " of ", width*height)

def decodeImage(pic, key):
	message = []
	print("Unlocking ", pic, " with ", key)
	img1 = Image.open(pic); img2 = Image.open(key)
	pixels1 = img1.load(); pixels2 = img2.load()
	width1, height1 = img1.size; width2, height2 = img2.size
	if width1 != width2 or height1 != height2:
		print("Pictures dont match!")
	else:
		for w in range(width1):
			for h in range(height1):
				colors1 = pixels1[w,h]; colors2 = pixels2[w,h]
				aaa = colors1[0]; bbb = colors2[0]
				if (aaa-bbb) != 0:
					message.append(aaa-bbb)
	message.reverse()
	print(message)


# Examples

#encodeImage("original.png", convertText("Just testing if this works","bin"), "modified.png", 1)

#decodeImage("modified.png", "original.png")

#message = readFile(textfile.txt)
