newphrase = "rainstorm"
# create a new variable called shortphrase and assign it a value by slicing the newphrase variable by removing the first 3 characters and the last 3 characters
# the first 3 characters are "rai"
# the last 3 characters are "orm"
# substring(string,start,end)
shortphrase = newphrase[0:len(newphrase)-6]
print(shortphrase)

