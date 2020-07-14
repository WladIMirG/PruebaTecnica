
def cantidadDeHijos(numeros, datos):

    """De acuerdo a los dígitos y a las combinaciones, se hace un conteo de predecesores o hijos por cada dígito"""
    nSucc = list()
    print ('Numero', numeros)
    print ('Este es el dato', datos)
    for numero in numeros:
        suc_c = list()
        print ('_____________________Numero', numero)
        for dato in datos:
            try:
                index = dato.index(numero)
                #print ('Este es el dato', dato)
                #print (index)
                suc_c.extend(list(dato[index + 1 :]))
            except ValueError:
                continue
        print (suc_c)
        print (set(suc_c))
        nSucc.append((len(set(suc_c)), numero))
    print (nSucc)
    return nSucc
                

def obtenerDatos():

    """Lee el contenido del archivo keylog.txt"""

    return set([str(number.rstrip()) for number in open("documentos/keylog.txt", "r")])

def obtenerDigitos(datos):
    """Obtiene los dígitos únicos que componen la contraseña buscada"""
    caracteres = set()
    for dato in datos:
        for c in dato:
            caracteres.add(c)
    return caracteres


class KeyLog(object):
    def __init__(self, ):
        pass
    pass
    
    
    def dataRead():
        return set([str(number.rstrip()) for number in open("documentos/keylog.txt", "r")])
        
    def digitO(datos):
        """Obtiene los dígitos únicos que componen la contraseña buscada"""
        caracteres = set()
        for dato in datos:
            for c in dato:
                caracteres.add(c)
        return caracteres

    def cantidadDeHijos(numeros, datos):

        """De acuerdo a los dígitos y a las combinaciones, se hace un conteo de predecesores o hijos por cada dígito"""
        nSucc = list()
        print ('Numero', numeros)
        print ('Este es el dato', datos)
        for numero in numeros:
            suc_c = list()
            print ('_____________________Numero', numero)
            for dato in datos:
                try:
                    index = dato.index(numero)
                    #print ('Este es el dato', dato)
                    #print (index)
                    suc_c.extend(list(dato[index + 1 :]))
                except ValueError:
                    continue
            print (suc_c)
            print (set(suc_c))
            nSucc.append((len(set(suc_c)), numero))
        print (nSucc)
        return nSucc
if __name__ == "__main__":
    datos = obtenerDatos()
    digitos = obtenerDigitos(datos)
    numero_hijos = cantidadDeHijos(digitos, datos)
    
    #Organizo los numeros de mayor a menor número de predecesores.
    print(sorted(numero_hijos, reverse=True))
    solucion = ''.join([x[1] for x in sorted(numero_hijos, reverse=True)])
    print ("La contraseña buscada es {0}".format(solucion))