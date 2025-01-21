def flatpak_instalation(self):
    for app in self.app_list:
        if self.is_flatpak_installed(app):
            print(f"{app} já está instalado.")
        else:
            print(f"{app} não está instalado. Instalando...")
            self.install_flatpak_app(app)
