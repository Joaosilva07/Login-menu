
class Login:
    def __init__(self, username="", password=""):
        self.username = username
        self.password = password

    def preenche_dados(self):
        self.username = input("Digite o username: ")
        self.password = input("Digite a senha: ")

    def salvar_dados_login(self):
        with open("logins.txt", "a", encoding="utf-8") as f:
            f.write(f"Username: {self.username}\n")
            f.write(f"Password: {self.password}\n")
        print("Dados escritos no arquivo logins.txt com sucesso.")


print("Bem vindo ao sistema de login")
login = Login()
login.preenche_dados()
login.salvar_dados_login()
