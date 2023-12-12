from ögrenciler import *

print("""--------------------
                **ÖGRENCİ EKRANI**
    ->İşlemler:
1-Ögrencileri göster
2-Ögrenci ekle
3-Ögrenci sil
4-Numaraları ve Toplamlarını göster
5-Ögrenci isimlerini göster
6-Ögrenci sorgula
7-Verileri güncelle
---------------------""")

ögr=Ögrenciler()

while True:
    islem=input("Ögr Ekran Secim: ")
    if(islem=="q"):
        print("Çıkıs yapılıyor...")
        time.sleep(2)
        print("Çıkıs yapıldı..")
        break
    elif(islem=="1"):
        ögr.ögrencilerigöster()
    elif(islem=="2"):
        ögr.ögrenciekle()
    elif(islem=="3"):
        isim=input("Silinecek isim: ")
        print("Siliniyor...")
        time.sleep(2)
        ögr.ögrencisil(isim)
        print("*Silindi..")
    elif(islem=="4"):
        ögr.numaralarıgöster()
        ögr.toplamnumaralar()
    elif(islem=="5"):
        ögr.isimlerigöster()
    elif(islem=="6"):
        isim=input("İsim sorgula: ")
        print("Sorgulanıyor...")
        time.sleep(2)
        print("---ÖGRENCİ BİLGİLERİ---")
        print("------------------------")
        ögr.ögrencisorgula(isim)
    elif(islem=="7"):
        ögr.verilerigüncelle()
    else:
        print("HATALİ SECIM")