def point_inside_polygon(x,y,poly):

    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

x=-12.05
y=-76.9830
p = (-12.033791491561715, -76.98292139648436), (-12.068710150732263, -76.99734095214842), (-12.068038680920273, -76.96094874023436), (-12.033791491561715, -76.98292139648436)
poly = [(-12.033791491561715, -76.98292139648436), (-12.068710150732263, -76.99734095214842), (-12.068038680920273, -76.96094874023436), (-12.033791491561715, -76.98292139648436)]
print(point_inside_polygon(x,y,poly))
