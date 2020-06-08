size("A5")

margins = (12.34, 13.23)
size = (width()-(margins[0]*2), height() - (margins[1]*2))

bg_color = (.18,.16,.24,0)
main_color = (0,.44,1,0)
    
cmykFill(*bg_color)
rect(margins[0], margins[1], size[0], size[1])