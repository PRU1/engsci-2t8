def initialize():
    # initialize global variables
    global hedons, health

    global cur_time
    global last_activity, last_activity_duration
    
    global last_finished
    global bored_with_stars
    global tired
    global star_power # tracks if you can use star power
    global star_power_count # counts the number times star_power has been used within 2 hours
    
    hedons = 0
    health = 0
    
    cur_star = None
    cur_star_activity = None
    
    bored_with_stars = False
    star_power_count = [0,0] # time, duration  
    
    last_activity = None
    last_activity_duration = 0
    tired = False
    star_power = False
    cur_time = 0
    last_finished = -1000

def star_can_be_taken(activity): # I dunno why you need this
    pass
    
def perform_activity(activity, duration):
    global health
    global hedons
    global star_power
    global cur_hedons
    global tired
    global star_power_count 
    # tired or star power condition
    if activity == "running":
        # calculate health
        deltaT1 = duration-180 if duration>=180 else 0
        health += 3*duration + deltaT1
        # calculate hedon
        if tired:
            hedons -= duration*2
        else:
            deltaT2 = duration-10 if duration>=10 else 0
            hedons += 2*10
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

    if star_power:
        star_power_count[0] += 1
        star_power_count[1] += duration
        if star_power[0] == 3 and star_power_count[1] >= 120:
            star_power = False # no star power for rest of simulation
        else:
            durationNew = 10 if duration>=10 else duration
            hedon += 3*durationNew
            # reset counter after 120 minutes has elapsed
            if star_power[1] > 120:
                star_power[1] -= 120
    tired = True # you are always tired, except for the first activity


def get_cur_hedons():
    global hedons
    return hedons
    
def get_cur_health():
    global health
    return health

def star_power_bust(): # keeps track if stars offered and span of time
    pass

def offer_star(activity):
    if bored_with_stars:
        star_power = False
    else:
        star_power = True
        
def most_fun_activity_minute():
    hedon_running = 0
    hedon_resting = 0
    hedon_textbook = 0

    if tired:
        hedon_running -= 2
        hedon_textbook -= 2
    else:
        hedon_running += 2
        hedon_textbook += 1
    hashmap = {hedon_running : "running", hedon_resting : "resting", hedon_textbook : "textbook"} 
    temp = max(hedon_running, hedon_resting, 0)
    return hashmap[temp]

################################################################################
#These functions are not required, but we recommend that you use them anyway
#as helper functions

def star_power_counter():
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