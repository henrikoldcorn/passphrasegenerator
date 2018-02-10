from random import randrange, SystemRandom



wordlist = open(r"C:\python\english.txt")
words = []
for line in wordlist:
    words.append(line)

passLength = int(input("number of words?"))

passphrase = "\n"
for x in range(passLength):
	listLength = len(words)
	randInt = SystemRandom().randint(0, listLength)
	passphrase += words[randInt % len(words)][:-1] + " "
print(passphrase)              

close = input("Press Enter to close. ")
