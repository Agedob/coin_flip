def flip():
    head = 0
    tails = 0
    for i in range(1,21,1):
        import random
        random_num = round(random.random())
        if random_num > 0:
            head += 1
            print "Attempt #",i,"Throwing a coin... It's a head! ... Got",head,"head(s) so far",tails,"tails so far"
        else:
            tails += 1
            print "Attempt #",i,"Throwing a coin... It's a tails! ... Got",head,"head(s) so far",tails,"tails so far"
flip()