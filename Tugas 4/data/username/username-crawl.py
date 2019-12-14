import twint

data = open("usr-list-macbook.txt").read()
# print(data)
c = twint.Config()
data_list = data.split("\n")
# username = data['username'].unique()
batas = len(data_list)
count = 31782
print(data_list[count])

while count <= batas:
    # for x in data_list[count]:
    print(data_list[count])
    c.Username = data_list[count]
    c.Custom["user"] = ["username", "location", "verified"]
    c.Store_json = True
    c.Output = "macbook-username.json"
    # c.Output = "test.json"
    twint.run.Lookup(c)
    count = count+1
    print(count)
# print(count)
