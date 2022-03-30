# Logistic Regression ile Tweet Duygu Analizi

Bu başlık altında inceleyecek olduğumuz konu öncelikle logistic regressiyon çalışma mekanızması ve logistic regression kullanarak tweeter da yazılmış bir yazının olumlu mu olumsuz bir cümle olduğunu sınıflandırma problemini ele alalım. Genel anlamda bakılacak olursa öncelikli olarak metini(text) vektör haline çevrilmesi ve vektör üzerinden duygu analizi yapılması gerekmektedir.

Bahsi geçen adımları ayrıntılar ile birlikte ele alalım.

<img src="logistic.png">

Resimden de anlaşılacağı üzere X girdileri bir tahmin fonksiyonundan geçerek bir tahmin değeri elde edilir. Daha sonda veri setimiz içerisinde var olan gerçek değerlerimiz yani Y değerleri ile tahmin değerleri Y_tahmin bir cost funksiyonuna tabi tutulur ve elde edilen değerler Q paramatere gönderilir ve en ideal seviyeye ulaşınca(loss(kayıp)) döngü sonlandırılır.

Bunu bir tweet üzerinden anlatacak olursak;
 Tweet: Bugün mutluyum çünkü NLP ögreniyorum.  "Temel amacımız burada bu tweetin pozitif düşünürsek "1" ile vektörize etmek olumsuz bir tweet olarak düşünürsek "0" ile vektörize etmektir."
 
 Daha basit düşünülecek olursa "X" girdilerimiz logistic regression algoritmasından geçerek bir output yani 1 veya 0 değeri döndürmesidir.
 
 X ===> Train Logistic Regression ===> Classification (0 veya 1) 
 
 İşlem adımlarını biraz daha detaylandırırsak 
