<div style="max-width:1100px;margin:auto;padding:40px;font-family:Arial,Helvetica,sans-serif;background:#0b0b0e;color:#e6e6e6;line-height:1.7">

<h1 style="color:#cfcfcf;">🎙️ Video / Ses Dosyasından Otomatik Metin (Türkçe) – faster-whisper</h1>

<p>
Bu proje, bilgisayarınızdaki bir video veya ses dosyasının içindeki konuşmaları
otomatik olarak yazıya dökmek için hazırlanmıştır.
Herhangi bir internet servisine dosya göndermeden, tamamen kendi bilgisayarınızda çalışır.
</p>

<p>
Özellikle:
ders kayıtları, konferans videoları, çevrim içi dersler ve uzun anlatımlar için uygundur.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🧰 Neye ihtiyaç var?</h2>

<p>
Bu programın çalışabilmesi için bilgisayarınızda aşağıdaki yazılımlar bulunmalıdır.
Her biri farklı bir görevi yerine getirir.
</p>

<h3 style="color:#cfcfcf;">Python</h3>

<p>
Programın kendisi Python dili ile yazılmıştır.
Python kurulu değilse program çalışmaz.
</p>

<ul>
<li>Önerilen sürüm: Python 3.10 veya üzeri</li>
<li>Komut satırında <b>python</b> komutu çalışmalıdır</li>
</ul>

<p>
Python yalnızca programı çalıştırmak için kullanılır.
Kod bilgisi zorunlu değildir.
</p>

<h3 style="color:#cfcfcf;">FFmpeg</h3>

<p>
FFmpeg, video dosyalarının içinden sesi çıkarmak ve
ses dosyasını uygun formata dönüştürmek için kullanılan yardımcı bir araçtır.
</p>

<p>
Eğer yalnızca <b>wav / mp3</b> gibi hazır ses dosyaları kullanıyorsanız
FFmpeg zorunlu değildir.
Ancak video (mp4, mkv, mov vb.) kullanacaksanız gereklidir.
</p>

<h3 style="color:#cfcfcf;">Python kütüphaneleri</h3>

<ul>
<li><b>faster-whisper</b> → konuşma tanıma modeli</li>
<li><b>ffmpeg-python</b> → Python üzerinden FFmpeg kullanımı</li>
</ul>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">⚙️ Kurulum</h2>

<h3 style="color:#cfcfcf;">1. Python kurulumu</h3>

<p>Python indirme sayfası:</p>

<a style="color:#9ad7ff" href="https://www.python.org/downloads/" target="_blank">
https://www.python.org/downloads/
</a>

<div style="background:#151518;border:1px solid #2a2a2a;padding:15px;border-radius:8px;margin-top:10px">
Kurulum ekranında mutlaka <b>Add Python to PATH</b> kutucuğunu işaretleyin.
</div>

<p>Kurulumdan sonra kontrol etmek için:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
python --version
</pre>

<p>
Eğer sürüm bilgisi görünüyorsa Python kurulumu tamamdır.
</p>

<h3 style="color:#cfcfcf;">2. FFmpeg kurulumu</h3>

<a style="color:#9ad7ff" href="https://ffmpeg.org/download.html" target="_blank">
https://ffmpeg.org/download.html
</a>

<p>
Windows için en pratik yöntem hazır (static) sürümü indirip zip dosyasından çıkarmaktır.
</p>

<ol>
<li>Zip dosyası indirilir</li>
<li>Bilgisayarda bir klasöre çıkartılır (örnek: C:\ffmpeg)</li>
<li>İçindeki <b>bin</b> klasörü Windows PATH değişkenine eklenir</li>
</ol>

<h4 style="color:#cfcfcf;">📷 Görsel ekleme alanları</h4>

<div style="border:2px dashed #666;padding:25px;border-radius:8px;color:#aaa;margin-bottom:10px">
FFmpeg indirme sayfası ekran görüntüsü
</div>

<div style="border:2px dashed #666;padding:25px;border-radius:8px;color:#aaa;margin-bottom:10px">
ffmpeg.exe bulunan bin klasörü
</div>

<div style="border:2px dashed #666;padding:25px;border-radius:8px;color:#aaa;margin-bottom:10px">
Windows ortam değişkenleri (PATH) ekranı
</div>

<p>Kurulumdan sonra kontrol:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
ffmpeg -version
</pre>

<h3 style="color:#cfcfcf;">3. Python kütüphaneleri</h3>

<p>
Komut istemcisi veya PowerShell açılır ve şu komutlar çalıştırılır:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
pip install faster-whisper
pip install ffmpeg-python
</pre>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">📂 Projeyi indirme</h2>

<p>
Bu projeyi kullanmak için GitHub sayfasından proje klasörünü bilgisayarınıza indirmeniz gerekir.
</p>

<p>
GitHub sayfasında:
<b>Code → Download ZIP</b> seçeneği ile indirin ve zipten çıkartın.
</p>

<p>
Çıkarttığınız klasörün içinde <b>transkript.py</b> dosyası bulunmalıdır.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">▶️ Çalıştırma</h2>

<p>
Öncelikle komut satırı açılır.
(Windows’ta Başlat menüsünden “PowerShell” yazmanız yeterlidir.)
</p>

<p>
Ardından <b>transkript.py</b> dosyasının bulunduğu klasöre gidilir.
</p>

<p>
Örnek: dosya Masaüstündeyse</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
cd $env:USERPROFILE\Desktop
</pre>

<p>
Programı başlatmak için:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
python transkript.py
</pre>

<p>
Program çalışırken:
</p>

<ul>
<li>Model ilk seferde otomatik olarak indirilir</li>
<li>Ses çözümleme işlemi başlar</li>
<li>Ekrana parça parça metinler yazdırılır</li>
</ul>

<p>
Uzun videolarda bu işlem birkaç dakika sürebilir.
</p>

<p>
İşlem tamamlandığında ekranda şu mesaj görülür:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
Bitti. cikti.txt oluşturuldu.
</pre>

<h3 style="color:#cfcfcf;">Giriş dosyasını değiştirme</h3>

<p>
Programın hangi ses dosyasını okuyacağı
<b>transkript.py</b> dosyası içindeki şu satırdan belirlenir:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
r"C:\Users\...\ses.wav"
</pre>

<p>
Kendi dosya yolunuzu buraya yazmanız yeterlidir.
</p>

<p>
Örnek:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
r"D:\videolar\ders1.wav"
</pre>

<p>
Dosyayı kaydettikten sonra program tekrar çalıştırılır.
</p>

<h3 style="color:#cfcfcf;">Programı tekrar çalıştırmak</h3>

<p>
Her yeni dosya için sadece şu iki komutu tekrar çalıştırmanız yeterlidir:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
cd dosyanin_bulundugu_klasor
python transkript.py
</pre>

<p>
Programı çalışırken durdurmak için:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
Ctrl + C
</pre>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">📄 Çıktı</h2>

<p>
Program çalıştırıldığı klasöre otomatik olarak şu dosyayı üretir:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
cikti.txt
</pre>

<h3 style="color:#cfcfcf;">Dosya yapısı</h3>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
[12.7-18.4] Merhaba arkadaşlar bugün derste...
</pre>

<p>
Köşeli parantez içindeki değerler:
konuşmanın videodaki başlangıç ve bitiş saniyeleridir.
</p>

<p>
Bu sayede video üzerinde ilgili bölüme çok hızlı şekilde geri dönülebilir.
</p>

<h3 style="color:#cfcfcf;">Ne için kullanılabilir?</h3>

<ul>
<li>Ders notu çıkarmak</li>
<li>Video arşivlerinden metinle arama yapmak</li>
<li>Özetleme ve yapay zekâ analizleri için ham veri üretmek</li>
<li>Alt yazı hazırlamak</li>
<li>Akademik çalışmalar için metin tabanı oluşturmak</li>
</ul>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🔐 Gizlilik ve veri güvenliği</h2>

<p>
Bu proje tamamen yerel olarak çalışır.
</p>

<ul>
<li>Ses ve video dosyalarınız hiçbir sunucuya gönderilmez.</li>
<li>Herhangi bir bulut servisi veya harici API kullanılmaz.</li>
<li>İşlem yalnızca sizin bilgisayarınızda yapılır.</li>
<li>Model dosyaları yalnızca bir kere indirilir ve bilgisayarınızda saklanır.</li>
</ul>

<p>
Bu yapı sayesinde:
</p>

<ul>
<li>ders kayıtları</li>
<li>özel konuşmalar</li>
<li>kişisel veriler</li>
</ul>

<p>
üçüncü kişilerle paylaşılmaz.
Bu proje çevrim dışı çalışabilecek şekilde tasarlanmıştır.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🛠️ Olası hatalar ve sık karşılaşılan sorunlar</h2>

<h3 style="color:#cfcfcf;">python komutu bulunamıyor</h3>

<p>
Sebep:
Python PATH değişkenine eklenmemiştir.
</p>

<h3 style="color:#cfcfcf;">ffmpeg bulunamadı</h3>

<p>
Sebep:
FFmpeg’in bin klasörü PATH’e eklenmemiştir.
</p>

<h3 style="color:#cfcfcf;">Dosya yolu bulunamadı</h3>

<p>
Genellikle:
</p>

<ul>
<li>dosya yolu yanlış yazılmıştır</li>
<li>dosya adı değiştirilmiştir</li>
<li>klasör adı hatalıdır</li>
</ul>

<h3 style="color:#cfcfcf;">Program çok yavaş çalışıyor</h3>

<p>
CPU ile çalışıldığı için normaldir.
Uzun videolarda işlem süresi doğal olarak uzar.
</p>

<h3 style="color:#cfcfcf;">İlk çalıştırmada uzun bekleme</h3>

<p>
İlk çalıştırmada konuşma modeli indirildiği için
başlangıç süresi daha uzun olabilir.
Sonraki çalıştırmalarda bu süre kısalır.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">📌 Proje amacı</h2>

<p>
Bu proje, öğrenciler, akademisyenler ve içerik üreticileri için
ücretsiz, yerel çalışan ve kurulumu kolay bir
Türkçe konuşma tanıma aracı sunmayı amaçlar.
</p>

</div>
