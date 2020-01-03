---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 12: Eligibility Traces"
description: " "
date:   2019-01-12
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/off-policy-methods-with-bolum-11
next-page-url: /blog/pekistirmeli-ogrenme/policy-gradient-methods-bolum-13
---

__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.Bölüm hakkında açılmış bir issue varsa tekrar açmayınız.*__

## Eligibility Traces


## The $$\lambda -$$ return

Geçerli bir güncelleme, sadece n-adımlı bir dönüşe değil, farklı $$ns$$'lerin ortalamalı olarak n-adımlı dönüşleri için de yapılabilir. Örneğin, yarısı iki-adımlı dönüşten, yarısı 4-adımlı dönüşten olan hedefe doğru güncelleme yapılabilir: $$\frac{1}2 G_{t:t+2} + \frac{1}2 G_{t:t+4}$$ Herhangi bir n-adımlı dönüş, bileşenleri pozitif ve toplamları 1 olduğu sürece, bu şekilde ortalaması alınarak hesaplanabilir. Basit bileşen güncellemelerinin ortalamasını alan güncelleme, bileşik güncelleme(compound update) olarak adlandırılır. Bileşik güncelleme yalnızca en uzun süreli bileşeninin güncellemesi tamamlandığında gerçekleştirilebilir.

TD ($$\lambda$$) algoritması, özel bir n-adımlı ortalama güncellemesi olarak görülebilir. Bu ortalama, n-adımlı ve her biri $$\lambda^{n-1}$$ ile orantılı tüm güncellemeleri içerir. Ağırlıkların toplamı 1 olması için 
(1 - $$\lambda$$) ile normalize edilir. Elde edilen güncelleme $$\lambda$$-dönüşü olarak adlandırılır.


$$G_t^\lambda \doteq (1 - \lambda) \sum_{n=1}^{\infty} \lambda^{n-1} G_{t:t+n}$$

Bir-adımlı dönüşe en büyük ağırlık verilir: $$1 - \lambda$$; iki-adımlı dönüşe bir sonraki en büyük ağırlık verilir: $$(1 - \lambda)\lambda$$; üç-adımlı dönüşe $$(1 - \lambda)\lambda^2$$; gibi. Ağırlıklar, her bir adımda $$\lambda$$ kadar azaltılır. Terminal durumuna ulaşıldıktan sonra, tüm n-adımlı dönüşler $$G_t$$'ye eşittir. Eğer istersek, sonlanma sonrası terimi ana toplamdan ayırabiliriz.

$$G_t^\lambda = (1 - \lambda) \sum_{n=1}^{T-t-1} \lambda^{n-1} G_{t:t+n} + \lambda^{T-t-1}G_t$$

Bu eşitlik, $$\lambda = 1$$ olduğunda ne olduğunu netleştiriyor. Bu durumda ana toplam sıfıra gidiyor, ve kalan terim alışık olduğumuz dönüşe($$G_t$$) indirgeniyor. Böylece, $$\lambda = 1$$ için, $$\lambda$$-dönüşüne göre güncellemek Monte Carlo Algoritması oluyor. Diğer taraftan, eğer $$\lambda = 0$$ ise, $$\lambda$$-dönüşüne göre güncellemek bir-adımlı TD oluyor.

$$\lambda$$-dönüşüne dayalı ilk öğrenme algoritmamızı tanımlayabiliriz: çevrimdışı $$\lambda$$-dönüşü algoritması(offline $$\lambda$$-return algorithm). Çevrimdışı algoritma olarak, bölüm süresince ağırlık vektörüne bir değişiklik yapmıyor. Bölüm bittiğinde, çevrimdışı güncellemelerin tamamı, her zamanki gibi yarı gradyan(semi gradient) kuralına göre, $$\lambda$$-dönüşünü hedef olarak kullanarak yapılır.


$$w_{t+1} \doteq w_t + a[G_t^\lambda - \hat{v}(S_t,w_t)] \nabla \hat{v}(S_t,w_t), {t = 0, ... , T -1}$$



## TD $$(\lambda)$$

TD $$(\lambda)$$ pekiştirmeli öğrenmede en eski ve en çok kullanılan algoritmalardan biridir. $$\lambda -$$ return’ü üç şekilde daha iyiye taşımaktadır. Öncelikle, bölüm sonundan ziyade her adımda ağırlık güncellemesi yapılması daha hızlı yakınsamayı ve işlem yükünün zaman dağılımını sağlamaktadır. Üçüncü olarak da, TD$$(\lambda)$$ yönteminin bölüm odaklı olmayan devamlı problemlere uygulanabilirlik sağladığı söylenebilir.

Fonksiyon yaklaşıklığı örneği üzerinden ilerlenirse, ağırlık vektörü boyutunda bir uygunluk izi tanımlanmalıdır, $$z_t ~ \epsilon ~ \mathbb{R}^d$$. Ağırlık vektörü uzun zamanlı hafıza olarak, uygunluk izleri ise kısa süreli hafıza olarak değerlendirilebilir, genellikle bölüm kadar uzun sürmemektedir. Yalnızca ağırlık vektörünü etkilemektedir. Uygunluk izleri sıfır ile başlatılır ve her değer gradyeni kadar artırılır.


$$z_{-1} ~ \dot{=} ~ 0,$$
$$z_t ~ \dot{=} ~ \gamma\lambda z_{t-1} + \nabla \hat{v}(S_t,w_t), \quad 0 \le t \le T$$

Bu güncelleme ile, en güncel ($$\gamma\lambda$$’ya dayanarak) durumlara karşılık gelen ağırlık vektörlerinin uygunluk izleri güncellenir. Bir anlamda bu duruma, her bir ağırlık değerinin uygunluğunu değiştirerek, ilgili ağırlıkların daha çok güncellenmesini sağlar. TD hatası şu şekilde hesaplanır:


$$\delta_t ~\dot{=}~ R_{t+1} + \gamma\hat{v}(S_{t+1}, w_t) - \hat{v}(S_t, w_t)$$


$$w_{t+1} ~\dot{=}~ w_t + \alpha\delta_tz_t$$

TD $$(\lambda)$$ uygunluk izleri, her bir durumun ilgili ödüle ne kadar katkı yaptığını işaret etmektedir.. $$\lambda = 0$$ durumunda, güncelleme yalnızca gradyen ile yapılmakta, bu da tek-adım TD yarı-gradyenine denk düşmektedir. Bu sebeple bu algoritmaya TD(0) denmektedir. $$\lambda = 1$$ durumunda ise, izlerin düşüşü yalnızca $$\gamma$$ ile olur, Monte Carlo davranışı ile aynı yönteme denk düşer. Bu algoritmaya da TD($$1$$) denmektedir.

TD($$1$$) bu anlamda bölümün bitmesine bağlı olmadan Monte Carlo davranışını gerçekleyebilmektedir. Bu sayede bölüm içi ödüller, halihazırda bölüm içerisinde davranış değişikliğini sağlayabilir.

## $$n$$$$-$$step Truncated $$\lambda-$$return Methods

Offline $$\lambda -$$ geri dönüş algoritması önemli bir idealdir, ancak sınırlı bir yararı vardır, çünkü bölümün sonuna kadar bilinmeyen $$\lambda -$$ geri dönüşü kullanır. Devam eden durumda, $$\lambda -$$geri dönüşü teknik olarak hiç bilinmemektedir, çünkü keyfi olarak büyük $$n$$ için $$n$$-adımlı geri dönüşlere bağlıdır ve dolayısıyla gelecekte keyfi olarak ödüller kazanır.Ancak, bağımlılık daha uzun gecikmeli ödüller için zayıflıyor,  her gecikme adımı için $$\gamma \lambda$$ azalır. O zaman olası yaklaşım, bazı adımlardan sonra diziyi kesmek olacaktır. Bu, $$n$$ adımlı geri dönüşlerde eksik ödüllerin tahmini değerlerle değiştirildiği doğal bir yoldur. Genel olarak, $$t$$ zamanı için bir sonraki horizon $$h$$ ‘ye kadar kısaltılmış $$\lambda$$$$-$$geri dönüşünü tanımlarız,


$$G_{t:h}^\lambda ~ \dot{=} ~ (1-\lambda)\sum\limits_{n-1}^{h-t-1}\lambda^{n-1}G_{t:t+n} + \lambda^{h-t-1}G_{t:h}, \quad 0 \le t \lt h \le T$$

Kısaltılmış $$\lambda -$$geri dönüş, $$n$$-adımlı yöntemlerine benzer bir $$n$$-adımlı $$\lambda -$$geri dönüş algoritmasıdır. Tüm bu algoritmalarda, güncellemeler $$n$$ adımlarla geciktirilir ve sadece ilk $$n$$'yi hesaba katar, ancak şimdi tüm $$k$$$$-$$adım geri dönüşler, Şekil 12.2'de olduğu gibi geometrik ağırlıklı olarak $$1$$ ≤ $$k$$ ≤ $$n$$ için dahil edilmiştir. Durum değeri olarak, bu algoritma ailesi kısaltılmış TD ($$\lambda$$) veya TTD (λ) olarak bilinir. Şekil 12.7'de gösterilen birleşik yedekleme diyagramı, en uzun bileşen güncellemesinin her zaman bölümün sonuna kadar devam etmek yerine en çok $$n$$ adımda olması dışında TD ($$\lambda$$) (Şekil 12.1) ile benzerdir.


![](https://d2mxuefqeaa7sj.cloudfront.net/s_DCB834881F61DA9DEBBFF7F45D63966F13405B8FD72C49DA380673CEA59ADE9D_1539154693128_image.png)



$$w_{t+n} ~ \dot{=} ~ w_{t+n-1} + \alpha[G_{t:t+n}^\lambda - \hat{v}(S_t, w_{t+n-1})]\nabla\hat{v}(S_t, w_{t+n-1}), \quad 0 \le t \lt T$$

Bu algoritma verimli bir şekilde uygulanabilir, böylece adım adım hesaplama $$n$$ ile ölçeklendirilmez (elbette hafızada olması gerekir).
 $$n$$$$-$$Aşama TD yöntemlerinde olduğu gibi, her bölümün ilk $$n-1$$ zaman adımlarında herhangi bir güncelleme yapılmamakta ve sonlandırma üzerine $$n-1$$ ek güncelleme yapılmaktadır. Verimli bir uygulama, $$k$$-adım λ-geri dönüşünün tam olarak yazılabileceği gerçeğine dayanır.
 

$$G_{t:t+k}^\lambda ~=~ \hat{v}(S_t, w_{t-1}) + \sum\limits_{i=t}^{t+k-1}(\gamma\lambda)^{i-t}\delta_i'$$
$$\delta_t' ~=~ R_{t+1} + \gamma\hat{v}(S_{t+1}, w_t) - \hat{v}(S_t, w_{t-1})$$

## Redoing Updates: Online $$\lambda-$$return Algorithm ( Üzerinden geçip düzenlicem)

Kesilen $$TD(\lambda)$$ ' de kesme parametresi $$n$$ seçimi bir değiş tokuş(tradeoff)** içerir. $$n$$, yöntemin çevrimdışı $$\lambda$$-geri dönüş(return) algoritmasına yakın şekilde yaklaşması için büyük olmalıdır, ancak güncelleştirmelerin daha çabuk yapılabilmesi ve davranışları daha erken etkileyebilmesi için küçük olmalıdır. İkisinden de en iyisini alınabilir mi? Evet, prensip olarak hesaplama karmaşıklığı pahasına da olsa yapılabilir.

Buradaki fikir, her zaman adımında yeni bir veri artışı toplandığında, geçerli bölümün başlangıcından bu yana tüm güncellemeleri geri almanız ve yinelemenizdir. Yeni güncellemeler, daha önce hazırlanmış olanlardan daha iyi olacak çünkü artık zaman adımının yeni verilerini dikkate alabilirler. Yani güncellemeler her zaman bir $$n-$$adım kısaltılmış $$\lambda-$$geri dönüş(return) hedefine doğrudur, ancak her zaman en son görüşü(horizon)** kullanırlar. Bu bölümdeki her geçişte biraz daha uzun bir görüş(horizon)-kesme** kullanabilir ve biraz daha iyi sonuçlar elde edebilirsiniz.
Kesilmiş $$\lambda-$$geri dönüş(return) (12.9) olarak tanımlandığını hatırlayın.


$$G_{t:h}^\lambda ~\doteq~ (1-\lambda) \sum\limits_{n=1}^{h-t-1}\lambda^{n-1} G_{t:t+n} ~+~ \lambda^{h-t-1} G_{t:h}.$$

Hesaplama karmaşıklığı bir sorun değilse, bu hedefin ideal olarak nasıl kullanılabileceğine bir göz atalım*. Bölüm, bir önceki bölümün sonundan $$w_0$$ ağırlıkları kullanılarak $$0$$ zamanında bir tahminle başlar. Öğrenme, veri görüşü(horizon)** zaman adımı 1'e genişletildiğinde başlar. Horizon 1'e kadar olan veriler göz önüne alındığında, adım 0'da ki hedefe yönelik hedef, sadece tek adımlı geri dönüş $$G_{0:1}$$ olabilir, bu da $$R_1$$ ve $$\hat{v}(S_1,w_0)$$ tahmininden önyükleme(bootstraping) noktalarını içerir. Bunun tam olarak $$G_{0:1}^\lambda$$ olduğu, denklemin ilk terimindeki toplamın sıfıra degenerating** olduğunu unutmayın. Bu güncelleme hedefini kullanarak $$w_1$$'i oluşturuyoruz. Ardından, veri ufkunu(horizon) adım 2'ye ilerlettikten sonra ne yapılır?
$$R_2$$ ve $$S_2$$'nin yanı sıra yeni $$w_1$$ şeklinde yeni verilerimiz var, bu yüzden şimdi $$S_0$$'dan ilk güncelleme için daha iyi bir güncelleme hedefi  $$G_{0:2}^\lambda$$ ve $$S_1$$'den ikinci güncelleme için daha iyi bir güncelleme hedefi $$G_{1:2}^\lambda$$ oluşturabiliriz*.Bu gelişmiş hedefleri kullanarak $$w_0$$'dan başlayarak $$w_2$$'yi üretmek için $$S_1$$ ve $$S_2$$'deki güncellemeleri yeniden düzenlenir . Şimdi ufku(horizon)* 3. adıma ilerlenir ve tekrarlanır, üç yeni hedef üretmek için geri dönülür, orijinal $$w_0$$ dan başlayarak $$w_3$$ üretmek için tüm güncellemeler yeniden yapılır. Ufuk(Horizon)* her geliştiğinde, tüm güncellemeler önceki ufuktan ağırlık vektörünü kullanarak $$w_0$$'dan başlayarak yeniden yapılır. Bu kavramsal algoritma, her biri birer ufukta(horizon), her biri farklı bir ağırlık vektörleri dizisi oluşturan bölüm üzerinde çoklu geçişler içerir. Açıkça tanımlamak için farklı ufuklarda* hesaplanan ağırlık vektörleri arasında ayrım yapmak zorundayız. Ufuk(Horizon) $$h$$'ye kadar olan sıradaki zamanda $$t$$ değerini üretmek için kullanılan ağırlıkları belirtmek için $$w_{t}^h$$kullanalım. Her dizideki ilk ağırlık vektörü $$w_{0}^h$$, önceki bölümden devralınan (bu nedenle tüm $$h$$ için aynıdır) ve her dizideki son ağırlık vektörü $$w_{h}^h$$, algoritmanın nihai ağırlık vektör dizisini tanımlar.


$$h ~=~ 1:$$     $$w_1^1 ~ \dot{=} ~ w_0^1 + \alpha[G_{0:1}^\lambda - \hat{v}(S_0, w_0^1)\nabla\hat{v}(S_0,w_0^1)]$$
    
$$h ~=~ 2:$$     $$w_1^2 ~ \dot{=} ~ w_0^2 + \alpha[G_{0:2}^\lambda - \hat{v}(S_0, w_0^2)\nabla\hat{v}(S_0,w_0^2)]$$
$$w_2^2 ~ \dot{=} ~ w_1^2 + \alpha[G_{1:2}^\lambda - \hat{v}(S_1, w_1^2)\nabla\hat{v}(S_1,w_1^2)]$$
    
$$h ~=~ 3:$$     $$w_1^3 ~ \dot{=} ~ w_0^3 + \alpha[G_{0:3}^\lambda - \hat{v}(S_0, w_0^3)\nabla\hat{v}(S_0,w_0^3)]$$
$$w_2^3 ~ \dot{=} ~ w_1^3 + \alpha[G_{1:3}^\lambda - \hat{v}(S_1, w_1^3)\nabla\hat{v}(S_1,w_1^3)]$$
$$w_3^3 ~ \dot{=} ~ w_2^3 + \alpha[G_{2:3}^\lambda - \hat{v}(S_2, w_2^3)\nabla\hat{v}(S_2,w_2^3)]$$

Son ufukta $$h=T$$ Bir sonraki bölümün başlangıç ağırlıklarını oluşturmak için geçecek olan nihai ağırlıkları $$w_{T}^T$$ elde ederiz. Bu kurallarda, önceki paragrafta açıklanan üç ilk sekans açıkça verilebilir:


$$w_{t+1}^h \doteq w_{t}^h~+~\alpha [G_{t:h}^\lambda-\hat{v}(S_t,w_{t}^h)]~\nabla\hat{v}(S_t,w_{t}^h),~0 \le t<h\le T.$$

Online $$\lambda$$-return algoritması tamamen çevrim içi olup, sadece $$t$$ zamanında mevcut olan bilgileri kullanarak, bir atak sırasında her adımda yeni bir ağırlık vektörünü belirlemektedir.Ana dezavantajı, her adımda bugüne kadar deneyimlenen bölümlerin üzerinden geçen karmaşık bir şekilde bir hesabının olmasıdır. Sonlandırma sırasında tüm adımlardan geçen ancak bölüm sırasında herhangi bir güncelleme yapmayan çevrimdışı λ-döndürme algoritmasından kesinlikle daha karmaşık olduğunu unutmayın. Buna karşılık, çevrim içi algoritmanın çevrimdışı bölümden daha iyi performans göstermesi beklenebilir; sadece çevrimdışı algoritma hiçbir şey yapmazken (bir güncelleme yaparken değil), aynı zamanda bölümün sonunda önyükleme(bootstrapping)'de kullanılan ağırlık vektörüdür. (Gλ) daha fazla sayıda bilgilendirici güncellemeye sahipti. Bu durum, 19-durumlu rastgele yürüyüş görevindeki iki algoritmayı karşılaştıran Şekil 12.8'de dikkatlice gözükürse görülebilir.


![Şekil 12.8 : 19-durum Rastgele Yürüme Sonuçları(Alıştırma 7.1): Çevrim içi ve çevrim dışı λ-döndürme(return) algoritmalarının performansı.](https://d2mxuefqeaa7sj.cloudfront.net/s_2EAF3026A66C014EC7FECE570C29230B6940663A5A967B749B8FAC1991708246_1539212965151_Screenshot_2.png)


Buradaki performans ölçüsü, bölümün sonunda çevrimdışı algoritma için en iyi durum olan $$\displaystyle \bar{VE}$$’ dir. Yine de, çevrim içi algoritma daha iyi bir performans sergiliyor. Karşılaştırma için, λ = 0 çizgisi her iki yöntem de de aynıdır.

## True Online TD$$(\lambda)$$

Çevrimiçi $$\lambda -$$dönüş algoritması şu anda en iyi $$TD$$ algoritmasıdır. Fakat çevrimiçi $$\lambda -$$dönüş algoritması çok karmaşıktır. Uygunluk izlerini kullanarak verimli bir geriye dönük görüntüleme algoritması üretmek için bu ileri görüş algoritmasını tersine çevirmenin bir yolu var mıdır? Lineer fonksiyon yaklaşımı için çevrimiçi $$\lambda -$$dönüş algoritmasının tam olarak hesaplamalı olarak uygun bir uygulaması olduğu ortaya çıkmaktadır. Bu uygulama, gerçek çevrimiçi $$TD(\lambda)$$ algoritması olarak bilinir, çünkü $$TD(\lambda)$$ algoritmasından daha iyi olan çevrimiçi $$\lambda -$$dönüş algoritmasının idealine göre daha doğrudur.

Gerçek çevrimiçi $$TD(\lambda) '$$nin türetilmesi fazla karmaşıktır ancak stratejisi basittir. Çevrimiçi $$\lambda -$$dönüş algoritması tarafından üretilen ağırlık vektörleri dizisi bir üçgene göre düzenlenebilir:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_7C5E62C149C2B59FAB3FED667E7AC688DE35B2F5E1057EC2CD0F4A3A1A6AAACB_1539201094191_paper.png)


Bu üçgenin bir satırı her adımda üretilir. Diyagonaldeki(çapraz) ağırlık vektörleri $$w_t^t,$$ gerçekten ihtiyaç duyulan tek şey olduğu gözüküyor. Birincisi yani $$w_0^0,$$ bölümün başlangıç ağırlık vektörüdür. Sonuncusu yani $$w_T^T,$$ son ağırlık vektörüdür ve diğer tüm vektörler dahil güncellemelerin $$n-$$adım dönüşlerinde ($$n-$$step returns) önyükleme yaparken rol oynar. Son algoritmada diyagonal ağırlık vektörleri bir üst simge olmaksızın yeniden adlandırılır, $$w_t = w_t^t.$$ Daha sonrasında strateji, her biri $$w_t^t$$ $$'$$yi daha önce hesaplamanın verimli bir yolunu bulmaktır. Eğer bu yapılırsa, $$\hat v(s,w) = w > x(s) '$$nin olduğu doğrusal durum için, gerçek çevrimiçi $$TD(\lambda)$$ algoritmasına ulaşırız:

$$w_{t+1} \doteq w_t + \alpha \delta_{t}z_{t}+\alpha(w_{t}^{T}x_{t}-w_{t-1}^{T}x_{t})(z_{t}-x_{t}),$$

$$x_t \doteq x(S_t)$$ kısaltmasını kullanırsak ve $$\delta_t$$ $$(12.6)'$$ da tanımlandığı gibi kullanılırsa, $$z_t$$ şöyle olur:

$$z_t \doteq \gamma \lambda z_{t-1} + (1-a \gamma \lambda z_{t-1}^{T} x_t) x_t.$$
Gerçek çevrimiçi $$TD(\lambda)$$ bellek gereksinimleri, geleneksel $$TD(\lambda)$$ ile aynıdır, ancak adım başına hesaplama yaklaşık $$\%50$$ artar. Genel olarak, adım başına hesaplama karmaşıklığı $$TD(\lambda)$$ ile aynı $$O(d)$$ kalır.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_7C5E62C149C2B59FAB3FED667E7AC688DE35B2F5E1057EC2CD0F4A3A1A6AAACB_1539276983219_Screenshot+from+2018-10-11+19-55-57.png)


Gerçek çevrimiçi TD($$\lambda$$)'da kullanılan uygunluk izi biriktirme izi (accumulating trace) olarak adlandırılan TD($$\lambda$$)'da kullanılan izden ayırt etmek için bir hollanda izi (dutch trace) olarak adlandırılır. Daha önceki çalışmalarda, genellikle tabular kutu için veya karo kodlamasıyla üretilenler gibi ikili özellik vektörleri için tanımlanan değiştirici izleme (replacing trace) adı verilen üçüncü tür bir iz kullanılır. Değiştirme izlemesi, özellik vektörünün bileşeninin 1 veya 0 olmasına bağlı olarak bileşen-bileşen (component-by-component) bazında tanımlanır:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_7C5E62C149C2B59FAB3FED667E7AC688DE35B2F5E1057EC2CD0F4A3A1A6AAACB_1539273423196_Screenshot+from+2018-10-11+18-56-53.png)


## *Dutch Traces in Monte Carlo Learning

(Monte Carlo Yönteminde Eş İzler)

Aslında, bu bölümde gösterilenler gibi Monte Carlo yönteminde bile uygunluk izleri ortaya çıkmaktadır. 
Gradyen Monte Carlo algoritması tahmin algoritması, bölümün her adımı için aşağıdaki güncellemeler dizisini takip eder:

$$w_{t+1} \doteq w_t + a[G - w_t x_t] x_t,  0 \leq t < T.$$

Örneği basitleştirmek için G dönüşü bölüm sonunda tek bir ödül olarak varsayılmaktadır. Aynı zamanda indirgenme yoktur. Bu durumda güncelleme aynı zamanda En Küçük Ortalama Kare Kuralı (Least Mean Square Rule) denilmektedir. Monte Carlo algoritmasında olduğu gibi tüm güncellemeler geri dönüşe bağlıdır. Bu yüzden bölüm sonuna kadar güncelleme yapılmamaktadır. MC algoritması offline bir algoritmadır ve bunun yönünü değiştirmeye çalışmak gerekmektedir. Bölüm sonunda ağırlık tekrar güncellenmektedir. Bu, ihtiyaçları ortadan kaldırmak ve her bölümün sonunda daha sonra kullanmak için daha iyi bir yol sağlamaktadır. Bunu yerine tüm özet korunarak ek bir uygunluk izi sunulmaktadır. Özellikle de güncellemelerin dizisi ile aynı genel güncellemeyi yeniden oluşturma konusunda verimli bir şekilde yeterli olmaktadır. Bölüm sonunda:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_0E40633B32860565FBBB5AD5C39026A4EF9F4137B87F39197101391B636CAD93_1539194100098_Screen+Shot+2018-10-10+at+20.42.52.png)


a_t-1 ve z_t-1 değerleri T-1 zaman aralığında ve O(d) karmaşıklığı olmadan aşamalı olarak güncellenebilen iki adet hafıza vektörleridir. Zt vektörü de aslında bir eş tarzı uygunluk izidir. Bu da eş izi γλ = 1 olduğu durumda z0=x0 olarak başlatılır:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_0E40633B32860565FBBB5AD5C39026A4EF9F4137B87F39197101391B636CAD93_1539194108191_Screen+Shot+2018-10-10+at+20.51.16.png)


Yardımcı vektörde ise a0=w0 olarak başlatılır ve:

![](https://d2mxuefqeaa7sj.cloudfront.net/s_0E40633B32860565FBBB5AD5C39026A4EF9F4137B87F39197101391B636CAD93_1539194118524_Screen+Shot+2018-10-10+at+20.53.49.png)


## Sarsa$$(\lambda)$$

Uygunluk izleri yöntemini eylem-değer yöntemlerine uygulamak için onuncu bölümdeki n-adımlı getiri kullanılır. Ve çevrimdışı $$\lambda$$-dönüşü algoritmasının eylem değer halinde ise $$v$$ yerine $$q$$ kullanılır. Bu formüller aşağıda görülebilir:


$$G_{t:t+n} ~\dot{=}~ R_{t+1} + ... + \gamma^{n-1}R_{t+n} + \gamma^n\hat{q}(S_{t+n}, A_{t+n}, w_{t+n-1}), \quad t + n \lt T$$
    
$$w_{t+1} ~\dot{=}~ w_t + \alpha[G_t^\lambda-\hat{q}(S_t, A_t w_t)]\nabla\hat{q}(S_t, A_t, w_t), \quad t=0,...,T-1$$

Bu yöntemin backup diagramına bakıldığında TD($$\lambda$$) algoritmasına benzediğini görülür. İkisinde de ilk güncellemede bir sonraki durum eylem çifti, ikinci güncellemede iki sonraki durum eylem çifti kullanılır ve bu böyle devam eder. Yani n. güncelleme için n adım sonrasının bilgisi kullanılır. En son(final) güncellemede ise getirinin tamamı kullanılır.

Eylem değerleri için zamansal fark yöntemi olan Sarsa($$\lambda$$), TD($$\lambda$$) ile aynı güncelleme kuralını kullanır ama TD hatası ve uygunluk izi hesaplarının eylem değer halini kullanır.

Aynı zamanda, ideal TD yöntemi olan çevrimiçi $$\lambda$$-dönüşü algoritmasının da eylem-değer uyarlaması vardır ve gerçek çevrimiçi Sarsa($$\lambda$$) (True Online Sarsa($$\lambda$$)) yöntemi denir. Bu yöntemin de çevrimiçi $$\lambda$$-dönüşünden tek farkı, n-adımlı getirinin yukarıda verilen eylem-değer halinin kullanılmasıdır.

## Variable $$\lambda$$ and $$\gamma$$

TD öğrenme algoritması duruma ve eyleme bağlı olarak her zaman adımında farklı $$\lambda$$ ve  $$\gamma$$ sahip olur ve  $$\lambda_t$$ ve $$\gamma_t$$ şeklinde ifade edilir. Böylece notasyonda değişiklik olur;


![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269262399_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269294659_image.png)



![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269315245_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269331920_image.png)


Dönüş(return) değeri 

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269537620_image.png)


şeklinde tanımlanır ve bu formülde toplamlar sonlu olduğundan tüm t için aşağıdaki çarpıma ihtiyaç duyarız.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539269789779_image.png)


Bu tanımın uygun bir yönü bölümler, başlangıç ve terminal durumları ile T’ yi özel durumlar ve miktarlar olarak dağıtmamıza izin verir. Terminal durumu sadece $$\gamma$$=0 olan ve başlangıç durumuna geçiş yapan bir hal olur.  Değişken önyüklemenin genelleştirilmesi problemde discounting* gibi bir değişiklik değil çözüm stratejisinde bir değişikliktir. Genelleme durumlar ve eylemler için λ-return etkiler. Yeni λ-return, yinelemeli olarak aşağıdaki gibi yazılabilir;


![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539271094072_image.png)


Bu denklem λ-return değerinin önyüklemeden etkilenmeyen bir ödül olduğunu ve muhtemelen bir sonraki durumda discounting* yapılmadığı durumda ikinci bir terim olduğunu ifade eder. Bir sonraki aşamada  sona ermediği sürece önyükleme derecesine bağlı olarak kendini iki duruma ayıran ikinci bir terime sahibiz. Bir sonraki adım için önyüklemeyi yaptığımız ölçüde bu terim tahmin edilen değerdir, önyükleme yapmadığımızda bu terim λ-return dir. 

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539271929447_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539271960656_image.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_64107606A11190F0E8BB9D893461A748CDB0E14A0B78E003EB69E74F0DEBFEF5_1539271973042_image.png)


## Off-policy Traces with Control Variates

## Watkins’s Q$$(\lambda)$$ to Tree-Backup$$(\lambda)$$

Yıllar boyunca Q-öğrenmeyi uygunluk izlerine kadar genişletmek için birkaç yöntem önerilmiştir. İlk Watkins Q (λ), açgözlü bir eylem yapıldığı müddetçe uygunluk izlerini her zamanki gibi azaltır ve açgözlü olmayan ilk eylemden sonra izleri sıfıra indirir.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_2C39B0DA3283498890F3C8FD0AB2ED413524A6AFBF50381D82E888EBF977D5EB_1539197598831_file.png)


TB (λ) kavramı basittir.Aşağıdaki şekilde yedekleme şemasında gösterildiği gibi, her uzunluktaki ağaç yedekleme güncellemeleri , önyükleme parametresine (λ) bağlı olacak şekilde ağırlıklandırılır.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_2C39B0DA3283498890F3C8FD0AB2ED413524A6AFBF50381D82E888EBF977D5EB_1539197634468_file.png)


Detaylı denklemleri elde etmek için genel önyükleme ve indirgeme parametrelerindeki doğru indekslerle, en iyi λ-dönüşü kullanarak hareket değerleri elde etmek için özyinelemeli bir formla başlamak ve daha sonra hedefin önyükleme durumunu genişletmek en iyisidir.

![](https://d2mxuefqeaa7sj.cloudfront.net/s_2C39B0DA3283498890F3C8FD0AB2ED413524A6AFBF50381D82E888EBF977D5EB_1539197644957_file.png)

![](https://d2mxuefqeaa7sj.cloudfront.net/s_2C39B0DA3283498890F3C8FD0AB2ED413524A6AFBF50381D82E888EBF977D5EB_1539197648195_file.png)


Bu, olağan parametre güncelleme kuralı ile birlikte TB (λ) algoritmasını tanımlar. Tüm yarı-gradyan algoritmalarında olduğu gibi, TB (λ), politika dışı verilerle ve güçlü bir function approximation ile kullanıldığında kararlı olmayacaktır. Bunun için bir sonraki bölümde sunulan yöntemlerden biriyle birleştirilmelidir.

## Stable Q-policy Methods with Traces

## Implementation Issues

## Conclusions