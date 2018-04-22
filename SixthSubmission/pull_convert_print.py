#simple pull, convert to float, print
text = "X-DSPAM-Confidence:    0.8475";
locale = text.find('0')
pull = float(text[23:35])
print(pull)
