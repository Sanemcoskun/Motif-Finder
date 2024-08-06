from matplotlib import pyplot as plt

dna = 'ATGCGTACGTAGCTAATGGTCTGATCGTCGTACATGGTAGATGCTAGTCTCGTACATGGTAGCTATGAGTCTGATCGTATGCGTACGTATATGCGTCGTACGTGATGTACGTAGCTATGA'

motif = 'ATG'
positions = []
    
def find_motifs(dna,motif):
    for i in range(len(dna) - len(motif) + 1): # dizi indekslemesi 0 dan başlar
        if dna[i:i+len(motif)] == motif: # 0'dan 3'e kadar olan kısmı motife eşit mi
            positions.append(i) # eşitse indeksi ekle     
    return positions

print(find_motifs(dna,motif))

#figure yeni bir grafik çerçevesi oluşturur
#figsize çerçeve boyutunu belirler.(genişlik, yükseklik)
plt.figure(figsize=(12, 2))

plt.vlines(x = positions, ymin=0,ymax=100,colors='red')
plt.title('Motif Positions in DNA Sequence')
plt.xlabel('Position in sequence')
plt.ylabel('Motif Found')
plt.yticks([])
plt.xticks(positions)
plt.grid(True,axis='x',linestyle='--',color='gray',alpha=0.7)
plt.show()

