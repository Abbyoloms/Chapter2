
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.remove('D')
plist.pop(2)
plist.insert(3, 'a')
plist.insert(4, 'p')
plist.insert(2, ' ')
for x in range(7):
    plist.pop()
    
new_phrase = ''.join(plist)
print(plist)
print(new_phrase)




