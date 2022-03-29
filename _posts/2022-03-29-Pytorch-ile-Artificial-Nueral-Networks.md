---
layout: post
author: "Ensar ERDOĞAN"
title:  "Pytorch ile Derin Ögrenme - Bölüm 2: Pytorch ile Artificial Neural Networks"
description: "Bu çalışma, Pytorch ve Artificial Neural Network mimarisini ve uygulamasını barındırmaktadır."
date:   2022-03-29
categories: derin-ogrenme
tags: ["derin-ogrenme"]
permalink: /blog/:categories/:title
next-page-url: /blog/derin-ogrenme/pytorch-ile-Artificial-Neural-Network
---

# Pytorch-ile-Artificial-Neural-Networks

# Pytorch Nedir?

Zaman içerisinde makine ögrenmesi algoritmaların problemlere çözüm olmasının azalmasıyla birlikte, verilerin boyutunun her geçen gün artmasıyla 
Deep Learning algoritmaların kullanılması da artmaktadır. Bu kapsam da ses tanıma, görüntü işleme, görüntü sınıflandırma, nesne tanıma vb. çalışmalarda 
derin ögrenme algoritmaları daha başarılı sonuçlar üretmiştir. Tüm bu işler yapılırken aynı zaman da zaman dan kazanmak için hız gereksinimi dogmuştur.
Bu bağlamda bakıldığında Pytorch derin ögrenme algoritmarın hızlı çalışmasını sağlayan açık kaynak bir python kütüphanesidir.

Pytorch ekran kartlarını kullanabilen ve böylelikle sağladığı hız bakımından oldukça popüler bir kütüphanedir.Pytorch'un başarılı olmasının nedenlerinden
bir tanesi de sinir ağı modelleri zahmetsizce oluştura bilmesidir. Pytorch aynı anda CPU ve GPU gibi arka planda başka işler için yapıları kullanabilir.
Pytorch'un Numpy kütüphanesine benzer kendi bir Tensor yapısı mevcuttur.

# Artificial Neural Networks Nedir ve Nasıl Çalışır?

Artificial Neural Networks(Yapay Sinir Ağları) derin ögrenme veya derin sinir ağı olarak adlandırılır. Temelinde Derin Ögrenme Bölüm-1 de bahsedilen Logistic Regression ![https://yz-ai.github.io/blog/derin-ogrenme/Pytroch-ile-Logistic-Regression] modelini alıp bu işlemi iki kez veya daha fazla tekrar etmektedir. ANN algoritmasında Logistic Regression algoritmasında olduğu gibi girdi ve çıktı katmanları vardır. Bu katmanlar arasında ekstra da hidden layer(gizli katman) adı verilen bir katman vardır. Arada bulunan bu gizli katmanların sayısı da aslında Derin Ögrenmedeki derin kelimesinin baş mimarını oluşturmaktadır.

Hidden layer girdilari görmedigi için gizli olarak nitelendirilir.Ayrıca girdi katmanı toplam katman sayısına dahil edilmez. ANN algoritmasını resim üzerinde inceleyelim.

 <img src="ann.png">
 
 Resimde de görüldüğü üzere girdi ve çıktı katmanların arsında bir tane de hidden layer bulunmaktaır. Bu gizli katmanın 5 adet düğümü olduğu görülmektedir. Burada belirtilen düğüm sayısı aynı zamanda modelin daha iyi sonuçlar verebilmesi için kullanılan hyper parametrelerinden bir tanesidir.
 ANN algoritmasında Logistic Regressionda olduğu gibi girdi katmanları ve çıktı katmanları değişmez.
 
 Girdi katmanından hidden layer giderken tercih edilen activasyon fonksiyonları kullanılır.(tanh,sigmoid.RELu vb.) Activasyon fonsiyonların ayrıntılı bir şekilde ögrenmek istiyorsanız @Merve Ayyüce Kızrak hocamın yazısını okumanızı tavsiye ederim. ![https://ayyucekizrak.medium.com/derin-%C3%B6%C4%9Frenme-i%C3%A7in-aktivasyon-fonksiyonlar%C4%B1n%C4%B1n-kar%C5%9F%C4%B1la%C5%9Ft%C4%B1r%C4%B1lmas%C4%B1-cee17fd1d9cd]
 Genellikle hidden layer katmanına giderken tanh activasyon fonksiyonu tercih edilir modelin daha iyi ögrenmesine sebebiyet verecektir.
 Hidden layerdan sonra gelen kısım aslında Logistic Regressiondaki yapının aynısıdır.
 
 Resimde Görülecegi üzerine bir ileri yayılım(Forward) birde geri yayılım gözükmektedir(backward). İleri yayılım Logistic Regressiondaki yapının aynısı sadece bunu iki kez ve daha fazla yapılmasıdır. Geriye doğru yayılım ise işlemin türevini almak demektir. Geriye yayılımdan elde edilen parametreler ile model tekrar eğitilir bu işleme de update parameters denilir.
 
 








