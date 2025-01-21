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
