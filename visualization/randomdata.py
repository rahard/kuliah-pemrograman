import random, string


with open("redisdb.log", "a") as myfile:
    #myfile.write("appended text")
    # data random
    for i in range(0, 100): # list kira-kira berapa orangnya
        x = random.randint(0, 100)
        root = random.choice(string.ascii_lowercase) + str(x)
        for j in range(0, x-1): # ini random followernya
            follower = random.choice(string.ascii_lowercase) + str(random.randint(0, 100))
            tmp=root+ ',' +follower + '\n'
            myfile.write("%s" %tmp)
