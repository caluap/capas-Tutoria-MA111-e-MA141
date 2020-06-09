size("A5")

margins = (12.34, 13.23)
size = (width()-(margins[0]*2), height() - (margins[1]*2))
w = size[0]
h = size[1]

bg_color = (.09,.1,.16,0)
main_color = (0,.44,1,0)

    
# 1. Introdução



# 2. Matrizes 2 × 2

newPage()
#cmykFill(*bg_color)
#rect(0,0, w, h)

cmykFill(*main_color)

grid_gap = 1.5
cols = 44

mod_size_x = (w - (grid_gap * (cols-1))) / cols

ratio = h/w
rows = round(ratio*cols)

angle_y = 45 / (rows-1)
angle_x = 45 / (cols-1)

mod_size_y = (h - (grid_gap * (rows -1))) / rows

for x in range(cols):
    for y in range(rows):
        with savedState():
            translate(margins[0], margins[1])
            cx = x*(mod_size_x+grid_gap) + mod_size_x/2
            cy = y*(mod_size_y+grid_gap) + mod_size_y/2
            angle = angle_y*y + angle_x*x
            rotate(angle, center=(cx,cy))
            #skew(angle_s*x,center=(xc,xy))
            rect(x*(mod_size_x+grid_gap),y*(mod_size_y+grid_gap), mod_size_x, mod_size_y)


# 3. Potências, equações exponenciais e logaritmos

newPage()


cmykFill(*main_color)

mod_size_y = (h - (grid_gap * (rows -1))) / rows
for x in range(cols):
    for y in range(rows):
        with savedState():
            translate(margins[0], margins[1])
            adj_x = (x/(cols-1))
            adj_y = (y/(rows-1))
            cx = x*(mod_size_x+grid_gap) + mod_size_x/2
            cy = y*(mod_size_y+grid_gap) + mod_size_y/2
            rotate(45*adj_y*adj_x, center=(cx,cy))
            
            cmykFill(*main_color)
            rect(x*(mod_size_x+grid_gap),y*(mod_size_y+grid_gap), mod_size_x*adj_x*adj_y, mod_size_y*adj_x*adj_y)

# 4. Polinômios e afins

newPage()

# 5. Trigonometria e Vetores

newPage()

# 6. Troca de variáveis e composição de funções

newPage()

# 7. Equação de retas e circunferências

newPage()

# 8. Transformações em gráficos

newPage()

# 9. Revisão para integrais por partes

newPage()

# 10. Revisão para integrais trigonométricas

newPage()

# 11. Revisão para frações parciais

newPage()
