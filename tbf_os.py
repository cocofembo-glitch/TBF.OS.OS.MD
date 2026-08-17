import time
import os
import subprocess
import urllib.request
import json
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.progress import Progress, TextColumn, BarColumn, TaskProgressColumn, TimeRemainingColumn
from rich.prompt import Prompt
from rich.align import Align

console = Console()

# ВЕЛИКИЙ ЧЕРЕП У СТИЛІ MF CONSOLE
SKULL_ART = """[bold red]
                uuuuuuu
            uu$$$$$$$$$$$uu
         uu$$$$$$$$$$$$$$$$$uu
        u$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$u
      u$$$$$$"   "$$$"   "$$$$$$u
      "$$$$"      u$u       $$$$"
       $$$u       u$u       u$$$
       $$$u      u$$$u      u$$$
        "$$$$uu$$$   $$$uu$$$$"
         "$$$$$$$"   "$$$$$$$"
           u$$$$$$$u$$$$$$$u
            u$"$"$"$"$"$"$u
 ___________________________________
/                                   \\
|     TBF.OS.OS.MD :: ACCESS DENIED |
\\___________________________________/
[/bold red]"""

def startup_animation():
    os.system("clear")
    
    # 1. Ефект миготливого курсора (6 секунд)
    boot_messages = [
        "Initializing TBF Kernel...",
        "Loading Security Modules...",
        "Establishing OSINT Proxies...",
        "Bypassing Firewalls...",
        "Allocating Virtual Memory...",
        "System Ready."
    ]
    
    for msg in boot_messages:
        console.print(f"[bold cyan][*] {msg}[/bold cyan]", end="")
        for _ in range(2):
            console.print("[bold white] █[/bold white]", end="\r")
            time.sleep(0.25)
            console.print("  ", end="\r")
            time.sleep(0.25)
        console.print()
    
    time.sleep(1)
    console.print("\n[bold yellow][!] Starting Deep Initialization Sequence...[/bold yellow]\n")

    # 2. Прогрес-бар на 20 секунд
    with Progress(
        TextColumn("[bold magenta]{task.description}"),
        BarColumn(bar_width=50, style="blue", complete_style="bold cyan"),
        TaskProgressColumn(),
        TimeRemainingColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Loading TBF.OS.OS.MD Core...", total=200)
        for _ in range(200):
            progress.update(task, advance=1)
            time.sleep(0.1)

    os.system("clear")

    # 3. Величезний череп MF Console
    skull_panel = Panel(
        Align.center(SKULL_ART + "\n\n[bold white blink]>>> PRESS ENTER TO SYSTEM OVERRIDE <<<[/bold white blink]"),
        border_style="bold red",
        title="[bold yellow]TBFPUMBA CORE SYSTEM[/bold yellow]",
        subtitle="[bold red]MF CONSOLE TERMINAL[/bold red]",
        padding=(1, 2)
    )
    console.print(skull_panel)
    input()

def show_header():
    os.system("clear")
    title_panel = Panel.fit(
        "[bold cyan]TBF.OS.OS.MD[/bold cyan]\n[dim white]Security Audit Toolkit v3.0[/dim white]",
        border_style="magenta",
        title="[bold yellow]TBFPUMBA[/bold yellow]",
        subtitle="[bold blue]Termux Edition[/bold blue]"
    )
    console.print(title_panel)

def scan_ports():
    show_header()
    target = Prompt.ask("[bold yellow]Введіть IP або домен для сканування[/bold yellow]")
    if not target:
        return

    console.print(f"\n[bold cyan][+] Запуск Nmap для {target}...[/bold cyan]\n")
    
    try:
        cmd = f"nmap -F --open {target}"
        result = subprocess.check_output(cmd, shell=True, text=True)
        
        table = Table(title=f"Результати сканування: {target}", header_style="bold magenta", border_style="cyan")
        table.add_column("Порт / Протокол", style="bold green")
        table.add_column("Стан", style="bold yellow")
        table.add_column("Сервіс", style="bold white")

        for line in result.split("\n"):
            if "/tcp" in line or "/udp" in line:
                parts = [p for p in line.split(" ") if p]
                if len(parts) >= 3:
                    table.add_row(parts[0], parts[1], parts[2])

        console.print(table)
    except Exception as e:
        console.print(Panel(f"[bold red]Помилка при виконанні Nmap:[/bold red]\n{e}", border_style="red"))

def osint_lookup():
    show_header()
    target = Prompt.ask("[bold yellow]Введіть IP для OSINT аналізу[/bold yellow]")
    if not target:
        return

    try:
        url = f"https://ipapi.co/{target}/json/"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())

        table = Table(title=f"OSINT Інформація: {target}", header_style="bold cyan", border_style="green")
        table.add_column("Параметр", style="bold yellow")
        table.add_column("Значення", style="bold white")

        table.add_row("IP", data.get("ip", "N/A"))
        table.add_row("Місто", data.get("city", "N/A"))
        table.add_row("Регіон", data.get("region", "N/A"))
        table.add_row("Країна", data.get("country_name", "N/A"))
        table.add_row("Провайдер (ASN)", data.get("org", "N/A"))

        console.print(table)
    except Exception as e:
        console.print(Panel(f"[bold red]Помилка отримання даних:[/bold red]\n{e}", border_style="red"))

def main_menu():
    while True:
        show_header()

        menu_table = Table(show_header=False, border_style="blue", box=None)
        menu_table.add_column("№", style="bold cyan")
        menu_table.add_column("Опис", style="bold white")

        menu_table.add_row("[1]", "Fast Port Scan (Сканер портів + Таблиця)")
        menu_table.add_row("[2]", "IP OSINT Lookup (Геолокація та ASN)")
        menu_table.add_row("[0]", "Вихід")

        console.print(Panel(menu_table, title="[bold green]Головне Меню[/bold green]", border_style="bright_blue"))

        choice = Prompt.ask("[bold yellow]Оберіть пункт[/bold yellow]", choices=["1", "2", "0"])

        if choice == "1":
            scan_ports()
            Prompt.ask("\n[dim]Натисніть Enter для продовження...[/dim]")
        elif choice == "2":
            osint_lookup()
            Prompt.ask("\n[dim]Натисніть Enter для продовження...[/dim]")
        elif choice == "0":
            console.print("[bold red]Завершення роботи TBF.OS.OS.MD...[/bold red]")
            break

if __name__ == "__main__":
    startup_animation()
    main_menu()

