size("A5")

margins = (12.34, 13.23)
size = (width()-(margins[0]*2), height() - (margins[1]*2))
w = size[0]
h = size[1]

bg_color = (.09,.1,.16,0)
main_color = (0,.44,1,0)
    
# 1. Introdução

# 2. Matrizes 2 × 2

translate(margins[0], margins[1])
cmykFill(*bg_color)
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
            xc = x*(mod_size_x+grid_gap) + mod_size_x/2
            xy = y*(mod_size_y+grid_gap) + mod_size_y/2
            angle = angle_y*y + angle_x*x
            rotate(angle, center=(xc,xy))
            #skew(angle_s*x,center=(xc,xy))
            rect(x*(mod_size_x+grid_gap),y*(mod_size_y+grid_gap), mod_size_x, mod_size_y)


# 3. Potências, equações exponenciais e logaritmos
# 4. Polinômios e afins
# 5. Trigonometria e Vetores
# 6. Troca de variáveis e composição de funções
# 7. Equação de retas e circunferências
# 8. Transformações em gráficos
# 9. Revisão para integrais por partes
# 10. Revisão para integrais trigonométricas
# 11. Revisão para frações parciais