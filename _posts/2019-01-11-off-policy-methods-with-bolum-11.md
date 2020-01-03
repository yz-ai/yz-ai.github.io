---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 11: Off-policy Control With Approximation"
description: " "
date:   2019-01-11
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/on-policy-control-bolum-10
next-page-url: /blog/pekistirmeli-ogrenme/eligibility-traces-bolum-12
---

__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.Bölüm hakkında açılmış bir issue varsa tekrar açmayınız.*__

--(?) olan yerlere ekleme yapılıcak

--Kullanılan matematiksel sembollerin karşılıkları:

$$\ {p_t}$$      : t zamanında importance sampling oranı \\
$$\ {p_{t:h}}$$   : t zamanından h zamanına kadar importance sampling oranı \\
$$\pi$$        : politika, karar verme kuralı \\
$$\ {b}$$
$$\ {A_t}$$     : t zamanındaki eylem(action) \\
$$\ {S_t}$$      : t zamanındaki durum(state) \\
$$\ {d}$$        : dimensionality , $$ {w}$$ bileşenlerinin sayısı \\
$$ {w,w_t}$$ : yaklaşık değer fonksiyonu temelini oluşturan ağırlığın d-vektörü \\
$$\alpha$$         :adım sayısı parametresi \\
$$\delta_t$$         : t anındaki temporal difference hatası \\
$$\hat{v}\ {(S_t, {w_t)}}$$  : ağırlık vektörü $${w}$$ olan $$\ {S}$$ durumunun yaklaşık değeri(approximate value) \\
$$\ {R_t}$$        : t anındaki reward \\
$$\ {r(\pi)}$$    : $$\pi$$ policy için ortalama reward \\
$$\bar {R_t}$$        : t anındaki tahmini$$\ {r(\pi)}$$ \\
$$\gamma$$          :discount rate parametresi \\
$$\hat{q}\ {(S_t,A_t, {w_t)}}$$   : ağırlık vektörü $$ {w}$$ olan $$\ {S}$$tate$$\ {A}$$ction çiftinin yaklaşık değeri(approximate value) \\

## Yaklaşıklama ile Politika Dışı Yöntemler(Off-Policy Methods with Approximation)

Politikalı ve politika dışı öğrenme yöntemlerini, genelleştirilmiş davranış politikası iterasyonunun öğrenme biçimlerinin doğasından bulunan keşif-sömürü arasındaki çatışmayı ele almak için iki alternatif yol olarak inceleriz. Bu bölümde politika dışı öğrenmeyi işlev yaklaşıklığı(function approximation) ile ele alacağız. İşlev yaklaşıklığı politika dışı öğrenmede politikalı öğrenmeye göre daha zordur. Politika dışı öğrenme yöntemleri, ne teorik olarak ne de deneysel olarak politikalı öğrenme kadar güçlü değildir.

Politika dışı öğrenmede verilmiş olan başka bir politikanın verisinden bir hedef politika için value-function öğrenmeye çalışırız. (?)Tahmin durumunda, her iki politikada statictir  ve verisi vardır, biz her iki durumda da durum veya eylem değerlerini öğrenmeye çalışırız. Kontrol durumunda action value öğrenilmiştir,her iki politikada öğrenme sırasında değişebilir $$\pi$$  $$\hat{q}$$'ya göre greedy veya $$\epsilon$$-greedy olabilir. 

Politika dışı öğrenmenin zorluğu ikiye ayrılır, bir tanesi tablo durumunda diğeri işlev yaklaşıklığı ile ortaya çıkar.İlk kısım target of the update, ikinci kısım distribution of the updates ile ilgilidir.

(?).on-policy dağıtım yarı gradyan yöntemlerin kararlılığı için önemlidir.Bununla başa çıkmak için iki genel yaklaşım araştırılmıştır. Birisi importance sampling yöntemi diğeri true gradient yöntemidir.Her iki yaklaşıma yönelik yöntemler sunucaz.Bu son teknoloji bir araştırma alanıdır ve bu yaklaşımlardan hangisinin pratikte en etkili olduğu net değildir.

## Yarı Gradyan Yöntemler

Yarı gradyan yöntemler off-policy öğrenme zorluklarının ilk kısmını ele alır(target of the update). Bu yöntemler bazı durumlarda sapma yapabilir(diverge) fakat genellikle başarılı biçimde kulanılırlar.

Tabular off-policy için bir çok algoritma vardır ve bu bölümde bu algoritmaları yarı gradyan algoritmalara dönüştürülmüş haliyle göreceğiz. İlk olarak bu algoritmaların birçoğunun kullandığı önem örneklemesini tanımlayalım:


$$\rho {_t} \ { } \dot {=} \rho {_{t:t}} \ { } \ {=} \ { } \frac{\pi\ {(A_t} {|} {S_t)} }{\ {b}\ {(A_t} {|} {S_t)} } \ {.}  \qquad(11.1)$$

state-value için one-step algoritması semi-gradient off-policy TD(0):


$$\ {w_{t+1}}\ { } \dot {=} \ { } {w_t +} \alpha\rho {_t} \delta {_t}  \triangledown \hat{v}\ {(S_t, {w_t)}} \ {,}  \qquad(11.2)$$

$$\delta_{t}$$ problemin episodic ve discounted veya continuing ve undiscounted olup olmamasına bağlı olarak iki şekilde tanımlanır.


$$\delta {_t}\ { } \dot {=} \ { } \ {R_{t+1} +} \gamma\hat{v}\ {(S_{t+1}, {w_t)}} \ {-} \hat{v} \ {(S_t, {w_t)}} \ {,} \qquad(11.3)$$


$$\delta {_t}\ { } \dot {=} \ { } \ {R_{t+1} -} \bar {R_{t}}\ {+} \hat{v}\ {(S_{t+1}, {w_t)}} \ {-} \hat{v} \ {(S_t, {w_t)}} \ {.}  \qquad(11.4)$$

action-value için one-step algoritması semi-gradient expected sarsa:


$${w_{t+1}}\ { } \dot {=} \ { } - {w_t +} \alpha \delta {_t} -\triangledown \hat{q}\ {(S_t,A_t,-{w_t)}} \ {,}  \qquad(11.5)$$


$$\delta_{t} \ \dot{=} \ R_{t+1} + \gamma \sum_{a} \pi (a | S_{t+1}) \hat{q} (S_{t+1},a,w_{t}) - \hat{q} (S_{t},A_{t},w_{t}), \qquad(episodic)$$ 

$$\delta_{t} \ \dot{=} \ R_{t+1} - R_{t} + \sum_{a} \pi (a | S_{t+1}) \hat{q} (S_{t+1},a,w_{t}) - \hat{q} (S_{t},A_{t},w_{t}). \qquad(continuing) $$


yukarıdaki formülde importance sampling ratio olmadığına dikkat edin.

bu algortimaların multi step versiyonu için hem state-value hem action-value importance sampling içerir.

semi gradient expected sarsa için $$n$$-step versiyon:

$${w_{t+n}}\ { } {\dot {=}} \ { }  {w_{t+n-1} +} \alpha\rho_{t+1}\cdots\rho_{t+n-1}\begin {bmatrix} \ {G_{t:t+n}}\ {-} \hat{q} \ {(S_t,A_t,{w_{t+n-1})}}\end {bmatrix} \triangledown \hat{q}\ {(S_t,A_t, {w_{t+n-1})}} \ {,} \qquad(11.6)$$


$$G_{t:t+n} \dot {=} R_{t+1}+\cdots + \gamma^{n-1} R_{t+n}+ \gamma^{n}\hat{q} (S_{t+n},A_{t+n}, w_{t+n-1})  {,} \qquad (episodic) $$


$${G_{t:t+n}}{ }  {\dot {=}} {R_{t+1}-}\bar {R_t+}\cdots  {R_{t+n}-}\bar {R_{t+n-1}+}\hat{q}  {(S_{t+n},A_{t+n}, {w_{t+n-1})}}  {,} \qquad(continuing) $$

n-step tree-backup algoritmasının yarı gradyan versiyonu:


$${w_{t+n}}\ { } {\dot {=}} \ { } {w_{t+n-1} +} \alpha\begin {bmatrix} \ {G_{t:t+n}}\ {-} \hat{q} \ {(S_t,A_t, {w_{t+n-1})}}\end {bmatrix} \triangledown \hat{q}\ {(S_t,A_t, {w_{t+n-1})}} \ {,} \qquad(11.7)$$


$$ {G_{t:t+n}}\ { } {\dot {=}}\ \hat{q} \ {(S_{t},A_{t}, {w_{t+-1})} +}\sum_{k=t}^{t+n-1}\delta_t\prod_{i=t+1}^k \gamma\pi {(A_i|S_i)}  \ {,} \qquad(11.8)$$

## Off-Policy Sapmasına Örnekler

Bu bölümde işlev yaklaşıklığı ile off-policy öğrenmenin 2. zorluğundan (distribution of updates) bahsedicez. Yarı gradyan ve diğer basit algoritmaların kararsız ve ıraksak olduğu durumlarda off-policy öğrenmeye bazı öğretici karşı örnekler tanımlarız(anlatırız).

Basit bir örnek düşünelim.Parametresi sadece birtek bileşen $$\ {w}$$ yi içeren vector $$ {w}$$ olan tahmini değerleri fonksiyonel formda $$\ {w}$$ ve $$\ {2w}$$ olan 2 durumumuz olsun.

## Ölümcül Üçlü

Şu ana kadarki tartışmamız istikrarsızlık ve ıraksaklık tehlikesini ortaya çıkaran ölümcül üçlü dediğimiz aşağıdaki üç elementin birleşmesiyle özetlenebilir:

Function approximation : Bellek ve hesaplama kaynaklarından çok daha büyük bir durum uzayı (state space) ölçeklemenin güçlü bir yolu(örneğin lineer işlev yaklaşıklığı veya yapay sinir ağları).
Bootstrapping : Yalnızca güncel ödüllere inanmak yerine var olan tahminlerle hedefleri güncelleme.
Off-policy training : Hedef davranış politikası tarafından üretilenlerin dışındaki geçişlerin dağıtımı üzerine eğitim.

Özellikle, tehlikenin kontrol veya genel politika iterasyonundan kaynaklanmadığını unutmayın.Bu durumlar analiz etmek için çok karmaşıktır, kararsızlık ölümcül üçlünün üç unsurunuda içerdiği zaman tahmin durumunda (prediction case) ortaya çıkar. Tehlike öğrenmeden ya da çevrenin belirsizliğinden kaynaklı değildir, çünkü çevrenin tamamen bilindiği dinamik programlama gibi planlama yöntemlerinde güçlü şekilde ortaya çıkar.

Eğer ölümcül üçlünün hepsi birden yoksa kararsızlıktan kaçınılabilir.

## Doğrusal Değer-Fonksiyon Geometrisi

Off-policy öğrenmenin kararlılık sorununu daha iyi anlamak için,value function approximationun nasıl öğrenildiğini daha soyut ve bağımsız şekilde düşünmek daha faydalı olacaktır.Tüm olası durum-değer fonksiyonlarının uzayını hayal edelim,tüm fonksiyonlar durumlardan gerçek sayılara dönüşür v :  S ->R.Bu değer fonksiyonlarının çoğu herhangi bir politikaya uymaz.

## Bellman Hatasında Olasılıksal Gradyan Azaltma

Değer fonksiyonu yaklaşımı ve yaklaşımın çeşitli hedefleri hakkında daha iyi bir anlayışa sahip olarak, artık off-policy öğrenmede kararsızlık sorununa geri dönüyoruz.

## Bellman Hatası Öğrenilebilir Değil

##  Gradyan-TD Yöntemler

Şimdi  $$\overline {PBE}$$'yi minimuma indirmek için SGD yöntemlerini dikkate alabiliriz.Gerçek SDG yöntemleri olarak  bu gradyan-TD yöntemleri off-policy eğitim ve doğrusal olmayan fonksiyon yaklaşımı altında bile güçlü yakınsama özelliklerine sahiptir.Bu gradyan-TD yöntemlerinin karmaşıklığı $$\ {O{(d^2)}}$$’dir,buna rağmen hedeflerimiz ulaşmaya çok yaklaşır.

$$\overline {PBE}{(w)=}{(X^\top D\bar\delta_{ {w}})}^\top {(X^\top DX)}^{-1} {(X^\top D\bar\delta_{ {w}})}$$

$$ {w}$$’ye göre gradyanı
$$\triangledown\overline {PBE} {(w)= 2}\triangledown\begin {bmatrix} {X^\top D\bar\delta_{ {w}})}\end {bmatrix}^\top{(X^\top DX)}^{-1} {(X^\top D\bar\delta_{ {w}})}$$

formüller gelicek

![](https://d2mxuefqeaa7sj.cloudfront.net/s_E71C644A13BDD2D1E3456BC2CBEE925BA47328AFF2B8357076D30DC1DBD61F99_1536228904017_file.png)



## Güçlü_TD Yöntemler

## Varyans Azaltma

Off policy öğrenme doğal olarak on policy öğrenmeye göre daha büyük bir varyanstır. Bu şaşırtıcı değildir zira bir davranış politikasına daha az ilişkili bilgiler verirseniz, davranış politikasının değeri ile ilgili daha az bilgi öğrenirsiniz.Aşırı durumlarda belkide hiçbir şey öğrenemezsiniz.Örneğin yemek pişirerek nasıl araba kullanılıcağını öğrenemezsiniz.Yalnızca hedef ve davranış politikaları ilişkiliyse benze durumlarda benzer eylemlerde bulunurlarsa politika dışı eğitimde önemli ilerlemeler kaydedilmelidir.

Politika dışı öğrenmeden yararlanma niyeti ilişkili fakat aynı olmayan politikaları genellemeyi mümkün kılmaktır.Problem deneyimleri en iyi şekilde nasıl kullanacağımızdır. Şimdi beklenen değerde kararlı olan bazı yöntemlere sahip olduğumuza göre(adım boyutları doğru olarak ayarlanmışsa) dikkatimizi tahminlerin varyansını azaltmaya çevirebiliriz.

Importance samplinge dayalı off policy yöntemlerinde varyansı azaltmak neden bu kadar kritiktir? Importance sampling genellikle politika oranlarının sonuçlarını içerir.Oranlar her zaman beklentide 1'dir fakat gerçekte çok yüksek veya 0 kadar düşük olabilir.Ardışık oranlar birbiriyle ilişkisizdir, bu yüzden daima beklenen değerlerdedir fakat çok yüksek varyansta olabilirler.Bu oranlar SGD yöntemlerinde adım büyüklüğü ile çarpılır,bu yüzden**

## Özet

Politika dışı öğrenme, kararlı ve verimli öğrenme algoritmalarını tasarlamada ustalığımızı test eden cazip bir sorundur. Tabular Q-öğrenme off policy öğrenmeyi kolaylaştırır ve Expected sarsa ve Tree backup algoritmalarında doğal bir genellemeye sahiptir. Fakat bu bölümde gördüğümüz gibi bu fikirleri önemli işlev yaklaşıklıklarına genişletmeliyiz, doğrusal işlev yaklaşımı bile yeni zorlukları beraberinde getirmekte ve pekiştirmeli öğrenme algoritmaları anlayışımızı derinleştirmeye zorlamaktadır.

Neden böyle zorluklarla uğraşıyoruz? Off policy algoritmalarının araştırılmasının bir sebebi keşif ve sömürü arasındaki zorlukla baş etmede esneklik sağlamaktır.Bir diğeri öğrenme davranışından kurtulmak ve hedef politikanın tiranlığından(baskınlık) kaçınmaktır. TD öğrenimi birçok görevi aynı anda çözmek için bir deneyim akışını kullanarak,birden fazla şeyi paralel olarak öğrenme olasılığına dayanır. Bunu özel durumlarda yapabiliriz fakat her durumda istediğimiz kadar verimli yapamayız.

Bu bölümde off-policy öğrenmenin zorluklarını ikiye böldük. Davranış politikası için öğrenme hedeflerini düzelten ilk kısım güncellemenin varyansını arttırma ve yavaş öğrenme pahasınada olsa tabular durum için tasarlanan teknikleri kullanır. Yüksek varyans muhtemelen off-policy öğrenme için her zaman bir sorun teşkil edecek.

off-policy öğrenme zorluklarının ikinci kısmı bootstrapping içeren yarı gradyan TD yöntemlerinin kararsızlığı olarak ortaya çıkmaktadır.Güçlü işlev yaklaşımı,off-policy öğrenme ve bootstrapping yapan TD yöntemlerinin verimliliği ve esnekliğini araştırıyoruz fakat bu ölümcül üçlünün üç yönünü tek bir algoritmada, kararsızlık potansiyelini ortaya çıkartmadan birleştirmek zor.

off-policy öğrenmenin tüm alanları nispeten yenidir ve daha oturmamıştır. Hangi yöntemlerin en iyi veya yeterli düzeyde olduğu henüz net değilidir. Bu bölümün sonunda ortaya konan yeni yöntemlerin karmaşıklıkları gerekli midir? Varyans indirgeme yöntemleri ile hangileri etkili bir şekilde birleştirilebilir? off-policy’nin öğrenme potansiyeli hala bir gizeme (anladığım kadarıyla gizemden kasıt genel yapay zeka) ulaşmanın en iyi yolu olarak cesaretini koruyor.

