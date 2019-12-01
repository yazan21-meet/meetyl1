
class post():
	def __init__(self,user,content):
		self.user=user
		self.content=content
class comment(post):
	def __init__(self,email,date):
		self.email=email
		self.date=date
	def person_commenting(self,email):
		print(self.email+ "has commented"+ text)
	def commenting_date(self,date):
		print("this comment was posted on"+ self.date)
class user():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		self.friends_list.append(user1)
		print(self.name+ "has added"+ email)
	def remove_friend(self,email):
		self.friends_list.remove(user1)
		print(self.name + "has removed"+ email)
	def post(self,text):
		self.posts.append(text)
		print(self.name+ "has posted"+ text)
	def get_userInfo(self):
		print("name: "+self.name)
		print("email: "+self.email)
		print("password: "+self.password)
		print("friends: "+str(self.friends_list))
		print("posts: "+str(self.posts))
user1=user("yazan "," yazandakkak@facebook"," 123")
user2=user("osama "," osamahijazi@facebook"," 234")
user2.add_friend(" yazandakkak@facebook")
user2.add_friend("samirhazboun@facebook")
user2.post(" a photo")
user2.remove_friend(" samirhazboun@facebook")
user2.get_userInfo()
user3=user("samir "," samirhazboun@facebook","543")
user3.add_friend(" yazandakkak@facebook")
user3.add_friend(" osamahijazi2facebook")
user3.post(" an article")
user3.remove_friend(" osamahijazi@facebook")
user3.get_userInfo()
