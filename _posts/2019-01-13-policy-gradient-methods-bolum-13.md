---
layout: post
author: "Pekiştirmeli Öğrenme Takımı"
title:  "Pekiştirmeli Öğrenme - Bölüm 13: Policy Gradient Methods"
description: " "
date:   2019-01-13
categories: pekistirmeli-ogrenme
tags: ["pekistirmeli-ogrenme"]
permalink: /blog/:categories/:title

prev-page-url: /blog/pekistirmeli-ogrenme/eligibility-traces-bolum-12
next-page-url: /blog/pekistirmeli-ogrenme/psychology-bolum-14
---

__*ÖNEMLİ:Bu başlık/bölüm kararlı sürümünde değildir,eksik ve yanlış yerlerin olması muhtemeldir,lütfen okurken buna dikkat ediniz gerektiği yerde issue açınız.Bölüm hakkında açılmış bir issue varsa tekrar açmayınız.*__

## Policy Gradient Methods

Şu ana kadar öğrendiğimiz değer fonksiyonunun aksine bu bölümde hiç bir değere danışmadan hareket eden bir politikayı inceleyeceğiz.

Değer fonksiyonu politikayı güncellemek için kullanılabilir ancak harekete bir etkisi olmayacak.

Politika parametremizi performans ölçüm değeri olarak kullandığımız J(Q) fonksiyonumuzun gradientini kullanarak maximum noktaya çekmeye yönelik güncelleyeceğiz(gradient ascent). 

Politika parametrelerinin performans fonksiyonunun maksimum noktaya ulaşmasına göre güncellendiği bu tip öğrenmeye genel olarak policy gradient metodu denir.

Ortam keşfini garantilemek için genelde politikanın deterministik olmamasını isteriz.Politikamız rastgeleliğe dayandığı zaman( ki bu durum policy gradient metodunun başlıca avantajlarındandır) ortam keşfini kendisi bir olasılıksal dağılım olduğu için kendiliğinden yapmış olacaktır.

Bu metodla birlikte bir değer fonksiyonu kullanıyorsak (bkz. ddpg algoritması) , bu tip öğrenme actor-critic olarak adlandırılır. Aktör politika parametrelerini içerir ve harekette bulunurken değer fonksiyonu kritik fonksiyon yaklaşımımızca tahmin edilir ve harekete bir etkisi olmaz.

Tüm avantajların yanında policy gradient metodunun bir avantajıda değer fonksionu yaklaşmına nazaran  alınacak hareket seçimlerinin yavaşça ve dramatik olmayan değişimidir.

    

Policy Gradient metodu sayesinde aynı gözüken ama farklı hareket alma gereği bulunduran durumlarında üstesinden gelmiş oluruz.

J(Q) yani performans fonksiyonu hem eylem seçimlerine hem de bu seçimlerin yapıldığı durumların dağılımına bağlıdır ve bunların her ikisi de politika parametresinin etkisine bağlıdır. Ancak politikanın duruma dağılımına etkisi çevreye bağlıdır ve genelde bilinmez.

Durum dağılımını ortadan kaldırmak için kullandığımız policy gradient ascent yöntemi politikamızın olasılıksal bir dağılım olmasından dolayı zor duruma düşekte. Bunun çözümü politikayı logaritmik değere çevirip türevlendirmek.

## REINFORCE: Monte Carlo Policy Gradient

Bir Monte Carlo algoritmasıdır ve bölüm tamamlandıktan sonra geriye dönük olarak yapılan tüm güncellemelerin  sadece episodik durum için iyi tanımlanmıştır. Ödülümüzü bölümün sonunda aldığımız için de çok kötü bir hareket dahi yapsak ödülümüz yüksek olduğu sürece farkedemeyeceğiz.

Sutton un kitabında verilen algoritmaya uygun olarak her bölüm bittiğinde bir toplam ödül geri dönütü üzerinden ödülün avantaj fonksiyonumuzun türevi ile çarpımı sonucu yenileme gerçekleştirilir.

Eligibility Vector(?)

## REINFORCE with Baseline

Politika gradyan teoremi, eylem değerinin keyfi bir temel çizgiye karşılaştırılmasını içerecek şekilde genelleştirilebilir ve bu çizgi yani baseline harekete bağlı olmayan her fonksiyon olabilir

$$baseline$$     $$b(s)$$:  $$q(s,a)-b(s)$$

Monte Carlo güncellemesinden tek farkı baseline değeridir.

## Actor–Critic Methods

REINFORCE-with-baseline metodu değer fonksiyonu kullansa dahi bunu kritik olarak değilde temel olarak kullandığı için bu metodlar arasına alamıyoruz.

Aktör kritik metodu; aktörümüz olan politika türevlendirme yöntemimizin, bölüm sonunda ödül alması ve bu ödülün tam olarak hangi hareket sayesinde alındığının bilinmemesi durumundan dolayı bize yardımcı olacak bir kritik değer fonksiyonu ihtiyacından doğmuştur.

Sutton un kitabında belirtilen formülizasyondan da anlaşılacağı üzere aktör kritik yöntemimizde toplam ödül yerine anlık ödül kullanımı sağlanabilmiştir.

