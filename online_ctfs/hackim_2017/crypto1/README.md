Crypto Question 1
========

> William Whitfield | Tuesday, February 21st, 2017

--------------------------------------------

> Breaking Brain
 
This was the first crypto challenge, worth 300 points.

We were given an [image](cryptopuzzle1.png) and told to find the private key and paste as an answer.

Within the image there was a passphrase with the beginning and end given and the rest obfuscated. `8lnXXXXXXXXnl8`

We were also given a hint that `nullcon8itsgr8` was scrambled for the passphrase as well as an address QR code.

In order to get the address from the QR Code I used [ZBar][zbar].

This gave the result:
```
$ zbarimg cryptopuzzle1.png
QR-Code:17iUnGoZbFrGS7uU9z2d2yRT9BKgVqnKnn
scanned 1 barcode symbols from 1 images in 0.1 seconds
```

Thus, the address is `17iUnGoZbFrGS7uU9z2d2yRT9BKgVqnKnn`.

Looking at the image given I saw that it had the title of a website called [brainwallet][brainwallet]. Looking it up on google I found it was related to [bitcoin][bitcoin].

Continuing to research the idea behind bitcoin generation I saw it was very involved mathematically in generating the private key. I did not want to have to implement this in python.

In addition I found the retired, but original [Brainwallet][brainwalletio] website. It can be used to obtain an address and private key using a passphrase.

Now I was thinking what if I can just use the website to enter the [permutations][permutations] of the unknown part of the passphrase. There's nice python libraries like [`urllib2`][urllib2] that can get data from a website.

However the site is running [javascript][javascript] and therefore is incompatible with `urllib2`.

I set on a search for a python library that could interface with javascript, discovering [`selenium`][selenium].

Selenium is a powerful tool that literally opens whatever web browser you use and works with it, sending keystrokes, mouse clicks, etc.

So, after working through the kinks of installing selenium I threw together the following script:
```
#!/usr/bin/env python

from itertools import permutations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mat_addr = '17iUnGoZbFrGS7uU9z2d2yRT9BKgVqnKnn'
pass_start = '8ln'
pass_end = 'nl8'
driver = webdriver.Firefox()
driver.get("https://brainwalletx.github.io/#generator")
time.sleep(5)
passphrase = driver.find_element_by_id("pass")
time.sleep(5)
addr = driver.find_element_by_id("addr")
time.sleep(5)

# original string is nullcon8itsgr8
# letters without beginning and ending are ucoitsgr
comb = permutations('ucoitsgr')
for i in comb:
    s = ''.join(i)
    p = pass_start + s + pass_end
    print p
    passphrase.send_keys(p)
    time.sleep(1)
    rec_addr = addr.get_attribute("value")
    print rec_addr
    if rec_addr == mat_addr:
        print p
        break
    passphrase.clear()
```

This python script runs through opening the web browser to the brainwallet web site and trying the permutations of the passphrase. There is a delay of 1 second in order for the website to execute its javascript and store the new value. Once the addresses matches the script breaks and you have to just copy and paste the passpharase for the flag.

After about an hour or so of testing passphrase I got the passphrase `8lnustorcginl8` to work.

Plugging this in for the private key gave us `5KjzfnM4afWU8fJeUgGnxKbtG5FHtr6Suc41juGMUmQKC7WYzEG`.

__Thus, the flag is `flag{5KjzfnM4afWU8fJeUgGnxKbtG5FHtr6Suc41juGMUmQKC7WYzEG}`__

[zbar]: http://zbar.sourceforge.net/
[brainwallet]: https://en.bitcoin.it/wiki/Brainwallet
[bitcoin]: https://en.wikipedia.org/wiki/Bitcoin
[brainwalletio]: http://brainwalletx.github.io/
[permutations]: https://en.wikipedia.org/wiki/Permutation
[urllib2]: https://docs.python.org/2/library/urllib2.html
[javascript]: https://en.wikipedia.org/wiki/JavaScript
[selenium]: https://pypi.python.org/pypi/selenium