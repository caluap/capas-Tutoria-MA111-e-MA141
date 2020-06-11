import math

size(814.377, 448.088)
#size(287.294, 130.947)
margins = (2, 2)
#margins = (1, 1)

size = (width()-(margins[0]*2), height() - (margins[1]*2))
w = size[0]
h = size[1]
ratio = h/w

grid_gap = 3
cols = 111

#grid_gap = 2
#cols = 59


bg_color = (.09,.1,.16,0)
main_color = (0,.44,1,0)

def mod_size(cols, grid_gap):
    mod_size_x = (w - (grid_gap * (cols-1))) / cols
    rows = round(ratio*cols)
    mod_size_y = (h - (grid_gap * (rows -1))) / rows
    return mod_size_x, mod_size_y, rows
    
    
mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)

angle_y = 180 / (rows-1)
angle_x = 30 / (cols-1)

for x in range(cols):
    for y in range(rows):
        with savedState():
            translate(margins[0], margins[1])
            cx = x*(mod_size_x+grid_gap) + mod_size_x/2
            cy = y*(mod_size_y+grid_gap) + mod_size_y/2
            
            angle = angle_y*y + angle_x*x

            rad = math.radians(angle)
            if x % 2 == 0 and y % 2 == 0:
                fact = 1
                cmykStroke(None)
                cmykFill(*main_color)
                if (x % 4 == 0 and y % 4 != 0) or (x % 4 != 0 and y % 4 == 0):
                    rotate(45, center=(cx,cy))
            else:
                fact = .5
                cmykStroke(*bg_color)
                sW = max(1, 3 * math.sin(math.radians(angle_y*y)) * math.cos(math.radians(angle_x*x)))
                strokeWidth(sW)
                cmykFill(None)
            
            delta_x = mod_size_x * (1-fact)/2
            delta_y = mod_size_y * (1-fact)/2
            
            rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)


