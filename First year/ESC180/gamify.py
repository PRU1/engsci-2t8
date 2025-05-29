def initialize():
    '''Initializes the global variables needed for the simulation.
    Note: this function is incomplete, and you may want to modify it'''
    
    global hedons, health
    global running_bank

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    
    global star_is_offered
    global cur_star_activity
    global star_offer_time

    global s1,s2,s3 # track time of star offer
    global sCount
    global tired
    tired = False
    
    sCount = 0 # count star occurences
    s1 = -1; s2 = -1; s3 = -1 

    running_bank = 180
    hedons = 0 
    health = 0
    
    star_is_offered = False
    cur_star_activity = ""
    bored_with_stars = False
    star_offer_time = 0
    
    last_activity = ""
    last_activity_duration = 0
    
    cur_time = 0
    
    last_finished = 0

def star_can_be_taken(ACTIVITY):
    global star_offer_time
    global cur_star_activity
    global cur_time
    global bored_with_stars
    global star_is_offered
    if bored_with_stars:
        return False 
    elif star_offer_time == cur_time and cur_star_activity == ACTIVITY and star_is_offered:
        # star offered and used at same time. star offered for ACTIVITY
        # print("the activity is", ACTIVITY)
        return True
    return False
    
def perform_activity(activity, duration):
    global health
    global hedons
    global star_power
    global cur_hedons
    global tired
    global star_power_count 
    global cur_time
    global last_activity
    global last_activity_duration
    global running_bank
    global last_finished

    # print("last time is ", last_finished, "time nom", cur_time)
    # check star power condition, you do not get hedons for resting
    if star_can_be_taken(activity): 
        # print("in star condition")
        # give you extra hedons
        length = 10 if duration >= 10 else duration
        hedons += 3*length
        # reset star offer
        star_is_offered = False

    # print("last time is ", last_finished, "time nom", cur_time)
    # check if tired
    # print(cur_time-last_finished)

    cur_time += duration # always update current time
    #print("cur-last", cur_time, last_finished)

    if (cur_time-duration)-last_finished < 120 and last_finished > 0:
        # print("I AM tired", cur_time-last_finished)
        tired = True
    else:
        tired = False

    # reset running_bank condition
    if last_activity == activity and activity == "running": 
        pass # inelegant code but easier to keep track of cases
    else:
        running_bank = 180

    # tired or star power condition
    if activity == "running":
        # calculate health
        dTB = 0 if running_bank >= duration else (duration-running_bank)
        health += (duration-dTB)*3 + dTB
        # update running bank
        running_bank = 0 if running_bank-duration < 0 else abs(duration-running_bank)

        # calculate hedon
        if tired:
            hedons -= duration*2
            # print("IM TIRED NOOOO")
            # print("-", duration*2)
        else:
            deltaT2 = duration-10 if duration>=10 else 0
            hedons += 2*(duration-deltaT2)
            hedons -= 2*deltaT2
            # print("+", 2*(duration-deltaT2), "-", 2*deltaT2)
    elif activity == "textbooks":
        # calculate health
        health += 2*duration
        # calculate hedon
        if tired:
            # print("I'm tired")
            hedons -= 2*duration
        else:
            # print("I'm not tired")
            deltaT3 = duration-20 if duration>=20 else 0
            hedons += 1*(duration-deltaT3)
            hedons -= 1*deltaT3
    elif activity == "rest":
        pass

    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration
    
    if activity != "resting":
        last_finished = cur_time # used for tracking tiredness
    

def get_cur_hedons():
    global hedons
    return hedons
    
def get_cur_health():
    global health 
    return health
    
def offer_star(activity):
    global sCount
    global s1,s2,s3
    sCount += 1 
    global cur_star_activity 
    global star_is_offered
    global star_offer_time
    global cur_time
    global bored_with_stars

    match sCount:
        case 1:
            s1 = cur_time
        case 2:
            s2 = cur_time 
        case 3:
            s3 = cur_time 
        case 4:
            # do values swap 
            s1 = s2 
            s2 = s3
            s3 = cur_time
            sCount = 0 # reset star counter
            
    if s3 - s1 <= 120 : # yikes
        if s3 > 0:
            #print("bored with stars!!")
            bored_with_stars = True
        elif s3 == s1: # handle case where 3 stars are offered at the same time
            #print("bored with stars!")
            bored_with_stars = True

    # update star is offered and star activity, to see if you can use the stars
    cur_star_activity = activity 
    star_is_offered = True
    star_offer_time = cur_time
        
def most_fun_activity_minute():
    global tired 
    hedon_running = hedonsInMin("running")
    hedon_resting = 0
    hedon_textbook = hedonsInMin("textbooks")

    hashmap = {hedon_running : "running", hedon_resting : "resting", hedon_textbook : "textbooks"} 
    temp = max(hedon_running, hedon_textbook)
    temp = max(0, temp)
    return hashmap[temp]

def hedonsInMin(activity):
    global star_power
    global cur_hedons
    global tired
    global star_power_count 
    global cur_time
    global last_activity
    global running_bank
    global last_finished

    hedons = 0 # local hedons
    duration = 1 # local duration
    cur_time_local = cur_time # don't change value of cur_time!
    tired_local = tired

    if star_can_be_taken(activity): 
        # give you extra hedons
        length = 10 if duration >= 10 else duration
        hedons += 3*length

    cur_time_local += duration # always update current time

    if (cur_time_local-duration)-last_finished < 120 and last_finished > 0:
         # print("I AM tired", cur_time-last_finished)
        tired_local = True
    # tired or star power condition
    if activity == "running":
        # calculate hedon
        if tired_local:
            hedons -= duration*2
        else:
            deltaT2 = duration-10 if duration>=10 else 0
            hedons += 2*(duration-deltaT2)
            hedons -= 2*deltaT2
    elif activity == "textbooks":
        if tired_local:
            hedons -= 2*duration
        else:
            deltaT3 = duration-20 if duration>=20 else 0
            hedons += 1*(duration-deltaT3)
            hedons -= 1*deltaT3
    return hedons

if __name__ == '__main__':
    initialize()
    perform_activity("running", 50)
    perform_activity("textbooks", 50)
    perform_activity("running", 40)  # Gets tired after 120 minutes
    print(get_cur_health())  # Expected: 50*3+ 2*50 + 40*3 = 370
    print(get_cur_hedons())  # Expected: 20 - 80 - 100 - 80 = -240

    initialize()
    perform_activity("running", 119)  # Almost tired but not quite
    offer_star("running")
    perform_activity("running", 1)  # Gains star bonus, not yet tired
    print(get_cur_hedons())  # Expected: 10*2 - 109*2 -2+3 = -197
    print(get_cur_health())  # Expected: 360 (120 * 3)

    initialize()
    perform_activity("running", 120)
    perform_activity("resting", 1)  # Rest immediately after becoming tired
    perform_activity("running", 30)  # Should still be tired, as resting is insufficient
    print(get_cur_health())  # Expected: 450 (120 * 3 + 30 * 3)
    print(get_cur_hedons())  # Expected: 2*10 - 110*2 - 30*2 = -260

    initialize()
    perform_activity("running", 120)
    perform_activity("textbooks", 60)
    perform_activity("running", 30)  # User is tired after 120 minutes
    print(get_cur_health())  # Expected: 510 (120 * 3 + 60 * 2 + 30 * 3)
    print(get_cur_hedons())  # Expected: -140 (10 * 2 + 110 * -2 -2*90)

    initialize()
    perform_activity("running", 120)
    perform_activity("resting", 240)  # Rest for 240 minutes to reset tiredness
    perform_activity("running", 60)  # Should not be tired
    print(get_cur_health())  # Expected: 540 (120 * 3 + 60 * 3)
    print(get_cur_hedons())  # Expected: -280 (10 * 2 - 110*2 + 10*2 - 50*2) 20+20-220-100

    initialize()
    offer_star("running")
    perform_activity("running", 10)
    perform_activity("running", 10)  # Star bonus should not apply after 10 minutes
    print(get_cur_hedons())  # Expected: 10 * 5 (first) + 10 * -2 (second)
    print(get_cur_health())  # Expected: 60 (20 * 3)

    initialize()
    perform_activity("running", 120)
    perform_activity("resting", 120)  # Rest for exactly 120 minutes
    perform_activity("running", 30)  # Not tired anymore
    print(get_cur_health())  # Expected: 450 (120 * 3 + 30 * 3)
    print(get_cur_hedons())  # Expected: -220 (10 * 2 + 110 * -2 + 20 - 40)

    initialize()
    perform_activity("running", 180)
    print(get_cur_health())  # Expected: 540 (180 * 3)
    print(get_cur_hedons())  # Expected: -320 (10 * 2 + 170 * -2)

    initialize()
    offer_star("running")
    perform_activity("running", 5)
    perform_activity("running", 3)
    print(get_cur_hedons())  # Expected: 5*3+5*2-6 = 19 (first 5 minutes gain star bonus, next 3 do not)

    initialize()
    offer_star("running")
    perform_activity("running", 10)  # Gains star bonus
    # off by 30 all the way down
    # health = 10*3=  30
    # hedons = 10*2 = 20
    offer_star("textbooks")
    perform_activity("textbooks", 10)  # Gains star bonus
    # hedons = 20 + -2*10 + 10*3 = 30
    # health = 30 + 20 = 50
    offer_star("running")
    perform_activity("running", 10)  # Gains star bonus
    # hedons = 30 - 20 + 30 = 40
    # health = 50 + 30 = 80
    offer_star("running")
    perform_activity("running", 10)  # Should not gain star bonus (user is bored)
    # health = 80 + 30 = 110
    # hedons = 40 - 20 = 20
    print(get_cur_hedons())  # Expected: 10 * 5 (first) + 10 * 4 (second) + 10 * 5 (third) + 10 * -2 (fourth)

    initialize()
    offer_star("running")
    perform_activity("running", 150)
    # health = 150*3 = 450
    # hedons = 2*10 - 140*2 + 30 = -230
    perform_activity("running", 80)
    # health = 450 + 3*30 + 50 = 490
    # hedons = -230 - 160 = -390
    offer_star("running")
    perform_activity("resting", 20)
    # no change in hedons/health
    perform_activity("running", 40)
    # no star power here
    # health = 490 + 120 = 710
    # hedons = -390 - 80 = -470
    offer_star("textbooks")
    perform_activity("textbooks", 20)
    # star should work
    # health = 710 + 40 = 750
    # hedons = -470 + 30 -40 = -480
    perform_activity("running", 3)
    # health = 750 + 9 = 759
    # hedons = -480 - 6 = -486
    offer_star("running")
    # voided star condition no extra hedons
    perform_activity("textbooks", 30)
    # health = 759 + 60 = 819
    # hedons = -486 - 60 = - 546
    print(get_cur_health())
    print(get_cur_hedons())




