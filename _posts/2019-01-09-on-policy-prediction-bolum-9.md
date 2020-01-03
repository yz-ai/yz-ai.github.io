---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 9: Yaklaşıklama İle Politikalı Öngörü"
description: "Bu çalışma, Richard Sutton ve Andrew Barto tarafından kaleme alınan RL: An introduction (Sutton, R. S., & Barto, A. G. 2018) kitabının çeviri ve özetini barındırmaktadır."
date:   2019-01-09
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title
prev-page-url: /blog/pekistirmeli-ogrenme/tabular-metotlar-bolum-8
next-page-url: /blog/pekistirmeli-ogrenme/on-policy-control-bolum-10
---


## Yaklaşıklama İle Politikalı Öngörü 

Bu bölümde değer fonksiyonu $$v_\pi$$ daha önce anlatılan kısımlardan farklı olarak, tablo olarak değil, yaklaşıklık olarak tanımlanacaktır. Bu fonksiyon kimi zaman doğrusal kimi zaman çok boyutlu bir fonksiyon olabilir. Genellikle bu yaklaşıklık, çok katmanlı bir sinir ağıyla tanımlanmaktadır. Bu noktada pekiştirmeli öğrenmeye, derin ön takısını eklememiz mümkün olmaktadır. Keza, problemimizin yapısı ve durum uzayının karmaşıklığına göre ilgili sinir ağının derinliği evrişimli sinir ağlarıyla kuvvetlendirilebilir.
Bu yaklaşımın en temelde çözmeyi hedef edindiği problemler, durum uzayı çok büyük olan problemlerdir. Yaklaşıklık kazandıran fonksiyonun $$w$$ ağırlıkları, durum uzayı tanımlarından çok daha küçük olacaktır $$(d<<|S|)$$.

## Değer-Fonksiyonu Yaklaşıklama (Value-Function Approximation)

Önceki bölümlerde, durum için değerler tablo üzerinden güncellendiği için basit bir fonksiyon olarak karşımıza çıkmaktaydı. Şimdi bu güncellemeyi, durum uzayının çok büyük olduğu durumları da kapsayacak şekilde daha karmaşık bir şekilde yapabiliriz. Geleneksel makine öğrenmesi metotlarında giriş ve çıkışın belli olduğu yaklaşımlarda denetimli öğrenmeyi (supervised learning) kullanmamız mümkün olmaktadır. Bu metotlardaki çıkışlar sayısal olduğu zaman bu yönteme, fonksiyon yaklaşıklama (function approximation) denmektedir. Pekiştirmeli öğrenme için bu metoda değer-fonksiyonu yaklaşıklama denmektedir. Sonuçta elde edilen sistem, giriş olarak durum, çıkış olarak değeri vermektedir.

Bu şekilde her güncellemeyi bir eğitim olarak görürsek, denetimli öğrenme’nin nimetlerinden faydalanabiliriz. Fakat bir çok denetimli öğrenme yöntemi eğitim setinin, defalarca ağ üzerinde eğitilmesi ile elde edilmektedir. Pekiştirmeli öğrenme için ise, eğitim çevrimiçi (online) yapılabilmelidir. Yani kademeli bir şekilde öğrenilen değerlerden etkili bir güncelleme yapılabilmelidir. Daha önce de bahsedildiği gibi, pekiştirmeli öğrenme durağan olmayan problemler ile yakın temas halindedir. Kullanılacak değer fonksiyonu yaklaşıklığı da bu gibi problemler için hazırlıklı olmalıdır.

## Değer Öngörüsü (Value Prediction)

Değer fonksiyonu yaklaşıklığı, tüm durumlara aynı değeri veremeyeceği, genel bir yapıda olacağı için bazı durumları diğerlerinden önemli kılmak şarttır. Bu sebeple bir durum dağılımı oluşturmamız gerekir.

$$
\qquad \mu(s) \geq 0 , \qquad \sum\mu(s) = 1
$$

Olacak şekilde, bu dağılım bize her durumdaki hatanın ne kadar “umurumuzda” olduğunu söyleyecektir. Buradaki hata değerimiz, değer fonksiyonu yaklaşıklığı $$\tilde{v}(s,w)$$ ile gerçek hata $$\tilde{v}(s)$$ değeri arasındaki kök ortalama hata (root mean square) farkıdır.  $$\overline{VE}$$ ile gösterilir.

$$
    \qquad \overline{VE}(w) \dot{=} \displaystyle\sum\limits_{s\epsilon{S}}\mu(s)\bigg[v_{\pi} - \tilde{v}(s,w)\bigg]^2 . \qquad(9.1)
$$

Bu eşitlik bize, gerçek değerler ile yaklaşık değerler arasındaki farkı verecektir ve genelde hata gösterimi için bu grafik kullanılır. Şunu da burada anımsamakta fayda var, $$\overline{VE}$$  pekiştirmeli öğrenme için performans ölçütü olmayabilir. Öncelik hedef politika belirlemek olduğu için, en iyi değer fonksiyonu yaklaşıklığı için $$\overline{VE}$$’yi minimize etmenin şart olduğu söylenemez fakat şu an alternatifi bulunmadığı için bunun üzerinden ilerlenecektir.

Yapay Sinir Ağları ve Karar Ağaçları gibi karmaşık değer fonksiyonu yaklaşıklıkları genellikle yerel optimuma yakınsamaktadır. Doğrusal olmayan değer yaklaşıklıklarında lokal optimum genellikle kabul edilebilmektedir. Nitekim bir çok yapay zeka yapısının mutlak en iyi’ye yakınsayacağı kesin bir şekilde söylenememektedir.

Takip eden bölümlerde gradyan prensipleriyle değer fonksiyonu yaklaşıklıkları yöntemleri incelenecektir.

## Rastgele Gradyen ve Yarı Gradyen Yöntemler

Değer Fonksiyonu Yaklaşıklığı yöntemlerinde Rastgele Gradyen Düşümü (SGD-*Stochastic Gradient-Descent*) sıklıkla kullanılmaktadır. Bu yöntemde $$w$$ ağırlıkları gerçek değerli bir vektördür. Her bir zaman değeri için bu ağırlıklar güncellenecektir. Öncesinde belirtildiği gibi, bu yaklaşıklık tüm durumlara tam doğru değeri veremeyecektir. Zira tüm durumların değerlerini öğretemeyeceğimiz gibi, rastgele seçilecek durumlarla fonksiyonu eğiterek, genelleştirilmiş bir sonuç bulunmaya çalışılacaktır.

Yaklaşıklık, gözlemlenen rastgele durumların değerleri ile eğitilerek, $$\overline{VE}$$ hatası minimize edilmeye çalışılmaktadır. Bu eğitim makine ve derin öğrenme uygulamalarında sıklıkla kullanılan SGD ile sağlanılabilir.

$$
    \qquad w_{t+1} \dot{=} w_t+\alpha\displaystyle[v_\pi(S_t)-\tilde{v}(S_t,w_t)\displaystyle]\triangledown\tilde{v}(S_t,w_t)   
$$

Bu formülasyonda $$\alpha$$ değeri adım büyüklüğünü temsil etmekle beraber, $$\triangledown f(w)$$ fonksiyonu ağırlıkların türevini belirtmektedir. Bu türev SGD’nin gradyen düşümünü belirlemektedir. SGD, çok küçük adımlarla ilerlemektedir. İlk başta bu istenmeyen bir durum gibi gözükse dahi, nihayetinde tüm örnekleri kapsayacak bir fonksiyon yaklaşıklığı için bu gereklidir. Bu sayede SGD bir yerel optimuma kesinlikle yakınsayacaktır. Lakin politika her bir adımdaki durumun değeri çevreyle etkileşimden alınan durum değeri ile aynı olmayabilir. Bu sebeple $$v_\pi(S_t)$$ yerine yanlı olmayan yaklaşık $$U_t$$ değeri konulabilir. Bu sayede formül şu şekilde güncellenebilir:

$$
    \qquad w_{t+1} \dot{=} w_t+\alpha\displaystyle[U_t-\tilde{v}(S_t,w_t)\displaystyle]\triangledown\tilde{v}(S_t,w_t) \qquad(9.7)
$$

Fakat bu şekilde kullanılan formül, politikanın değerine yakınsamayabileceği için tam gradyen düşümü sağlamayacaktır. Buna Yarı Gradyen Düşümü denmektedir. İlk bakışta Yarı Gradyen düşümü, tam yaklaşıklık sağlamıyor gibi görünse de ilerleyen bölümlerde sağladığı iyileştirmeler fark edilecektir. Zira amaç öğrenimin sürekli ve çevrimiçi olmasını sağlamaktadır. 

Ek olarak, Durum Toplanması (state aggregation) fonksiyon yaklaşıkları için genelleştirici bir yöntemdir. Her bir durum grubunun bir yaklaşık değeri olur. Durumun değeri, bağlı olduğu grup ile belirlenir ve durum değişiklikleri grubun değerini etkiler. Bu SGD’nin özel bir durumudur ve gradyen, $$\triangledown\tilde{v}(S_t,w_t)$$, $$S_t$$’nin grubunun elemanı için 1; olmayanı için 0 olur.

## Doğrusal Yöntemler

Fonksiyon yaklaşıklığının en önemli durumlarından biri $$\tilde{v}({*},w)$$ yaklaşıklığının $$w$$ ağırlıklarına göre doğrusal olmasıdır. Her bir $$s$$ durumu için gerçek değerli bir vektör vardır, $$x(s)\dot{=}(x_1(s), x_2(s), ..., x_d(s))^T$$ bu vektör $$w$$ ağırlık vektörü ile aynı eleman sayısına sahip olacaktır. 

$$
    \qquad \tilde{v}(s,w) \dot{=} w^Tx(s) \dot{=} \displaystyle\sum\limits_{i=1}^{d}w_i x_i(s)  \qquad(9.8)
$$

$$x_i(s)$$ öznitelik vektörü olarak isimlendirilir. Bu fonksiyonun durumlar için verdiği her bir değer birer özniteliktir. Yine benzer şekilde doğrusal fonksiyon yaklaşıklığı için SGD kullanılabilir.

$$
    \qquad w_{t+1} \dot{=} w_t+\alpha\displaystyle[U_t-\tilde{v}(S_t,w_t)\displaystyle]x(S_t).   
$$

## Doğrusal Yöntemler için Öznitelik İnşası

Doğrusal yöntemler hem hız hem yaklaşıklık konusunda çok etkilidir. Pekiştirmeli öğrenme sistemlerinin alan bilgisini öğrenmesi için öznitelik inşası önemli bir kısım teşkil etmektedir. Yaklaşıklığı genelleştirmek için bu yöntemler önem taşır.

### Polinomlar

Bir çok problemin durumu sayısal olarak ifade edilebilir. Bu problemlere “sopa dengeleme”, “kumarcı problemi” örnekleri verilebilir. Bu gibi problemler için pekiştirmeli öğrenme, bağlanım (regression) ve enterpolasyon (interpolation) çözümleri ile benzeşmektedir. 

Örnek olarak, iki boyutlu bir problem düşünebiliriz. $$s$$ durumunu iki boyutlu olarak $$s_1$$ ve $$s_2$$ olarak isimlendirebiliriz. Burada öznitelik fonksiyonunu en basit şekliyle $$x(s) = (s_1, s_2)^T$$ olarak tanımlayabiliriz. Fakat böyle tanımlandığı müddetçe iki boyutun birbirine olan etkisini göz önüne almamış olacağız. $$x(s) = (1, s_1, s_2, s_1 s_2)^T$$ olarak gösterirsek, paralel fonksiyon olması durumunu 1 ve iki boyutun etkileşimlerini “çarpım” ile dikkate almış oluruz. Burada iki boyutu çoğaltarak yüksek boyutlu etkileşimlerde elde etmemiz mümkündür.

  $$x(s) = (1, s_1, s_2, s_1 s_2, s_1^2, s_2^2 ,s_1^2 s_2, s_1 s_2^2, s_1^2 s_2^2)^T$$

Karmaşık fonksiyonları yüksek seviyeli polinomları temsil etmek daha kolay olmaktadır. Fakat boyut etkileşimleri sınırsız olabileceği için, bu etkileşimlerin bir alt kümesini seçmek uygun olacaktır. 

### Fourier

Bir diğer doğrusal yöntem ise, fonksiyon yaklaşıklığını Fourier serileriyle tanımlamaktır. Standart Fourier serisi, $$\tau$$ periyotlu ve $$\tau$$ periyoduna tam bölünebilen periyotlu sinüs ve kosinüs serilerinin toplamlarıyla oluşturulur. Tek boyutlu Fourier özellik uzayı şu şekilde tanımlanabilir:

$$
    \qquad x_i(s) = cos(i \pi s), \qquad s \in [0, 1]
$$

Her durum $$k$$ boyutlu bir vektör ile tanımlansın, $$s=(s_1, s_2, ..., s_k)^T, s_i \in [0, 1]$$, i’nci özellik uzayı şu şekilde gösterilebilir:

$$
    \qquad x_i(s) = cos(\pi s^T c^i)   
$$

$$
    \qquad c^i=(c_1^i, c_2^i, ..., c_k^i)^T, \quad c_j^i\epsilon \{ 0, ..., n\}, \quad j=1, ..., k \quad i=0, ..., (n+1)^k   
$$

$$c^i$$ tamsayı vektörü, durum uzayının her bir boyutuna bir katsayı atanmasını sağlamaktadır. Örneğin $$c=(0, 0)^T$$ değerinde, bu özellik iki boyut için de sabit kalmaktadır.

Yarı Gradyen, TD(0) veya Sarsa yönteminde Fourier cosine özellikleri kullanılması durumunda her özellik için ayrı bir adım-boyutu kullanılması önerilmektedir.

Örnek olarak, $$x_i$$ özelliği için, $$\alpha_i = \alpha / \sqrt{(c_1^i)^2 + ... + (c_k^i)^2}$$  kullanılabilir.

Yine diğer doğrusal yöntemler gibi, durum boyut sayısı büyüdükçe, özellik uzayından bir alt küme seçmek uygun olacaktır. Fourier serisinin avantajı, $$c_i$$ vektörlerini düzenleyerek yaklaşıklığı ince ayara tabi tutmanın kolay olmasıdır.

### Kaba Kodlama

Kaba kodlama (Coarse Coding) olarak isimlendirilen yöntem, iki boyutlu bir durum uzayı üzerinde dairesel bölgelere tekabül eden bir özellik uzayı olarak düşünülebilir. Eğer bir durum ilgili özellik bölgelelerinin içerisindeyse ilgili özellik 1 değerini almakta, diğer özellikler 0 değerini almaktadırlar.

Doğrusal gradyen düşümü fonksiyon yaklaşıklığı olduğunu varsayarsak, her bir dairenin bir $$w$$ ağırlığı olacaktır. Herhangi bir durum eğitilirken, durumun bulunduğu yeri içine alan her daire, her $$w$$ güncellenecektir. Dairelerin boyutu, sayısı ve şekli yaklaşıklığı etkileyecektir.

### Kare Kodlama

Kare kodlama, kaba kodlamanın kare şeklinde olanı olarak düşünülebilir. Bu yöntemde farklı olarak, düzlem üzerinde parçalama, bir çok partisyon ile uygulanır. Bu yöntem evrişimli sinir ağları yapısındaki filtrelere benzemektedir. Her bir partisyon bir özelliği işaret eder.

Genelleştirme, partisyonların durum ile kesiştikleri noktada güncelleme yöntemi ile sağlanır. Aşağıdaki resimde, nokta durumu göstermektedir. Noktanın kesiştiği partisyonlar belirli bir yönteme göre güncellenerek genelleştirme sağlanır. Örneğin sol alt güncelleme yöntemi, tam köşegen yardımıyla sağlanmıştır.

![Kare kodlamada neden asimetrik kaymalar tercih edilir.]({{ site.url }}/assets/images/RL-sutton-ozet/sekil-91.png)

Kareye ek olarak, probleme göre farklı bir çok yapıda partisyon şekli seçilebilir.

### Dairesel Tabanlı Fonksiyonlar

Dairesel Tabanlı Fonksiyonlar (Radial Basis Functions), kaba kodlamanın sürekli değere sahip özellikleri genelleştirmeye yarar. Bu kez kaba kodlama ve kare kodlamadan farklı olarak özellikler $$[0, 1]$$ arasında istenen değere sahip olabilmektedir. Tipik bir RBF özelliği aşağıdaki şekilde gösterilebilir:

$$
    x_i(s)\dot{=}exp\bigg(-\displaystyle\frac{||s-c_i||}{2\sigma_i^2}\bigg) 
$$

RBF’in en temel avantajı, yaklaşıklıkların keskin olmaması ve türevi alınabilir olmasıdır. Dezavantajı ise işlemsel gereksiniminin fazla olması ve ince ayarının zor olmasıdır.

## Doğrusal Olmayan Fonksiyon Yaklaşıklıkları - Yapay Sinir Ağları

Yapay Sinir Ağları (YSA) fonksiyon yaklaşıklıkları için sıklıkla kullanılmaktadır. YSA Bir çok makine öğrenmesi problemine başarılı bir şekilde cevap vermektedir. Özellikle son dönemlerde katman sayısının artırılması ve Evrişimli Sinir Ağları/Kapsül Ağları gibi yeni yöntemlerle makine öğrenmesi altın çağını yaşamaktadır.

Yapay Sinir Ağlarının gizli katmanları, aslında daha önce bahsedilen özellik inşasını sağlamaktadır. Bu şekilde özelliklerin elle inşa edilmesine gerek olmamaktadır. Pekiştirmeli Öğrenme’de YSA değer fonksiyonlarını öğrenmek için TD hatasını kullanabilmekte, gradyen haydut ve politika gradyenini eğitmek için kullanılabilmektedir. Daha sonraki bölümlerde geriye yayılım algoritmaları dışında pekiştirmeli öğrenme özelinde sinir ağının nasıl eğitilebileceği konusunda çalışmalar paylaşılacaktır.

YSA’da dikkat edilmesi gereken nokta, çok katmanlı yapılarda aşırı öğrenme (overfitting) durumudur. Aşırı öğrenme genelleştirmenin karşısındaki en büyük problemdir. Derin öğrenme alanında bu mesele için için halihazırda bir çok mekanizma kullanılmaktadır.

YSA’larında sıklıkla ve başarıyla kullanılan bazı yöntemler şunlardır:

* Derin Anlama Ağları (Deep Belief Networks)
* Toptan Normalleştirme (Batch Normalization)
* Derin Artık Ağları (Deep Residual Networks)
* Derin Evrişimli Ağlar (Deep Convolutional Networks)

## En Küçük Kareler TD

Önceki bölümlerde, TD(0) metodu ile, doğrusal fonksiyon yaklaşıklıklarının TD sabit noktaya yakınsayacağını belirtmiştik:

$$
    w_{TD} = A^{-1}b, \quad A\dot{=}\mathbb{E}[x_t(x_t - \gamma x_{t+1})^T], b\dot{=}\mathbb{E}[R_{t+1}x_t] 
$$

Bu noktaya yakınsamak için iteratif yöntemden ziyade, bu değerlere tahmini bir değer hesaplayıp, sabit noktayı direkt hesaplayabiliriz. En Küçük Kareler TD (Least Squares TD) yöntemi bunu sağlamaktadır. 

$$
    \hat{A_t}\dot{=}\displaystyle\sum\limits_{k=0}^{t-1}x_k(x_k-\gamma x_{k+1})^T + \epsilon I, \quad \hat{b_t} \dot{=} \displaystyle\sum\limits_{k=0}^{t-1} R_{t+1}x_k \qquad (9.20) 
$$

Bu hesaplama veri anlamında efektif olsa dahi, işlemsel olarak yükü büyüktür. Bunu göz önüne alarak veri boyutu ile işlemsel yük arasında seçim yapılmalıdır.

## Bellek Tabanlı Fonksiyon Yaklaşıklığı

Bellek tabanlı yaklaşıklıklarda, bir durumun değerine ihtiyaç duyulmadığı müddetçe hesaplama yapılmaz. Eğitim süresince örnekler bellekte tutulur ve ilgili durumun tahmininin hesaplanması gerektiği zaman, bellekten değerler alınarak ilgili hesaplama yapılır. Bu yönteme tembel öğrenme (lazy learning) denir. Bu fonksiyon yaklaşıklığında parametre kullanılmadığı için, parametrik-olmayan (non-parametric) yöntemler arasına girmektedir.

Birçok bellek tabanlı yaklaşıklık mekanizması bulunmaktadır. Bu bölümde yalnızca yerel yaklaşıklık yöntemi (local approximation) örneklenecektir. Bir durum için değer hesaplanması istenince, ona en yakın olan komşu (nearest neighbor) durumun değeri dönülerek basitçe yerel öğrenme yapılabilmektedir. Benzer şekilde, değer hesaplaması istenen duruma en yakın olan durumların değerlerinin ağırlıklı ortalamaları da alınabilmektedir. 

Mutlak yaklaşıklıktan (global approximation) kaçınmak, yüksek boyut probleminden kaçınmak için ideal bir yöntem olmaktadır. Zira durum uzay boyutları arttıkça tabular yöntemlerde mutlak yaklaşıklık için bellek ihtiyacı üstel olarak büyümektedir. Lakin, iki yöntem için de işlemsel ihtiyaç örnek ve bellek miktarı yükseldikçe büyümektedir. Veri yapıları ile ilgili çalışmalar işlemsel ihtiyaca yardımcı olmaktadır.

## Kernel Tabanlı Fonksiyon Yaklaşıklığı

Bellek tabanlı yaklaşıklıklarda, $$s$$ durumu için aranan komşu durumların uzaklığını tanımlayan fonksiyonlara kernel fonksiyonu (kernel function) denmektedir. Örnekle, $$k(s, s')$$ formülasyonu, $$ s$$ durumu için aranan komşuluk bilgisinin ağırlığını vermektedir. 

Başka bir bakış açısıyla kernel fonksiyonları, durumlar arası genelleştirmeyi (generalization) ve alakayı (relevant knowledge) belirlemektedir. Kare kodlamada kullanılan filtre de, tam anlamıyla karşılamasa dahi kernel fonksiyonuna bir örnek olarak verilebilir. Kernel bağıntısı (kernel regression), bellekte tutulan her örneğin hedefini ağırlıklı ortalama kullanarak hesaplayan bir yöntemdir. $$\mathcal{D}$$ hafızada tutulan örnekler ve $$g(s')$$, $$s'$$ durumu için hafızadaki hedef olarak belirlenirse kernel bağıntısı aşağıdaki şekilde tanımlanabilir.

$$
    \hat{v}(s,\mathcal{D}) = \displaystyle\sum\limits_{s'\epsilon\mathcal{D}}k(s,s')g(s') \qquad(9.23)
$$

En sıklıkla kullanılan kernel, Gaussian Radial Basis Function (RBF) olmaktadır. Ağırlıklar SGD ile öğrenilmekte olup, öğrenme başladıktan sonra kernel’in boyutu ve merkezi değiştirilerek bağıntı hesaplanabilmektedir.
