import os, zipfile

class GhostOS:
    def __init__(self):
        self.user = "ghost23261"
        self.distros = ["alpine", "archlinux", "artix", "fedora", "opensuse", "ubuntu", "void"]
        
    def get_prompt(self):
        return f"\n\033[1;35m{self.user}@razr_flip\033[0m:~$ "

    def mochate(self):
        with zipfile.ZipFile('ghost_os_share.zip', 'w') as zipf:
            zipf.write('main.py')
        return "\n[+] ¡Ya me moché! Project zipped as 'ghost_os_share.zip'. Rólate un poco a los compas!"

    def show_menu(self):
        os.system('clear')
        print("\033[1;36m" + "="*50 + "\033[0m")
        print(" 👻 \033[1;37mGHOST OS | F-DROID EDITION | AL CIEN\033[0m 👻 ")
        print("\033[1;36m" + "="*50 + "\033[0m")
        print(" [kali]       : Enter NetHunter Lab (Root)")
        print(" [debian]     : Enter OS Dev Lab (LFS/Kernel)")
        print(" [distros]    : List 7 backup Linux environments")
        print(" [apk]        : Open APK Factory")
        print(" [mochate]    : Zip & Share Code with Compas")
        print(" [clear/exit] : Manage Session")
        print("\033[1;36m" + "="*50 + "\033[0m")

    def execute(self, cmd):
        cmd = cmd.strip().lower()
        if not cmd: return
        
        if cmd == "kali":
            print("\n[+] Booting Kali NetHunter Red Team Lab...")
            os.system("nethunter -r")
        elif cmd == "debian":
            print("\n[+] Booting Debian OS Dev Environment...")
            os.system("proot-distro login debian")
        elif cmd == "distros":
            print(f"\nAvailable: {', '.join(self.distros)}")
        elif cmd in self.distros:
            os.system(f"proot-distro login {cmd}")
        elif cmd == "apk":
            os.system("mkdir -p ~/GhostOS_App/apk_factory && cd ~/GhostOS_App/apk_factory && ls -la")
            print("\n[+] APK Factory ready. Use 'apktool d <app.apk>'")
        elif cmd == "mochate":
            print(self.mochate())
        elif cmd == "clear":
            self.show_menu()
        elif cmd == "exit":
            exit()
        else:
            os.system(cmd)

if __name__ == "__main__":
    app = GhostOS()
    app.show_menu()
    while True:
        try:
            line = input(app.get_prompt())
            app.execute(line)
        except (EOFError, KeyboardInterrupt):
            print("\n[!] Shutting down Ghost OS...")
            break
