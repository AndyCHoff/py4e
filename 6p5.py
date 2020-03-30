# Exercise 6.5 Completed

text = "X-DSPAM-Confidence:    0.8475";
num = text.find(':')
sale = float(text[num+1:])
print(sale)
