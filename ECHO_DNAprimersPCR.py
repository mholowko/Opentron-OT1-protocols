import csv

a = [] #Unique ID --> [ID, Template, FWD, REV]
b = [] #DNA template
c = [] #forward primer
d = [] #reverse primer

with open('UniqueID.csv', newlinw='') as e:
	UniqueID = csv.reader(e)
	for row in UniqueID:
		a.appened(row)
UniqueID.close()

i=0
for i in range(len(a)):
	formula = a[i]
	i += 1
	with open('DNA.csv', newline='') as f:
	    DNA = csv.reader(f)
	    k=0
	    for row in DNA:
	    	if row[k][0] == formula[1]:
	    		z = [0,0]
	    		z[0] = row[0]
	    		z[1] = row[1]
	    		b.append(z)
	    		break

	    	else:
	    		k += 1
	DNA.close()

	with open('Primers.csv', newline='') as h:
		primers = csv.reader(h)
		k = 0
		for row in primers:
			if row[k][0] == formula[2]:
					z = [0,0]
					z[0] = row[0]
					z[1] = row[1]
					c.append(z)
					break

			elif row[k][0] == formula[3]:
					z = [0,0]
					z[0] = row[0]
					z[1] = row[1]
					d.append(z)
					break

			else:
				k += 1

	primers.close()

with open('DNA_primers.csv', 'w', newline='') as g:
	DNA_primers = csv.reader(g)
	DNA_primers.writerow(["ID", "DNA Template", "Location", "Forward Primer", "Location", "Reverse Primer", "Location"])
	i = 0
	for row in DNA_primers:
		DNA_primers.writerow(a[i][0]+b[i]+c[i]+d[i])
		i += 1
DNA_primers.close()
