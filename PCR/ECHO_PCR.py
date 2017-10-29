import csv

a = [] #Unique ID --> [ID, Template, FWD, REV]
b = [] #DNA template
c = [] #forward primer
d = [] #reverse primer
adding_DNA_template = []
adding_fwd_primer = []
adding_rvr_primer = []

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
					b.append(row[1])
					break

	with open('PrimerList.csv', newline='') as h:
		primers = csv.reader(h)
		k = 0
		for row in primers:
			for k in range(len(a)):
				if row[0] == i[2]:
						c.append(row[1])
						break

				elif row[0] == i[3]:
						d.append(row[1])
						break

destination_well = [A1, A2, A3, A4, A5, A6, A7, A8, B1, B2, B3, B4, B5, B6, B7, B8, C1, C2, C3, C4, C5, C6, C7, C8, D1, D2, D3, D4, D5, D6, D7, D8, E1, E2, E3, E4, E5, E6, E7, E8, F1, F2, F3, F4, F5, F6, F7, F8, G1, G2, G3, G4, G5, G6, G7, G8, H1, H2, H3, H4, H5, H6, H7, H8]

f.close()
h.close()
for i in range(len(a)):
    n = [0,0,0,0,0]
    n[0] = Plate1
    n[1] = b[i]
    n[2] = destPlate100
    n[3] = destination_well[i]
    n[6] = 20    #transfer volume
    adding_DNA_template.append(n)

with open('ECHO_DNA_template.csv', 'w', newline='') as g:
	DNA_template = csv.writer(g)
	DNA_template.writerow(["Source Plate Barcode", "Source Well", "Destination Plate Barcode", "Destination Well", "Transfer Volume"])
	DNA_template.writerows(adding_DNA_template)

g.close()

for i in range(len(a)):
    n = [0,0,0,0,0]
    n[0] = Plate1
    n[1] = c[i]
    n[2] = destPlate100
    n[3] = destination_well[i]
    n[6] = 20    #transfer volume
    adding_fwd_primer.append(n)

for i in range(len(a)):
    n = [0,0,0,0,0]
    n[0] = Plate2
    n[1] = d[i]
    n[2] = destPlate100
    n[3] = destination_well[i]
    n[6] = 20    #transfer volume
    adding_rvr_primer.append(n)

with open('ECHO_primers.csv', 'w', newline='') as j:
	fwd_rvr_primers = csv.writer(g)
	fwd_rvr_primers.writerow(["Source Plate Barcode", "Source Well", "Destination Plate Barcode", "Destination Well", "Transfer Volume"])
	fwd_rvr_primers.writerows(adding_fwd_primer)
	fwd_rvr_primers.writerows(adding_rvr_primer)

j.close()
