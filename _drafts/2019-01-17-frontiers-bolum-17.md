---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 17: Frontiers"
description: "Bu çalışma, Richard Sutton ve Andrew Barto tarafından kaleme alınan RL: An introduction (Sutton, R. S., & Barto, A. G. 2018) kitabının çeviri ve özetini barındırmaktadır."
date:   2019-01-17
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/applications-and-case-studies-bolum-16

---
__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.*__

## Frontiers


Bu son bölümde, bu kitabın kapsamının dışında kalan ancak pekiştirmeli öğrenmenin(RL) geleceği için önemli gördüğümüz konulara değineceğiz.

## 17.1 Genel Değer Fonksiyonları ve Yardımcı Görevler(General Value Functions and Auxiliary Tasks)

Uzun vadeli ödül dışındaki sinyalleri kontrol ve tahmin etmek neden yararlı olabilir ? Bunlar ana görev olan ödülü, maksimize etmeye yardımcı olan görevlerdir. Bir cevap olarak,  çeşitli sinyalleri tahmin ve kontrol etmek güçlü bir çevresel(environment) model oluşturabilir. Bu cevabı daha anlaşılabilir kılmak için birkaç konsepti daha anlamamız gerek. Bu yüzden bunu bir sonraki bölüme erteliyoruz. İlk olarak farklı tahminlerin çokluğu RL ajanına nasıl fayda sağlar buna bakalım.

Yardımcı görevlerin ana göreve yardımcı olabilmesi için ana görevde bulunan bazı temsillere ihtiyaç duyabilir. Bazı yardımcı görevler daha basit olabilir. Eğer basit yardımcı görevlerin iyi özellikleri erkenden bulunabilirse, bu özellikler ana görevin öğrenme hızını arttırabilir.

Bir yapay sinir ağı(ANN) düşünelim. Son katmanını her biri farklı bir görev üzerinde çalışan bölümlere/kafalara ayıralım. Bir bölüm yaklaşık değer fonksiyonunu üretebilir diğerleri de yardımcı görevler için çözüm üretebilir. Araştırmacılar, piksel değerlerindeki değişim, bir sonraki zaman adımında alacağım ödülü tahmin etmek gibi yardımcı görevler üzerinde denediler. Çoğu durumda ana görevin öğrenilmesini hızlandırdığı görüldü(Jaderberg et al., 2017)

Son olarak, yardımcı görevlerin belkide en önemli rolü bu kitap boyunca yaptığımız durumun temsilinin(state representation) sabit olduğu ve ajana verildiği varsayımının ötesine gidiyor. Bu rolü açıklamak için, birkaç adım geriye gidelim ve bu varsayımın büyüklüğünü ve onu kaldırmanın etkilerine bakalım.

## 17.4 Ödül Sinyallerini Tasarlamak(Designing Reward Signals)

Ödül sinyallerini tasarlamaktan bahsederken, ajana her $$t$$ anında $$R_t$$ ödülünü hesaplayan ve ajana gönderen ortamın parçasını tasarlamaktan bahsediyoruz.

Basit ve kolayca tanımlanabilen bir amaç(goal) olsa da, seyrek ödül(sparse reward) problemi genellikle ortaya çıkar. Ajanın amacına bir kez ulaşması için sıklıkla sıfır olmayan ödül sinyalleri vermek, birçok başlangıç koşulundan verimli bir şekilde tek başına öğrenmesi, zorlu bir görev olabilir. Amaca doğru ilerlemeyi işaret eden sinyaller seyrek olabilir, çünkü ilerlemenin tespit edilmesi zor hatta imkansızdır. Ajan uzun süreler boyunca amaçsızca dolaşabilir(Minsky buna "plateau problem" demişti,1961).

Pratikte, ödül sinyalinin tasarlanması, genellikle kabul edilebilir sonuçlar üreten gayri resmi bir deneme-yanılma ile yapılır. Eğer ajan öğrenmede başarısız olursa, çok yavaş öğrenirse, veya yanlış şeyi öğrenirse, tasarlayan kişi ödül sinyalini ayarlar ve tekrardan dener.

Ödülü tasarlayan kişinin ajanı ödüllendirirken ana amaca yardımcı olduğunu düşündüğü bazı alt görevleri(subgoal) de ödüllendirmesi seyrek ödül(sparse reward) problemine çözüm önerilerinden biri olabilir. Ancak bu iyi niyetli ek ödüller, ajanın istenilenden farklı davranmasına neden olabilir; bu da ajanın genel amacını başaramamasıyla sonuçlanabilir. Daha iyi bir yöntem olarak, ödül sinyalini yalnız bırakıp değer-fonksiyonu tahminini(value-function approximation*) sonuçta ne olması gerektiği gibi bir ilk tahmin ile başlatabiliriz. Gerçek optimum değer fonksiyonunun($$v_*$$) ilk tahmini olarak $$v_0 : S \rightarrow R$$ başlattığımızı düşünelim.

$$\hat{v}(s, w) \doteq {W^T x(s)} + v_0(s)$$

Yukarıdaki denklemde ilk ağırlık vektörünü($$W$$) 0 ile başlatırsak, değer fonksiyonunun ilk değeri $$v_0$$ olur. Bu ilklendirme, $$v_0$$'ın keyfi bütün formları için yapılabilir, ancak her zaman eğitimi hızlandırmayı garanti etmez.

Ya ödüllerin ne olduğu hakkında bir bilgimiz yoksa ancak ortamda başka bir ajan(agent) var ise? Davranışları gözlemlenebilen, belki de çalıştığımız görevde uzman olan bir insan? Bu durumda "imitation learning" olarak bilinen metodları kullanabiliriz. Buradaki fikir, uzman ajandan yararlanırken ondan daha iyi performans gösterme olasılığını açık bırakmak. Uzman ajanın davranışından öğrenmek, denetimli öğrenme yoluyla veya ters pekiştirmeli öğrenme(inverse reinforcement learning) olarak bilinen, ödül sinyalini çıkarmak ve sonradan politikayı(policy) öğrenmek için bu sinyali kullanan pekiştirmeli öğrenme algoritması ile gerçekleştirilebilir.


## 17.5 Kalan Problemler(Remaining issues)

Bu bölümde, ileride yapılacak araştırmalarda ele alınması gereken altı konuyu vurgulayacağız.

İlk olarak, tamamen artan ve çevrimiçi(online) ayarlarda iyi çalışan, güçlü parametrik fonksiyon yaklaşım yöntemlerine ihtiyacımız var. Derin öğrenme ve yapay sinir ağları(ANN) bu yönde büyük bir adım ancak sadece büyük eğitim kümelerinde toplu(batch) eğitim ile iyi çalışıyor. 

İkinci olarak, daha sonraki öğrenmenin genelleşmesi için, özellikleri(features) öğrenen iyi metodlara ihtiyacımız var. Bu konu, genel olarak "representation learning", "constructive induction", ve "meta-learning" olarak adlandırılan genel bir problemin örneğidir. Tecrübeyi, yalnızca istenilen fonksiyonu öğrenmek için değil de gelecekteki öğrenmeyi daha iyi genelleştiren, ve böylece daha hızlı çalışacak şekilde nasıl kullanabiliriz? Bu problem 1950'ler ve 1960'lardaki yapay zeka ve örüntü tanımanın kökenine uzanan eski bir problemdir. Böyle bir aralık bir duraksama vermeli. Belki de çözümü yoktur. Ancak bir çözüm bulma ve etkinliğini gösterme zamanının henüz ortaya çıkmadığı da eşit derecede muhtemeldir.

Üçüncü olarak, öğrenilmiş çevre modelleriyle planlama için ölçeklenebilir(scalable) yöntemlere ihtiyacımız var. Planlama yöntemlerinin AlphaGo Zero ve satranç gibi oyunun kurallarından dolayı ortamın tamamen bilindiği veya tasarımcılar tarafından sağlanabildiği oyunlarda son derece etkili olduğu kanıtlandı. Ancak ortam modelinin veriden öğrenildiği ve planlama için kullanıldığı örnekler çok nadir.

Dördüncü olarak, ajanın çalıştığı ve yetkinliğini geliştirdiği görevlerin otomatik olarak seçilmesi gelecekteki araştırmalar tarafından ele alınması gereken bir konu. Ajanın hangi görevlerde uzmanlaşması gerektiğini ajanın kendisinin karar vermesini istiyoruz. Bunlar çoktan bilinen genel görevin alt görevleri olabilir.

Beşinci olarak gelecekteki araştırmalar tarafından ele alınması gereken konu, merağın, analog hesabı ile davranış ve öğrenmenin etkileşimi. Bu bölümde off-policy yöntemler kullanılarak birçok görevin aynı anda öğrenildiği bir sistem hayal ediyoruz. Alınanan eylemler tabiki bu sistemi etkileyecek, bu da öğrenmenin ne kadar gerçekleştiğini ve hangi görevlerin öğrenildiğini belirleyecek.

Son olarak, gelecekteki araştırmalarda dikkat edilmesi gereken son problem, ajanları güvenli bir şekilde fiziksel ortamlara yerleştirmek.Bu, gelecekteki araştırmalar için aciliyet gerektiren alanlardan birisi.

## 17.6 Yapay Zekanın Geleceği(The Future of Artificial Intelligence)

Pekiştirmeli öğrenmenin (RL) psikoloji ve nörobilim ile olan bağlantıları yapay zekanın uzun dönemli amaçlarından birisi: akıl hakkında temel sorulara ve beyinden nasıl ortaya çıktığına ışık tutuyor. Pekiştirmeli öğrenme, beynin ödül sistemine, motivasyona ve karar verme süreçlerini nasıl anladığımıza zaten katkıda bulunuyor. Psikiyatri alanına olan bağlantısı ile, uyuşturucu bağımlılığı da dahil olmak üzere ruhsal bozuklukların tedavisine yönelik yöntemlere katkıda bulunacağına inanmak için iyi sebepler var.

Pekiştirmeli öğrenmenin katkı yapabileceği alanlardan birisi de insan karar alma sürecine yardımda bulunmak. Simüle edilmiş ortamlarda pekiştirmeli öğrenme(RL) ile elde edilen politikalar, eğitim, sağlık, ulaşım, enerji ve kamu sektöründe kaynak tahsisi gibi alanlarda karar verici insanlara tavsiye verebilir. 

Pekiştirmeli öğrenme (RL) ajanı(agent), gerçek dünya ile veya gerçek dünyanın bir parçasının simülasyonu ile etkileşime girerek öğrenir. Simulasyonlar, ajanın kendine veya çevreye zarar vermeden, öğrenebileceği ve keşif yapabileceği ortamlar sunar. Yine de pekiştirmeli öğrenmenin tam potansiyeli, sadece kendi dünyalarında değil bizim dünyamızda hareket eden, öğrenen, keşfeden ajanlar gerektirmektedir.

Kapanışta, bizler sadece izleyici değil, geleceğimizin tasarımcıları olduğumuzu kabul etmeliyiz. Bireysel olarak yaptığımız seçimler ile, ve toplumlarımızın yönetimlerine nasıl etki edeceğimiz ile, yeni bir teknolojinin sağladığı faydaların, getirdiği zararları aşmasını sağlayabiliriz.
