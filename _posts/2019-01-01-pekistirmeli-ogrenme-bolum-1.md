---
layout: post
title:  "Pekiştirmeli Öğrenme - Bölüm 1: Giriş"
description: "Pekiştirmeli öğrenme, amaca yönelik ne yapılması gerektiğini öğrenen bir makine öğrenmesi yaklaşımıdır."
date:   2019-01-01
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme", ""]
permalink: /blog/:categories/:title
next-page-url: /blog/pekistirmeli-ogrenme/cok-kollu-haydutlar-bolum-2
---

## Pekiştirmeli Öğrenme

Pekiştirmeli öğrenme, amaca yönelik ne yapılması gerektiğini öğrenen bir makine öğrenmesi yaklaşımıdır. Pekiştirmeli öğrenmede ajan (agent) adı verilen öğrenen makinemiz karşılaştığı durumlara bir tepki verir ve bunun karşılığında da sayısal bir ödül sinyali alır. Ajan/öğrenen makine aldığı bu ödül puanını maksimuma çıkartmak için çalışır. Bu şekilde çalışan deneme yanılma yöntemi, pekiştirmeli öğrenmenin en ayırt edici özelliğidir.

Pekiştirmeli Öğrenme, Markov karar süreci denilen bir model kullanmaktadır. Markov karar süreçlerinin en önemli 3 özelliği; algılama (sensation), eylem (action) ve hedef (goal). Pekiştirmeli öğrenme yaklaşımı makine öğrenmesinin denetimli/danışmanlı öğrenme (supervised learning) ve denetimsiz/danışmansız öğrenme (unsupervised learning) yaklaşımlarından farklıdır.

* Denetimli öğrenme; etiketli bir veri yığınından eğitim ve test kümesi oluşturularak, eğitim kümesi üzerinden bir modelin oluşturulması, bu modelin performansının (öğrenme düzeyinin) test kümesi üzerinden incelenmesine dayalıdır. Bu sayede yeni gelen etiketsiz örnekler, model yardımıyla etiketleri tahmin edilebilir hale gelmektedir.
* Denetimsiz öğrenme, genellikle etiketlenmemiş verilerin koleksiyonlarında kümeleme yapmaya yöneliktir.

Pekiştirmeli Öğrenme sürecindeki en önemli zorluklar, keşif (exploration) ve sömürü (exploitation) kavramlarının uygulamaya geçirilmesidir. Ajanın daha fazla ödül elde etmesi için geçmişte denediği ve pozitif ödül aldığı eylemleri seçmelidir. Ajan ödül elde etmek için daha önce deneyimlediği eylemlerden yararlanır, ancak karşılaştığı bir durumda daha fazla ödül alabileceği eylemler varsa bunları da keşfetmelidir. Böylece ajan, çeşitli eylemler denemeli ve en iyi sonuç/ödül alabildiklerini aşamalı olarak desteklemelidir.

Tüm pekiştirmeli öğrenme ajanları açık hedeflere sahip olup çevrenin özelliklerini algılayabilir ve çevrelerini etkileyebilecek eylemleri seçebilirler. Ajan denildiği zaman bir organizma veya robot gibi bir varlık ifade edilmemektedir. Ajan, eylemi gerçekleştiren ve öğrenen etkendir.

Bir ajan daha büyük bir davranış sisteminin bir bileşeni olabilir. Pekiştirmeli öğrenmenin en önemli özelliklerinden birisi, diğer mühendislik disiplinleriyle olan etkileşimidir. Pekiştirmeli Öğrenme, psikoloji ve sinir-bilimi ile etkileşime girmiş ve her iki konuya da önemli faydalar sağlamıştır.

## Örnekler


* Satranç oyuncusu bir hamle kararı aldığında muhtemel hamleleri ve karşıt cevaplarını planlar. Belirli konumları ve hareketleri sezgisel yargılarla belirler.
* Bir mobil robot daha fazla çöp toplamak için yeni bir odaya girip girmeyeceğine karar verir. Bu karar, akünün mevcut şarj seviyesine ve geçmişte şarj cihazını ne kadar çabuk ve kolay bulabildiğine dayanır.
* Psikolojik açıdan bakıldığında, bir karar verme sürecinde kararları nasıl verdiğimiz ve bu kararların sonuçlarının öğrenmemizi sağlayıp sağlamadığının cevabını planlar.
* Nörobilim açısından, beyinde hangi bölgelerin yer aldığı ve bu bölgelerin birbirleriyle bağlantılarının neler olduğu sorularının cevabını planlar.


## Pekiştirmeli Öğrenme Ögeleri

Bir Pekiştirmeli Öğrenme sisteminde ajan ve çevre (environment) dışında biri opsiyonel olmak üzere dört unsur bulunur:

1. Politika (policy)
2. Ödül (reward signal)
3. Değer/Durum Değeri (value function)
4. Çevre modeli (model)

Politika; ajanın içinde bulunduğu durumda alabileceği aksiyonu belirler. Bir nevi etki-tepki eşleşmesi olarak düşünülebilir. İçinde bulunulan durum bir etki olarak kabul edilirse ajan buna karşılık bir tepki (action) verir. Bu politika basit bir aksiyon olarak tanımlanabileceği gibi bütün durumları karşılayan bir arama tablosu şeklinde de tanımlanabilir. Politika dinamik olarak da nitelenebilir. Bunun temel nedeni, ajanın içinde bulunduğu durumu değerlendirerek alabileceği aksiyonları aramasından (farkına varmasından) kaynaklanmaktadır.

Ödül; ajanının gerçekleştirmiş olduğu bir aksiyona karşılık çevreden aldığı puandır. Bir pekiştirmeli öğrenme ajanının amacı, uzun vadede aldığı ödülleri maksimum seviyeye ulaştırmaktır. Ödül alınan aksiyonun ne kadar iyi veya kötü olduğunu belirleyen değerdir (basit bir şekilde mutluluk veya acı ile eşleştirilebilir). Ajan, izlemiş olduğu politikayı bu ödülleri esas alarak zaman içerisinde değiştirir. Örneğin alınan bir aksiyonun sonrasında düşük bir puan elde ediliyorsa, gelecekte ajan aynı duruma geldiğinde farklı bir aksiyon almayı tercih edebilir.

Durum değeri; ajanın içinde bulunduğu durumdan ve o durumu takip eden diğer durumlardan bekleyebileceği ödüllerin toplamıdır. Ödüller anlık olarak neyin iyi neyin kötü olduğunu ifade ederken, durum değeri uzun vadede neyin iyi neyin kötü olduğunu ifade eder. Örneğin; bir durum, düşük bir ödüle fakat yüksek bir değere sahip olabilir. Bunun nedeni düşük ödül veren durumu takip eden yüksek ödüllü diğer durumlardır. Tam tersi de mümkündür. Yüksek ödül veren bir durumdan sonra sürekli olarak düşük ödüller veren durumlar da olabilir. Buradaki durum “ileri görüşlülük” gibi düşünülebilir.

Model, isteğe bağlı olarak sisteme dahil edilen bir unsurdur. Çevrenin bir simülasyonu olup ajanın bir aksiyonu gerçekleştirmeden önce bu aksiyon sonucunda alabileceği ödülü ve doğuracağı durumu tahmin etmesini sağlamaktadır. Bu sayede bir planlama yapılarak ajanın davranışında değişiklik meydana gelebilecektir.

## Kapsam ve Sınırlamalar

Pekiştirmeli Öğrenme, yoğun bir şekilde durum(state) kavramına dayanmaktadır. Politika ve değer fonksiyonunda girdi olarak kullanılırken; modelde ise hem girdi hem de çıktı olarak kullanılmaktadır.

## Örnek: Tic-Tac-Toe ve Pekiştirmeli Öğrenme Ögeleri

Tic-Tac-Toe, iki kişinin sırayla 3'e 3'lük bir masada, yatayda, dikeyde ve çaprazda aynı işareti tamamlaması ile kazanılır. Bir oyuncu X işaretlerken, diğeri O işaretler. Eğer üç işaret oyun sonunda tamamlanamamışsa oyun berabere biter. Bu oyunda iyi bir oyuncu hiç bir zaman kaybetmez. Bu çalışma için beraberliği de kaybetmeyi de eşit ölçüde kötü olarak düşünelim. Kazanma şansımızı nasıl artırabiliriz?

![Örnek Tic-Tac-Toe Oyunu]({{ site.url }}/assets/RL-sutton-ozet/sekil-11.png)

En iyi hamleyi yapma(minimaks) şansımız yok, çünkü karşımızdaki oyuncunun neyi seçeceği, stratejisi tam olarak bilinemez. Oyunun durumuna göre kaybedecek yolu da seçebilir. Minimaks iki tarafın da davranışının belli olduğu durumlarda kullanılabilir.

Bu gibi karar problemlerinde dinamik programlama gibi bir klasik optimizasyon metodu kullanılabilir ve optimize sonuç bulunabilir. Fakat bu kez karşı oyuncunun yapabileceği tüm hamleleri tanımlamak gerekecektir. Bu bilginin olmadığını varsayalım, ki genelde bu şekilde olacaktır. Fakat bu bilgiye deneyim ile ulaşılabilir. Oyun defalarca oynanarak, karşı oyuncunun davranışı belli bir seviyeye kadar modellenebilir. Bu model kullanılarak dinamik programlama ile optimize çözüm bulunabilir.

Politika burada, her durumda hangi aksiyonun alınması gerektiğini söyleyecektir. Her durum tanımı, 3'e 3'lük bir tahtada olabilecek tüm olasılıksal hamleleri kapsar. Her durum için karşı oyuncu ile bir kaç oyun oynanarak kazanma şansı hesaplanır. Daha sonra bir evrimsel bir optimizasyon algoritması ile bu politika iyileştirilir.

Değer fonksiyonu (Value function) ise, durumları işaret eden numaralardan oluşan bir tablo ile hazırlanır. Tablodaki duruma karşılık gelen değer yüksekse o durumda kazanma olasılığımız daha yüksek olacaktır. X’lerin (biz) kazandığı durumlara 1, 0'ların (karşı) kazandığı durumlara 0 ve diğer durumlara 0.5 değeri atanır ve oyun oynanmaya başlanır. Aksiyonlarımızı durumlardaki değerlere bakarak, çoğunlukla yüksek olanı seçeriz. Bazen rastgele seçimler yaparak “arayışa” çıkarız. Rastgele yapmadığımız bilinçli seçimlerde, geçiş yaptığımız değerle eski değer arasındaki değer farkını kullanarak, eski değeri güncelleriz. Buna zamansal fark öğrenimi(temporal difference learning) denilmektedir. Bu yöntem sabit bir karşı oyuncuyu, yani oynama şeklini değiştirmeyen, yahut çok yavaş değiştiren, mükemmel olmayan bir oyuncuyu yenecektir.

Politika için; oyun süresince herhangi bir kazanç alınmamaktadır. Oyun kazanılırsa tüm kararlar ödüllendirilir. Değer için oyun süresince her kazanç özgün olarak ödüllendirilir.

Pekiştirmeli Öğrenme, herhangi bir karşı oyuncu olmadan, yahut çekişmeli bir ortam olmadan da çalışabilir. Ödülün ne zaman geleceğinin belli olmadığı herhangi bir sürekli veya adım problemine uygulamak mümkündür.

Anlatılan çözüm yaklaşımı, yalnızca tic-tac-toe gibi durum uzayı küçük olan problemlerde değil, durum uzayı boyutu ~$10^{20}$ olan tavla gibi problemlere de uygulanabilir. Yapay sinir ağları ile entegre ederek tavla problemine Gerry Tesauro çözüm aramıştır. Durum sayısının çokluğundan kaynaklı olarak hepsini deneyimlemek olanaksızdır. Buna rağmen daha önce yazılan botlardan çok daha iyi başarılar elde edilmiştir. Yapay sinir ağı, kazanılan deneyimi genelleştirerek tüm durumlara olan ihtiyacı ortadan kaldırmıştır. Pekiştirmeli öğrenmede deneyimin genelleştirmesi gerekmektedir. Bu nedenle yapay sinir ağları, derin öğrenme gibi eğiticili öğrenme uygulamaları tasarlanabilecek olgulardan beslenmek çok önemlidir.