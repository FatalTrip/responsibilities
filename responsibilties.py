# DISCLAIMER!!!


guests_list = []

class ResearchGuest:
	def __init__(self, guest_name=None):
	    self.guest_name = guest_name
	    # self.reports includes reports about every media file that is found about a guest
	    self.reports = None
	    # short report is for preparation of guests list. {occupation: ..., }
	    self.short_report = None
	    # social media accounts are needed to track comments and feedbacks about the podacst
	    self.social_medias = ['www.reddit.com/r/lexfridman', 'www.twitter.com/lexfridman', 'www.youtube.com/user/lexfridman', 'www.linkedin.com/in/lexfridman', 'lexfridmanpodcast@mail.com']
	
	def get_public_info_report(self, name):
	    # getting all search results as a dict of {result: link}
	    with open(`www.google.com/${name}`, 'r') as a search_results:
	        if search_results:
	            # looking up every result
	            for result, link in search_results:
	                # comparing whether there is a report about this result
	                if result not in list(self.reports.keys()):
	                    # make_report reads a result and makes a report based on it
	                    result.make_report()
	                    self.reports[result] = link
	    return self.reports
		            
	def get_short_report(self, name):
	    with open(`www.google.com/${name}`) as search_result:
	        # search for occupation in results of search
	        occupations = {key: test_dict[key] for key in test_dict.keys() & {'occupations'}}
		achivements = {key: test_dict[key] for key in test_dict.keys() & {'achivements'}}
		public_appearances = {key: test_dict[key] for key in test_dict.keys() & {'interviews', 'podcasts', 'blogposts'}}
		comments_and_posts = {key: test_dict[key] for key in test_dict.keys() & {'comment', 'post'}}
		# conclude() takes data as an argument and makes conclusion about data's meaning and interesting parts of it
		interests_conclusion = conclude(comments_and_posts)
		self.short_report = {'occupations': occupations, 'achivements': achivements, 'public_appearances': public_appearances, 'interests_conclusion': interests_conclusion} 
		return self.short_report
	        
		        
	def collect_suggestion_comments(self):
		for media in self.social_medias:
		    with open(media) as guest_suggestion_comments:
		        if guest_suggestion_comments:
		            for comment in guest_suggestion_comments:
				name = comment.find('name')
		                if !comment.is_constructive(): ##### there it should append to list of guest that inherited from parent class
					self.get_short_report(name)
			    self.get_public_info_report(name)
		            
		                
		                
