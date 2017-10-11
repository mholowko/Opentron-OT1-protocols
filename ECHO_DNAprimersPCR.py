import csv

a = [] #Unique ID
b = [] #DNA template
c = [] #forward primer
d = [] #reverse primer

with open('UniqueID.csv', newlinw='') as e:
	UniqueID = csv.reader(e)
	for row in UniqueID:
		a.appened(row)

with open('DNA.csv', newline='') as f:
    DNA = csv.reader(f)
    for row in DNA:
    	z = [0,0]
    	z[0] = row[0]
    	z[1] = row[1]
    	b.append(z)

with open('Primers.csv', newline='') as h:
	primers = csv.reader(h)
	i = 0
	for row in primers:
		i += 1
		if i%2==1:
			z = [0,0]
			z[0] = row[0]
			z[1] = row[1]
			c.append(z)

		else:
			z = [0,0]
			z[0] = row[0]
			z[1] = row[1]
			d.append(z)

with open('DNA_primers.csv', 'w', newline='') as g:
	DNA_primers = csv.reader(g)
	DNA_primers.writerow(["ID", "DNA Template", "Location", "Forward Primer", "Location", "Reverse Primer", "Location"])
	i = 0
	for row in DNA_primers:
		DNA_primers.writerow(a[i]+b[i]+c[i]+d[i])
		i += 1
