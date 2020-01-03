---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 14: Psychology"
description: " "
date:   2019-01-14
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/policy-gradient-methods-bolum-13
next-page-url: /blog/pekistirmeli-ogrenme/neuroscience-bolum-15
---
__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.Bölüm hakkında açılmış bir issue varsa tekrar açmayınız.*__


## Psychology

Bu bölümün amacı pekiştirmeli öğrenme ile hayvan öğrenmesinin birbirleri ile olan ilişkilerini incelemektir. Psikoloji bilimi her ne kadar düşünme ve sorgulama gibi alanlara kaysa da bilinçsel işlemenin bazı alanları pekiştirmeli öğrenmenin hesaplama perspektifi ile bağlantılıdır.

## 14.1. Tahminleme ve Kontrol
Bu kitapta anlatılan algoritmalar tahminleme ve kontrol olmak üzere iki ana kategoride toplanmıştır. Tahminleme algoritmaları, ajanın bulunduğu ortamdaki niteliklerin zaman içinde nasıl gelişeceğinin beklentisine bağlı olan nicelikleri tahminler. Özellikle ajanın alacağı ödüle odaklanmış olarak, tahminleme algoritmaları "politika değerlendirme algoritmaları" rolünü üstlenmekle kalmayıp ortamın tüm niteliklerini tahminlerler. Tahminleme algoritmaları ile klasik koşullanma arasındaki ilişki ödül veya ceza olmasına bakmaksızın bir sonraki uyarıcıyı tahminlemektir. Oysa edimsel koşullanmada hayvanın ne yaptığına bağlı olarak sevdiği (ödül) veya sevmediği (ceza) bir şey verilir. Hayvan aldığı ödül veya cezaya göre davranışını değiştirmeyi öğrenir. Klasik koşullanmanın aksine, takviyeli uyarıcının hayvanın davranışına bağlı olduğu söylenir. Pekiştirmeli öğrenmenin politika gleiştirme algoritmalarına karşılık gelen Kontrol, bu tür öğrenmenin temelini oluşturur. 
Klasik koşullanmanın Tahminleme, edimsel koşullanmanın Kontrol olduğunu düşünürerek pekiştirmeli öğrenmeyi hayvan öğrenmesine bağlasak da gerçekte durum çok daha karmaşıktır. Psikolojide pekiştirme ifadesi orjinale bir davranışın güçlendirilmesi olarak kullanılsa da sıklıkla zayıflatılması anlamında da kullanılır.

## 14.2. Klasik Koşullanma
Klasik yada Povlov Koşullanmasında, başlangıçta nötr olan bir uyarıcı (zil sesi), hayvanın koşulsuz tepkiye (ağzının sulanması) sebep olan koşullu uyarıcıyı (yemek) hatırlatması ile koşullu uyarıcı haline dönüşür. Önce nötr uyarıcı devam ederken (zil çalarken) koşulsuz uyarıcı (yemek) verilirse Geickmeli Koşullanma, Nötr uyarıcıdan sonra koşulsuz uyarıcı veririlse İzli Koşullanma gerçekleşir.
Gecikmeli Koşullanma: 
Nötr Uyarıcı: XXXXXX______ (zil sesi)
Kşsz Uyarıcı: ________XX (yemek)
İzli Koşullanma
Nötr Uyarıcı: XXXXX_________ (zil sesi)
Kşsz Uyarıcı: ________XX (yemek)
US: Unconditined Stimuli, Koşulsuz Uyarıcı, yemek
UR: Unconditined Response, Koşulsuz Refleks, yemek ile oluşan salya
CS: Conditioned Stimulus, Koşullu Uyarıcı, zil sesi
CR: Conditioned Response, Koşullu Refleks, zil sesi ile oluşan salya
## 14.2.1. Engelleme ve Üst Düzey Koşullanma (sf286-287)
Engelleme birden fazla uyarıcının olduğu durumda bir koşullu uyarıcının diğerini baskılayarak koşullu şartlanmaya izin vermediği durumları ifade eder. Üst Düzey Koşullanmada ise, havyanın koşullandığı bir uyarıcı ile koşullanmadığı bir (veya daha fazla) uyarıcının birlikte verilmesi sonucu koşullanmadığı uyarıcıya da koşullanması durumudur. Ancak ikinin üzerindeki çoklu uyarıcıların pekiştirme değeri, uyarıcının her defasanıda ödül/ceza ile birlikte verilmemesi sebebiyle düşmektedir. 
Araçsal Koşullanmada (bağlaşım kuramı) da birden fazla uyarıcı durumu oluşur. Birincil pekiştiriciyi çağrıştıran uyarıcının kendisi pekiştirici haline dönüşürken birincil uyarıcı ikincil uyarıcıya (veya üst seviye) dönüşür. Koşullu pekiştirme ise sahip olduğumuzda yapacaklarımızı çağrıştıran, koşullu pekiştireç olan para için neden çalıştığımızı açıklar.
## 14.2.2. Rescorla-Wagner Modeli (sf287-289)
Bu model klasik koşullanmanın engelleme kavramı (yada bloklama) üzerine geliştirilmiştir. Modelin ana fikri, hayvanın sadece beklentilerinden farklı sonuçlar elde ettiğinde, yani şaşırdığında öğreniyor olmasıdır. 
Bir çok bileşenli uyarandan oluşan bir bileşik Koşullu Uyarıcı klasik şartlanma deneyinde, "toplam ilişkisel güç" olarak adlandırılan, her bir uyarıcının ilişkisel gücü, her bileşenin kendisinin ilişkisel gücünde değil, tüm bileşik uyarıcılar ile ilişkili bir ilişkisel kuvvete bağlı olarak değişir. (Başka bir deyişle, birden fazla uyarıcının bulunduğu bir öğrenme ortamında uyarıcıların gücü her bir uyarıcının kendi gücü ile değil, tüm uyarıcıların bileşik gücü ile ilişkilidir.) Modelin en önemli varsayımı, uyarıcıların bileşik ilişkisel kuvveti, her bir bileşenin ayrı ilişkisel güçlerinin toplamına eşit olmasıdır. 
*** DETAY ***
Örnek:
Yeni bir köpek edindiğimizi düşünelim. Köpeğimiz evin kapı zilini ilk kez duyduğunda kapı zili ile kapıda birisinin olacağı ilişkisi sıfır olacaktır. Ancak bir süre sonra her kapı zili çalışında birisinin geliyor olması sonrasında bu ilişki öğrenme sürecinde 0'dan 100'e çıkacaktır. Zil haricinde kapının tıklaması da aynı öğrenme süreci geçerlidir. Her iki uyaranın da öğrenme süreci devam ederken, örneğin, zil 20, tıklama 10 seviyesindeyken kapı hem tıklanıp hem de zile basılırsa bu durumda ikisinin toplamı 30 olacaktır.
Bileşik uyaranların güçlerindeki ilişkisel değişim aşağıdaki formül ile ifade edilmektedir.
Burada A daha önceden deneyimlenmiş bir uyaran (kapı zili), X de yeni deneyimlenen bir uyaran (kapının tıklanması) olabilir. Y ise A ve X uyaranlarını takip eden bir durum (birisinin gelmesi), Koşulsuz Uyarıcı'yı ifade etmektedir. VA ve VX, A ve X uyaranlarının ayrı ayrı; VAX ise ikisinin aynı anda olması durumundaki güçlerini ifade etmektedir. ve adım büyüklüğü parametresi (öğrenme hızını), (RY - VAX) değeri ise tahminleme hatasını ifade etmektedir.
A uyaranının gücündeki değişim, Y durumunun gerçekleşmesi ile köpeğin beklentisi arasındaki fark çarpı öğrenme hızı olmaktadır. Yani kapı zili çaldığında (A) kapıda birisi varsa (Y) ve köpeğin beklentisi (VA) yoksa A uyaranının gücündeki değişim (100-0)öğrenme hızı olacaktır. Tersi durumda, kapı zili çaldığında köpeğin beklentisi 100 ise ancak kapıda kimse yoksa A uyaranın gücü (0-100)öğrenme hızı kadar değişecektir. Köpeğin kapı zilini (A) öğrenmiş ve zil çaldığında birisinin gelmiş olması beklentisi VA=100 ise, ve zil çaldığında birisi gelmiş ise -sürpriz yok-, RY=100 bu durumda A uyaranın gücündeki değişim dVA = (100-100)*öğrenme hızı = 0 olacaktır. Böylece önceki öğrenilen bilgi, yeni öğrenmeyi bloklamış olmaktadır.
Her bir denemenin d boyutlu bir vektör ile gösterildiğini varsayalım. 
x(s) = (x1(s), x2(s), ..., xd(s))T
Koşullu Uyarıcı'nın bulunduğu durumlar 1, bulunmadığı durumlar 0 olsun. d boyutlu vektörün ilişkisel gücü w ise, s durumunun bileşik ilişkisel kuvveti;
olur. Bu pekiştirmeli öğrenmede değer tahminleme'ye karşılık gelir ve bunu Koşulsuz Uyarıcı tahminlemesi olarak düşünürüz.
t'nin deneme sayısı olduğunu kabul edersek, t denemesi sonrasında wt vektörünün wt+1 olarak güncellenmesi aşağıdaki şekilde gerçekleşir.
burada adım büyüklüğü parametresi, tahminleme hatasını göstermektedir. 
Makine öğrenmesi açısından Rescorla-Wagner modeli hata düzeltmeli eşlikli öğrenmedir, en küçük ortalama kareler (Least Mean Square) ile aynıdır. Model mükemmel ya da eksiksiz bir klasik koşullanma modeli değildir.
*** /DETAY ***
## 14.2.3. Zamansal Fark (Temporal Difference) Modeli (sf289-290)
Zamansal Fark modeli deneme bazlı olan RW modelinin aksine zaman bazlıdır. RW modelinde her bir t denemesi uyaranın ne şekilde verildiğinden bağımsız olarak verilip verilmediği ile ilgilenir. Zamansal Fark modelinde ise uyaranın ne şekilde ve nasıl bir zaman aralığında verildiği önem kazanmaktadır.
Bu modelde t RW deki gibi öğrenme denemelerini değil zamanı ifade etmektedir. Varsayalım ki t ve t+1 durumları arasındaki süre 0.01 sn, her bir öğrenme denemesi ise her bir zaman dilimi ile ilişkili durumlar dizisi olsun ve t adımındaki durum koşullu uyarıcının deneme esnasında mevcut olup olmadığını belirten bir gösterge olmak yerine uyaranın ne şekilde gösterildiğini göstersin. Hayvan açısından baktığımızda her biri öğrenme denemesi hayvanın dünya ile olan deneyimlerinden ibarettir.
*** DETAY ***
TD modelinde öğrenme
şeklindedir. Burada RW modelindeki x(St) yerini zt almıştır ve RW modelinde tahminleme hatasıyken burada TD hatası’dır;
Burada 0-1 arasında bir indirgeme katsayısı, Rt t anındaki tahmin hedefi, ve de t ve t+1 adımındaki bileşik ilişkisel kuvveti ifade etmektedir.
zt ise uygunluk izleri vektörüdür (chapter 12). 
*** /DETAY ***

## 14.2.4. Zamansal Fark Model Simülasyonları (sf290-297)
Biden fazla uyarann zaman içerisinde bir seri halinde verildiği durumlarda uyaranlar aynı anda yada birbirlerini takip eder bir şekilde verilmeyebilir. Gerçek zamanlı koşullanma modelleri uyaranların ne şekilde verildiklerini göstermek açısından önemlidirler. Bu modeller uyaranların denemeler arasında nasıl değiştiklerini ve indirgeme ve uygunluk izleri ile nasıl ilişkili olduklarını göstermektedirler.
Aşağıda TD modelinin davranışlarını gözlemlerken kullanılan üç farklı uyaran gösterim şekline yer verilmiştir. Tümleşik Seri Bileşen (Complete Serial Compound) , MikroUyaran, Mevcudiyet. TSB de uyaranın varlığı zaman içerisinde birbirini takip eden sinyaller şeklinde gösterilir. MU’da gösteriminde her dış uyaran bir iç uyaranı tetikler ve bu iç uyaranların etkileri TSB’de olduğu gibi ardısıra değil, zaman içerisinde etkilerin azalan ve birbiri üzerine binecek şekilde sönümlenen sinyaller halindedir. Mevcudiyet ise sadece uyaranın var olup olmadığının 1 ve 0 olara ifade edildiği bir gösterim şeklidir. Bu haliyle bile Zamansal Fark modeli klasik şartlanmada görülen birçok zaman olgusunu oluşturabilmektedir.
TSB modelindeki sorunlardan bir tanesi farklı uyaranların bloklama etkisidir. Farklı uyaranların farklı zamanlarda birlikte verilmesi öğrenme deneyiminde farklılaşmalara sebep olmaktadır. Önce A’nın verilip ardından A kaldırılıp B uyaranınnı verilmesi durumunda B’nin olmadığı örneklerde A’nın ilişkisel gücü daha düşük ölçülmüştür.
Simülasyonlar
Aşağıda A ve B uyaranlarının farklı zaman ve sürelerde verilmesi durumunda bir uyaranın ortamda bulunup bulunmamasına göre diğer uyaranın ilişkisel gücünü (wCSA, wCSB), ve toplam ilişkisel gücü w gösteren grafikler yer almaktadır.
## 14.3. Araçsal Şartlandırma (sf297-301)
Klasik koşullanma deneylerinin aksine araçsal şartlanmada hayvanın davranışı ön plandadır. Uyaranın verilmesi hayvanın davranışının sonucuna bağlıdır. Hayvan yaptığı bir davranışın sonucunda bir uyarıcı alır, bu uyarana göre davranışını sürdürür ya da vazgeçer. Araçsal koşullanma genellikle operant koşullanma olarak değerlendirilse de aralarında farklılıklar bulunmaktadır.
Pekiştirmeli öğrenme algoritmalarının özellikleri bu kuramın temellerini oluşturan Thorndike’ın ,daha çok deneme yanılma olarak bilinen, Etki Yasası’ndan esinlenmektedir. Etki Yasası’nda öğrenme arama ve hatırlama şeklinde açıklanır. Arama her bir durumda birçok aksiyon arasından uygun olanı seçmek, hatırlama ise durumlar ile o durumdaki en iyi aksiyonu ilişkilendirme şeklinde açıklanmaktadır. 
Araştırmalar aksiyon seçiminin ne kadar tesadüfi ve ne kadar yardım olarak olacağı konusunda farklı yaklaşımlara sahiptir. Pekiştirmeli öğrenmede e-greedy ve üst güven eşiği gibi yaklaşımlar kullanılır. Thorndike’ın deneylerinde yaptığı incelemelerde hayvanların içgüdüsel olarak yaptığı rastgele davranışların tamamen rastgele olmadığı, makul harekeler arasında rastgele olduğu gözlemlenmiştir. Diğer yandan hayvanların içgüdüsel davranışlardan birisini seçmek yerine içinde bulunduğu durumun kapsamına uygun olan içgüdüsel hareketler içerisinden keşif yaptığı düşünülebilir.
Skinner’ın ortaya attığı operant koşullanmaki operant, alınan aksiyonun hayvanın çevresi üzerindeki etkilerini vurgulamaktadır. Skinner etki yasasını tümüyle onaylamamış, ilişkisel bağlantıya karşı çıkarak kendiliğinden spontan bir şekilde yapılan davranışlardan seçim yapmayı vurgulamıştır.
Skinner’ın bir diğer katkısı da istenilen davranışların birbirini izleyen yaklaşımlarını güçlendirerek bir hayvanı eğitme süreci olan “şekillendirme” kavramıdır. Basit bir problemden başlayıp zorluk seviyesini öğrenme süreci boyunca artırarak ilerleme öğrenmeyi hızlandırmak verimli bir yaklaşım olmaktadır.
Araçsal şartlanmadaki bir kavram da motivasyondur. Motivasyon davranışın yönünü ve gücünü veya coşkusunu etkiler. Pekiştirmeli öğrenme ile motivasyonu doğrudan ilişkilendirmek zor olsa da bazı güçlü bağlantılar mevcuttur. Örneğin ajanın motivasyonu uzun vadede aldığı toplam ödülü maksimize etmek üzerinedir. Bir diğeri de ajanın değer fonksiyonları ile bir sonraki aksiyonlardan en yüksek değere sahip sonraki adımlara yönlendiren aksiyonu seçmesidir.
Motivasyonun bir diğer boyutu ise, motivasyon durumu sadece öğrenmeyi değil, hayvanın öğrenmeden sonraki davranışının gücünü ve coşkusunu da etkiler. Örneğin bir labirentin içerisindeki yemeği bulmayı öğrenen farelerden aç olan tok olana göre daha hızlı koşacaktır.
## 14.4. Gecikmeli Pekiştirme (sf301-302)

Etki yasasının bağlantılar üzerinde geriye dönük bir etkisi vardır, ve yasanın ilk eleştirileri bugünde olan bir olayın geçmişi nasıl etkilediğini açıklayamamasıdır. Benzer şekilde öğrenme aksiyon ve aksiyonu takip eden ödül arasındaki zaman farkı olmasına rağmen öğrenme gerçekleşebilmektedir. Bu kitapta yer alan Pekiştirmeli Öğrenme algoritmaları bu problem için basit yöntem içermektedir. Uygunluk İzleri (Eligibility Traces) ve Zamansal Fark (Temporal Difference).
Pavlov’a göre her uyaran zihinde bir süre iz bırakır ve bu iz öğrenmeyi mümkün kılar. Buna “İze Koşullanma” denir Edimsel koşullanmada da uyaranların bıraktığı izler hareketler ve takip eden ödül/ceza arasındaki köprüyü oluşturmaktadır. Hull’ın teorisinde pekiştiricinin zaman aralığı arttıkça araçsal koşullanmanın gücündeki azalışı açıklamaktadır. Bu kitapta anlatılan uygunluk izleri de Hull’ın anlattıkları gibidir: geçmiş durum ziyaretlerinin veya durum-hareket ikililerinin azalan izleridir. Deneylerde görülmüştir ki, gecikme süresi boyunca şartlar koşullu pekiştiricinin gelişmesine olanak sağlamışsa, yani gecikme süresince uyaran varlığı devam ediyorsa, gecikmenin artması öğrenmeyi engelleyici bir ikincil pekiştireç kadar azaltmamıştır.

## 14.5. Bilişsel Haritaları (tureng:psikoloji) (sf302-303)
Model bazlı pekiştirmeli öğrenme algoritmaları pisikologların “bilişsel haritalar” olarak ifade ettikleri kavram ile ortak elemanlara sahiptirler. Planlama ve öğrenme bölümünde anlatıldığı gibi çevre modeli ile ajanın aldığı aksiyonlara karşılık çevrenin durum değişikliği ve ödül/ceza açısından nasıl tepki vereceği, öğrenme ile de bu modelden bir politika hesaplayan tüm süreçler anlatılmak istenmektedir. 
Hayvan öğrenmesinde önemli sorulardan birisi de hayvanların öğrenirken bir çevre modeli kullanıp kullanmadıkları, kullanıyorlarsa bu modeli nasıl öğrendikleridir. Bazı araştırmacılar, “Gizli Öğrenmeyi” göstererek öğrenme ve davranışın uyarıcı-tepki (S-R) görüşüne karşı çıkıyorlardı. Edward Tolman ile ilişkilendirilen Gizli Öğrenmede, hayvan ödül olmasa da çevrenin bilişsel haritasını öğrendiğini, ve daha sonra bu haritayı amaca ulaşmak için kullanabildiğini açıklamaktadır. Modern yaklaşımda bilişsel haritaler mekansal olarak kısıtlanmamakta, daha çok çevresel modeller veya hayvanın görev alanı modelini (task space model) kapsamaktadır. Gizli Öğrenme’nin bilişsel harita açıklaması hayvanlarn model bazlı algoritmalar kullandığını ve ödül/ceza olmasa da çevresel modelleri öğrenebildikleri ifade eder.
Tolman hayvanların çevrelerini birbirini izleyen uyaran-uyaran ilişkileri ile öğrendiklerini açıklar. Birbirini izleyen S-S’ (durum-sonraki durum) çiftlerinde S gözlemlendiğinde model S’ durumu için bir beklenti oluşturur. Buna aksiyonu da ekleyince SA-S’ haline dönüşür. Ödül açısından bakarsak bir durumda alınan aksiyon sonucunda kazanılacak ödül SA-R şeklinde ifade edilir. Bunların tamamı ajanın çevreyi araştırırken ödül alsa da almasa da bilişsel benzeri haritalar oluşturabileceği eşlikli öğrenmedir.

## 14.6. Alışkanlıksal ve Amaç Odaklı Davranış (sf303-306)
Pekiştirmeli öğrenmedeki model bazlı ve model tabanlı ve model tabanlı olmayan pekiştirmeli öğrenme algoritmaları psikolojideki alışanlık ve amaç odaklı davranış modeline denk gelmektedir. Alışkanlıklar uygun uyarıcılar karşısında gösterilen davranış desenleri olup hemen hemen otomatik olarak karşımıza çıkarlar. Amaç odaklı kontrol çevresel değişimlere çok daha kolay uyum sağlama avantajına sahipken, alışkanlıksal davranış bilinen bir çevrede çok daha hızlı cevap vermeyi sağlar, ancak çevredeki değişikliklere hızlı uyum sağlayamaz. Model bazlı algoritmalar durum-aksiyon ikililerinin değerlerine göre en uygun durumu seçerken model bazlı olmayan bir strateji aksiyon değerleri yerine en uygun politikayı seçecektir.
Model tabanlı olmayan algoritmalarda fare labirenti birçok kez ödülü bulana kadar baştan sona gitmeli ve politikasını ve/veya hareket-değer fonksiyonunu güncellemesi gerekecek. Model tabanlı ajan ise kendi kişisel deneyimine ihtiyaç duymadan çevresindeki değişikliklere uyum sağlayabilir. Modelindeki bir değişiklik (planlama yolula) politikasını değiştirmesini sağlar. Planlama sayesinde değişikliklerin sonuçlarını hiç ilişkilendirilmese de saptayabilir.
Gizli Öğrenme deneylerinde olduğu gibi ödülün bir durumdan diğerine değiştiği “Çıktı değer düşüklüğü” deneyleri, hayvanın bir alışkanlık mı öğrendiği yoksa davranışının amaç odaklı mı olduğu sonucunu vermektedir. Fareler ile yapılan bir deneyde fareler bir manivelaya basarak şeker almak üzere eğitilirler. Daha sonra manivelaya basmadan çeker alabilecekleri şekilde 15 dk serbeset bir şekilde şeker almalarına izin verilir. Ardından farelerin bir kısmına mide bulantısı verecek bir ilaç enjekte edilir. 3. takrar sonrasında enjekte edilen fareler şeker yemezler, şekerin ödül değeri düşürülmüş olur. Bir sonraki gün enjekte edilen ve edilmeyen fareler manivelanın bulunduğu ancak şeker vermediği şekilde tekrar aynı odaya konulur. Enjekte edilen farelerin belirgin şekilde daha düşük yanıt oranları olduğu görülür. Sonuç olarak fareler manivelaya basıp mide bulantısı ile karşılaşmamalarına rağmen, manivela ile şekeri, şeker ile de mide bulantısını ilişkilendirmişlerdir.
Model bazlı ve model bazlı olmaya algoritmaların her ikisini de kullanmak için sebepler vardır. Yeterli tekrar ile amaç odaklı davranış alışkanlığa döner. Fareler ile yapılan bir başka deneyde iki grup fare 100 ve 500 kez ödül alacak şekilde eğitilmişlerdir. Ardından şekerlerin ödül değerleri düşürülmüş (farelere mide bulantısı enjekte edilerek) ve fareler tekrar odaya alınmıştır. Sonuç olarak normal düzeyde eğitilen farelerde, aşırı eğitilen farelere oranla değer düşürülmesi manivelaya çok daha az basılması sonucunu üretmiştir. Aşırı eğitilen farelerde ise çok daha az etkili olmuştur. Yani normal eğitilen fareler amaç odaklı hareket ederken fazla eğitilen fareler alışkanlık odaklı hareker ediyorlar.
Daw, Niv ve Dayan (2005)’e göre hayvanlar hem model bazlı hem de model bazlı olmayan süreçler kullanırlar. 

## 14.7. Özet (sf306-312)


Terimler için kullanılan kaynaklar:
https://egitimvaktim.com/dosyalar/2011/04/klasik-tepkisel-kosullanma.pdf
http://www.kpsskonu.com/egitim-bilimleri/ogrenme-psikolojisi/klasik-kosullanma-ilkeleri-2/
http://www.kpsskonu.com/egitim-bilimleri/ogrenme-psikolojisi/klasik-kosullanma/
http://www.psikolojisozlugu.com/secondary-reinforcement-ikincil-pekistirme
