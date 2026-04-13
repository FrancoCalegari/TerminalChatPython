import socket
import threading
import sys
import subprocess
import os

# --- AUTO-INSTALACIÓN DE DEPENDENCIAS ---
def install_dependencies():
    try:
        import colorama
    except ImportError:
        print("Instalando dependencias necesarias...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "colorama"])
        print("Dependencias instaladas. Reiniciando script...\n")
        os.execv(sys.executable, ['python'] + sys.argv)

install_dependencies()
from colorama import Fore, Style, init

# Inicializar colorama para compatibilidad con Windows/PowerShell
init(autoreset=True)

# --- CONFIGURACIÓN ---
PORT = 50005  # Puerto arbitrario para el chat
BUFFER_SIZE = 1024

def get_ip():
    """Obtiene la IP local del dispositivo."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # No necesita conexión real, solo para obtener la interfaz activa
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def listener(sock, my_name):
    """Hilo encargado de recibir mensajes continuamente."""
    while True:
        try:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            decoded_msg = data.decode('utf-8')
            
            # Evitar mostrar nuestros propios mensajes duplicados
            if not decoded_msg.startswith(f"[{my_name}]"):
                print(f"\n{Fore.GREEN}{decoded_msg}{Style.RESET_ALL}")
                print(f"{Fore.CYAN}{my_name}:{Style.RESET_ALL} ", end="", flush=True)
        except Exception as e:
            print(f"\n{Fore.RED}Error recibiendo mensaje: {e}")
            break

def main():
    print(f"{Fore.YELLOW}=== LAN UDP CHAT v1.0 ==={Style.RESET_ALL}")
    
    user_name = input("Introduce tu nombre para el chat: ").strip()
    if not user_name:
        user_name = "Anonimo"

    # Configuración del Socket UDP con Broadcast
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    
    # En Termux/Linux a veces es necesario bindear a '' o a la IP de broadcast
    try:
        sock.bind(('', PORT))
    except Exception as e:
        print(f"{Fore.RED}Error al bindear el puerto: {e}")
        return

    # Iniciar hilo de escucha
    thread = threading.Thread(target=listener, args=(sock, user_name), daemon=True)
    thread.start()

    print(f"\n{Fore.BLUE}Conectado. Escribe /help para ver comandos.{Style.RESET_ALL}")
    
    while True:
        msg = input(f"{Fore.CYAN}{user_name}:{Style.RESET_ALL} ")
        
        if msg.startswith('/'):
            cmd = msg.split()[0].lower()
            if cmd == '/help':
                print(f"{Fore.YELLOW}Comandos disponibles:")
                print("/help   - Muestra este mensaje")
                print("/ipinfo - Muestra tu dirección IP local")
                print("/info   - Información sobre el funcionamiento del script")
                print("/exit   - Salir del chat")
            
            elif cmd == '/ipinfo':
                print(f"{Fore.MAGENTA}Tu IP local es: {get_ip()}")
            
            elif cmd == '/info':
                print(f"{Fore.WHITE}\n--- Información Técnica ---")
                print("Este script utiliza el protocolo UDP (User Datagram Protocol).")
                print("A diferencia de TCP, UDP permite el uso de 'Broadcasting', lo que")
                print("significa que los mensajes se envían a la dirección 255.255.255.255,")
                print("siendo recibidos por cualquier dispositivo en la misma subred que")
                print(f"esté escuchando en el puerto {PORT}. No requiere un servidor central.")
                print("---------------------------\n")
            
            elif cmd == '/exit':
                print("Saliendo...")
                break
            else:
                print(f"{Fore.RED}Comando no reconocido.")
        else:
            # Enviar mensaje por broadcast
            full_msg = f"[{user_name}]: {msg}"
            sock.sendto(full_msg.encode('utf-8'), ('<broadcast>', PORT))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nChat finalizado.")
        sys.exit()
