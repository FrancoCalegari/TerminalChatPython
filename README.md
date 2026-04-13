# Terminal Chat Python (UDP Broadcast)

Este es un chat de terminal sencillo que utiliza el protocolo UDP y "broadcast" para permitir la comunicación entre múltiples dispositivos en la misma red local (LAN) sin necesidad de un servidor central.

## Características
- Comunicación en tiempo real por UDP.
- Descubrimiento automático de pares mediante broadcast.
- Interfaz colorida en la terminal.
- Comandos integrados (`/help`, `/ipinfo`, `/info`, `/exit`).
- Auto-instalación de dependencias (Colorama).

---

## Guía de Ejecución por Plataforma

### 🐧 Linux (Terminal)
Para Linux, se recomienda el uso de un entorno virtual (`venv`) para mantener las dependencias aisladas.

1. **Abrir la terminal** en la carpeta del proyecto.
2. **Crear el entorno virtual** (si no existe):
   ```bash
   python3 -m venv venv
   ```
3. **Activar el entorno virtual**:
   ```bash
   source venv/bin/activate
   ```
4. **Ejecutar el chat**:
   ```bash
   python3 chat.py
   ```

### 🪟 Windows (PowerShell)
En Windows, PowerShell es la herramienta recomendada.

1. **Abrir PowerShell** en la carpeta del proyecto.
2. **Crear el entorno virtual** (si no existe):
   ```powershell
   python -m venv venv
   ```
3. **Activar el entorno virtual**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   *Nota: Si recibes un error de ejecución de scripts, ejecuta PowerShell como administrador y usa: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`*
4. **Ejecutar el chat**:
   ```powershell
   python chat.py
   ```

### 🍎 macOS (Terminal)
El proceso es idéntico a Linux.

1. **Abrir la terminal** (Terminal.app o iTerm2).
2. **Crear el entorno virtual**:
   ```bash
   python3 -m venv venv
   ```
3. **Activar el entorno virtual**:
   ```bash
   source venv/bin/activate
   ```
4. **Ejecutar el chat**:
   ```bash
   python3 chat.py
   ```

### 📱 Termux (Android)
Termux es una terminal potente para Android.

1. **Actualizar paquetes e instalar Python**:
   ```bash
   pkg update && pkg upgrade
   pkg install python
   ```
2. **Navegar a la carpeta del proyecto** (si descargaste el código):
   ```bash
   cd /ruta/a/la/carpeta/TerminalChatPython
   ```
3. **Ejecutar directamente** (Termux no suele requerir venv para scripts simples, pero puedes usarlo):
   ```bash
   python chat.py
   ```

---

## Comandos del Chat
Dentro del chat, puedes usar los siguientes comandos:
- `/help`: Muestra la lista de comandos disponibles.
- `/ipinfo`: Muestra tu dirección IP local.
- `/info`: Explica brevemente cómo funciona la tecnología UDP Broadcast.
- `/exit`: Cierra la aplicación de forma segura.

## Requisitos
- Python 3.6 o superior.
- Conexión a una red local (LAN) que permita tráfico UDP/Broadcast (la mayoría de los routers domésticos lo permiten).
