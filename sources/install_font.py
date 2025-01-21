def install_font(self):

    # URL da fonte no repositório oficial do Nerd Fonts
    url_fonte = (
        "https://github.com/ryanoasis/nerd-fonts/releases/download/v3.0.2/FiraCode.zip"
    )
    diretorio_fonte = os.path.expanduser("~/.fonts")  # Diretório de fontes do usuário
    caminho_zip = os.path.expanduser("~/FiraCode.zip")  # Caminho temporário para o ZIP

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
        subprocess.run(["unzip", "-o", caminho_zip, "-d", diretorio_fonte], check=True)
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
