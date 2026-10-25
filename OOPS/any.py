from oops_proj import chatbook

user1 = chatbook()
print(user1.get_name())
user1.set_name("AGENT")
print(user1.get_name())


chatbook.set_id(10)
user2 = chatbook()
print(user2.id)
