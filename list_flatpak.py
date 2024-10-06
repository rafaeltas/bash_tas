import subprocess

# Executa o comando flatpak list --app e captura a saída
result = subprocess.run(["flatpak", "list", "--columns=application"], capture_output=True, text=True)

# Verifica se o comando foi bem-sucedido
if result.returncode == 0:
    # Captura a saída padrão do comando
    output = result.stdout
    
    # Divide a saída em linhas
    app_ids = output.splitlines()
    
    # Gera o arquivo .txt com os Application IDs dos aplicativos
    with open("flatpak_app_ids.txt", "w") as file:
        for app_id in app_ids:
            file.write(app_id + "\n")
    
    print("Arquivo 'flatpak_app_ids.txt' gerado com sucesso!")
else:
    print("Erro ao executar o comando flatpak list:", result.stderr)
