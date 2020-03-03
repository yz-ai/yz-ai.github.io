---
layout: post
author: "Fatih Çağatay Akyön"
title:  "Yüz Sahteciliğini Önleme (Face Anti-Spoofing) Hakkında Bilmeniz Gerekenler"
description: "Yüz sahteciliğini önleme araştırma alanıyla ilgili; önemli terimler ve metrikler, saldırı türleri, uygulama alanları, en güncel çalışmaların özeti ve halka açık verisetlerini öğrenin."
date:   2019-02-27
categories: yuz-tanima
tags: ["yuz-tanima"]
permalink: /blog/:categories/yuz-sahteciligini-onleme

## Ne hakkında konuşacağız

Biyometrik tanımlama, en eski kişi doğrulama tekniklerinden biridir. Parolalar ve anahtarlar casusluk yoluyla elde edilebilir, çalınabilir, unutulabilir veya taklit edilebilir.  Ancak kişinin kendisinin benzersiz özelliklerini taklit etmek ve kaybetmek çok daha zordur. Bu özellikler; parmak izleri, ses, retinanın damarlarının şekli ve daha fazlası olabilir.

Ancak tahmin ettiğiniz üzere biyometrik sistemleri de kandırmaya çalışanlar var. İşte bu makalenin konusu da: Saldırganlar başka bir kişiyi taklit ederek yüz tanıma sistemlerinden nasıl kaçınmaya çalışıyor ve bu nasıl tespit edilebilir!

**Bu makaleyi okuduktan sonra neler hakkında bilgi sahibi olacaksınız:**

 - Yüz tanıma (face recognition) ve yüz sahteciliği (face spoofing) arasındaki ilişki
 - Yüz sahteciliği önleme (face anti-spoofing) alanında kullanılan temel terimler ve metrikler  
 - Yüz sahteciliği saldırı türleri  
 - Yüz sahteciliğini önleme yöntemlerinin uygulama alanları  
 - Seçilen akademik yüz sahteciliğini önleme makalelerinin kilit noktaları
 - Yüz sahteciliği veri kümelerindeki geçerli mevcut durum

## Yüz tanıma teknolojisinden yüz sahteciliğine
Günümüzün yüz tanıma sistemleri muazzam bir doğruluk göstermektedir. Büyük veri setlerinin ve karmaşık mimarilerin ortaya çıkmasıyla, **0.000001'e (milyonda bir hata!) kadar yüz tanıma doğruluğu** elde etmek mümkün hale geldi ve artık mobil platformlara aktarma için uygunlar. Bu yüz tanıma sistemlerinin günlük kullanımının yaygınlaşmasına tek engel; onların zayıf taraflarıydı.

Teknik gerçekliğimizde başka bir kişiyi taklit etmek için en sık  kullanılan yöntem maskelerdir. Örneğin, aşağıdaki resimde olduğu gibi siyahi bir maske takarak bir bankayı soyun:

![](https://miro.medium.com/max/1170/0*-AA1QJl_qiwtADqu)
Yüz tanıma sistemlerini kandırmanın en iyi yolu kişinin kendi yüzü yerine başka birinin yüzünü sunmasıdır. Maskeler; yazıcıdan çıktısı alınan başkasına ait yüzün fotoğrafından, ısıtmalı çok karmaşık üç boyutlu maskelere kadar tamamen farklı kalitede olabilir, ayrı bir sayfa veya ekran şeklinde de sunulabilir, kişinin başına da takılabilir.

Samsung'daki **Iris tarayıcısı** ve iPhone X'teki  **Face ID** sistemini aldatma girişimi ile birlikte, yüz sahteciliği konusuna olan ilgi de artmaya başladı. Aşağıdaki şekilde, Vietnam güvenlik şirketi olan Bkav'ın, **Face ID'yi aşmak için kullandığı maske**yi görüyorsunuz. Maske, silikon burun, 3 boyutlu yazıcıdan çıkarılmış parçalar ve 2 boyutlu fotoğraflardan oluşuyor. Detaylı bilgiye [bu videodan da](https://www.youtube.com/watch?v=kSwzTqM3t_0) ulaşabilirsiniz.

![](https://miro.medium.com/max/692/0*AdUio17zq30vgfvz)

Bu tür güvenlik açıklarının varlığı, bir saldırganın nüfuz etmesinin önemli kayıplara yol açabilecği bankacılık veya şehir güvenlik sistemlerinde otomatik yüz doğrulama sistemlerinin kullanımını tehlikeye sokmaktadır.

## Terminoloji
Kimlik/yüz sahteciliğini önleme araştırma alanı oldukça yenidir ve hâlâ herkes tarafından geçerli ortak bir terminolojiyle sahip olduğu söylenemez. Yine de önemli terimleri elimden geldiğince Türkçe'ye çevirmeye çalışacağım:

**Kimlik sahteciliği saldırısı (Spoofing-attack):** Kimlik sistemini sahte bir biyometrik parametre (bu durumda, bir kişi veya kişinin yüzü) sunarak aldatma girişimi.

**Kimlik sahteciliğini önleme (Anti-spoof):** Bu tür aldatmacalara karşı koymak için bir dizi koruyucu önlem. Bir tanımlama sisteminin konveyörüne yerleştirilmiş çeşitli teknolojiler ve algoritmalar şeklinde uygulanabilir.

**Sunum saldırısı (Presentation attack):** Sistemin kullanıcıyı yanlış tanımlamasını veya tanımlanmasını engellemesini sağlayabilmek için; bir resim, kaydedilmiş bir video vb. gösterilmesi.

**Normal (Bona Fide):** Sistemin olağan giriş / davranışına, yani bir saldırı OLMAYAN her şeye karşılık gelir.

**Sunum saldırı aracı (Presentation attack instrument):** Bir saldırı aracı, örneğin vücudun yapay olarak yapılmış bir parçası.

**Sunum saldırısı algılama (Presentation attack detection):** Bu tür saldırıları otomatik olarak tespit etme yolları.

**HTER metriği (Toplam-Toplam Hata Oranı - toplam hatanın yarısı):** Kimlik sahteciliğini önleme sisteminin kalitesini belirlemek için kullanılır. Yetkisiz bir kişinin yanlış doğrulama sayısının (FAR - Yanlış Kabul Oranı) ve yetkili bir kişinin kaçırılan doğrulama sayısının (FRR - Yanlış Reddetme Oranı) ikiye bölünmesiyle hesaplanır:  
  
HTER = (FAR+ FRR) / 2  
  
Biyometrik sistemlerde, bir saldırganın sisteme girmesini önlemek için mümkün olan her şeyi yapmak için genellikle en büyük dikkat FAR'a gösterilmektedir ve bu konuda iyi ilerleme keydedilmiştir. Bunun dez avantajı, FRR'deki kaçınılmaz artıştır - yanlışlıkla davetsiz misafir olarak sınıflandırılan dürüst kullanıcıların sayısı.

> Arka arkaya onuncu kimlik reddinden sonra duvara fırlatılan telefon sayısını azaltmak istiyorsanız, FRR'ye dikkat etmelisiniz.

**EER metriği (Eşit Hata Oranı):** ROC eğrisindeki FAR ve FRR'nin aynı olduğu nokta, yani ROC eğrisinin x + y = 1 çizgisiyle kesiştiği noktadaki FAR (X ekseni) değeri.

![](https://miro.medium.com/max/461/0*H_fQ7328n0Osniwq)
## Saldırı türleri
Artık saldırganların tanıma sistemini nasıl kandırdığı örnek resimlerle inceleyebiliriz.

Hile yapmanın en popüler yolu maskelerdir. Başka bir kişinin maskesini takıp yüzünüzü bir tanımlama sistemine sunmaktan daha bariz bir saldırı yöntemi yoktur (genellikle **maske saldırısı (mask spoofing)** olarak adlandırılır).

![](https://miro.medium.com/max/1331/0*tOsrXX4cyVhZQfK7)
Ayrıca kendinizin veya bir başkasının fotoğrafını bir kağıda yazdırabilir ve kameraya tutabilirsiniz **(basılı saldırı (printed attack)** olarak adlandırılır).

![](https://miro.medium.com/max/1331/0*4-itmVi3nGyYBtO2)
**Tekrar saldırısı (replay attack)** biraz daha karmaşıktır. Kameraya, daha önce başka bir kişinin kaydedilmiş bir videosunun oynatıldığı bir cihazın ekranı gösterilir. Yöntemin karmaşıklığı, pratikteki kullanımını azaltıyor gibi anlaşılmasın, çünkü bu tarz saldırıların önleme sistemini geçme ihtimali çok daha yüksektir. Çünkü mevcut yüz tanıma sistemleri, sahtekarlık tespiti yaparken genellikle zaman dizilerinin analizine dayanan işaretleri kullanır, örneğin göz açıp kapatmayı, başın mikro hareketlerini, yüz ifadelerinin varlığını, nefes almayı takip eder. Tüm bunlar, video ile kolayca tekrar edilebilir.

![](https://miro.medium.com/max/1331/0*wVUjhL3Jbi3KdOgZ)
## Uygulama alanları
Yüz tanıma uygulanan her yerde sahteciliğe karşı önlemler alınması gerekir. Yüz sahteciliği ve kimlik sahtekarlıkları aşağıdaki konularla ilişkilidir ancak bunlarla sınırlı değildir:

 -  Dijital bankacılık
-   ATM'lerdeki kimlik doğrulamaları
-   Adli soruşturmalar
-   Çevrimiçi mülakatlar/sınavlar
-   Perakende suçları
-   Okul gözetimi
-   Kolluk kuvvetleri
-   Casino güvenliği

## Geleneksel sahteciliği önleme teknikleri
Kamera önünde videodan tekrar oynatılan veya çıktısı alınmış yüz görüntüleri, fotoğrafın/videonun kalitesindeki deformasyon özniteliklerinden tespit edilebilir. Muhtemelen, gözle bile olsa, bazı yerel desenler bile görüntüde tespit edilecektir. Bu, örneğin, çerçeveden tespit edilen yüzün farklı alanları için **yerel ikili kalıpları (Local binary patterns, LBP)** hesaplanarak yapılabilir. LBP, bu çizim ile özetlenebilir:

![](https://miro.medium.com/max/667/0*Tm4fIdyQ_UrtR28Y)

Görüntü analizine dayalı yüz sahteciliğini önleme algoritmalarının öncüsü olarak düşünülebilen, LBP tabanlı sahtekarlık önleme algoritmasının (2012) blok şeması:

![](https://miro.medium.com/max/1336/0*XSyLx6JUcuZUGxC2)
Verilen algoritmada, görüntüdeki her bir piksel için LBP hesaplanırken, komşularının sekizi sırayla alınır ve değerleri karşılaştırılır. Değer merkezi pikselden daha büyükse bir, küçükse sıfır olarak atanir. Böylece, her piksel için 8 bitlik bir dizi elde edilir. Elde edilen sekanslara dayanarak, **SVM sınıflandırıcısı**nına girdi olarak verilen **piksel histogram ı (a per-pixel histogram)** oluşturulur.

Bu yontemin HTER değeri %15 kadardır ve saldırganların önemli bir kısmının çok çaba sarf etmeden güvenlik sistemini gecebildigi anlamına gelir, ancak tehditlerin %85 oranında elendiğine dikkat edilmelidir. Algoritma, 50 katılımcının 1200 kısa videosundan ve üç tür saldırıdan (basılı saldırı, mobil saldırı, yüksek çözünürlüklü saldırı) oluşan IDIAP Replay-Attack veri kümesinde test edildi.

## Derin öğrenme temelli sahteciliği önleme teknikleri

Bir noktadan sonra, derin öğrenmeye geçişin olgunlaştığı belli oldu. Ön yargıyla yaklaşılan “derin öğrenme devrimi”, yüz sehteciliğiyle karşı karşıya kaldı.

2017 yılında yapılan bir çalışmada, sahtecilik tespiti için **yama ve derinlik tahminine dayalı bir sinir ağı** önerildi:

![](https://miro.medium.com/max/1600/0*lH7rb1Nvzn-AMlXw)
İlk olarak, girdi görüntüsünde yüz algılanır. Bu yüz, sinir ağı tabanlı model içeren 2 dala girdi olarak verilir. İlk dal, tespit edilen yüz bölgesinden yamalar (patches) çıkarır ve her bir yama için bir sahtelik puanı tahmin eder. İkinci dal, **derinliğe dayalı bir CNN modeli** ile onun ucuna bağlanmış bir **öznitelik çıkarıcıdan** oluşur. Burada, yüzün derinlik haritası tahmin edilir ve sonrasında çıkarılan derinlik öznitelikleri, ikili sahte / gerçek tahmini yapan SVM tabanlı bir sınıflandırıcıya girdi olarak verilir. Önerilen tüm modellerin / sınıflandırıcıların ayrı ayrı eğitildiği unutulmamalıdır (ortak bir kayıp fonksiyonu ile uçtan uca eğitim yoktur). Yöntem CASIA-FASD MSU-USSA ve Replay-Attack veri kümelerinde sırasıyla 2.27, 0.21 ve 0.72 HTER degerlerini elde etti.

2018'de yapılan bir çalışmada, sahte yüz tespiti için 3 boyutlu CNN tabanlı ağ önerilmiştir:

![](https://miro.medium.com/max/878/0*_cbQtljMshVrLqYi)
Bu çalışmada, **3 boyutlu evrişimsel sinir ağı katmanları**, **zaman serisi görüntü çerçevelerinden öznitelik çıkarmak için** kullanılır. Kayıp fonksiyonu olarak, **çapraz entropi (cross-entropy)** ve **maksimum ortalama tutarsızlık (maximum mean discrepancy)** hatasının kombinasyonu kullanılmaktadır. Bu yöntem Idiap veri kümesinde 1.2 HTER elde etti.

2019 yılında yapılan bir çalışmada ise, sıfır atış yüz sahteciliği önleme (zero shot face anti-spoofing) problemi için derin bir ağaç modeli (deep tree model) önerilmiştir. Ağaç yapısı ve birimleri aşağıda görülebilir:

![](https://miro.medium.com/max/1304/0*d0YVDDma61ccsb0M)![](https://miro.medium.com/max/572/0*davXRx4dYMq2nMrP)

Ayrıca, mevcut en fazla sayıda sahtecilik (spoof) türüne (12 sahtecilik türü) sahip bir sahtecilik veri kümesi (SiW-M veri kümesinde) yayımladılar. **Kayıp fonksiyonları; 2 denetimli** (gerçek/ sahte yüz kategorizasyonu için ikili çapraz entropi (binary cross entropy) ile maske için ortalama fark (mean error)) **ve 2 denetimsiz** (daha büyük PCA tabanını (larger PCA basis) teşvik eden bir yönlendirme kaybı (routing loss) ile alt grupların verimli şekilde eğitilememesi durumlarda dengesizlik yönlendirme (imbalance routing) sorununun üstesinden gelen bir benzersiz kayıp (unique loss)) **terimden oluşmaktadır**. Yöntem, SiW-M veri kümesinde 16.1 EER elde etti (2019 itibariyle en iyisi).

## Veriyi ezberlemek çözüm değil
Neyse ki, halka açık birçok sahtecilik önleme veri kümesi var. CASIA, Idiap, Replay-Attack ve daha fazlası… Mevcut bazı veri kümelerinde en iyi performans gösteren yöntemlere bir göz atalım:
![](https://miro.medium.com/max/525/0*ut3WMow-aSd3JpSS)![](https://miro.medium.com/max/1055/0*dqccOAA4XmdHGG_D)![](https://miro.medium.com/max/541/0*Bk-T0cRMW559ouyK)![enter image description here](https://miro.medium.com/max/1397/0*ogY-pv4cgCYllzcj)
Tablolarda görülebileceği gibi, yüz sahtecilik önleme sorunu veri **kümelerini tekil olarak düşündüğümüzde** çözülmüş gibi görünmektedir. Bununla birlikte, sinir ağını bir veri setinde eğitmeye ve başka bir veri kümesine test etmeye çalışırsanız, sonuçların o kadar da iyimser çıkmadığını göreceksiniz.

Patel’in 2016 makalesinde sunulan sonuçlar, yeterince karmaşık bir sinir ağı yapısı üzerinde, göz kırpma/doku gibi güvenilir öznitelikler kullanılsa bile, bilinmeyen veri kümelerindeki sonuçların **tatmin edici olmayacağını** göstermektedir:


![](https://miro.medium.com/max/1140/0*iWJTe_Hh-bCaWcvv)![](https://miro.medium.com/max/833/0*l0ymLjDPVg79q5wv)
Yukarıdaki tabloda USSA veri seti eğitilen modelin Replay-Attack ve FASD veri kümeleri üzerindeki test sonuçları görülebilir. Veri kümeleri yeterli çeşitliliğe sahip olmadığından, **bir veri kümesinde eğitilmiş modeller diğer kümeler üzerinde genelleme yeteneğine sahip olamıyor**.

## Son sözler

 - Yüz tanıma için kullanılan hemen hemen tüm teknolojiler yüz sahteciliğine karşı da kullanılabilmektedir. **Yüz tanıma için geliştirilen her şey, şu ya da bu şekilde, saldırı analizi için bir kullanım buldu**.
 - Yüz tanıma ve yüz sahtecilini önleme alanlarinin gelişme dereceleri arasında açık bir dengesizlik vardır. Tanıma teknolojileri koruma sistemlerinden önemli ölçüde öndedir. **Ayrıca, yüz tanıma sistemlerinin pratik kullanımını engelleyen en önemli etken, güvenilir koruma sistemlerinin olmamasıdır**. Literatürde neredeyse tüm ilgi özellikle yüz tanımaya kaydı ve saldırı tespit sistemlerinin literetürü bu sebepten dolayı daha geride kaldı.
 - **Mevcut veri kümeleri doygunluğa ulaştı.** On temel veri kümesinden beşinde sıfır hataya ulaşıldı. Bu, sahtecilik önleme alanında büyük ilerleme kaydedildiğini ancak genelleme yeteneğinin geliştirilmesine olanak sağlanamadığını gösterir. Yeni verilere ve yeni deneylere ihtiyacımız var.
 - Konuya artan ilgi ve büyük oyuncular tarafından tanıtılan yüz tanıma teknolojileriyle, **iddialı ekipler için “fırsat pencereleri” ortaya çıktı**, çünkü mimari düzeyde yeni bir çözüme fazlaca ihtiyaç var.

## Referanslar
> "Bu çalışma, Fatih Çağatay Akyön tarafından kaleme alınan https://medium.com/codable/face-anti-spoofing-starter-kit-f248ed195a3c Medium makalesinin Türkçe çevirisidir."
1.  Souza, L., Oliveira, L., Pamplona, M., & Papa, J. (2018). How far did we get in face spoofing detection?. _Engineering Applications of Artificial Intelligence_, _72_, 368–381.
2.  Chingovska, I., Anjos, A., & Marcel, S. (2012, September). On the effectiveness of local binary patterns in face anti-spoofing. In _2012 BIOSIG-proceedings of the international conference of biometrics special interest group (BIOSIG)_ (pp. 1–7). IEEE.
3.  Atoum, Y., Liu, Y., Jourabloo, A., & Liu, X. (2017, October). Face anti-spoofing using patch and depth-based CNNs. In _2017 IEEE International Joint Conference on Biometrics (IJCB)_ (pp. 319–328). IEEE.
4.  Li, H., He, P., Wang, S., Rocha, A., Jiang, X., & Kot, A. C. (2018). Learning generalized deep feature representation for face anti-spoofing. _IEEE Transactions on Information Forensics and Security_, _13_(10), 2639–2652.
5.  Liu, Y., Stehouwer, J., Jourabloo, A., & Liu, X. (2019). Deep tree learning for zero-shot face anti-spoofing. In _Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition_ (pp. 4680–4689).
6.  Patel, K., Han, H., & Jain, A. K. (2016, October). Cross-database face antispoofing with robust feature representation. In _Chinese Conference on Biometric Recognition_ (pp. 611–619). Springer, Cham.

