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
**1. Clone the repository:**
  ```bash
    git clone https://github.com/bl4ckm4mb4-6/monitor-risorse.git
    cd monitor-risorse
  ```
**2. Install the necessary dependencies:**
  ```bash
    pip install -r requirements.txt
  ```

## 💻 Usage:
**Run the script:**
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

**⚠️ Note:** The console interface and the generated log files are written in **Italian**.

## 📦 Used Libraries:
- [psutil](https://pypi.org/project/psutil/) - System and hardware statistics.
- [rich](https://pypi.org/project/rich/) - Console text formatting and styles.
- [keyboard](https://pypi.org/project/keyboard/) - Global hotkey management.
- [pyadl](https://pypi.org/project/pyadl/) - Interface to the AMD Display Library.

---

*Project created for educational purposes for lightweight hardware monitoring.*

---


## 📦 Executable version (.exe)

For convenience, the project has been compiled into an executable file using **PyInstaller**. This allows you to start monitoring without having to manually install Python or any dependencies.

### How to use it:
1. Download the `monitor_risorse.exe` file from the section [Releases](https://github.com/bl4ckm4mb4-6/monitor-risorse/releases/).
2. Run the executable by double-clicking (if your antivirus blocks it, read the note below).
3. The log file will be automatically created on your Desktop.


> **⚠️ Note on Antivirus & False Positives:** Due to the nature of hardware monitoring and the implementation of global hotkeys, some security software may flag this application as a **false positive**. This is expected behavior for scripts that interact directly with system inputs and sensors. To ensure full functionality, you may need to add the executable to your antivirus exclusion list.


## 🖥️ Compatibility
**OS**: Windows 10 / 11 (64-bit)

**Architecture**: x86_64

**Hardware**: Optimized for **AMD GPUs**.


_Note: If you are using a different GPU (NVIDIA/Intel), you will need to modify the source code to disable or adapt the GPU monitoring section before recompiling._


## 🛠️ How to create the executable (.exe) yourself
If you prefer to compile the script from source code for security or customization reasons, you can do so using **PyInstaller** which is already included in the `requirements.txt` file.

### Procedure:

**1. Install PyInstaller (if you downloaded the dependencies from `requirements.txt` you can skip step 1):**

  Open Terminal and type:
```bash
    pip install pyinstaller
```

**2. Compile the script:**

Open the project folder in the terminal, and run the command:
```bash
    pyinstaller --onefile --name "Monitor Risorse" --icon "monitor.ico" monitor_risorse.py
```

- `--onefile`: Create a single `.exe` file instead of a folder full of files.
- `--name`: Give a name to the executable, so you can call it as you want.
- `--icon`: Assign an icon to the executable. You can find mine in the repository, but you can replace it with your own.

**3. Retrieve the file:**

Once the process is complete, you'll find your executable file in the newly created `dist/` folder. A `build/` folder and a `.spec` file are also created, which you can delete without problems. You can then move the executable file to any folder you like.
