def proyeccion (ingreso:int,plazo_anios:int)->float:
    y=plazo_anios*2
    n=0
    while n<y:
        total= ingreso + ingreso*0.056235
        n+=1
        ingreso= total
        if n>6:
            ingreso+= 1000000
    return total    
