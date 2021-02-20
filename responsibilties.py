class ResearchGuest:
	def __init__(self, guest_name):
	    self.guest_name = guest_name
	    # self.reports includes reports about every media file that is found about a guest
	    self.reports = None
	    # short report is for preparation of guests list. {occupation: ..., }
	    self.short_report = {'occupation': None, 'achivements': None, 'public_appearances': None, 'interests_conclusion': None}
	    # social media accounts are needed to track comments and feedbacks about the podacst
	    self.social_medias = ['www.reddit.com/r/lexfridman', 'www.twitter.com/lexfridman', 'www.youtube.com/user/lexfridman', 'www.linkedin.com/in/lexfridman', 'lexfridmanpodcast@mail.com']
	
	def get_constructive_guest_info(self):
	    # getting all search results as a dict of {result: link}
	    with open(`www.google.com/${self.guest_name}`, 'r') as a search_results:
	        if search_results:
	            # looking up every result
	            for result, link in search_results:
	                # comparing whether there is a report about this result
	                if result not in list(self.reports.keys()):
	                    # make_report reads a result and makes a report based on it
	                    result.make_report()
	                    self.reports[result] = link
		            
	def get_short_report(self):
	    with open(`www.google.com/${self.guest_name}`) as search_result:
	        # search for occupation in results of search
	        occupation = {key: test_dict[key] for key in test_dict.keys() & {'occupation'}}
	        
		        
	def collect_suggestion_comments(self.social_medias):
		for media in self.social_medias:
		    with open(media) as guest_suggestion_comments:
		        if guest_suggestion_comments:
		            for comment in guest_suggestion_comments:
		                if comment.constructive
		                
		                
		                
