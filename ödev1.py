import math

# Noktaların listesini tanımlayın (örnek noktalar)
noktalar = [(1, 2), (4, 6), (5, 1), (2, 3)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def oklidMesafesi(nokta1, nokta2):
    return math.sqrt((nokta2[0] - nokta1[0])**2 + (nokta2[1] - nokta1[1])**2)

# Mesafeleri saklamak için liste
mesafeler = []

# Her nokta çifti arasındaki mesafeleri hesaplayın
for i in range(len(noktalar)):
    for j in range(i + 1, len(noktalar)):
        mesafe = oklidMesafesi(noktalar[i], noktalar[j])
        mesafeler.append(mesafe)

# Minimum mesafeyi bulun ve yazdırın
min_mesafe = min(mesafeler)
print(f"Minimum Öklid mesafesi: {min_mesafe}")
