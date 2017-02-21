#!/usr/bin/env python

from itertools import permutations
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Solution passphrase is 8lnustorcginl8
# Solution private key is flag{5KjzfnM4afWU8fJeUgGnxKbtG5FHtr6Suc41juGMUmQKC7WYzEG}
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