import random
import time
import thread
import multiprocessing
def generate_id():
    threadlock = thread.allocate_lock()
    multiprocesslock = multiprocessing.RLock()
    multiprocesslock.acquire()
    threadlock.acquire()
    _id = '{0}{1}'.format(int(time.time()*1000000), random.randint(100,999))
    threadlock.release()
    multiprocesslock.release()
    return _id

MAP_STRING = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

def id_to_string(id):
	s = ""
	id = int(id)
	while id:
		s = MAP_STRING[id%62] + s
		id = id/62
	return s

def string_to_id(s):
	try:
		id = 0
		for c in s:
			id = id*62 + MAP_STRING.index(c)
		return id
	except Exception, e:
		raise Exception("Invalid Url")

