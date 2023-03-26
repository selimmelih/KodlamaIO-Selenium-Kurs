# HTML Nedir?

"""
Hiper Metin İşaretleme Dili(HTML) web sayfalarını oluşturmak için kullanılan standart metin işaretleme dilidir.
Dilin son sürümü HTML5'tir. HTML, bir programlama dili olarak tanımlanamaz.
Zira HTML kodlarıyla kendi başına çalışan bir program yazılamaz.
"""

# HTML Locators Nedir ?

"""
Locators(Konumlandırıcı), Selenium IDE'ye hangi web tabanlı objeler üzerinde çalışması gerektiğini söyleyen bir komuttur.
Doğru elementin tanımlanması, otomasyon oluşturmanın ön koşuludur.

En yaygın locator çeşitleri;
ID
Name
ClassName
TagName
LinkText
CssSelector
Web sitelerinde tagname’ler bulunur.
Bu tagname’lerin sahip olduğu stil, name, id gibi attribute’ler vardır.
Selenium’un anlayacağı şekilde nesneleri web elementlere çevirirken ilk önce id’si ve name’i var mı?
diye bakılır yok ise CssSelector ve Xpath ile nesneyi bulmaya çalışırız.
"""

# Selenium'da Aksiyonlar
"""
#.click() -> O an selector neredeyse oraya tıklama işlemi yapar.
#.sendKeys()-> send keys ile kutucuğa yazı yazma/aratma işlemlerini yaparız
#.findElement(By, by) -> Alanları bulmak için findElement (By, by) kullanırız
# .get() -> Bağlanmak istediğimiz websitesine erişmek için kullanılır.
# .maximize_window() -> Açılan sayfayı tam ekran görüntülememize yarar.
#webdriver.Chrome(ChromeDriverManager().install()) -> Google Chrome üzerinde çalışmamızı sağlar
"""