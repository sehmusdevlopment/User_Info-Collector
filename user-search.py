ad=input("Adınız: ")
yas=int(input("yaşınız: "))
boy=float(input("Boyunuz  (örn: 1.75):"))
ogrenci_mi=input("öğrenci misiniz (E/H): ").strip().upper()== "E"
hobiler=[]
print("Lütfen 3 hobi giriniz: ")
for i in range(3):
    hobi=input(f"{i+1}. hobinizi girin: ")
    hobiler.append(hobi)

print("\n--- kullanıcı bilgileri ---")

print("ad: ",ad)
print("yas",yas)
print("boy",boy)
print("öğrenci mi?: ","evet"if ogrenci_mi else "hayır")
print("Hobiler:",",".join(hobiler))
print("\n--- Veri Türleri ---")
print("ad →", type(ad))
print("yas →", type(yas))
print("boy →", type(boy))
print("ogrenci_mi →", type(ogrenci_mi))
print("hobiler →", type(hobiler))