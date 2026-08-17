# TBF.OS.OS.MD 🚀

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Termux%20%2F%20Linux-green?style=for-the-badge&logo=android&logoColor=white)
![UI](https://img.shields.io/badge/UI-Rich%20TUI-magenta?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)
![Author](https://img.shields.io/badge/Developer-TBFPUMBA-orange?style=for-the-badge)

> **Security Audit & Network Recon Suite for Termux**  
> Потужний консольний інструмент для мережевої розвідки та аудиту з сучасним кіберпанк TUI-інтерфейсом.

---

## 📌 Основні можливості

- ⚡ **Fast Port Scanner** — автоматизований сканер відкритих портів на базі Nmap із виводом у графічні таблиці.
- 🌍 **IP OSINT Lookup** — миттєвий збір публічних даних за IP-адресою (геолокація, місто, провайдер, ASN).
- 🎨 **Cyberpunk TUI** — анімований запуск, прогрес-бари, системні сповіщення та об'ємний ASCII-банер.

---

## 📥 Встановлення та запуск у Termux

```bash
# 1. Оновлення пакетів та встановлення залежностей
pkg update && pkg install python nmap git -y

# 2. Клонування репозиторію
git clone https://github.com/ВАШ_USERNAME/TBF.OS.OS.MD.git (https://github.com/ВАШ_USERNAME/TBF.OS.OS.MD.git)
cd TBF.OS.OS.MD

# 3. Встановлення бібліотеки Rich
pip install -r requirements.txt

# 4. Запуск інструменту
python tbf_os.py
