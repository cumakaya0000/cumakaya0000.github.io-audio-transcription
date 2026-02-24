# cumakaya0000.github.io-audio-transcription
Audio-transcription
<div style="max-width:1100px;margin:auto;padding:40px;font-family:Arial,Helvetica,sans-serif;background:#0b0b0e;color:#e6e6e6;line-height:1.7">

<h1 style="color:#cfcfcf;">🎙️ Video / Ses Dosyasından Otomatik Metin (Türkçe) – faster-whisper</h1>

<p>
Bu proje, video veya ses dosyalarının içindeki konuşmaları otomatik olarak yazıya dökmek
(transkript üretmek) için hazırlanmıştır.
Özellikle ders videoları, kayıtlar ve uzun anlatımlar için pratik bir çözümdür.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🧰 Neye ihtiyaç var?</h2>

<p>
Programın sorunsuz çalışabilmesi için aşağıdaki bileşenlerin tamamı gereklidir.
Her biri farklı bir işi üstlenir.
</p>

<h3 style="color:#cfcfcf;">Python</h3>

<p>
Program Python dili ile yazılmıştır.
Bilgisayarda Python kurulu değilse program çalışmaz.
</p>

<ul>
<li>Önerilen sürüm: Python 3.10 ve üzeri</li>
<li>Komut satırında <b>python</b> komutu çalışmalıdır</li>
</ul>

<h3 style="color:#cfcfcf;">FFmpeg</h3>

<p>
FFmpeg, video dosyasının içindeki sesi ayıklamak ve sesi modele uygun hale getirmek için
kullanılır.
MP4, MKV gibi video dosyaları için zorunludur.
</p>

<h3 style="color:#cfcfcf;">Python kütüphaneleri</h3>

<ul>
<li>faster-whisper → konuşma tanıma modeli</li>
<li>ffmpeg-python → Python üzerinden FFmpeg kullanımı</li>
</ul>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">⚙️ Kurulum</h2>

<h3 style="color:#cfcfcf;">1. Python kurulumu</h3>

<p>
Python indirme sayfası:
</p>

<a style="color:#9ad7ff" href="https://www.python.org/downloads/" target="_blank">
https://www.python.org/downloads/
</a>

<div style="background:#151518;border:1px solid #2a2a2a;padding:15px;border-radius:8px;margin-top:10px">
Kurulum sırasında mutlaka <b>Add Python to PATH</b> seçeneğini işaretleyin.
</div>

<p>Kurulumdan sonra kontrol:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
python --version
</pre>

<h3 style="color:#cfcfcf;">2. FFmpeg kurulumu</h3>

<a style="color:#9ad7ff" href="https://ffmpeg.org/download.html" target="_blank">
https://ffmpeg.org/download.html
</a>

<p>
Windows için en pratik yöntem:
hazır (static) sürümü indirip zipten çıkarmaktır.
</p>

<ol>
<li>Zip dosyası indirilir</li>
<li>Bir klasöre çıkartılır</li>
<li>İçindeki <b>bin</b> klasörü PATH’e eklenir</li>
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

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
pip install faster-whisper
pip install ffmpeg-python
</pre>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">▶️ Çalıştırma</h2>

<p>
Öncelikle <b>transkript.py</b> dosyanızın bulunduğu klasöre gidilmelidir.
</p>

<p>Örneğin dosya Masaüstündeyse:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
cd Desktop
</pre>

<p>Programı başlatmak için:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
python transkript.py
</pre>

<p>
Program çalışırken model indirilir, ses çözülür ve konuşmalar analiz edilir.
Uzun videolarda işlem süresi uzayabilir.
</p>

<p>İşlem bittiğinde:</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
Bitti. cikti.txt oluşturuldu.
</pre>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">📄 Çıktı</h2>

<p>
Program çalıştırılan klasöre otomatik olarak şu dosyayı üretir:
</p>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
cikti.txt
</pre>

<h3 style="color:#cfcfcf;">Dosya yapısı</h3>

<pre style="background:#151518;padding:12px;border-radius:8px;color:#e6e6e6">
[12.7-18.4] Merhaba arkadaşlar bugün derste...
</pre>

<p>
Her satırda konuşmanın başladığı ve bittiği saniye bilgisi bulunur.
Bu sayede videodaki ilgili bölüme hızlıca dönülebilir.
</p>

<h3 style="color:#cfcfcf;">Ne için kullanılabilir?</h3>

<ul>
<li>Ders notu hazırlamak</li>
<li>PDF / Word dökümanı üretmek</li>
<li>Video arşivlerinde metinle arama yapmak</li>
<li>Özetleme ve yapay zekâ analizleri için girdi üretmek</li>
</ul>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🔐 Gizlilik ve veri güvenliği</h2>

<p>
Bu proje tamamen yerel olarak çalışır.
</p>

<ul>
<li>Video veya ses dosyanız hiçbir sunucuya gönderilmez.</li>
<li>İşlem yalnızca kendi bilgisayarınızda yapılır.</li>
<li>Oluşturulan metin sadece sizin diskinizde oluşur.</li>
<li>Harici API, bulut servisi veya çevrim içi analiz yoktur.</li>
</ul>

<p>
Bu nedenle ders kayıtları, kişisel görüşmeler ve özel içerikler için
bulut tabanlı servislerden çok daha güvenlidir.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">🛠️ Olası hatalar ve sık karşılaşılan sorunlar</h2>

<h3 style="color:#cfcfcf;">python komutu bulunamıyor</h3>

<p>
Sebep:
Python PATH’e eklenmemiştir.
</p>

<h3 style="color:#cfcfcf;">ffmpeg bulunamadı hatası</h3>

<p>
Sebep:
FFmpeg bin klasörü PATH’e eklenmemiştir.
</p>

<h3 style="color:#cfcfcf;">Model çok yavaş çalışıyor</h3>

<p>
Sebep:
CPU ile çalışıldığı için normaldir.
Uzun videolarda işlem süresi artar.
</p>

<h3 style="color:#cfcfcf;">Dosya yolu hatası</h3>

<p>
Genellikle dosya adında boşluk olması veya yanlış klasörde çalıştırma
sebebiyle oluşur.
</p>

<hr style="border:1px solid #2a2a2a">

<h2 style="color:#cfcfcf;">📌 Proje amacı</h2>

<p>
Bu proje, ders videolarını otomatik olarak yazıya dökmek isteyen öğrenciler,
akademik çalışma yapanlar ve içerik üreticileri için
basit, ücretsiz ve yerel çalışan bir çözüm sunmayı amaçlar.
</p>

</div>
