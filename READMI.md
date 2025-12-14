# Mini Project IoT – MQTT Room Monitoring

## 📌 Deskripsi
Project ini merupakan mini project untuk mensimulasikan sistem **IoT Room Monitoring** menggunakan protokol **MQTT** dan broker cloud **HiveMQ**.  
Sistem ini mensimulasikan monitoring **konsumsi energi** dan **status motor** pada beberapa ruangan tanpa menggunakan sensor fisik.

---

## 🎯 Tujuan Project
- Memahami konsep komunikasi IoT menggunakan MQTT
- Mengimplementasikan arsitektur publish–subscribe
- Mensimulasikan room monitoring pada lingkungan cloud
- Menghubungkan edge device ke cloud broker

---

## 🧠 Konsep Sistem
- **Publisher** berperan sebagai perangkat IoT (edge device)
- **Broker MQTT (HiveMQ)** sebagai perantara komunikasi
- **Subscriber** berperan sebagai sistem monitoring penerima data

---

## 🏗️ Arsitektur

Publisher (Python)
↓
HiveMQ Broker
↓
Subscriber (Python)


---

## 📊 Data yang Dimonitor
- **Room**: Identitas ruangan (kelas, lab, server room)
- **Energy Usage**: Konsumsi energi (Watt)
- **Motor Status**: ON / OFF
- **Timestamp**: Waktu pengiriman data

---

## 🛠️ Teknologi yang Digunakan
- Python 3
- MQTT Protocol
- HiveMQ Public Broker
- Library: `paho-mqtt`

---

## ▶️ Cara Menjalankan Project

### 1. Clone repository
```bash
git clone https://github.com/galangam/mini-project-iot-mqtt.git
cd mini-project-iot-mqtt

2. Aktifkan virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependency

pip install paho-mqtt

4. Jalankan Subscriber

python subscriber.py

5. Jalankan Publisher (terminal baru)

python publisher.py

📌 Contoh Output

{
  "room": "lab_komputer",
  "energy_usage_watt": 523.45,
  "motor_status": "ON",
  "timestamp": "2025-12-14 11:32:26"
}

✅ Hasil

    Publisher berhasil mengirim data monitoring

    Subscriber berhasil menerima data secara real-time

    Sistem berjalan sesuai konsep IoT dan MQTT

📎 Catatan

Project ini menggunakan data simulasi dan tidak terhubung dengan sensor fisik.
Virtual environment (venv) tidak disertakan dalam repository sesuai best practice.

👨‍💻 Author

Galang
Mini Project – Edge Computing & IoT in Cloud
