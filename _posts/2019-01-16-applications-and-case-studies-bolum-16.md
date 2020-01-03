---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 16: Applications and Case Studies"
description: " "
date:   2019-01-16
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/neuroscience-bolum-15
next-page-url: /blog/pekistirmeli-ogrenme/frontiers-bolum-17
---
__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.*__

## Uygulamalar ve Vaka Çalışmaları ( Applications and Case Studies)

Bu bölümde pekiştirmeli öğrenmenin birkaç vaka çalışmalarından bahsedilecektir. Bunlardan birkaçı ekonomik anlamda potansiyelin önemli uygulamalarıdır. Bu uygulamaların bazılarında kullanılan algoritmalar daha karmaşıktır.

Pekiştirmeli öğrenme uygulamaları halen rutin olmaktan uzaktır ve tipik olarak bilim kadar çok sanat gerektirir. Buna istinaden pekiştirmeli öğrenmedeki güncel araştırmaların hedeflerinden biri de daha kolay ve daha anlaşılır uygulamalar yapmaktır.

## Tavla Oynama

Gerald Tesauro tarafından oluşturulan tavla oyunu, pekiştirmeli öğrenmenin en etkileyici uygulamalarından biri olmuştur. Tesauro’nun uygulaması, biraz tavla bilgisini gerektiriyordu. Ardından uygulama tavlayı öğrendi ve dünyanın en güçlü büyük ustalarının seviyesine yakınlaştı.
Tavla oyunu, zamansal fark öğrenimi algoritmasının basit bir kombinasyonudur. Çok katmanlı yapay sinir ağları kullanılarak doğrusal olmayan fonksiyon yaklaşımları, algoritmanın geriye dönük hataları ile eğitilmiştir.
Tavla, dünya şampiyonası maçları ve sayısız turnuvalar ile dünyanın her yerinde oynanması anlamlı olan bir oyundur. 24 konumlu bir tahtada 15 siyah, 15 beyaz olmak 30 taş ile oynanmaktadır. Aşağıdaki şekilde beyaz oyuncu perspektifinden gösterildiği gibi oyunun başlangıcında tipik bir başlangıç pozisyonu belirlenir. Beyaz oyuncunun zarları yuvarlaması sonucu 5 ve 2 elde edilmiştir. Bu, beyaz oyuncunun taşlarından birini 5 adım ve birini de 2 adım taşıyabileceği anlamına gelmektedir. Taşıma tek taş üzerinden de gerçekleştirilebilir. Eğer ki beyaz taşın taşındığı yerde bir tane siyah taş varsa bu taş çıkarılır ve siyah oyuncunun attığı zardan 6 elde edilene kadar siyah oyuncu oyuna dahil müdahale edemez. 6 elde edildiğinde çıkarılan taş oyuna alınarak devam edilir. Beyaz oyuncu bu şekilde oynayarak taşları son çeyrek (19-24) bölgeye taşır. Devamında atılan zarlar boyunca son çeyrekteki taşlar dışarı çıkarılır. Aynı şekilde siyah oyuncu da beyaz oyuncuya ters istikamette oyununa devam eder. Bütün taşları çıkaran oyuncu oyunu kazanır.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C41C11916508AAA403C1CCB16CC091917CB21D0D09D0292BD29BAF36887C033E_1535397167647_ss.PNG)


Tavla oyunu zamansal fark öğrenimi algoritmasının doğrusal olmayan bir formunu kullanmıştır. Tahmini değer, v^(s,w), tahtanın pozisyonu (s)’ten başlayarak kazanma olasılığını kastetmektedir. Bunu başarmak için, oyunun kazanıldığı yerdeki ödüller dışında tüm ödüllerin sıfır olması gerekmektedir. Değer fonksiyonunu uygulamak için, tavla oyunu aşağıdaki gibi standart çok katmanlı bir yapay sinir ağı modeli kullanmaktadır.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C41C11916508AAA403C1CCB16CC091917CB21D0D09D0292BD29BAF36887C033E_1535397220821_sss.PNG)


Bu yapay sinir ağı modeli, giriş birimleri katmanı, gizli birimlerin katmanı ve son olarak çıkış birimlerinden oluşmaktadır. Ağa giriş tavla pozisyonunu temsil etmektedir. Çıkış ise pozisyon değerinin tahminini temsil etmektedir.

Bir tavla pozisyonunun temsili değeri verildiğinde ağ, standart bir şekilde tahmini değeri hesaplamaktadır. Her bağlantıya giriş değerinden gizli bir birim karşılık gelmektedir. Her giriş değerinden gelen sinyaller, karşılık gelen ağırlıklar ile çarpılmaktadır. Çarpımlar ise gizli birimde toplanmaktadır. Çıkış (h(j)) ve gizli birim (j) olmak üzere aşağıdaki formüldeki gibi ifade edilmektedir:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C41C11916508AAA403C1CCB16CC091917CB21D0D09D0292BD29BAF36887C033E_1535397255206_1.png)


Yukarıdaki formülde xi, i. giriş birimini ve wij, j. gizli katmanın bağlantısının ağırlığını temsil etmektedir. Bu sayede ağdaki tüm katmanların ağırlığı w parametresi ile ifade edilmektedir. Sigmoidin çıkışı her zaman 0 ile 1 arasında değişmektedir.

Tavla oyunu, zamansal fark öğrenimi algoritmasının geri yayılım formunu kullanmaktadır. Geri yayılım aşağıdaki formüldeki gibi ifade edilmektedir:


$$w_{t+1}\doteq w_t + \alpha [R_{t+1}+ \gamma \hat{v}(S_{t+1},w_t)- \hat{v}(S_t,w_t)]z_t$$
Bu formülde $$W_t$$, tüm değiştirilebilir parametre vektörü ve zt, uygunluk belirtileri (eligibility traces) vektörü olarak ifade edilmektedir. wt’nin her bir bileşeni;



$$z_t \doteq \gamma \lambda z_{t-1} + \bigtriangledown\hat{v} (S_t,w_t)$$



$$z_0 \doteq 0$$.
formülü ile güncellenmektedir.

Yukarıda bahsedilen bilgileri kullanarak öğrenme kuralını uygulamak için tavla oyunu kaynağı gerekmektedir. Tesauro, tavla oyununu kendi kendine oynayarak oyunların bitmeyen dizisini elde etmiştir. Tavla oyunu hareketleri seçmek için, zar atışının ve ortaya çıkacak sonuçların karşılık geleceği pozisyonların her 20 ya da daha fazla yolu oynayabileceğini düşünmektedir. Değerlerin karşılık geldiği her tahmin, ağa danışılmaktadır. Daha sonra en yüksek tahmini değer ile elde edilen pozisyon seçilmektedir. Bu şekilde devam ederek tavla oyununun hamleleri ile her iki tarafın da çok sayıda tavla oyunu üretmesi sağlanmaktadır.

## Samuel'in Dama Oyuncusu

Samuel, göreceli sadeliği daha güçlü bir şekilde odaklanabilmek için satranç yerine dama oyununu seçmiştir. Oyunda mevcut pozisyondan en iyi hamle yapabilmek için Shannon’un minimax teoremi temel alınmıştır. Bu teoremde arama ağacından geriye doğru gittikçe her konum en iyi hamle sonucunu verecek şekilde pozisyonun puanını dikkate alarak makinede skoru bir üst seviyeye taşımak amaçlanmıştır. Aynı zamanda bu oyunu seçmesinin bir sebebi de oyundaki iyi ve kötü hamlelerin not edilmesiyle iyi ve kötü hamle ayrımını yapmaktır.

Samuel, iki ana öğrenme yöntemi kullanmıştır. Bunlardan biri ezbelenmiş öğrenme(rote learning) olup en basit öğrenme yöntemidir. Diğer öğrenme metodu ise genelleme ile öğrenme(learning by generalization) metodur. Samuel’in bu metotları tavlada kullanılan kavramlarla aynıdır.

Program kendisinin başka bir versiyonuna karşı birçok oyun oynadı ve her hareketinden sonra bir güncelleme gerçekleştirildi. Aşağıdaki diyagramda her açık renkli daire programın bulunduğu konumu temsil etmektedir. Her hareket halinde konumun değerinde güncelleme yapılmaktadır. Her iki tarafa da hareket ettirilerek ikinci bir hareket ettirme pozisyonu elde edilmektedir. Böylece genel olarak gerçek olayların tam hareketi üzerinde bir yedekleme oluşur ve sonrasında diyagramdaki gibi olası olaylar gerçekleşir.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C41C11916508AAA403C1CCB16CC091917CB21D0D09D0292BD29BAF36887C033E_1535572511430_image.png)



## Bellek Kontrolünü Optimize Etme

Çoğu bilgisayar düşük maliyeti ve yüksek kapasitesi nedeniyle ana bellek olarak dinamik rastgele erişim belleği(DRAM) kullanmaktadır. Bir bellek denetleyicisi dinamik olarak değişimle uğraşmak zorundadır. Özellikle de aynı DRAM’i paylaşan çok çekirdekli modern işlemcilerde zorlu bir programlama problemidir.

DRAM’e erişmek zaman kısıtlayıcılarına göre yapılması gereken bir dizi adım içermektedir. DRAM sistemleri, her biri birden fazla DRAM yongasından oluşur. Satır ve sütun halinde düzenlenmiş çoklu hücre dizinleri içermektedir. Burada her hücre, kapasitör üzerindeki yükü paylaşarak tutmaktadır. Hücrelerin yenilenmesi durumu DRAM’in dinamik olmasının nedeni açıklanmaktadır.

Aşağıdaki şekil, pekiştirmeli öğrenme hafıza denetleyicisinin üst düzey bir görünümüdür. Zamanlayıcı, pekiştirmeli öğrenme ajanıdır. Zamanlayıcının çevresi, işlem sırasının özelliklerini temsil etmektedir ve eylemleri ise DRAM sistemine birer komuttur.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_C41C11916508AAA403C1CCB16CC091917CB21D0D09D0292BD29BAF36887C033E_1535655586457_11.PNG)

## İnsan-Seviye Video Oyunu Oynama


Google DeepMind’deki bir grup araştırmacı etkileyici bir derin çok katlı yapay sinir ağlarının özellik tasarım sürecini otomatik hale getirme üzerinde çalıştı. Pekiştirmeli öğrenmede çok katlı yapay sinir ağları işlev yaklaşımı için kullanılmaktadır. Pekiştirmeli öğrenmenin geri yayılım ile birleştirmesiyle çarpıcı sonuçlar elde edilmiştir.

Mnih ve arkadaşları derin Q ağı (DQN) olarak adlandırılan bir derin öğrenme aracı geliştirmişlerdir. Çok katmanlı veya derin bir kıvrımlı YSA ile birleştiren görüntüler gibi verilerin mekansal dizilerini işlemek için uzman YSA ile Q öğrenmenin birleştirilmesiyle elde edilmiştir. Bunu göstermek için DQN’in bir oyun emilatörü ile etkileşime girerek 49 farklı Atari 2600 video oyununu oynamayı öğrenmesini sağlamışlardır. DQN, 49 oyunun her biri için farklı bir politika öğrendi. Fakat aynı ham girdiyi, ağ mimarisini ve parametre değerlerini (adım boyutu, indirim oranı ve tüm oyunlar için bir çok uygulama) kullandı. DQN, bu oyunların büyük bir kısmında insan seviyesinde ya da ötesinde oyun seviyeleri elde etti. Her ne kadar oyunlar aynı video görüntü akışlarını izleyerek oynamış olsa da diğer yönlerden de geniş ölçüde farklılık göstermektedirler.

## Go Oyununa Hakim Olma

Eski Çin oyunu olan Go, yıllardır yapay zeka araştırmacılarına meydan okumaktadır. Diğer oyunlardaki insan seviyesinde beceri veya insan üstü beceriye sahip olan yöntemler Go programını üretmede başarılı olamamıştır. Go programcıları topluluğu ve uluslararası yarışmalar sayesinde, Go oyununun seviyesi yıllar boyunca önemli ölçüde gelişmiştir.

DeepMind’de bulunan bir ekip derinlemesine yapay sinir ağları, denetimli öğrenme, Monte Carlo arama ağacı ve pekiştirmeli öğrenmeyi birleştirerek bu engeli ortadan kaldıran AlphaGo oyununu geliştirmiştir.

# AlphaGo

AlphaGo’yu böylesine güçlü yapan ana yenilik, hem bir politika hem de pekiştirmeli öğrenme tarafından öğrenilen bir değer fonksiyonu tarafından yönlendirilen yeni bir MCTS sürümü ile hareketleri seçmesiydi. Bu hareketleri derin kıvrımlı yapay sinir ağları tarafından oluşturulan fonksiyon yaklaşımları yardımıyla seçimi desteklemiştir. Diğer bir önemli özellik ise ağların rastgele ağırlıklarından başlayarak pekiştirmeli öğrenme yerine, daha önce insan hareketlerinden oluşan geniş bir koleksiyondan önceki denetimli öğrenmenin sonucu olan ağırlıklardan başlamış olmasıdır.

# AlphaGo Zero

AlphaGo ile deneyim elde eden DeepMind ekibi, AlphaGo Zero geliştirdi. AphaGo’nun aksine, bu program oyunun temel kurallarının ötesinde hiçbir insan verisi kullanmamıştır. Sadece kendi kendine oynayan pekiştirmeli öğrenmeden, Go tahtasındaki taşların konum girdilerinden öğrenilmiştir.

## Kişiselleştirilmiş Web Servisleri

Haber makalelerinin veya reklamların yayınlanması gibi web servislerinin kişiselleştirilmesi, kullanıcıların web sitesiyle ilgili memnuniyetini artırmak amaçlıdır. Bir politika, söz konusu kullanıcıların, çevrimiçi etkinlik geçmişlerinden çıkarılan ilgi alanlarına ve tercihlerine göre her bir kullanıcı için en iyi olduğu düşünülen içeriği önermektedir. Bu, makine öğrenimi ve özellikle de pekiştirmeli öğrenme için önemli bir alandır. Bir pekiştirmeli öğrenme sistemi, kullanıcının geri bildirimlerine yanıt olarak ayarlamalar yaparak öneri politikası geliştirmektedir. Kullanıcılardan geri bildirim etmenin bir yolu, web sitesi memnuniyet anketleri yapmaktır. Bu sayede gerçek zamanlı olarak geri bildirim alınmaktadır.


## İdeal Sıcaklık

Kuşlar ve planörler, uçuşlarını sürdürebilmek için küçük veya sıfır enerji harcayarak yukarı doğru hava akımlarından yararlanmaktadırlar. Bu davranış termal yükseliş olarak adlandırılmakta olup yükselen hava akımını mümkün olduğunca uzun süre kullanarak ince ve çevresel uyarılara cevap vermeyi gerektiren karmaşık bir beceridir. Reddy, Celani, Sejnowski ve Vergassola, yükselen hava akımlarına eşlik eden güçlü atmosferik türbülansta etkili olan termal yükselen politikalarını araştırmak için pekiştirmeli öğrenmeyi kullanmışlardır. Ana hedefleri ise kuşların algılarına duydukları anlayışı ve etkileyici termal yükselişini sağlamak için onları nasıl kullandıklarını anlamaktı.

