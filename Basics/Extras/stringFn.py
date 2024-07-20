# String Functions & Methods

s = "Surya Pugazh"
print(s)

#String Methods

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count('u'))
print(s.endswith('zh'))
print(s.find('u',1)) # '1' parameter gives next index
print(s.replace('y','i'))

#Boolean Function

str = "surya"
print(str.isupper())
print(str.islower())
print(str.isalnum()) # To check it's alphanumeric
print(str.isalpha())

#Split Lines

a = "He\nis\na\nGood\nBoy"
print(a.splitlines()) # it remove '\n' and make it as list
print(a.splitlines(True)) # it print as same as with '\n' and make it as list
print(s.split(" ")) # it split by Gap
print(s.split(",")) # it split by ','

#Strip - remove Gap

sent = "   This is the Gaped Sentence     "
print(len(sent))
print(len(sent.strip())) # strip remove Gap in String
print(len(sent.lstrip())) # lstrip remove left Gap
print(len(sent.rstrip())) # lstrip remove right Gap

# Partition - used on DataBase operation like split Year/Month

date = "27-05-2005"
print(date)
print(date.partition('-'))  # 'date', '-', 'month-year'
