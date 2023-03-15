"""Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

Bu öğrenci kayıt sistemine;

Aldığı isim soy isim ile listeye öğrenci ekleyen
Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
Listeye birden fazla öğrenci eklemeyi mümkün kılan
Listedeki tüm öğrencileri tek tek ekrana yazdıran
Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir."""

ogrenciListesi =[]
print(ogrenciListesi)

# Listeye Öğrenci Eklemek
def ogrenciEkle(isim, soyisim):
    ogrenci = isim + " " + soyisim
    ogrenciListesi.append(ogrenci)
    print(ogrenci, "eklendi.")

# Listeden Öğrenci Silmek
def ogrenciSil(isim, soyisim):
    sil = isim + " " + soyisim
    if sil in ogrenciListesi:
        ogrenciListesi.remove(sil)
        print(sil, "silindi.")
    else:
        print(sil, "bulunamadi.")

# Listeye Çoklu Öğrenci Eklemek
def cokOgrenciEkle(*ogrenciler):
    for ogrenci in ogrenciler:
        ogrenciListesi.append(ogrenci)
        print(ogrenci, "eklendi.")

# Öğrencileri Ekrana Yazdırmak
def ekranaYazdir():
    for i in ogrenciListesi:
        print("Ogrenci: ", i)

# İndeks Numarasını Yazdırmak
def indexNo(ad_soyad):
    return ogrenciListesi.index(ad_soyad)

# Listeden Çoklu Silme Yapmak
def cokluSil(isim_soyisim):
    for ogrenci in isim_soyisim:
        ogrenciListesi.remove(ogrenci)

"""sayi = int(input("Kaç öğrencinin kaydı silinecek ?: "))
ogrenci = 0
def cokluSil(isim_soyisim):
    while ogrenci <= sayi:
            ogrenciListesi.remove(sayi)"""

ogrenciEkle("Selim","Melih")
print(ogrenciListesi)
ogrenciEkle("Ahmet", "Mithat")
print(ogrenciListesi)
ogrenciSil("Selim","Melpoih")
print(ogrenciListesi)
cokOgrenciEkle("Selim Turhan", "Melih Turhan")
print(ogrenciListesi)
ekranaYazdir()
print("Girilen ismin listedeki indeks değeri: ", indexNo("Selim Turhan"))
cokluSil(["Selim Melih", "Ahmet Mithat"])
print(ogrenciListesi)
