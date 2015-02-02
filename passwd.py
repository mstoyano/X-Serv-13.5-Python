#!/usr/bin/python

fd = open("/etc/passwd", "r")
usuarios = fd.readlines()
dicc = {}

for linea in usuarios: 
    conf = linea.split(":")
    usuario = conf[0]
    shell = conf[-1][:-1]

    dicc[usuario] = shell

print 'El usuario "root" utiliza: ' + dicc["root"]
print 'El usuario "imaginario" utiliza: ', 

try:
    print dicc["imaginario"]

except KeyError:
    print "ERROR! El usuario solicitado no existe."


