# BestCloudAcademyCase

1) İlk görevdeki API’yi geliştirmek için öncelikle Python için Flask kurulumu yaptım. Daha sonrasında @app.route fonksiyonu itle /whoami uzantısına JSON formatında isim ve soyismi içeren çıktıyı ekledim.

2) İkinci aşamada ise /alert uzantısını Webhook’a bağladım (Webhook Unique URL: https://webhook.site/26ea7387-4afc-4c0b-ace9-3e429f161b8a) ve post request olarak düzenledim. Ve post request attığımda Webhook’da şöyle bir çıktı aldım.

![] (/Users/utkumert/Desktop/SS1.png)

3) Üçüncü aşamada ise önce bilgisayarıma Docker kurdum ve bir Docker üyeliği oluşturdum. Daha sonrasında ise bir Dockerfile oluşturarak içerisine şu komutları ekledim.

FROM python:3.8-slim-buster
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", “run"]

4) Daha sonrasında docker build işlemlerini yaptım ve Docker'da şöyle sonuçlar aldım.

![] (/Users/utkumert/Desktop/SS2.png)
![] (/Users/utkumert/Desktop/SS3.png)
![] (/Users/utkumert/Desktop/SS4.png)
![] (/Users/utkumert/Desktop/SS5.png)

5) Terminalde yazdığım docker images ve docker ps işlemleri sonucu da aşağıdaki çıktıları aldım.

![] (/Users/utkumert/Desktop/SS6.png)
![] (/Users/utkumert/Desktop/SS7.png)

6) Tüm bu işlemler sonucunda üçüncü görevde istenildiği gibi yaptıklarımı bir Jenkins Pipeline’a bağlamak istedim bunu için Jenkins’i terminalden indirdim ve işlemde başarılı olamadım daha sonrasında ise jenkins.war dosyasını indirdim. Ve bu dosyayı Java ile çalıştırmayı denediğimde aşağıdaki gibi bir uyarı aldım.

![] (/Users/utkumert/Desktop/SS8.png)

Bilgisayarımdaki Java sürümü yüksek olduğu için bu hatayı aldığımı anladım. Jenkins ile izlediğim tüm videolarda bağlantıyı localhost:8080 üzerinden yapıldığını gördüm fakat hiçbir browser üzerinden buraya ulaşamadığım için 3. Görevi yerine getiremedim.
