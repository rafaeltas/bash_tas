import subprocess
from platform import system
import platform
import distro

class TasMybash:
    def __init__(self):
        # Data
        self.os_pkg_data = {"Linux":{"Fedora": "dnf", "Ubuntu": "apt",
                            "Arch": "pacman"}, "Windows": "winget"}
        self.app_list = [
            "app.drey.Dialect",
            "app.moosync.moosync",
            "com.discordapp.Discord",
            "com.github.tchx84.Flatseal",
            "com.heroicgameslauncher.hgl",
            "com.mattjakeman.ExtensionManager",
            "com.obsproject.Studio",
            "com.obsproject.Studio.Plugin.InputOverlay",
            "com.stremio.Stremio",
            "com.unity.UnityHub",
            "com.usebottles.bottles",
            "com.valvesoftware.Steam",
            "fr.handbrake.ghb",
            "fr.natron.Natron",
            "io.freetubeapp.FreeTube",
            "io.github.flattool.Warehouse",
            "io.github.giantpinkrobots.flatsweep",
            "io.github.jeffshee.Hidamari",
            "io.github.peazip.PeaZip",
            "io.github.peazip.PeaZip.Addon.i386",
            "io.github.shiftey.Desktop",
            "io.github.zen_browser.zen",
            "io.gitlab.adhami3310.Converter",
            "it.mijorus.gearlever",
            "it.mijorus.smile",
            "net.ankiweb.Anki",
            "net.pcsx2.PCSX2",
            "nl.hjdskes.gcolor3",
            "org.blender.Blender",
            "org.blender.Blender.Codecs",
            "org.duckstation.DuckStation",
            "org.gimp.GIMP",
            "org.gnome.Extensions",
            "org.gnome.FontManager",
            "org.gnome.Solanum",
            "org.gnome.World.PikaBackup",
            "org.gnome.gitlab.YaLTeR.VideoTrimmer",
            "org.godotengine.Godot",
            "org.kde.krita",
            "org.localsend.localsend_app",
            "org.nickvision.tubeconverter",
            "org.qbittorrent.qBittorrent",
            "org.ryujinx.Ryujinx",
            "org.telegram.desktop",
            "org.telegram.desktop.webview",
            "org.videolan.VLC"
        ]
        self.install_packages = [
            "sudo dnf copr enable peterwu/rendezvous",
            "sudo dnf install bibata-cursor-themes",
        ]
        self.gnome_config = [
            "gsettings set org.gnome.desktop.peripherals.mouse accel-profile 'flat'",
            "gsettings set org.gnome.desktop.interface cursor-theme 'Bibata-Modern-Amber'",
        ]
        self.identificar_sistema_operacional()
        
        
    def identificar_sistema_operacional(self):
        sistema = system()
        if sistema == "Windows":
            print("Você está usando o Windows.")
        elif sistema == "Linux":
            print("Você está usando o Linux.")
            current_distro = distro.name()
            self.single_distro = current_distro.split()
            if self.single_distro[0] == "Fedora":
                print("aqui tem um fedorinha, eeeeeem")
                self.upgrade_os(self.os_pkg_data[f"{sistema}"][f"{self.single_distro[0]}"])
                self.flatpak_instalation()
                # self.instalation_custom_gnome()
            else:
                print("tem nada não")
        elif sistema == "Darwin":
            print("Você está usando o macOS.")
        else:
            print("Não foi possível identificar o sistema operacional.")

    # FLATPAKS VERIFICATION
    def flatpak_instalation(self):
        for app in self.app_list:
            if self.is_flatpak_installed(app):
                print(f"{app} já está instalado.")
            else:
                print(f"{app} não está instalado. Instalando...")
                self.install_flatpak_app(app)

    # Função para verificar se um app está instalado
    def is_flatpak_installed(self, app_id):
        result = subprocess.run(
            ["flatpak", "list", "--app"],
            stdout=subprocess.PIPE,
            text=True
        )
        return app_id in result.stdout

    # Função para instalar um app usando Flatpak
    def install_flatpak_app(self, app_id):
        subprocess.run(["flatpak", "install", "-y", app_id])

    def upgrade_os(self, os_pkg):
        subprocess.run(
            ["sudo", f'{os_pkg}', "update", "-y"], capture_output=True, text=True)
    
    def instalation_custom_gnome(self, os_pkg):
        for comando_str in self.install_packages:
            # Divide a string em partes para formar uma lista
            comando = comando_str.split()
            print(f"Executando: {' '.join(comando)}")  # Mostra o comando que está sendo executado
            subprocess.run(comando)
    
    def gnome_configuration(self):
        for comando_str in self.gnome_config:
            # Divide a string em partes para formar uma lista
            comando = comando_str.split()
            print(f"Executando: {' '.join(comando)}")  # Mostra o comando que está sendo executado
            subprocess.run(comando)


TasMybash()
