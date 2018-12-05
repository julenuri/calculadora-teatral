#Esta aplicación contiene la operación en Python de la Duración de la obra
#Las variables están explicadas en las siguientes líneas
print("""Bienvenido a la Calculadora de La Duración de una Obra Teatral
por favor, introduzca los datos cuando sea indicado.""")
aplausosfin = 130
nombre = input("¿Cuál es el nombre de la obra?\n")
m = input("¿Es un musical?(responde sí o no)\n")
p = int(input("Inserte número de páginas\n"))
c = int(input("Inserte número de canciones\n"))
a = int(input("Inserte el número de actos\n"))
d = input("¿Tiene decorado pesado que hay que cambiar?(responde sí o no)\n")

if m!="sí":
    m=0
else:
    m=1
if d!="sí":
    d=1.5
else:
    d=1

duracionobra = (p*120) + (c*180) + (m*c*40) + (a*30*d) + (aplausosfin)
duracionobramin = int(duracionobra/60)
duracionobrahor = int(duracionobra/3600)
duracionobraresto1 = duracionobra%60
duracionobraresto2 = duracionobramin%60

print("Estimo que la obra", nombre, "durará:", duracionobra, "segundos,")
print("que son unos", duracionobramin, "minutos y ",duracionobraresto1, "segundos.")
print("y son", duracionobrahor, "horas, ", duracionobraresto2, "minutos y ", duracionobraresto1, "segundos.")
if duracionobra>7200:
    print("Sería recomendable plantearse realizar descanso para evitar que al público se le haga demasiado pesada.")