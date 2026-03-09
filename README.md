# monitor-risorse
A lightweight, text-based system monitor written in Python that tracks CPU, RAM, Disk, and GPU (AMD) usage, saving data in real time to a log file on the Desktop.

## ✨ Functionality:
- **Real-time Monitoring:** Track CPU and GPU usage percentages.
- **Memory and Disk Management:** View details on used/total RAM and disk I/O statistics.
- **Automatic Logging:** Writes data to `monitor_log.txt` directly on your desktop for later analysis.
- **Elegant Interface:** Uses the `Rich` library for a clean terminal display with panels and colors.
- **Quick Close:** Global hotkey (`Shift + Space`) to safely end monitoring from any window.

## 🛠️ Hardware & Software Requirements:
- **Operating System:** Windows (for Desktop path and `pyadl` support).
- **GPU:** Specific support for **AMD** graphics cards via ADL (AMD Display Library).
- **⚠️ Note on Antivirus:**
    - Some security software may block the execution of the script or the `keyboard` library by mistakenly identifying them as potential threats.
    - If the script crashes on startup, try adding the project folder or the Python interpreter to your antivirus exclusions.

## 🚀 Installation:
1. **Clone the repository:**
  ```bash
    git clone https://github.com/bl4ckm4mb4-6/monitor-risorse.git
    cd monitor-risorse
  ```
2. **Install the necessary dependencies:**
  ```bash
    pip install -r requirements.txt
  ```

## 💻 Usage:
- **Run the script:**
  ```bash
    python monitor_risorse.py
  ```

Upon startup, the program will begin recording data every 30 seconds (configurable in the code). To stop the process, press:
`Shift + Space`

## 📂 Log Structure:
The file generated on your desktop will have a format similar to the following:
```bash
  2026-03-09 16:53:40
  -----MONITORAGGIO RISORSE-----
  Uso CPU: 12.5%
  Uso RAM: 45.2%  (Usata: 7.23 GB / Totale: 16.00 GB)
  Uso Disco: 60.1% (Libero: 120.45 GB)
  Byte letti: 14.20 MB    Byte scritti: 5.12 MB
  Uso GPU: 22%
```
