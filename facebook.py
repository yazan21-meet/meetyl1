class user():
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=password
		self.friends_list=[]
		self.posts=[]
	def add_friend(self,email):
		friends.append(user1)
		print(self.name+ "has added"+ self.email)
	def remove_friend(self,email):
		friends.remove(user1)
		print(self.name+ "has removed"+ self.email)
	def post(self,text):
		self.posts.append(text)
		print(self.name+ "has posted"+ text)
user1=user("yazan","yazandakkak@facebook","123")