## # SORU 1 -> Python'da Veri Tiplerini araştırınız, her bir veri tipi için kendi cümlelerinizle açıklamalar yazınız.
# Yorum satırı kullanmak için # işareti kullanılır.
"""
çok satırlık
yorum için ise
3 tırnak
bu tırnakların arasına yazılabilir
3 tırnak
"""
a = 1907 # sayi (integer) tipinde değişken
b = 19.07 # float tipinde değişken
c = "Kodlama.io" # String (Metin) tipinde değişken
d = ["python","selenium","kursu"] # liste tipinde değişken
e = ("istanbul","büyükşehir","belediyesi") # demet(tuple) tipinde değişken
f = {"Istanbul", "Milano", "Viyana"} # küme(set) tipinde değişken
g= {
    "ulke":"Türkiye",
    "sehir":"Istanbul",
    "yas": 23
} # sözlük (dict) tipinde değişken (g) değişkeni
h = True #boolean tipinde değişken True ya da False olabilir.

kullaniciMail = "kodlamaio@gmail.com"
kullaniciSifre = "kodlama123456"

girisMail = input("Kullanıcı girişi yapmak için mail adresinizi giriniz: ")
girisSifre= input("Kullanıcı girişi yapmak için şifrenizi giriniz: ")


if kullaniciMail == girisMail and kullaniciSifre == girisSifre:
    print("Kullanıcı girişi başarıyla sonuçlandı.")
elif kullaniciMail == girisMail and kullaniciSifre !=girisSifre:
    print("Şifreniz hatalı.")
elif kullaniciMail != girisMail and kullaniciSifre == girisSifre:
    print("Mail Adresiniz hatalı")
else:
    print("Kullanıcı adı ve şifre hatalı lütfen tekrar deneyiniz.")

