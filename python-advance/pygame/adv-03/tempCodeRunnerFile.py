    if act==True:
            for i in range(len(snow_list)):
                pygame.draw.circle(screen,WHITE,snow_list[i][:2],snow_list[i][3]-3)
                snow_list[i][0]+=snow_list[i][2]
                snow_list[i][1]+=snow_list[i][3]
                if snow_list[i][1]>bg_y:
                    snow_list[i][1]=random.randrange(-50,-10)
                    snow_list[i][0]=random.randrange(0,bg_x)