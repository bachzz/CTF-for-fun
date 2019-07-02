from Crypto.PublicKey import RSA

pub_key = RSA.importKey(open('pub.key','r'))

print "n = ",pub_key.n
print "e = ",pub_key.e
