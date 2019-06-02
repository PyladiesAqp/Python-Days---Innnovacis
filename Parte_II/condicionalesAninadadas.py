peso = int(raw_input("¿Cual es tu peso?"))


if (peso>=20 and peso<=40):
    print "Desnutricion"

elif(peso>=41 and peso<=100):
    print "analizemos..."

    if(peso>=41 and peso<=65):
        print "buen peso"

    elif(peso>=66 and peso<=100):
        print "sobrepeso"

    
else:
    print "datos incorrectos"





