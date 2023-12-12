import sqlite3
import time

con=sqlite3.connect("ögrenciler.db")
cursor=con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS ögrenciler (isim TEXT,soyad,numara INT)")

class Ögrenci():

    def __init__(self,isim,soyad,numara):
        self.isim=isim
        self.soyad=soyad
        self.numara=numara

    def __str__(self):
        return "İsim: {}\nSoyad: {}\nNumara: {}\n-------------------".format(self.isim,self.soyad,self.numara)


class Ögrenciler():

    def ögrenciekle(self):
        isim=input("İsim: ")
        soyad=input("Soyad: ")
        numara=input("Numara: ")
        print("Ekleniyor...")
        time.sleep(2)
        cursor.execute("INSERT INTO ögrenciler (isim,soyad,numara) VALUES(?,?,?)",[isim,soyad,numara])
        con.commit()
        print("Eklendi..")

    def ögrencisil(self,isim):
        cursor.execute("DELETE FROM ögrenciler WHERE isim=?",[isim])
        con.commit()

    def ögrencilerigöster(self):
        print("Sorgulanıyor...")
        time.sleep(2)
        print("---ÖGRENCİLER---")
        cursor.execute("SELECT * FROM ögrenciler")
        liste=cursor.fetchall()
        if(len(liste)==0):
            print("Listede öğrenci bulunmuyor...")
        else:
            for i in liste:
                ögrenci=Ögrenci(i[0],i[1],i[2])
                print(ögrenci)

    def numaralarıgöster(self):
        print("Sorgulanıyor....")
        time.sleep(2)
        print("---NUMARALAR---")
        cursor.execute("SELECT numara FROM ögrenciler")
        liste=cursor.fetchall()
        if(len(liste)==0):
            print("Listede numara yok...")
        else:
            for i in range(len(liste)):
                print(i,".nıncı indeksin verisi: ",liste[i])

    def isimlerigöster(self):
        print("---SADECE İSİMLER---")
        cursor.execute("SELECT isim FROM ögrenciler")
        liste=cursor.fetchall()
        if(len(liste)==0):
            print("Listede isim bulunmuyor...")
        else:
            for i in range(len(liste)):
                print(i,".nıncı indeksin verisi: ",liste[i])

    def toplamnumaralar(self):
        cursor.execute("SELECT * FROM ögrenciler")
        liste=cursor.fetchall()
        toplam=0
        for i in liste:
            toplam=toplam+i[2]
        print("--------------")
        print("Toplam: ",toplam)
        print("---------------")

    def ögrencisorgula(self,isim):
        cursor.execute("SELECT * FROM ögrenciler WHERE isim=?",[isim])
        liste=cursor.fetchall()
        if(len(liste)==0):
            print("Böyle bir ögrenci ismi yok...")
        else:
            ögrenci=Ögrenci(liste[0][0],liste[0][1],liste[0][2])
            print(ögrenci)

    def verilerigüncelle(self):
        cursor.execute("SELECT * FROM ögrenciler")
        data=cursor.fetchall()
        print("---İLK DEGERLER---")
        for i in data:
            print(i)

        print("--Güncellenicek satırı seçiniz--\n1- Ögrenci soyadı güncelle\t2-Numara güncelle")
        print("-------------------------------------------------------")
        satır = input("Cevap: ")
        print("----------------------------------------------------")
        if(satır=="1"):
            isim=input("Hangi ögrencinin soyadını güncelliceksiniz?: ")
            soyad=input("Yeni soyad: ")
            print("*Güncelleniyor...")
            time.sleep(2)
            cursor.execute("UPDATE ögrenciler SET soyad=? WHERE isim=?",[soyad,isim])
            cursor.execute("SELECT * FROM ögrenciler")
            data=cursor.fetchall()
            print("----*GÜNCEL HALİ*----")
            for i in data:
                print(i)
        elif(satır=="2"):
            isim=input("Hangi ögrencinin numarasını güncelliceksiniz?: ")
            numara=input("Yeni numara: ")
            print("*Günelleniyor...")
            time.sleep(2)
            cursor.execute("UPDATE ögrenciler SET numara=? WHERE isim=?",[numara,isim])
            cursor.execute("SELECT * FROM ögrenciler")
            data = cursor.fetchall()
            print("----*GÜNCEL HALİ*----")
            for i in data:
                print(i)
        else:
            print("Hatali secim")


        con.commit()









    def vtkapat(self):
        con.close()
