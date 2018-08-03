
#This is the core. It's pretty basic, make a hashable array and 
def dedupe_emails(emails_list):
	deduped_emails = {}
	count = 0
	for each in emails_list:
		count += 1
		if each not in deduped_emails:
			deduped_emails[each] = ""

	return list(iter(deduped_emails.keys()))