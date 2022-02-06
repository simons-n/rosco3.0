import praw
print("it's running")
checked_id_list = open("checked_ids.txt", "w")
log = open("rosco_log.txt", "w")
new_log = ""
new_ids = ""
new_log.append("running this \n")
try:
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
    dare_urls = []

    for submission in subreddit.new(limit = 20): 
        new_log.append("looping through posts, this is ID: " + submission.id + "\n")
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
        
    new_log.append("dare_urls list length is: " + len(dare_urls) + "\n")

    if 0 != len(dare_urls):
        new_log.append("Out of For loop \n")
        urlstring = ""
        count = 1
        for url in dare_urls:
            urlstring = urlstring + "[Link Number " + str(count) + "]" + "(" str(url) + ") \n\n"
            count += 1
        reddit.redditor("QuickDiamonds").message("New nerd plastic!", urlstring)
except:
    new_log.append("oopsie error hee hee \n")

checked_id_list.write(new_ids)
log.write(new_log)
log.close()
checked_id_list.close()