# from platform import system

# class TesteAlgo:
#     def __init__(self):
#         sistema = system()
#         print(sistema)
#         if sistema == "Windows":
#             print("Você está usando o Windows.")
#         elif sistema == "Linux":
#             print("Você está usando o Linux.")
#         elif sistema == "Darwin":
#             print("Você está usando o macOS.")
#         else:
#             print("Não foi possível identificar o sistema operacional.")
                
# TesteAlgo()

import platform
import distro

# Sistema Operacional e versão
print(f"Sistema: {platform.system()}")              # Ex: Windows, Linux, Darwin (macOS)
print(f"Versão: {platform.version()}")              # Ex: Versão do sistema operacional
print(f"Release: {platform.release()}")             # Ex: Número da versão principal do SO

# Informações detalhadas do sistema
print(f"Nome da máquina: {platform.node()}")        # Nome da máquina
print(f"Arquitetura: {platform.architecture()}")    # Arquitetura do sistema (32-bit ou 64-bit)
print(f"Processador: {platform.processor()}")       # Nome do processador
print(f"Plataforma: {platform.platform()}")         # Plataforma detalhada

# Versão do Python
print(f"Python versão: {platform.python_version()}") # Versão do Python em uso
print(f"Compilador Python: {platform.python_compiler()}") # Compilador utilizado para construir o Python
print(f"Implementação do Python: {platform.python_implementation()}") # Implementação (CPython, PyPy, etc.)

# Distribuição (Linux)
if platform.system() == "Linux":
    print(f"Distribuição Linux: {distro.name()} {distro.version()}")
elif platform.system() == "Darwin":
    print(f"macOS Versão: {platform.mac_ver()}")

# Informações sobre o Windows (se aplicável)
if platform.system() == "Windows":
    print(f"Windows Versão: {platform.win32_ver()}") # Informações sobre o Windows

