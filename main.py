from machine import I2C, Pin
from htu21d import HTU21D
from lm75a import LM75A
from network_manager import conectar_wifi
from umail import SMTP
from secrets import EMAIL_USER, EMAIL_PASS, SMTP_SERVER, SMTP_PORT
import time

i2c = I2C(0, scl=Pin(22), sda=Pin(21))
sen_ambiental=HTU21D(i2c)
sen_componente= LM75A(i2c, address=0x48)

UMBRAL_SEGURIDAD = 35.0
alerta_enviada=False

#print ("Temperatura:", sen_ambiental.read_temperature())
#print("Humedad:", sen_ambiental.read_humidity())

def enviar_alerta_email(temp):
    try:
        smtp=SMTP(SMTP_SERVER, SMTP_PORT, EMAIL_USER, EMAIL_PASS)
        smtp.login()
        smtp.send(EMAIL_USER, "ALERTA DE SEGURIDAD ESP32", f"Temperatura critica detectada: {temp}°C")
        smtp.quit()
        print("Correo enviado exitosamente.")
        
    except Exception as e:
        print(f"Error enviando correo: {e}")

def verificar_seguridad():
    global alerta_enviada
    try:
        temp_amb=sen_ambiental.read_temperature()
        hum_amb=sen_ambiental.read_humidity()
        time.sleep(.1)
        temp_comp=sen_componente.temp()
        
        print(f"Ambiente: {temp_amb:.2f}°C, Humedad:{hum_amb:1f} | Componente: {temp_comp:.2f}°C")
        #Se evalua si esta en sistema de peligro
        if temp_amb > UMBRAL_SEGURIDAD or temp_comp > UMBRAL_SEGURIDAD:
            if not alerta_enviada:#Solo enviamos si no habiamos enviado antes
                print("!!! ALERTA DE SEGURIDAD: SOBRECALENTAMIENTO !!!")
                enviar_alerta_email(max(temp_amb,hum_amb , temp_comp))
                alerta_enviada=True #Marcamos que ya enviamos la alerta
        #Si la temperatura vuelve a la normalidad, resetea el filtro
        elif temp_amb < (UMBRAL_SEGURIDAD - 2.0) and temp_comp < (UMBRAL_SEGURIDAD - 2.0):
            if alerta_enviada:
                print("Sistema regreso a zona segura")
                alerta_enviada=False
    except OSError:
        print(f"Error de bus I2C detectado, reintentando en el siguiente ciclo...")
    
if conectar_wifi():
    print("Sistema de monitoreo iniciado.")
    while True:
        verificar_seguridad()
        time.sleep(5)
        
else:
    print("No se pudo conectar a la red. El sistema continuara offline")
    

        
    
    