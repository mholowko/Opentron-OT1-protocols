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

destination_well1 = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12]
destination_well2 = [I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, J1, J2, J3, J4, J5, J6, J7, J8, J9, J10, J11, J12, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, L1, L2, L3, L4, L5, L6, L7, L8, L9, L10, L11, L12, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, N1, N2, N3, N4, N5, N6, N7, N8, N9, N10, N11, N12, O1, O2, O3, O4, O5, O6, O7, O8, O9, O10, O11, O12, P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12]

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
    n[3] = destination_well1[i]
    n[6] = 20    #transfer volume
    adding_fwd_primer.append(n)

for i in range(len(a)):
    n = [0,0,0,0,0]
    n[0] = Plate2
    n[1] = d[i]
    n[2] = destPlate100
    n[3] = destination_well2[i]
    n[6] = 20    #transfer volume
    adding_rvr_primer.append(n)

with open('ECHO_primers.csv', 'w', newline='') as j:
	fwd_rvr_primers = csv.writer(g)
	fwd_rvr_primers.writerow(["Source Plate Barcode", "Source Well", "Destination Plate Barcode", "Destination Well", "Transfer Volume"])
	fwd_rvr_primers.writerows(adding_fwd_primer)
	fwd_rvr_primers.writerows(adding_rvr_primer)

j.close()
