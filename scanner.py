from machine import Pin, I2C

#Configurar I2C en los pines estandar
i2c = I2C(0, scl=Pin(22), sda=Pin(21))

print ("Escaneando busI2C...")
devices = i2c.scan()

if len(devices) == 0:
    print("No se encontraron dispositivos. Revisa el cableado.")
    
else:
    print("Dispositivos encontrados:", len(devices))
    for device in devices:
        print("Direccion decimal:", device,"| Hexadecimal:",hex(device))