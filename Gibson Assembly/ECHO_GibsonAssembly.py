import csv

adding_extractedDNA = []

source_well = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, D1, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, I1, I2, I3, I4, I5, I6, I7, I8, I9, I10, I11, I12, K1, K2, K3, K4, K5, K6, K7, K8, K9, K10, K11, K12, M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, O1, O2, O3, O4, O5, O6, O7, O8, O9, O10, O11, O12]

destination_well = [A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, B1, B2, B3, B4, B5, B6, B7, B8, B9, B10, B11, B12, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12, E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, F1, F2, F3, F4, F5, F6, F7, F8, F9, F10, F11, F12, G1, G2, G3, G4, G5, G6, G7, G8, G9, G10, G11, G12, H1, H2, H3, H4, H5, H6, H7, H8, H9, H10, H11, H12]

for i in range(len(a)):
    n = [0,0,0,0,0]
    n[0] = Plate1
    n[1] = source_well[i]
    n[2] = destPlate100
    n[3] = destination_well[i]
    n[6] = 20    #transfer volume
    adding_extractedDNA.append(n)

with open('ECHO_GibsonAssembly.csv', 'w', newline='') as g:
	extracted_DNA = csv.writer(g)
	extracted_DNA.writerow(["Source Plate Barcode", "Source Well", "Destination Plate Barcode", "Destination Well", "Transfer Volume"])
	extracted_DNA.writerows(adding_extractedDNA)

g.close()
