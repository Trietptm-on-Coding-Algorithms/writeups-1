Enigma
========

> William Whitfield | Tuesday, February 21st, 2017

--------------------------------------------

> Its World War II and Germans have been using Enigma to encrypt their messages. Our analysts have figured that they might be using XOR-encryption. XOR-encrption is vulnerable to a known-plaintext attack. Sadly all we have got are the encrypted intercepted messages. Your task is to break the Enigma and get the flag.

This was the third crypto challenge, worth 30 points.

We were given a series of six ciphertexts with the hint that they were encrypted using XOR.

We have a nice [tool](breakRepeatKeyXOR.py) that will provide you with a list of key lengths and their scores, with lowest being the best. The only caveat is that the file needs to be in [base64][base64].

So I ran [`base64`][base64_command] and piped it into an appropriately named file.

```
$ base64 1e > 1e64
```

This happened for all six ciphertexts and probably could've been written better in a script.

Then, as any sane person would do, I started working from the last ciphertext with the first output being:
```
$ python breakRepeatKeyXOR.py 6e64
Keylength: 1        Score: 5.0
Keylength: 2        Score: 3.0
Keylength: 3        Score: 5.0
Keylength: 4        Score: 1.75
Keylength: 5        Score: 3.2
Keylength: 6        Score: 2.66666666667
Keylength: 7        Score: 2.85714285714
Keylength: 8        Score: 2.625
Keylength: 9        Score: 3.55555555556
Keylength: 10       Score: 1.9
Keylength: 11       Score: 2.90909090909
Keylength: 12       Score: 2.91666666667
Keylength: 13       Score: 3.23076923077
Keylength: 14       Score: 2.07142857143
Keylength: 15       Score: 2.73333333333
Keylength: 16       Score: 3.375
Keylength: 17       Score: 3.11764705882
Keylength: 18       Score: 3.66666666667
Keylength: 19       Score: 3.10526315789
Keylength: 20       Score: 2.85
Keylength: 21       Score: 3.0
Keylength: 22       Score: 3.18181818182
Keylength: 23       Score: 3.4347826087
Keylength: 24       Score: 2.29166666667
Keylength: 25       Score: 3.0
Keylength: 26       Score: 2.96153846154
Keylength: 27       Score: 3.2962962963
Keylength: 28       Score: 3.03571428571
Keylength: 29       Score: 2.93103448276
Keylength: 30       Score: 2.86666666667
Keylength: 31       Score: 2.58064516129
Keylength: 32       Score: 3.15625
Keylength: 33       Score: 3.0
Keylength: 34       Score: 2.91176470588
Keylength: 35       Score: 3.0
Keylength: 36       Score: 2.77777777778
Keylength: 37       Score: 2.59459459459
Keylength: 38       Score: 2.60526315789
Keylength: 39       Score: 2.15384615385
Keylength: 40       Score: 2.525
Recomended: 4
Choose a key length: 4
Recommended Keys:

*Leave empty to try all keys*
Key: 
Wio7veoqehqrn Ixrpxsos37Nuo72 ޫbrtp. Nrndxy Str dtr Ltrfeobngxy srqori
Wim7vemqehsrn Kxrpzsos17Num72 ܫbrvp. Lrndzy Svr dvr Lvrfembngzy spqork
Win7venqehprn Hxrpysos27Nun72 ߫brup. Orndyy Sur dur Lurfenbngyy ssqorh
Wio veofehqen Iorpxdos3 Nuo 2 ޼brtg. Nendxn Ste dte Ltefeoungxn srfori
Wim vemfehsen Korpzdos1 Num 2 ܼbrvg. Lendzn Sve dve Lvefemungzn spfork
Win venfehpen Horpydos2 Nun 2 ߼brug. Oendyn Sue due Luefenungyn ssforh
Wio6veopehqsn Iyrpxros36Nuo62 ުbrtq. Nsndxx Sts dts Ltsfeocngxx srpori
Wim6vempehssn Kyrpzros16Num62 ܪbrvq. Lsndzx Svs dvs Lvsfemcngzx sppork
Win6venpehpsn Hyrpyros26Nun62 ߪbruq. Osndyx Sus dus Lusfencngyx ssporh
```

In each case the recommended keys are not human readable characters, as they are any ascii value so I will leave that section blank.

Here we can see some plaintext `Win venfehpen` but it's not exactly readable at first becasue it's in German. This is interesting.

Therefore I moved on to the fifth ciphertext which produced:
```
$ python breakRepeatKeyXOR.py 5e64
Keylength: 1        Score: 4.0
Keylength: 2        Score: 2.0
Keylength: 3        Score: 3.0
Keylength: 4        Score: 2.25
Keylength: 5        Score: 3.0
Keylength: 6        Score: 2.5
Keylength: 7        Score: 2.71428571429
Keylength: 8        Score: 2.625
Keylength: 9        Score: 2.11111111111
Keylength: 10       Score: 2.6
Keylength: 11       Score: 2.45454545455
Keylength: 12       Score: 2.08333333333
Keylength: 13       Score: 3.23076923077
Keylength: 14       Score: 2.14285714286
Keylength: 15       Score: 2.06666666667
Keylength: 16       Score: 3.25
Keylength: 17       Score: 2.64705882353
Keylength: 18       Score: 2.94444444444
Keylength: 19       Score: 2.63157894737
Keylength: 20       Score: 2.7
Keylength: 21       Score: 2.7619047619
Keylength: 22       Score: 2.77272727273
Keylength: 23       Score: 2.39130434783
Keylength: 24       Score: 2.625
Keylength: 25       Score: 2.92
Keylength: 26       Score: 2.61538461538
Keylength: 27       Score: 3.37037037037
Keylength: 28       Score: 2.42857142857
Keylength: 29       Score: 2.79310344828
Keylength: 30       Score: 2.6
Keylength: 31       Score: 3.09677419355
Keylength: 32       Score: 2.53125
Keylength: 33       Score: 2.81818181818
Keylength: 34       Score: 2.5
Keylength: 35       Score: 2.8
Keylength: 36       Score: 2.5
Keylength: 37       Score: 2.78378378378
Keylength: 38       Score: 2.71052631579
Keylength: 39       Score: 2.61538461538
Keylength: 40       Score: 2.6
Recomended: 2
Choose a key length: 2
Recommended Keys:

*Leave empty to try all keys*
Key: 
Berichte der britischen Marineüberwachung in Ihrer Region. Gehen Sie undercover
```

___This looks better!___

The translated German to English is `Reports of the British naval surveillance in your region. Go undercover`

Alright this looks promising, let's move on to the fourth ciphertext.

```
$ python breakRepeatKeyXOR.py 4e64
Keylength: 1        Score: 2.0
Keylength: 2        Score: 3.5
Keylength: 3        Score: 3.33333333333
Keylength: 4        Score: 2.75
Keylength: 5        Score: 2.4
Keylength: 6        Score: 2.16666666667
Keylength: 7        Score: 3.71428571429
Keylength: 8        Score: 2.625
Keylength: 9        Score: 2.77777777778
Keylength: 10       Score: 2.7
Keylength: 11       Score: 2.81818181818
Keylength: 12       Score: 3.5
Keylength: 13       Score: 2.84615384615
Keylength: 14       Score: 2.71428571429
Keylength: 15       Score: 3.33333333333
Keylength: 16       Score: 3.125
Keylength: 17       Score: 2.88235294118
Keylength: 18       Score: 3.05555555556
Keylength: 19       Score: 2.94736842105
Keylength: 20       Score: 3.65
Keylength: 21       Score: 3.14285714286
Keylength: 22       Score: 2.68181818182
Keylength: 23       Score: 3.39130434783
Keylength: 24       Score: 3.16666666667
Keylength: 25       Score: 3.04
Keylength: 26       Score: 3.03846153846
Keylength: 27       Score: 2.55555555556
Keylength: 28       Score: 2.60714285714
Keylength: 29       Score: 2.34482758621
Keylength: 30       Score: 1.8
Keylength: 31       Score: 2.0
Keylength: 32       Score: 2.0
Keylength: 33       Score: 1.60606060606
Keylength: 34       Score: 1.55882352941
Keylength: 35       Score: 1.08571428571
Keylength: 36       Score: 1.33333333333
Keylength: 37       Score: 1.24324324324
Keylength: 38       Score: 1.07894736842
Keylength: 39       Score: 1.0
Keylength: 40       Score: 0.725
Recomended: 40
Choose a key length: 1
Recommended Keys:

*Leave empty to try all keys*
Key: 
Der Code für den Tag ist BITCTF{Focke-Wulf Fw 200}
```

You may be asking yourself why I didn't choose the recommended key length. For one, 40 is a multiple of the actual key length of 1 resulting in it having the lowest score. Also, having chosen 40 first I found my computer crashing from trying to bruteforce the keys when the actual length was only 1.

So there you have it, __The code for the day is: `BITCTF{Focke-Wulf Fw 200}`__

[base64]: https://en.wikipedia.org/wiki/Base64
[base64_command]: https://linux.die.net/man/1/base64