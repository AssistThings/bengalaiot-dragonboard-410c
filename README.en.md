# bengalaiot-dragonboard-410c

[Português](README.md) · [Español](README.es.md) · **English**

The original **Bengala IoT** (smart cane) prototype on the DragonBoard 410c (Linaro).

- `Ultrassom1.py` and `Ultrassom2.py` read two ultrasonic sensors and play an alert sound (`ding.ogg`) when an obstacle is closer than 50 cm.
- `Buzzer.py` handles the emergency button: when pressed, it turns on the buzzer and sends an SMS through Twilio.
- `BengalaIotStart` launches all three scripts at once.

## Dependencies

- Twilio
- mraa (Linaro ships with it, so check before installing)
- pygame (to play the alert sound)

Before running, fill in the Twilio credentials and phone numbers in `Buzzer.py` (`<twilio_sid>`, `<twilio_token>`, `<destination_phone>`, `<your_phone>`, `<sms_body>`).

## Running

1. Copy all files to `/home/linaro/Bengalaiot/` on the board (the path `BengalaIotStart` uses).
2. Make `BengalaIotStart` executable:
   ```bash
   chmod 755 BengalaIotStart
   ```
3. Run it by clicking the file in the desktop, or with:
   ```bash
   ./BengalaIotStart
   ```

---

Part of [AssistThings](https://assistthings.github.io/en/): open assistive technology with AI and IoT.
