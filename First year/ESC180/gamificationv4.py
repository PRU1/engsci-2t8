def initialize():
    '''Initializes the global variables needed for the simulation.'''
    
    global hedons, health
    global running_bank

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    
    global star_is_offered
    global cur_star_activity
    global star_offer_time

    global s1, s2, s3  # track time of star offer
    global sCount
    
    sCount = 0  # count star occurrences
    s1 = 0
    s2 = 0
    s3 = 0

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
    '''Check if the star power can be taken for the given activity.'''
    global star_offer_time, cur_star_activity, cur_time, bored_with_stars, star_is_offered

    if bored_with_stars:
        return False
    elif star_offer_time == cur_time and cur_star_activity == ACTIVITY and star_is_offered:
        return True
    return False

def perform_activity(activity, duration):
    '''Simulate the activity and update health and hedons.'''
    global health, hedons, cur_time, last_activity, last_activity_duration
    global running_bank, last_finished, tired, star_is_offered

    cur_time += duration  # always update current time
    tired = (cur_time - last_finished) < 120  # check if tired
    
    if star_can_be_taken(activity) and activity != "rest":
        # star power gives extra hedons
        length = min(10, duration)
        hedons += 3 * length
        star_is_offered = False

    # reset running bank condition
    if last_activity != activity or activity != "running":
        running_bank = 180

    # Activity-specific logic
    if activity == "running":
        # calculate health
        dTB = 0 if running_bank >= duration else (duration - running_bank)
        health += (duration - dTB) * 3 + dTB

        running_bank = max(0, running_bank - duration)

        # calculate hedons
        if tired:
            hedons -= duration * 2
        else:
            deltaT2 = max(0, duration - 10) # time after 10 min
            hedons += 2 * (duration - deltaT2)
            hedons -= 2 * deltaT2
            print("+", 2*(duration-deltaT2), "-", 2*deltaT2)

    elif activity == "textbooks":
        # calculate health
        health += 2 * duration
        # calculate hedons
        if tired:
            hedons -= 2 * duration
        else:
            deltaT3 = max(0, duration - 20)
            hedons += 1 * (duration - deltaT3)
            hedons -= 1 * deltaT3

    elif activity == "rest":
        pass  # resting has no health or hedon effect

    last_activity = activity
    last_activity_duration = duration
    last_finished = cur_time  # track time of last finished activity

def get_cur_hedons():
    '''Return the current hedons.'''
    global hedons
    return hedons
    
def get_cur_health():
    '''Return the current health.'''
    global health 
    return health
    
def offer_star(activity):
    '''Offer a star for a specific activity.'''
    global sCount, s1, s2, s3, cur_star_activity, star_is_offered, star_offer_time, cur_time, bored_with_stars

    sCount += 1 
    if sCount == 1:
        s1 = cur_time
    elif sCount == 2:
        s2 = cur_time 
    elif sCount == 3:
        s3 = cur_time
    elif sCount == 4:
        s1, s2 = s2, s3  # shift values
        s3 = cur_time
        sCount = 0  # reset star counter

    # check for boredom
    if s3 - s1 <= 120 and s1 > 0 and s3 > 0:
        bored_with_stars = True

    cur_star_activity = activity
    star_is_offered = True
    star_offer_time = cur_time
        
def most_fun_activity_minute():
    '''Return the activity that would give the most hedons in the next minute.'''
    if star_is_offered and not bored_with_stars:
        return cur_star_activity
    return "rest"  # default to resting if no better option is available

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def get_effective_minutes_left_hedons(activity):
    '''Return the number of minutes during which the user will get the full
    amount of hedons for activity activity.'''
    pass
    
def get_effective_minutes_left_health(activity):
    pass    

def estimate_hedons_delta(activity, duration):
    '''Return the amount of hedons the user would get for performing activity
    activity for duration minutes.'''
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
    print(get_cur_health())            # 150 = 90 + 30 * 2                    # Test 5
    print(get_cur_hedons())            # -80 = -20 + 30 * (-2)                # Test 6
    offer_star("running")
    perform_activity("running", 20)
    print(get_cur_health())            # 210 = 150 + 20 * 3                   # Test 7
    print(get_cur_hedons())            # -90 = -80 + 10 * (3-2) + 10 * (-2)   # Test 8
    perform_activity("running", 170)
    print(get_cur_health())            # 700 = 210 + 160 * 3 + 10 * 1         # Test 9
    print(get_cur_hedons())            # -430 = -90 + 170 * (-2)              # Test 10
