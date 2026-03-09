import time
import os
import psutil
import keyboard
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from datetime import datetime
from pyadl import ADLManager

console = Console()
EXIT = "Shift+Space"
running = True
path_log = os.path.join(os.environ["USERPROFILE"], "Desktop", "monitor_log.txt")

def gpu_info():
    try:
        # Interrogazione al sistema
        devices = ADLManager.getInstance().getDevices()
        if devices:
            gpu = devices[0]
            gpu_usage = gpu.getCurrentUsage()
            return gpu_usage
        return 0
    except:
        return 0

def monitor():
    with open(path_log, "a", encoding="utf-8") as file:
        global status
        status = console.status("[bold dark_orange]Monitoraggio in corso...")
        while running:
            status.start()
            # CPU stats
            cpu = psutil.cpu_percent(interval=1)
            # RAM stats
            ram = psutil.virtual_memory()
            # Disk stats
            disco = psutil.disk_usage("C:")
            io = psutil.disk_io_counters()
            # GPU stats
            gpu = gpu_info()

            file.write(f"Uso CPU: {cpu}%\n")
            file.write(f"Uso RAM: {ram.percent}%  (Usata: {ram.used / (1024**3):.2f} GB / Totale: {ram.total / (1024**3):.2f} GB)\n")
            file.write(f"Uso Disco: {disco.percent}%  (Usato: {disco.used / (1024**3):.2f} GB / Totale: {disco.total / (1024**3):.2f} GB / Libero: {disco.free / (1024**3):.2f} GB)\n")
            file.write(f"Byte letti: {io.read_bytes / (1024**2):.2f} MB\tByte scritti: {io.write_bytes / (1024**2):.2f} MB\n")
            file.write(f"Uso GPU: {gpu}%\n\n")
            # Scrive immediatamente i dati sul disco
            file.flush()
                
            # Attesa non bloccante
            # Fa 300 pause da 0.1 secondi. 300 * 0.1 = 30 secondi
            for i in range(300):
                if not running:
                    time.sleep(0.7)
                    return
                time.sleep(0.1)

def stop_monitor():
    global running
    running = False
    status.stop()
    console.print(f"\n[bold dodger_blue1][LOG] Dati salvati in {path_log}")
    console.print("[bold yellow1][INFO] Chiusura programma...\n")


# MAIN
# Listener in ascolto in background
keyboard.add_hotkey(EXIT, stop_monitor, suppress=True)

console.print("\n")
testo = Text("MONITORAGGIO RISORSE",style="bold green", justify="center")
pannello = Panel(testo, subtitle="1.0", style="bold green", padding=(0, 4) ,expand=False)
console.print(Align.center(pannello))
console.print(f"\nBenvenuto in monitor risorse!")
console.print(f"Premi [bold cyan1]{EXIT}[/bold cyan1] per terminare il programma.")

with open(path_log, "w", encoding="utf-8") as file:
    data = datetime.now().strftime(f"%Y-%m-%d %H:%M:%S")
    file.write(data)
    file.write(f"\n\n-----MONITORAGGIO RISORSE-----\n")

try:
    monitor()
finally:
    keyboard.unhook_all()
    status.stop()