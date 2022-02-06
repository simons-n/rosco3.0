import praw

checked_id_list = open("checked_ids.txt", "w")

# initialize with appropriate values 
client_id = "nG84SJfoLrAmmKL_wbSBSg" 
client_secret = "yu2H4D2R4LxIZT8x6HUZIWlqoobKfw" 
username = "Rosco3Point0" 
password = "GiveMe40kMinis" 
user_agent = "check for tabletop game figures by u/Rosco3Point0" 
  
# creating an authorized reddit instance 
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent) 

# to find the top most submission in the subreddit "MLPLounge" 
subreddit = reddit.subreddit('Miniswap') 
new_ids = ""
dare_urls = []

for submission in subreddit.new(limit = 20): 

    # creating variables
    post = submission.selftext

    # check if we've already seen this submission
    already_seen = False
    submission.id in checked_id_list.read():
        already_seen = True
    if 0 != len(new_ids):
        new_ids = new_ids + ", "
    new_ids = new_ids + str(submission.id)
    
    
    # if we haven't seen it, check if it has stuff we want
    if already_seen == False:
        if post != None and ("kommando" in post or ("octarius" and "terrain" in post) or "kill rig" in post or "killrig" in post or ("killa" and "kan" in post) or ("slave" and "ogryn" in post) or ("ogryn" and "necromunda" in post) or "stormboy" in post or "catacombs" in post or ("warboss" and "mega" in post)):
            
            # if it's dare, add it to urls to know about!
            dare_urls.append(submission.url)
    

if 0 != len(dare_urls):
    urlstring = ""
    count = 1
    for url in dare_urls:
        urlstring = urlstring + "[Link Number " + str(count) + "]" + "(" str(url) + ") \n\n"
        count += 1
    reddit.redditor("QuickDiamonds").message("New nerd plastic!", urlstring)


checked_id_list.write(new_ids)
checked_id_list.close()