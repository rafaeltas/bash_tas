import asyncio


class TasMyBash:
    def __init__(self):
        self.main_process()

    def main_process(self):
        pass

    async def atualizar_pacote(self):
        # Cria o subprocesso de forma assíncrona
        process = await asyncio.create_subprocess_exec(
            "sudo",
            "dnf",
            "update",
            "-y",
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )

        # Loop para ler a saída do subprocesso enquanto ele está em execução
        for stdout_line in process.stdout:
            print(stdout_line.decode())  # Imprime a saída no terminal

        # Loop para ler os erros do subprocesso, se houver
        for stderr_line in process.stderr:
            print(
                stderr_line.decode(), end="", file=sys.stderr
            )  # Imprime erros no terminal

        # Aguarda o subprocesso terminar e verifica o código de retorno
        returncode = await process.wait()

        # Se o código de retorno for 0, o processo foi bem-sucedido
        if returncode == 0:
            print("\nProcesso concluído com sucesso.")
        else:
            print(f"\nErro no processo. Código de retorno: {returncode}")


# Exemplo de uso
TasMyBash()
