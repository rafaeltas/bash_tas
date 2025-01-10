from concurrent.futures import process
import subprocess
from platform import system
import distro
import os
import shutil
import requests
import asyncio

# separe in fuctions to better
# Make a function to compile softwares
# Make function to config Ghostty terminal


class TasMybash:
    async def __init__(self):
        # Data
        self.os_pkg_data = {
            "Linux": {"Fedora": "dnf", "Ubuntu": "apt", "Arch": "pacman"},
            "Windows": "winget",
        }
        self.app_list = [
            "app.drey.Dialect",
            "com.github.tchx84.Flatseal",
            "com.mattjakeman.ExtensionManager",
            "com.obsproject.Studio",
            "com.stremio.Stremio",
            "com.usebottles.bottles",
            "com.valvesoftware.Steam",
            "fr.handbrake.ghb",
            "io.freetubeapp.FreeTube",
            "io.github.flattool.Warehouse",
            "io.github.giantpinkrobots.flatsweep",
            "io.github.peazip.PeaZip",
            "io.github.shiftey.Desktop",
            "io.github.zen_browser.zen",
            "io.gitlab.adhami3310.Converter",
            "it.mijorus.gearlever",
            "it.mijorus.smile",
            "net.ankiweb.Anki",
            "net.pcsx2.PCSX2",
            "nl.hjdskes.gcolor3",
            "org.blender.Blender",
            "org.duckstation.DuckStation",
            "org.gimp.GIMP",
            "org.gnome.FontManager",
            "org.gnome.Solanum",
            "org.gnome.gitlab.YaLTeR.VideoTrimmer",
            "org.godotengine.Godot",
            "org.kde.krita",
            "org.localsend.localsend_app",
            "org.nickvision.tubeconverter",
            "org.qbittorrent.qBittorrent",
            "org.ryujinx.Ryujinx",
            "org.videolan.VLC",
            "io.github.nokse22.Exhibit",
        ]
        self.install_packages = [
            "sudo dnf install gnome-tweaks -y",
            "sudo dnf upgrade -y",
            "sudo gnome-tweaks -y",
            "sudo kiall gnome-tweaks",
            "sudo dnf install @development-tools -y",
            "sudo dnf copr enable peterwu/rendezvous -y",
            "sudo dnf install bibata-cursor-themes -y",
            "sudo dnf install ulauncher -y",
            "sudo dnf install solaar -y",
            "sudo dnf install neovim -y",
            "sudo dnf install python3-pip -y",
            "sudo dnf install fzf -y",
            "sudo dnf install luarocks -y",
            "sudo dnf copr enable pgdev/ghostty -y",
            "sudo dnf install ghostty -y",
            "sudo dnf install zsh -y",
        ]

        self.gnome_config = [
            "gsettings set org.gnome.desktop.peripherals.mouse accel-profile 'flat'",
            "gsettings set org.gnome.desktop.interface cursor-theme 'Bibata-Modern-Classic'",
            "gsettings set org.gnome.desktop.interface cursor-size 20",
            "gsettings set org.gnome.desktop.interface accent-color 'purple'",
            "gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'",
            "gsettings set org.gnome.desktop.wm.preferences button-layout 'appmenu:minimize,close'",
            "gsettings set org.gnome.mutter center-new-windows true",
            "gsettings set org.gnome.shell.extensions.dash-to-dock dash-max-icon-size 32",
        ]

        self.custom_shortcuts_dic = {
            "0": {
                "shortcut_name": "Launch Ulauncher",
                "shortcut_command": "ulauncher-toggle",
                "shortcut_binding": "<Control>space",
            },
            "1": {
                "shortcut_name": "Open Terminal",
                "shortcut_command": "ghostty",
                "shortcut_binding": "<Control><Alt>T",
            },
            "2": {
                "shortcut_name": "Emojis Smille",
                "shortcut_command": "flatpak run it.mijorus.smile",
                "shortcut_binding": "<Super>.",
            },
            # Adicione mais atalhos conforme necessário
        }

        tasks = [idenitificar_sistema_operacional()]
        await asyncio.gather(*tasks)

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
                self.upgrade_os(
                    self.os_pkg_data[f"{sistema}"][f"{self.single_distro[0]}"]
                )
                self.flatpak_instalation()
                # self.instalation_custom_gnome(
                #     self.os_pkg_data[f"{sistema}"][f"{self.single_distro[0]}"]
                # )
                # self.gnome_configuration()
                # self.neovim_configuration()
                # self.install_font()
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
            ["flatpak", "list", "--app"], stdout=subprocess.PIPE, text=True
        )
        return app_id in result.stdout

    # Função para instalar um app usando Flatpak
    def install_flatpak_app(self, app_id):
        subprocess.run(
            [
                "flatpak",
                "install",
                "--from",
                f"https://flathub.org/repo/appstream/{app_id}.flatpakref",
                "-y",
            ]
        )

    async def upgrade_os(self, os_pkg):
        new_repos_flatpak = [
            "flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo",
        ]
        process = await asyncio.create_subprocess_exec("sudo", os_pkg, "update", "-y")
        for comando_str_repo in new_repos_flatpak:
            # Divide a string em partes para formar uma lista
            comando_repo = comando_str_repo.split()
            print(
                f"Executando: {' '.join(comando_repo)}"
            )  # Mostra o comando que está sendo executado
            subprocess.run(comando_repo)

    def terminal_config(self):
        pass


TasMybash()
