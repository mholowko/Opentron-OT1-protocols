import csv

a = [] #Unique ID --> [ID, Template, FWD, REV]
b = [] #DNA template
c = [] #forward primer
d = [] #reverse primer
combined = []

with open('PartsList.csv', newline='') as e:
	Parts = csv.reader(e)
	for row in Parts:
		a.append(row)
e.close()
del a[0]
i=0
for i in a:
	with open('TemplateList.csv', newline='') as f:
		Template = csv.reader(f)
		for row in Template:
			k=0
			for k in range(len(a)):
				if row[0] == i[1]:
					z = [0,0]
					z[0] = row[0]
					z[1] = row[1]
					b.append(z)
					break

	with open('PrimerList.csv', newline='') as h:
		primers = csv.reader(h)
		k = 0
		for row in primers:
			for k in range(len(a)):
				if row[0] == i[2]:
						z = [0,0]
						z[0] = row[0]
						z[1] = row[1]
						c.append(z)
						break

				elif row[0] == i[3]:
						z = [0,0]
						z[0] = row[0]
						z[1] = row[1]
						d.append(z)
						break

f.close()
h.close()
for i in range(len(a)):
    n = [0,0,0,0,0,0,0]
    n[0] = a[i][0]
    n[1] = b[i][0]
    n[2] = b[i][1]
    n[3] = c[i][0]
    n[4] = c[i][1]
    n[5] = d[i][0]
    n[6] = d[i][1]
    combined.append(n)

with open('DNA_primers.csv', 'w', newline='') as g:
	DNA_primers = csv.writer(g)
	DNA_primers.writerow(["ID", "DNA Template", "Location", "Forward Primer", "Location", "Reverse Primer", "Location"])
	DNA_primers.writerows(combined)

g.close()
