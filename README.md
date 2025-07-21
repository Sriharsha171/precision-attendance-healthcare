# precision-attendance-healthcare
A smart, hygienic, and accurate facial recognition attendance system built using Python, OpenCV, and KNN. Designed for healthcare environments to ensure secure, real-time staff tracking.

A contactless facial recognition-based attendance system built using Python, OpenCV, and the K-Nearest Neighbors (KNN) algorithm. Designed specifically for healthcare environments to enhance hygiene, accuracy, and real-time attendance tracking.

> ⚠️ **Note**: This project is designed to run exclusively on a **Raspberry Pi** setup with a connected camera module.

---

## 👨‍⚕️ Problem Statement
Manual attendance systems in hospitals can be error-prone, unhygienic, and time-consuming. This system replaces traditional methods with a facial recognition solution that offers speed, accuracy, and hygiene — essential in clinical settings.

---

## 🧪 Features
Real-time facial recognition using camera
Contactless attendance logging
Doctor-specific schedule popup
GUI for data collection and monitoring
Data stored in central database or local file

---

## 🤝 Authors
Chandana S, Harsha Mohan G R, Pramodh S, Sriharsha B K
Guided by Dr. Vidya E V
East West Institute of Technology
Department of Artificial Intelligence and Machine Learning

---

## 🧠 Technology Stack
- Raspberry Pi 4 (8GB RAM)
- Python 3
- OpenCV
- K-Nearest Neighbors (KNN)
- Histogram of Oriented Gradients (HOG)
- Tkinter (GUI)
- Pandas, NumPy

---

## 🔧 Hardware Requirements

- Raspberry Pi 4 (Recommended: 8GB RAM)
- Pi Camera Module / USB Webcam
- Monitor, Keyboard, Mouse
- Raspbian OS 64-bit (or compatible Raspberry Pi OS)

---

## 🖥️ How to Run

```bash
# On Raspberry Pi terminal
sudo apt update
pip install -r requirements.txt
python3 src/main.py
