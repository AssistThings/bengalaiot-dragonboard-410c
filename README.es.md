# bengalaiot-dragonboard-410c

[Português](README.md) · **Español** · [English](README.en.md)

Prototipo original de la **Bengala IoT** (bastón inteligente) en la DragonBoard 410c (Linaro).

- `Ultrassom1.py` y `Ultrassom2.py` leen dos sensores ultrasónicos y reproducen una alerta sonora (`ding.ogg`) cuando un obstáculo está a menos de 50 cm.
- `Buzzer.py` controla el botón de emergencia: al presionarlo, enciende el zumbador y envía un SMS con Twilio.
- `BengalaIotStart` abre los tres scripts a la vez.

## Dependencias

- Twilio
- mraa (Linaro ya la trae instalada, así que pruébala antes de instalarla)
- pygame (para reproducir la alerta sonora)

Antes de ejecutar, completa en `Buzzer.py` las credenciales de Twilio y los números de teléfono (`<twilio_sid>`, `<twilio_token>`, `<destination_phone>`, `<your_phone>`, `<sms_body>`).

## Ejecución

1. Copia todos los archivos a `/home/linaro/Bengalaiot/` en la placa (es la ruta que usa `BengalaIotStart`).
2. Da permiso de ejecución al archivo `BengalaIotStart`:
   ```bash
   chmod 755 BengalaIotStart
   ```
3. Para ejecutarlo, haz clic en el archivo desde la interfaz gráfica o usa el comando:
   ```bash
   ./BengalaIotStart
   ```

---

Parte de [AssistThings](https://assistthings.github.io/es/): tecnología asistiva abierta con IA e IoT.
