# DataCenter Thermal Guardian (ESP32 IoT)
Descripción del Proyecto
Sistema de monitoreo ambiental y de componentes diseñado para entornos de servidores (DataCenters). Implementa una arquitectura resiliente capaz de detectar anomalías térmicas y notificar al administrador en tiempo real mediante protocolos seguros.

## Características Principales
* Monitoreo Dual: Lectura simultánea de temperatura ambiente (HTU21D) y temperatura de componentes críticos (LM75A).

* Lógica de Resiliencia: Implementación de manejo de excepciones I2C para evitar el bloqueo del bus en condiciones de interferencia electromagnética.

* Comunicación Segura: Envío de notificaciones mediante SMTP con autenticación.

* Gestión de Estados: Lógica de histéresis para prevenir ataques de denegación de servicio (DoS) por saturación de alertas (anti-spam).

* Seguridad de Credenciales: Uso de secrets.py con .gitignore para proteger la exposición de datos sensibles.

## Estructura del Repositorio
- main.py: Lógica principal y bucle de control de seguridad.

- umail.py: Cliente SMTP ligero para el envío de notificaciones.

- htu21d.py / lm75a.py: Drivers para los sensores I2C.

- network_manager.py: Módulo de conexión Wi-Fi.

- .gitignore: Archivo de configuración para excluir credenciales de la subida al repositorio.

## Instalación
Clonar el repositorio.

Crear un archivo secrets.py siguiendo el formato:
- WIFI_SSID = "Tu_SSID"
- WIFI_PASS = "Tu_Password"
- EMAIL_USER = "tu_correo@gmail.com"
- EMAIL_PASS = "tu_app_password"
- SMTP_SERVER = "smtp.gmail.com"
- SMTP_PORT = 587

Sincronizar los archivos a la ESP32 usando Pymakr o VS Code.
