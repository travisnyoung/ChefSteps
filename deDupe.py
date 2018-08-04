
#This is the core. It's pretty basic, make a hashable array and 
def dedupe_emails(emails_list):
	deduped_emails = {}
	for each in emails_list:
		if each not in deduped_emails:
			deduped_emails[each] = ""

	return list(iter(deduped_emails.keys()))

"""
TODO:
Need a function that can take a JSON POST and turn that into the list being de-
duped, then one that takes the results and turn them back into a JSON array to
be handed back to the UI/further business logic (amazon SMS maybe?)

Also probably some preliminary validation ("is this an email address?")
"""