import random
import timeit
import uuid
import deDupe

def make_test_data(length):
	emails_list = []
	#this could wind up with +1 pieces of test data, but it's good enough for ballparking.
	while len(emails_list) < length:
		uname = str(uuid.uuid4())
		emails_list.append(uname + "@test.test")
		#I can't be assured that this completely accurate every time, but it's
		#going to be good enough for ballparking 50% dupe ratio.
		if random.random() <= .5:
			emails_list.append(uname + "@test.test")
	
	print("%d Items in the test list" % len(emails_list))
	return emails_list

def test_perf_hundred_k():
	runtime = timeit.timeit("deDupe.dedupe_emails(data)", number=1, setup="data = make_test_data(100000)", globals=globals())
	print("deduped 100000 emails in %d seconds" % runtime)
	assert runtime <= 1

def test_ordering():
	test_data = ['one@test.test', 'two@test.test', 'one@test.test', 'three@test.test']
	finished = deDupe.dedupe_emails(test_data)
	assert finished == ['one@test.test', 'two@test.test', 'three@test.test']