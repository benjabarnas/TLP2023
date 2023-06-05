n=1
for i in range(n):
    cordx=int(input("ingrese la cordenada x "))
    cordy=int(input("ingrese la cordenada y"))
    if cordx<0 and cordy<0:
        tipo = "cuadrante 3"
    else:
        if cordx<0 and cordy>0:
                tipo = "cuadrante 2"
        else:
            if cordx>0 and cordy>0:
                tipo = "cuadrante 1"
            else:
                if cordx>0 and cordy<0:
                    tipo = "cuadrante 4"
                
print ("Las cordenadas pertenecen al ", tipo)
