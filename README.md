# bengalaiot-dragonboard-410c

**Português** · [Español](README.es.md) · [English](README.en.md)

Protótipo original da **Bengala IoT** na DragonBoard 410c (Linaro).

- `Ultrassom1.py` e `Ultrassom2.py` leem dois sensores ultrassônicos e tocam um alerta sonoro (`ding.ogg`) quando um obstáculo está a menos de 50 cm.
- `Buzzer.py` cuida do botão de emergência: ao ser pressionado, liga o buzzer e envia um SMS pelo Twilio.
- `BengalaIotStart` abre os três scripts de uma vez.

## Dependências

- Twilio
- mraa (o Linaro já vem com ela instalada, então teste antes de instalar)
- pygame (para tocar o alerta sonoro)

Antes de rodar, preencha em `Buzzer.py` as credenciais do Twilio e os números de telefone (`<twilio_sid>`, `<twilio_token>`, `<destination_phone>`, `<your_phone>`, `<sms_body>`).

## Execução

1. Copie todos os arquivos para `/home/linaro/Bengalaiot/` na placa (é o caminho usado em `BengalaIotStart`).
2. Dê permissão de execução ao arquivo `BengalaIotStart`:
   ```bash
   chmod 755 BengalaIotStart
   ```
3. Para executar, clique no arquivo na interface gráfica ou use o comando:
   ```bash
   ./BengalaIotStart
   ```

---

Parte do [AssistThings](https://assistthings.github.io): tecnologia assistiva aberta com IA e IoT.
