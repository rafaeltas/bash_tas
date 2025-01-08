import subprocess
from platform import system
import distro
import os
import shutil
import requests

# separe in fuctions to better
# Make a function to compile softwares
# Make function to config Ghostty terminal


class TasMybash:
    def __init__(self):
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
                self.install_font()
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
        new_repos_flatpak = [
            "flatpak remote-add --if-not-exists flathub-beta https://flathub.org/beta-repo/flathub-beta.flatpakrepo",
        ]
        for comando_str_repo in new_repos_flatpak:
            # Divide a string em partes para formar uma lista
            comando_repo = comando_str_repo.split()
            print(
                f"Executando: {' '.join(comando_repo)}"
            )  # Mostra o comando que está sendo executado
            subprocess.run(comando_repo)

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

    def terminal_config(self):
        pass

    def install_font(self):

        # URL da fonte no repositório oficial do Nerd Fonts
        url_fonte = "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/FiraCode.zip"
        diretorio_fonte = os.path.expanduser(
            "~/.fonts"
        )  # Diretório de fontes do usuário
        caminho_zip = os.path.expanduser(
            "~/FiraCode.zip"
        )  # Caminho temporário para o ZIP

        try:
            # Baixando a fonte
            print("Baixando FiraCode Nerd Font...")
            response = requests.get(url_fonte, stream=True)
            response.raise_for_status()  # Verifica se o download foi bem-sucedido

            with open(caminho_zip, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Download concluído!")

            # Criando o diretório de fontes, se necessário
            if not os.path.exists(diretorio_fonte):
                os.makedirs(diretorio_fonte)
                print(f"Diretório {diretorio_fonte} criado.")

            # Extraindo o ZIP usando o comando `unzip`
            print("Extraindo a fonte para o diretório .fonts...")
            subprocess.run(
                ["unzip", "-o", caminho_zip, "-d", diretorio_fonte], check=True
            )
            print("Fonte instalada com sucesso!")

            # Atualizando o cache de fontes
            print("Atualizando o cache de fontes...")
            subprocess.run(["fc-cache", "-fv"], check=True)
            print("Cache atualizado!")

        finally:
            # Removendo o arquivo ZIP temporário
            if os.path.exists(caminho_zip):
                os.remove(caminho_zip)
                print("Arquivo ZIP temporário removido.")

    def neovim_configuration(self):
        """
        Function receive the "who" is the OS to apply the correctly installation.
        """
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

        # Add news plugins
        # Caminho do diretório de origem (onde a pasta "plugins" está)
        diretorio_origem = f"{self.expansao}/bash_tas/plugins"

        # Caminho do diretório de destino (para onde você quer copiar os arquivos)
        diretorio_destino = f"{self.expansao}/.config/nvim/lua/plugins"

        # Lista de arquivos para copiar
        arquivos = ["catppuccin.lua", "render-markdown.lua", "alpha.lua"]

        # Copiar os arquivos
        for arquivo in arquivos:
            caminho_origem = os.path.join(diretorio_origem, arquivo)
            caminho_destino = os.path.join(diretorio_destino, arquivo)

            try:
                shutil.copy(caminho_origem, caminho_destino)
                print(f"{arquivo} copiado com sucesso!")
            except FileNotFoundError:
                print(f"O arquivo {arquivo} não foi encontrado!")
            except Exception as e:
                print(f"Erro ao copiar {arquivo}: {e}")

    def set_shortcuts(self):
        # Define o caminho base para os atalhos personalizados
        keybinding_path = (
            "/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/"
        )

        # Configura a lista de atalhos
        shortcut_paths = [
            f"{keybinding_path}custom{index}/" for index in self.custom_shortcuts_dic
        ]
        subprocess.run(
            [
                "gsettings",
                "set",
                "org.gnome.settings-daemon.plugins.media-keys",
                "custom-keybindings",
                str(shortcut_paths).replace(
                    "'", '"'
                ),  # Formata como JSON para o gsettings
            ]
        )

        # Itera sobre o dicionário para configurar cada atalho
        for index, shortcut in self.custom_shortcuts_dic.items():
            custom_path = f"{keybinding_path}custom{index}/"

            # Configura o nome do atalho
            subprocess.run(
                [
                    "gsettings",
                    "set",
                    f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{custom_path}",
                    "name",
                    shortcut["shortcut_name"],
                ]
            )

            # Configura o comando do atalho
            subprocess.run(
                [
                    "gsettings",
                    "set",
                    f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{custom_path}",
                    "command",
                    shortcut["shortcut_command"],
                ]
            )

            # Configura a combinação de teclas do atalho
            subprocess.run(
                [
                    "gsettings",
                    "set",
                    f"org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:{custom_path}",
                    "binding",
                    shortcut["shortcut_binding"],
                ]
            )

        print("Atalhos configurados com sucesso!")


TasMybash()
