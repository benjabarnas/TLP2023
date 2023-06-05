numx=int(input("ingrese un valor"))
numy=int(input("ingrese un valor"))
if numx>0 and numy>0:
    print("las coordenadas solicitadas estan en el primer cuadrante")
else:
    if numx<0 and numy<0:
        print("las coordenadas solicitadas estan en el tercer cuadrante")
    else:
        if numx>0 and numy<0:
            print("las coordenadas solicitadas estan en el segundo cuadrante")
        else:
            if numx<0 and numy>0:
                print("las coordenadas solicitadas estan en el cuarto cuadrante")
