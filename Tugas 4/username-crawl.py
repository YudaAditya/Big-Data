import twint
import pandas as pd

data = pd.read_json('data/macbook.json', lines=True)
# print(data['username'].head(5))
c= twint.Config()

username = data['username'].unique()
print(username.len())

count=0
# f = open("data/usr-list-macbook.txt","w")
for x in username:
    c.Username = x
    c.Custom["user"] = ["username", "location", "verified"]
    c.Store_json = True
    c.Output = "data/macbook-username.json"
    # f.write(x + "\n")
    print(x)
    count+=1
    print(count)
    twint.run.Lookup(c)
# f.close()
# print(count)
