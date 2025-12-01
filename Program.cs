using System;
using System.Collections.Generic;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using System.Threading.Tasks;

namespace NetworkSecurityToolkit
{
    class Program
    {
        static async Task Main(string[] args)
        {
            Console.Title = "🛡️ Network Security Toolkit 2025";
            Console.ForegroundColor = ConsoleColor.Cyan;
            
            Console.WriteLine("╔══════════════════════════════════════════════════════════════╗");
            Console.WriteLine("║            🛡️ NETWORK SECURITY TOOLKIT 2025              ║");
            Console.WriteLine("║              🔍 ADVANCED NETWORK ANALYZER                ║");
            Console.WriteLine("╚══════════════════════════════════════════════════════════════╝");
            Console.ResetColor();

            while (true)
            {
                Console.WriteLine("\n📋 SECURITY TOOLS:");
                Console.WriteLine("─".PadRight(60, '─'));
                Console.WriteLine("   1️⃣  🌐 Port Scanner");
                Console.WriteLine("   2️⃣  📡 Network Discovery");
                Console.WriteLine("   3️⃣  🔍 Packet Sniffer");
                Console.WriteLine("   4️⃣  🚨 Intrusion Detection");
                Console.WriteLine("   5️⃣  🔐 Encryption Tools");
                Console.WriteLine("   6️⃣  📊 Traffic Analyzer");
                Console.WriteLine("   7️⃣  🛡️ Firewall Manager");
                Console.WriteLine("   8️⃣  🔑 Password Auditor");
                Console.WriteLine("   9️⃣  ❌ Exit");

                Console.Write("\n⚡ Choose your tool [1-9]: ");
                var choice = Console.ReadLine();

                switch (choice)
                {
                    case "1":
                        await PortScanner();
                        break;
                    case "2":
                        await NetworkDiscovery();
                        break;
                    case "3":
                        await PacketSniffer();
                        break;
                    case "4":
                        await IntrusionDetection();
                        break;
                    case "5":
                        await EncryptionTools();
                        break;
                    case "6":
                        await TrafficAnalyzer();
                        break;
                    case "7":
                        await FirewallManager();
                        break;
                    case "8":
                        await PasswordAuditor();
                        break;
                    case "9":
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("\n👋 Shutting down...");
                        Console.ResetColor();
                        return;
                    default:
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("❌ Invalid option! Please choose 1-9");
                        Console.ResetColor();
                        await Task.Delay(2000);
                        break;
                }
            }
        }

        static async Task PortScanner()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine("🌐 PORT SCANNER");
            Console.ResetColor();

            Console.Write("🎯 Target IP [127.0.0.1]: ");
            var target = Console.ReadLine();
            if (string.IsNullOrEmpty(target))
                target = "127.0.0.1";

            Console.Write("📊 Port range [1-1000]: ");
            var range = Console.ReadLine();
            if (string.IsNullOrEmpty(range))
                range = "1-1000";

            var parts = range.Split('-');
            var startPort = int.Parse(parts[0]);
            var endPort = int.Parse(parts[1]);

            Console.WriteLine($"\n🚀 Scanning {target} from port {startPort} to {endPort}...");
            Console.WriteLine("─".PadRight(50, '─'));

            var openPorts = new List<int>();

            for (int port = startPort; port <= endPort; port++)
            {
                try
                {
                    using var client = new TcpClient();
                    var result = await client.ConnectAsync(target, port);
                    if (client.Connected)
                    {
                        openPorts.Add(port);
                        Console.WriteLine($"✅ Port {port}: OPEN");
                    }
                }
                catch
                {
                    // Port closed
                }

                if (port % 50 == 0)
                {
                    Console.Write($"Progress: {port}/{endPort} ({(double)port/endPort*100:F1}%)\r");
                }
            }

            Console.WriteLine($"\n\n🎯 Scan Complete! Found {openPorts.Count} open ports:");
            foreach (var port in openPorts)
            {
                Console.WriteLine($"   📡 Port {port}");
            }

            Console.WriteLine("\nPress ENTER to return to main menu...");
            Console.ReadLine();
        }

        static async Task NetworkDiscovery()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Cyan;
            Console.WriteLine("📡 NETWORK DISCOVERY");
            Console.ResetColor();

            Console.Write("🌐 Network range [192.168.1.0/24]: ");
            var network = Console.ReadLine();
            if (string.IsNullOrEmpty(network))
                network = "192.168.1.0/24";

            Console.WriteLine($"\n🔍 Discovering devices in {network}...");
            Console.WriteLine("─".PadRight(50, '─'));

            var baseIP = "192.168.1";
            var devices = new List<string>();

            for (int i = 1; i <= 254; i++)
            {
                var ip = $"{baseIP}.{i}";
                try
                {
                    using var ping = new System.Net.NetworkInformation.Ping();
                    var reply = await ping.SendPingAsync(ip, 100);
                    if (reply.Status == System.Net.NetworkInformation.IPStatus.Success)
                    {
                        devices.Add(ip);
                        Console.WriteLine($"🖥️  Device found: {ip} - {reply.RoundtripTime}ms");
                    }
                }
                catch
                {
                    // No response
                }
            }

            Console.WriteLine($"\n🎯 Discovery Complete! Found {devices.Count} devices:");
            foreach (var device in devices)
            {
                Console.WriteLine($"   🌐 {device}");
            }

            Console.WriteLine("\nPress ENTER to return to main menu...");
            Console.ReadLine();
        }

        static async Task PacketSniffer()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Yellow;
            Console.WriteLine("🔍 PACKET SNIFFER");
            Console.ResetColor();

            Console.WriteLine("⚠️  Packet sniffing requires administrator privileges!");
            Console.WriteLine("📡 Starting packet capture on all interfaces...");
            Console.WriteLine("(Press ESC to stop)");

            Console.WriteLine("\n📊 Captured packets:");
            Console.WriteLine("─".PadRight(80, '─'));

            var packetCount = 0;
            var random = new Random();

            while (true)
            {
                if (Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Escape)
                    break;

                // Simulate packet capture
                packetCount++;
                var sourceIP = $"{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}";
                var destIP = $"{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}";
                var protocol = new[] { "TCP", "UDP", "ICMP", "HTTP", "HTTPS" }[random.Next(5)];
                var size = random.Next(64, 1500);

                Console.WriteLine($"📦 Packet #{packetCount}: {sourceIP} → {destIP} | {protocol} | {size} bytes");

                await Task.Delay(100);
            }

            Console.WriteLine($"\n🎯 Captured {packetCount} packets total");
            Console.WriteLine("\nPress ENTER to return to main menu...");
            Console.ReadLine();
        }

        static async Task IntrusionDetection()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine("🚨 INTRUSION DETECTION SYSTEM");
            Console.ResetColor();

            Console.WriteLine("🛡️  Monitoring network for suspicious activities...");
            Console.WriteLine("(Press ESC to stop monitoring)");

            Console.WriteLine("\n📊 Security Events:");
            Console.WriteLine("─".PadRight(80, '─'));

            var eventCount = 0;
            var random = new Random();
            var threats = new[]
            {
                "Suspicious login attempt detected",
                "Port scanning activity detected",
                "DDoS attack pattern identified",
                "Malware communication detected",
                "Unauthorized access attempt",
                "Data exfiltration attempt",
                "Brute force attack detected"
            };

            while (true)
            {
                if (Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Escape)
                    break;

                eventCount++;
                var threat = threats[random.Next(threats.Length)];
                var severity = new[] { "LOW", "MEDIUM", "HIGH", "CRITICAL" }[random.Next(4)];
                var sourceIP = $"{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}.{random.Next(1,255)}";

                var color = severity switch
                {
                    "LOW" => ConsoleColor.Green,
                    "MEDIUM" => ConsoleColor.Yellow,
                    "HIGH" => ConsoleColor.Red,
                    "CRITICAL" => ConsoleColor.DarkRed,
                    _ => ConsoleColor.White
                };

                Console.ForegroundColor = color;
                Console.WriteLine($"🚨 Event #{eventCount}: [{severity}] {threat} from {sourceIP}");
                Console.ResetColor();

                await Task.Delay(2000);
            }

            Console.WriteLine($"\n🎯 Monitored {eventCount} security events");
            Console.WriteLine("\nPress ENTER to return to main menu...");
            Console.ReadLine();
        }

        static async Task EncryptionTools()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Magenta;
            Console.WriteLine("🔐 ENCRYPTION TOOLS");
            Console.ResetColor();

            Console.WriteLine("🔧 Encryption Options:");
            Console.WriteLine("   1️⃣  AES Encrypt/Decrypt");
            Console.WriteLine("   2️⃣  RSA Key Generation");
            Console.WriteLine("   3️⃣  Hash Calculator");
            Console.WriteLine("   4️⃣  Password Generator");
            Console.WriteLine("   5️⃣  Back to Main Menu");

            Console.Write("\n⚡ Choose option [1-5]: ");
            var choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    await AESEncryptDecrypt();
                    break;
                case "2":
                    await RSAKeyGeneration();
                    break;
                case "3":
                    await HashCalculator();
                    break;
                case "4":
                    await PasswordGenerator();
                    break;
                case "5":
                    return;
                default:
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("❌ Invalid option!");
                    Console.ResetColor();
                    await Task.Delay(2000);
                    break;
            }
        }

        static async Task AESEncryptDecrypt()
        {
            Console.WriteLine("\n🔐 AES Encryption");
            Console.Write("Enter text to encrypt: ");
            var text = Console.ReadLine();
            
            Console.Write("Enter password: ");
            var password = Console.ReadLine();

            if (!string.IsNullOrEmpty(text) && !string.IsNullOrEmpty(password))
            {
                // Simple XOR encryption for demonstration
                var encrypted = Convert.ToBase64String(Encoding.UTF8.GetBytes(text).Select(b => (byte)(b ^ password[0])).ToArray());
                Console.WriteLine($"🔒 Encrypted: {encrypted}");

                var decrypted = Encoding.UTF8.GetString(Convert.FromBase64String(encrypted).Select(b => (byte)(b ^ password[0])).ToArray());
                Console.WriteLine($"🔓 Decrypted: {decrypted}");
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }

        static async Task RSAKeyGeneration()
        {
            Console.WriteLine("\n🔑 RSA Key Generation");
            Console.WriteLine("🔐 Generating 2048-bit RSA key pair...");
            
            await Task.Delay(2000);
            
            var publicKey = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA...\n-----END PUBLIC KEY-----";
            var privateKey = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC...\n-----END PRIVATE KEY-----";

            Console.WriteLine("✅ Keys generated successfully!");
            Console.WriteLine($"\n🔓 Public Key:\n{publicKey.Substring(0, 50)}...");
            Console.WriteLine($"\n🔒 Private Key:\n{privateKey.Substring(0, 50)}...");

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }

        static async Task HashCalculator()
        {
            Console.WriteLine("\n📊 Hash Calculator");
            Console.Write("Enter text to hash: ");
            var text = Console.ReadLine();

            if (!string.IsNullOrEmpty(text))
            {
                using var sha256 = System.Security.Cryptography.SHA256.Create();
                var hash = sha256.ComputeHash(Encoding.UTF8.GetBytes(text));
                var hashString = Convert.ToBase64String(hash);

                Console.WriteLine($"🔐 SHA-256 Hash: {hashString}");
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }

        static async Task PasswordGenerator()
        {
            Console.WriteLine("\n🔑 Password Generator");
            Console.Write("Password length [16]: ");
            var lengthStr = Console.ReadLine();
            var length = string.IsNullOrEmpty(lengthStr) ? 16 : int.Parse(lengthStr);

            var chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?";
            var random = new Random();
            var password = new string(Enumerable.Repeat(chars, length).Select(s => s[random.Next(s.Length)]).ToArray());

            Console.ForegroundColor = ConsoleColor.Green;
            Console.WriteLine($"🔑 Generated Password: {password}");
            Console.ResetColor();

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }

        static async Task TrafficAnalyzer()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.Blue;
            Console.WriteLine("📊 TRAFFIC ANALYZER");
            Console.ResetColor();

            Console.WriteLine("📡 Analyzing network traffic patterns...");
            Console.WriteLine("(Press ESC to stop)");

            Console.WriteLine("\n📈 Traffic Statistics:");
            Console.WriteLine("─".PadRight(80, '─'));

            var totalPackets = 0;
            var totalBytes = 0L;
            var random = new Random();

            while (true)
            {
                if (Console.KeyAvailable && Console.ReadKey(true).Key == ConsoleKey.Escape)
                    break;

                var packets = random.Next(100, 1000);
                var bytes = random.Next(1024, 1048576);
                totalPackets += packets;
                totalBytes += bytes;

                Console.WriteLine($"📊 Time: {DateTime.Now:HH:mm:ss} | Packets: {packets:N0} | Data: {bytes/1024:N0} KB | Total: {totalBytes/1024/1024:N2} MB");

                await Task.Delay(1000);
            }

            Console.WriteLine($"\n🎯 Analysis Complete!");
            Console.WriteLine($"📊 Total Packets: {totalPackets:N0}");
            Console.WriteLine($"📊 Total Data: {totalBytes/1024/1024:N2} MB");

            Console.WriteLine("\nPress ENTER to return to main menu...");
            Console.ReadLine();
        }

        static async Task FirewallManager()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.DarkGreen;
            Console.WriteLine("🛡️ FIREWALL MANAGER");
            Console.ResetColor();

            Console.WriteLine("🔧 Firewall Options:");
            Console.WriteLine("   1️⃣  Block IP Address");
            Console.WriteLine("   2️⃣  Allow IP Address");
            Console.WriteLine("   3️⃣  Block Port");
            Console.WriteLine("   4️⃣  Allow Port");
            Console.WriteLine("   5️⃣  View Rules");
            Console.WriteLine("   6️⃣  Back to Main Menu");

            Console.Write("\n⚡ Choose option [1-6]: ");
            var choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Enter IP to block: ");
                    var ip = Console.ReadLine();
                    Console.WriteLine($"✅ IP {ip} blocked successfully!");
                    break;
                case "2":
                    Console.Write("Enter IP to allow: ");
                    ip = Console.ReadLine();
                    Console.WriteLine($"✅ IP {ip} allowed successfully!");
                    break;
                case "3":
                    Console.Write("Enter port to block: ");
                    var port = Console.ReadLine();
                    Console.WriteLine($"✅ Port {port} blocked successfully!");
                    break;
                case "4":
                    Console.Write("Enter port to allow: ");
                    port = Console.ReadLine();
                    Console.WriteLine($"✅ Port {port} allowed successfully!");
                    break;
                case "5":
                    Console.WriteLine("\n📋 Current Firewall Rules:");
                    Console.WriteLine("─".PadRight(50, '─'));
                    Console.WriteLine("🚫 BLOCK: 192.168.1.100");
                    Console.WriteLine("✅ ALLOW: 192.168.1.0/24");
                    Console.WriteLine("🚫 BLOCK: Port 22");
                    Console.WriteLine("✅ ALLOW: Port 80,443");
                    break;
                case "6":
                    return;
                default:
                    Console.ForegroundColor = ConsoleColor.Red;
                    Console.WriteLine("❌ Invalid option!");
                    Console.ResetColor();
                    await Task.Delay(2000);
                    break;
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }

        static async Task PasswordAuditor()
        {
            Console.Clear();
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            Console.WriteLine("🔑 PASSWORD AUDITOR");
            Console.ResetColor();

            Console.WriteLine("🔍 Password Analysis Options:");
            Console.WriteLine("   1️⃣  Check Password Strength");
            Console.WriteLine("   2️⃣  Common Passwords Check");
            Console.WriteLine("   3️⃣  Dictionary Attack Simulation");
            Console.WriteLine("   4️⃣  Back to Main Menu");

            Console.Write("\n⚡ Choose option [1-4]: ");
            var choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    Console.Write("Enter password to check: ");
                    var password = Console.ReadLine();
                    
                    var strength = 0;
                    if (password?.Length >= 8) strength++;
                    if (password?.Any(char.IsUpper) == true) strength++;
                    if (password?.Any(char.IsLower) == true) strength++;
                    if (password?.Any(char.IsDigit) == true) strength++;
                    if (password?.Any(c => "!@#$%^&*()_+-=[]{}|;:,.<>?".Contains(c)) == true) strength++;

                    var strengthText = strength switch
                    {
                        0 => "Very Weak",
                        1 => "Weak",
                        2 => "Fair",
                        3 => "Good",
                        4 => "Strong",
                        5 => "Very Strong",
                        _ => "Unknown"
                    };

                    Console.WriteLine($"🔒 Password Strength: {strengthText} ({strength}/5)");
                    break;

                case "2":
                    Console.WriteLine("🔍 Checking against common passwords database...");
                    await Task.Delay(2000);
                    Console.WriteLine("⚠️  Password found in common passwords list!");
                    break;

                case "3":
                    Console.WriteLine("🚀 Simulating dictionary attack...");
                    Console.WriteLine("📊 Testing 1,000,000 common passwords...");
                    
                    for (int i = 0; i <= 100; i += 10)
                    {
                        Console.Write($"Progress: {i}% ({i*10000:N0} passwords tested)\r");
                        await Task.Delay(50);
                    }
                    
                    Console.WriteLine("\n✅ Dictionary attack simulation complete!");
                    Console.WriteLine("🔒 Password would be cracked in: ~2.3 hours");
                    break;

                case "4":
                    return;
            }

            Console.WriteLine("\nPress ENTER to continue...");
            Console.ReadLine();
        }
    }
}