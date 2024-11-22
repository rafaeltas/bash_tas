import subprocess
from platform import system
import distro
import os


class TasMybash:
    def __init__(self):
        # Data
        self.os_pkg_data = {
            "Linux": {"Fedora": "dnf", "Ubuntu": "apt", "Arch": "pacman"},
            "Windows": "winget",
        }
        self.app_list = [
            "app.drey.Dialect",
            "app.moosync.moosync",
            "com.discordapp.Discord",
            "com.github.tchx84.Flatseal",
            "com.heroicgameslauncher.hgl",
            "com.mattjakeman.ExtensionManager",
            "com.obsproject.Studio",
            "com.stremio.Stremio",
            "com.usebottles.bottles",
            "com.valvesoftware.Steam",
            "fr.handbrake.ghb",
            "io.freetubeapp.FreeTube",
            "io.github.flattool.Warehouse",
            "io.github.giantpinkrobots.flatsweep",
            "io.github.jeffshee.Hidamari",
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
            "org.gnome.World.PikaBackup",
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
            "sudo dnf copr enable peterwu/rendezvous -y",
            "sudo dnf install bibata-cursor-themes -y",
            "sudo dnf install ulauncher -y",
            "sudo dnf install solaar -y",
            "sudo dnf install neovim -y",
            "sudo dnf install akmod-nvidia -y",
            "sudo npm install -g pyright -y",
            "sudo dnf install python3-pip -y",
            "sudo pip install pylint black rich -y",
            "sudo dnf install gnome-shell-extension-dash-to-dock -y",
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

        self.identificar_sistema_operacional()
        self.set_shortcuts()

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
                self.instalation_custom_gnome(
                    self.os_pkg_data[f"{sistema}"][f"{self.single_distro[0]}"]
                )
                self.gnome_configuration()
                self.neovim_configuration()
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

    def upgrade_os(self, os_pkg):
        subprocess.run(["sudo", f"{os_pkg}", "update", "-y"], text=True, check=True)

    def instalation_custom_gnome(self, os_pkg):
        for comando_str in self.install_packages:
            # Divide a string em partes para formar uma lista
            comando = comando_str.split()
            print(
                f"Executando: {' '.join(comando)}"
            )  # Mostra o comando que está sendo executado
            subprocess.run(comando)

    def gnome_configuration(self):
        for comando_str in self.gnome_config:
            # Divide a string em partes para formar uma lista
            comando = comando_str.split()
            print(
                f"Executando: {' '.join(comando)}"
            )  # Mostra o comando que está sendo executado
            subprocess.run(comando)

    def neovim_configuration(self):
        self.expansao = os.path.expanduser("~")
        # self.nvim_config = ["~/.config/nvim/lua/plugins"]

        self.git_comandos = [
            f"git clone https://github.com/LazyVim/starter {self.expansao}/.config/nvim",
            f"rm -rf {self.expansao}/.config/nvim/.git",
            f"rm -rf {self.expansao}/.config/nvim/.gitignore",
            f"rm -rf {self.expansao}/.config/nvim/README.md",
            f"rm -rf {self.expansao}/.config/nvim/LICENSE",
        ]
        for comando_str in self.git_comandos:
            comando = comando_str.split()
            subprocess.run(comando)

        # for commline in self.nvim_config:
        # comand = commline
        # dir_nvim = os.path.expanduser(f"{comand}")
        # os.makedirs(f"{dir_nvim}", exist_ok=True)

        # with open(os.path.expanduser('~/.config/nvim/init.lua'), 'a') as file:
        # file.write('require("keymaps")\n')
        # file.write('require("options")\n')
        # file.write('require("plugins.lazy")\n')

    def set_shortcuts(self):
        # pass

        # Define o caminho base para os atalhos personalizados
        keybinding_path = (
            "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/"
        )
        custom_binding = "custom0/"
        full_path = keybinding_path + custom_binding

        # Define os comandos para configurar o atalho
        shortcut_name = "Launch Ulauncher"
        shortcut_command = "ulauncher-toggle"
        shortcut_binding = "<Control>space"

        # Configura a lista de atalhos
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.settings-daemon.plugins.media-keys",
                "custom-keybindings",
                f"['{full_path}']",
            ]
        )

        # Configura o nome do atalho
        subprocess.run(
            [
                "gsettings",
                "set",
                f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{full_path}",
                "name",
                f"'{shortcut_name}'",
            ]
        )

        # Configura o comando do atalho
        subprocess.run(
            [
                "gsettings",
                "set",
                f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{full_path}",
                "command",
                f"'{shortcut_command}'",
            ]
        )

        # Configura a combinação de teclas do atalho
        subprocess.run(
            [
                "gsettings",
                "set",
                f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{full_path}",
                "binding",
                f"'{shortcut_binding}'",
            ]
        )

        print("Atalho configurado com sucesso!")

        gnome_set_keys = "gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
        add_new_custom = " [/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/]"
        command_make = gnome_set_keys + add_new_custom
        make_list_commands = command_make.split()

        command_to_add = "'Launch Ulauncher',"
        edit_new_command = f":/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name {command_to_add}"
        make_list_ulaunch = edit_new_command.split()

        subprocess.run(
            make_list_commands,
        )


TasMybash()
