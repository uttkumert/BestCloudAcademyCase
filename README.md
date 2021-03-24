# BestCloudAcademyCase

1) İlk görevdeki API’yi geliştirmek için öncelikle Python için Flask kurulumu yaptım. Daha sonrasında @app.route fonksiyonu itle /whoami uzantısına JSON formatında isim ve soyismi içeren çıktıyı ekledim.

2) İkinci aşamada ise /alert uzantısını Webhook’a bağladım (Webhook Unique URL: https://webhook.site/26ea7387-4afc-4c0b-ace9-3e429f161b8a) ve post request olarak düzenledim. Ve post request attığımda Webhook’da şöyle bir çıktı aldım.

<img width="1440" alt="SS1" src="https://user-images.githubusercontent.com/60819292/112382093-79520e00-8cfc-11eb-87d1-4c46e3371183.png">


3) Üçüncü aşamada ise önce bilgisayarıma Docker kurdum ve bir Docker üyeliği oluşturdum. Daha sonrasında ise bir Dockerfile oluşturarak içerisine şu komutları ekledim.

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", “run"]


4) Daha sonrasında docker build işlemlerini yaptım ve Docker'da şöyle sonuçlar aldım.


<img width="1362" alt="SS4" src="https://user-images.githubusercontent.com/60819292/112382213-a1da0800-8cfc-11eb-9489-7e20569da9e1.png">


<img width="1362" alt="SS5" src="https://user-images.githubusercontent.com/60819292/112382238-aacad980-8cfc-11eb-9281-dc0c46f18ae3.png">



5) Terminalde yazdığım docker images ve docker ps işlemleri sonucu da aşağıdaki çıktıları aldım.

<img width="996" alt="SS6" src="https://user-images.githubusercontent.com/60819292/112382293-bddda980-8cfc-11eb-9f4d-fa3c57a2d325.png">

<img width="1040" alt="SS7" src="https://user-images.githubusercontent.com/60819292/112382355-cd5cf280-8cfc-11eb-9129-f54b26610501.png">



6) Tüm bu işlemler sonucunda üçüncü görevde istenildiği gibi yaptıklarımı bir Jenkins Pipeline’a bağlamak istedim bunu için Jenkins’i terminalden indirdim ve işlemde başarılı olamadım daha sonrasında ise jenkins.war dosyasını indirdim. Ve bu dosyayı Java ile çalıştırmayı denediğimde aşağıdaki gibi bir uyarı aldım.

<img width="1040" alt="SS8" src="https://user-images.githubusercontent.com/60819292/112382412-dd74d200-8cfc-11eb-83bf-b4e72bf50d64.png">


Bilgisayarımdaki Java sürümü yüksek olduğu için bu hatayı aldığımı anladım. Jenkins ile izlediğim tüm videolarda bağlantıyı localhost:8080 üzerinden yapıldığını gördüm fakat hiçbir browser üzerinden buraya ulaşamadığım için 3. görevi yerine getiremedim.
