import os 

descapho = { }
numero_despacho  = { }


def registro_salida (diccionario, nombre,contacto,placa_veh,descripcion_veh,descripcion_carga, ruta):
    if placa_veh == '' or nombre == '' or contacto == '' or descripcion_veh == '' or descripcion_carga == '' or ruta == '':
        enter = input('Debe diligenciar toda la información solicitada <ENTER>')
    else:
        diccionario[placa_veh] = {'nombre': nombre, 'contacto': contacto, 'descripcion vehiculo': descripcion_veh, 'descripcion de carga': descripcion_carga, "Ruta": ruta}
        enter = input(f'\nLa persona {nombre} ha sido registrada con éxito <ENTER>')
        
        
        

    