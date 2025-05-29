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
    
    sCount = 0 # count star occurences
    s1 = 0; s2 = 0; s3 = 0

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
    global last_finished 

    print (last_finished, cur_time, cur_star_activity, star_is_offered)
    if bored_with_stars:
        print("BORED WITH STARS NOOOOOO")
        return False 
    elif star_offer_time == cur_time and cur_star_activity == ACTIVITY and star_is_offered:
        # star offered and used at same time. star offered for ACTIVITY
        print("star condition met")
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

    # check star power condition, you do not get hedons for resting
    if star_can_be_taken(activity) and activity != "rest": 
        # give you extra hedons
        length = min(10, duration)
        hedons += 3*length
        # reset star offer
        star_is_offered = False

    cur_time += duration # always update current time

    # check if tired
    
    print("tired check", last_finished, cur_time)
    """ 
    if cur_time-last_finished < 120 and last_finished != 0:
        tired = True
    else:
        tired = False
    """
    if last_activity_duration < 120 and last_activity_duration != 0:
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
        print("bank", running_bank)
        # calculate health
        dTB = 0 if running_bank >= duration else (duration-running_bank)
        health += (duration-dTB)*3 + dTB
        # update running bank
        #running_bank = 0 if running_bank-duration < 0 else abs(duration-running_bank)
        if running_bank-duration < 0:
            running_bank = 0
        else:
            running_bank = abs(duration-running_bank)
            print("running bank updated")
            print(running_bank)

        # calculate hedon
        if tired:
            hedons -= duration*2
        else:
            deltaT2 = duration-10 if duration>=10 else 0
            hedons += 2*(duration-deltaT2)
            hedons -= 2*deltaT2
    elif activity == "textbooks":
        # calculate health
        health += 2*duration
        # calculate hedon
        if tired:
            hedons -= 2*duration
        else:
            deltaT3 = duration-20 if duration>=20 else 0
            hedons += 1*duration
            hedons -= 1*deltaT3
    elif activity == "rest":
        pass

    last_activity_duration = duration # set activity of last duration for tireness checking
    """
    if last_activity == activity:
        last_activity_duration += duration
    else:
        last_activity = activity
        last_activity_duration = duration
    """
    
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
            s2 = s3
            s1 = s2 
            s3 = cur_time
            sCount = 0 # reset star counter
            
    # check for boredom
    if s3 - s1 <= 120 and s1>0 and s3>0 : # yikes
        bored_with_stars = True

    # update star is offered and star activity, to see if you can use the stars
    cur_star_activity = activity 
    star_is_offered = True
    star_offer_time = cur_time
        
def most_fun_activity_minute():
    pass
    
################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes'''
    pass
            

def estimate_health_delta(activity, duration):
    pass
        
################################################################################
        
if __name__ == '__main__':
    initialize()
    perform_activity("running", 30)    
    print(get_cur_hedons())            # -20 = 10 * 2 + 20 * (-2)             # Test 1
    print(get_cur_health())            # 90 = 30 * 3                          # Test 2           		
    print(most_fun_activity_minute())  # resting                              # Test 3
    perform_activity("resting", 30)    
    offer_star("running")              
    print(most_fun_activity_minute())  # running                              # Test 4
    perform_activity("textbooks", 30)  
    print(get_cur_health())            # 150 = 90 + 30*2                      # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10