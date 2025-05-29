    # test cases. Thank you ChatGPT

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
    offer_star("textbook")
    perform_activity("textbook", 20)
    # star should work
    # health = 710 + 40 = 750
    # hedons = -470 + 30 -40 = -480
    perform_activity("running", 3)
    # health = 750 + 9 = 759
    # hedons = -480 - 6 = -486
    offer_star("running")
    # voided star condition no extra hedons
    perform_activity("textbook", 30)
    # health = 759 + 60 = 819
    # hedons = -486 - 60 = - 546

