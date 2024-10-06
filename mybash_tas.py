import subprocess
from platform import system
import platform
import distro
# Verificar o OS atual do usuário
# Executando o comando sudo dnf upgrade

# Abre o arquivo txt com os Application IDs
# with open("flatpak_app_ids.txt", "r") as file:
#     # Lê todas as linhas do arquivo e remove espaços em branco ou quebras de linha
#     app_list = [line.strip() for line in file.readlines()]


# for my_app in app_list:
#     subprocess.run(["sudo", "flatpak", "install", "flathub", f'{
#                    my_app}'], capture_output=True, text=True)


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
        self.identificar_sistema_operacional()
        
    def identificar_sistema_operacional(self):
        sistema = system()
        if sistema == "Windows":
            print("Você está usando o Windows.")
        elif sistema == "Linux":
            print("Você está usando o Linux.")
            if "Fedora" in distro.name():
                print("aqui tem um fedorinha, eeeeeem")
                self.upgrade_os(self.os_pkg_data["Linux"]["Fedora"])
            else:
                print("tem nada não")
        elif sistema == "Darwin":
            print("Você está usando o macOS.")
        else:
            print("Não foi possível identificar o sistema operacional.")

    def upgrade_os(self, os_pkg):
        subprocess.run(
            ["sudo", f'{os_pkg}', "upgrade", "-y"], capture_output=True, text=True)


TasMybash()
