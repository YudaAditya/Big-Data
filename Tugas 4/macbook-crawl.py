import twint

# Configure
c = twint.Config()
c.Custom["tweet"]=["id","date","time","timezone","user_id","username","name","place","tweet","mentions","urls","photos","replies_count","retweets_count","likes_count","hashtags","cashtags","link","retweet","quote_url","video","user_rt_id","near","geo","source","retweet_date"]
# c.Custom["user"]=["id","name","username","location"]
c.Location = True
c.Lang = "en"
c.Search = "Macbook"
c.Store_json = True
# c.Store_csv = True
c.Output = "data/macbook.json"
c.Since = "2019-01-01"
c.Until = "2019-01-22 05:21:29"


#Run
twint.run.Search(c) 
# twint.run.Lookup(c) 