# Logistic Regression ile Tweet Duygu Analizi

Bu başlık altında inceleyecek olduğumuz konu öncelikle logistic regressiyon çalışma mekanızması ve logistic regression kullanarak tweeter da yazılmış bir yazının olumlu mu olumsuz bir cümle olduğunu sınıflandırma problemini ele alalım. Genel anlamda bakılacak olursa öncelikli olarak metini(text) vektör haline çevrilmesi ve vektör üzerinden duygu analizi yapılması gerekmektedir.

Bahsi geçen adımları ayrıntılar ile birlikte ele alalım.

<img src="logistic.png">

Resimden de anlaşılacağı üzere X girdileri bir tahmin fonksiyonundan geçerek bir tahmin değeri elde edilir. Daha sonda veri setimiz içerisinde var olan gerçek değerlerimiz yani Y değerleri ile tahmin değerleri Y_tahmin bir cost funksiyonuna tabi tutulur ve elde edilen değerler Q paramatere gönderilir ve en ideal seviyeye ulaşınca(loss(kayıp)) döngü sonlandırılır.

Bunu bir tweet üzerinden anlatacak olursak;
 Tweet: Bugün mutluyum çünkü NLP ögreniyorum.  "Temel amacımız burada bu tweetin pozitif düşünürsek "1" ile vektörize etmek olumsuz bir tweet olarak düşünürsek "0" ile vektörize etmektir."
 
 Daha basit düşünülecek olursa "X" girdilerimiz logistic regression algoritmasından geçerek bir output yani 1 veya 0 değeri döndürmesidir.
 
 X ===> Train Logistic Regression ===> Classification (0 veya 1) 
 
 İşlem adımlarını biraz daha detaylandırırsak metin halindeki tweet bilgisini kelimelere ayrırmamız gerekmektedir.
 
 <img src="vocabulary.png">
 
 Her bir tweet deki benzersiz kelimeleri alarak kendi kelime dağarcığımızı oluşturmamız gerekmektedir. Kelime dağarcığı(Vocabulary) benzersiz kelimeler olarak anlandırılır. Bunu temsilen de "V" harfi kullanılmaktadır.
 
 Tweet içerisindeki benzersiz kelimeler tespit edildikten sonra olumlu sınıf ve olumsuz sınıf olarak ikiye ayrılmalıdır. Sınıf ayrımı gerçekleştikten sonra her bir tweet içerisinde tekrar eden kelimeler toplanarak kelimenin yanına yazılır ki bu işleme frekans çıkarma denir.
 
 <img src="features.png">
 
 Frekansı belirlenen kelimeler özellik çıkarma işlemine tabi tutulur. Burada x(m) tweet özellik sayısını, "1" değeri bias değeri, freqs(w,1) olumlu kelimeler, freqs(w,0) olumsuz kelimeleri temsil etmektedir.
 
 Tüm bunlardan bahsettikten sonra Tweet üzerinde Duygu Analizi yapabilmek için sırasıyla şu adımlardan geçirilmelidir;
 
 1-) Stop words'ler ve noktalama işaretleri(punctuction) çıkarılır.
 
 2-) "@" ve url bilgileri çıkarılır.
 
 3-) Kelimelerin köküne inilir(stemming) ve metin içerisindeki kelimeler küçük harfe dönüştürülür.(lowercasing)
 
 Son olarak bu aşamalardan sonra Trainning ve Testing işlemlerine geçilir. Tüm algoritmalarda olduğu gibi Logistic Regression algoritmalarında temel amaç minimum maliyet fonksiyonu(cost) elde etmektir. Düşük cost ile birlikte yüksek accuracy(doğruluk) oranı elde edilmelidir. Doğruluk hesaplanır iken gerçek değerler ile,tahmin değerleri aynı olduğu sayı toplam değere bölünmesi ile elde edilir. 
 
 <img src="testing.png">
 
 
