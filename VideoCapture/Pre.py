

f = open("valll.txt","a")

for i in range(3353):
	ss=str(i)
	sz=len(ss)
	kk="00"
	for j in range(4-sz):
		kk = kk + '0'

	f.write("frankfurt/" + kk + str(i) + ".png\n")
