#programa cotizaciones (cerraduras y cocinas)
#este programa mostrara los productos mas reelevantes de la empresa

# cotizar = str(input('''bienvenido al programa para cotizar.

# escriba: a para cotizar cocinas
# escriba: b para cotizar puertas
# escriba: c para cotizar ventanas y/o vidireras
# escriba: d para cotizar pasamanos
# escriba: f para cotizar cabinas de baño
# escriba: g para cotizar rejas
# escriba: h para cotizar muebles
# escriba: i para cotizar mesones

# ¿que producto deseas cotizar el dia de hoy? '''))

if cotizar == 'a':
    print('ustedinas')
 desea cotizar coc
elif cotizar == 'b':
    print('usted desea cotizar puertas')

elif cotizar == 'c':
    print('usted desea cotizar ventanas y/o vidrieras.')

    sistema = int(input('''nota: recordar que el tramo de perfil lo venden de 6m (revisar inventario)

escriba: 1 para cotizar en sistema 50-20
escriba: 2 para cotizar en sistema 80-25
escriba: 3 para cotizar en sistema 7-44
escriba: 4 para cotizar en sistema 38-31
escriba: 5 para cotizar en sistema 70-38

¿en que sistema desea cotizar la ventaneria? '''))

#sistema 50-20
    if sistema == 1:
        print('usted eligio el sistema 50-20')

        vidrio = int(input('''a continuacion se muestran los tipos de vidrio, por favor seleccione uno:

escriba: 1 para vidiro claro
escriba: 2 para vidrio bronce
escriba: 3 para vidrio grabado
escriba: 4 para vidrio anti reflectivo'''))

        if vidrio == 1:
            print('usted eligio el vidrio claro')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 2:
            print('usted eligio el vidrio bronce')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 3:
            print('usted eligio el vidrio grabado')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 4:
            print('usted eligio el vidrio anti reflectivo')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        else:
            print('usted no eligio un vidrio disponible')

#sistema 80-25
    elif sistema == 2:
        print('usted eligio el sistema 80-25')

        vidrio = int(input('''a continuacion se muestran los tipos de vidrio, por favor seleccione uno:

escriba: 1 para vidiro claro
escriba: 2 para vidrio bronce
escriba: 3 para vidrio grabado
escriba: 4 para vidrio anti reflectivo'''))

        if vidrio == 1:
            print('usted eligio el vidrio claro')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 2:
            print('usted eligio el vidrio bronce')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 3:
            print('usted eligio el vidrio grabado')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 4:
            print('usted eligio el vidrio anti reflectivo')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        else:
            print('usted no eligio un vidrio disponible')

    #sistema 7-44
    elif sistema == 3:
        print('usted eligio el sistema 7-44')

        vidrio = int(input('''a continuacion se muestran los tipos de vidrio, por favor seleccione uno:

escriba: 1 para vidiro claro
escriba: 2 para vidrio bronce
escriba: 3 para vidrio grabado
escriba: 4 para vidrio anti reflectivo'''))

        if vidrio == 1:
            print('usted eligio el vidrio claro')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 2:
            print('usted eligio el vidrio bronce')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 3:
            print('usted eligio el vidrio grabado')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 4:
            print('usted eligio el vidrio anti reflectivo')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        else:
            print('usted no eligio un vidrio disponible')

    #sistema 38-31
    elif sistema == 4:
        print('usted eligio el sistema 38-31')

        vidrio = int(input('''a continuacion se muestran los tipos de vidrio, por favor seleccione uno:

escriba: 1 para vidiro claro
escriba: 2 para vidrio bronce
escriba: 3 para vidrio grabado
escriba: 4 para vidrio anti reflectivo'''))

        if vidrio == 1:
            print('usted eligio el vidrio claro')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 2:
            print('usted eligio el vidrio bronce')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 3:
            print('usted eligio el vidrio grabado')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 4:
            print('usted eligio el vidrio anti reflectivo')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 4mm
escriba: 2 para calibre de 5mm
escriba: 3 para calibre de 6mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 4mm')

            elif calibre == 2:
                print('usted eligio un calibre de 5mm')

            elif calibre == 3:
                print('usted eligio un calibre de 6mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        else:
            print('usted no eligio un vidrio disponible')

    #sistema 70-38
    elif sistema == 5:
        print('usted eligio el sistema 70-38')

        vidrio = int(input('''a continuacion se muestran los tipos de vidrio, por favor seleccione uno:

escriba: 1 para vidiro claro
escriba: 2 para vidrio bronce
escriba: 3 para vidrio grabado
escriba: 4 para vidrio anti reflectivo'''))

        if vidrio == 1:
            print('usted eligio el vidrio claro')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 5mm
escriba: 2 para calibre de 6mm
escriba: 3 para calibre de 7mm
escriba: 4 para calibre de 8mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 5mm')

            elif calibre == 2:
                print('usted eligio un calibre de 6mm')

            elif calibre == 3:
                print('usted eligio un calibre de 7mm')

            elif calibre == 4:
                print('usted eligio un calibre de 8mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 2:
            print('usted eligio el vidrio bronce')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 5mm
escriba: 2 para calibre de 6mm
escriba: 3 para calibre de 7mm
escriba: 4 para calibre de 8mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 5mm')

            elif calibre == 2:
                print('usted eligio un calibre de 6mm')

            elif calibre == 3:
                print('usted eligio un calibre de 7mm')

            elif calibre == 4:
                print('usted eligio un calibre de 8mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        elif vidrio == 3:
            print('usted eligio el vidrio grabado')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 5mm
escriba: 2 para calibre de 6mm
escriba: 3 para calibre de 7mm
escriba: 4 para calibre de 8mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 5mm')

            elif calibre == 2:
                print('usted eligio un calibre de 6mm')

            elif calibre == 3:
                print('usted eligio un calibre de 7mm')

            elif calibre == 4:
                print('usted eligio un calibre de 8mm')

            else:
                print('usted no escogio un calibre valido para este sistema')


        elif vidrio == 4:
            print('usted eligio el vidrio anti reflectivo')

            calibre=int(input('''a continuacion se muestran los diferentes calibres que se manejan en este sistema
por favor seleccione uno:

escriba: 1 para calibre de 5mm
escriba: 2 para calibre de 6mm
escriba: 3 para calibre de 7mm
escriba: 4 para calibre de 8mm'''))

            if calibre == 1:
                print('usted eligio un calibre de 5mm')

            elif calibre == 2:
                print('usted eligio un calibre de 6mm')

            elif calibre == 3:
                print('usted eligio un calibre de 7mm')

            elif calibre == 4:
                print('usted eligio un calibre de 8mm')

            else:
                print('usted no escogio un calibre valido para este sistema')

        else:
            print('usted no eligio un vidrio disponible')

    else:
        print('usted no eligio un sistema valido')

elif cotizar == 'd':
    print('usted desea cotizar pasamanos')

elif cotizar == 'f':
    print('usted desea cotizar cabinas de baño')

elif cotizar == 'g':
    print('usted desea cotizar rejas')

elif cotizar == 'h':
    print('usted desea cotizar muebles')

elif cotizar == 'i':
    print('usted desea cotizar mesones')

else:
    print('en este momento no tenemos este producto disponible, mil disculpas')