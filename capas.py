import math

size("A5")

margins = (12.34, 13.23)
size = (width()-(margins[0]*2), height() - (margins[1]*2))
w = size[0]
h = size[1]
ratio = h/w

grid_gap = 1.5
cols = 44

bg_color = (.09,.1,.16,0)
main_color = (0,.44,1,0)

def mod_size(cols, grid_gap):
    mod_size_x = (w - (grid_gap * (cols-1))) / cols
    rows = round(ratio*cols)

    mod_size_y = (h - (grid_gap * (rows -1))) / rows
    
    return mod_size_x, mod_size_y, rows


    
# 1. Introdução
def mod1():
    pass

# 2. Matrizes 2 × 2

def mod2():
    newPage()
    cmykFill(*main_color)

    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    angle_y = 45 / (rows-1)
    angle_x = 45 / (cols-1)
    
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cx = x*(mod_size_x+grid_gap) + mod_size_x/2
                cy = y*(mod_size_y+grid_gap) + mod_size_y/2
                angle = angle_y*y + angle_x*x
                rotate(angle, center=(cx,cy))

                rad = math.radians(angle)
                fact = 0.15 + 0.85 * math.sin(rad) * math.cos(rad) * 2
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)
# 3. Potências, equações exponenciais e logaritmos

def mod3():
    newPage()
    cmykFill(*main_color)
    
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    
    
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                adj_x = .2 + .8 * (x/(cols-1))
                adj_y = .2 + .8 * (y/(rows-1))
                cx = x*(mod_size_x+grid_gap) + mod_size_x/2
                cy = y*(mod_size_y+grid_gap) + mod_size_y/2
                rotate(45*adj_y*adj_x, center=(cx,cy))
           
                rect(x*(mod_size_x+grid_gap),y*(mod_size_y+grid_gap), mod_size_x*adj_x*adj_y, mod_size_y*adj_x*adj_y)

# 4. Polinômios e afins
def mod4():
    newPage()
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cmykFill(*main_color)
                # https://www.wolframalpha.com/input/?i=parabola+passing+through+%282%2C60%29%2C%2822%2C4%29%2C%2841%2C60%29
                calc_y = round(x**2 * 14 / 95 - x * 602 / 95 + 6848 / 95)
                if calc_y <= y:
                    fact = .8 * (1-y/rows) + .2
                else:
                    fact = .15 * (1-y/rows) + .1
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)

# 5. Trigonometria e Vetores
def mod5():
    newPage()
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cmykFill(*main_color)
                rad_x = math.pi * x/(cols-1)
                rad_y = math.pi * y/(rows-1)
                
                fact = min(1, math.cos(rad_x) * math.sin(rad_y))
                
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)

# 6. Troca de variáveis e composição de funções
def mod6():
    newPage()
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cmykFill(*main_color)
                # https://shar.es/aHM6en 
                # {2,60}, {11,4},{22,20},{33,4}{41,60}
                a = 17707 / 19242630
                b = 762208 / 9621315
                c = 2342279 / 1012770
                d = 22861798 / 874665
                e = 2747074 / 26505
                calc_y = round(a * x ** 4 - b * x ** 3 + c * x ** 2 - d * x + e)
                if calc_y > y:
                    fact = .6 * (1-y/rows) + .4
                else:
                    fact = .15 * (1-y/rows) + .1
                    
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)
                
# 7. Equação de retas e circunferências
def mod7():
    newPage()
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cmykFill(*main_color)
                if x >= y:
                    fact = max(0.15, min(1, y/cols))
                else:
                    fact = max(0.15, 1 - y/rows)
                    cx = x*(mod_size_x+grid_gap) + mod_size_x/2
                    cy = y*(mod_size_y+grid_gap) + mod_size_y/2
                    rotate(45, center=(cx,cy))
                    
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)

# 8. Transformações em gráficos
def mod8():
    newPage()
    mod_size_x, mod_size_y, rows = mod_size(cols, grid_gap)
    for x in range(cols):
        for y in range(rows):
            with savedState():
                translate(margins[0], margins[1])
                cmykFill(*main_color)
                if round(y) == round((x/5.556)**2):
                    fact = 0.5
                    cx = x*(mod_size_x+grid_gap) + mod_size_x/2
                    cy = y*(mod_size_y+grid_gap) + mod_size_y/2
                    rotate(45, center=(cx,cy))
                else:
                    fact = 1 - max(0.25, min(0.75, y/cols))
                    
                delta_x = mod_size_x * (1-fact)/2
                delta_y = mod_size_y * (1-fact)/2
                rect(x*(mod_size_x+grid_gap) + delta_x,y*(mod_size_y+grid_gap) + delta_y, mod_size_x*fact, mod_size_y*fact)

# 9. Revisão para integrais por partes
def mod9():
    newPage()

# 10. Revisão para integrais trigonométricas
def mod10():
    newPage()

# 11. Revisão para frações parciais
def mod11():
    newPage()


mod1()
mod2()
mod3()
mod4()
mod5()
mod6()
mod7()
mod8()
#mod9()
#mod10()
#mod11()
