class RedeSocial:
    def __init__(self):
        self.usuarios = {}
        self.posts = []

    def cadastrar_usuario(self, nome, email, idade, data_nasc):
        self.usuarios[nome] = {
            "email": email,
            "idade": idade,
            "data_nasc": data_nasc,
            "amigos": []
        }
        print(f"{nome} ta entrado")

    def adicionar_amizade(self, usuario1, usuario2):
            self.usuarios[usuario1]["amigos"].append(usuario2)
            self.usuarios[usuario2]["amigos"].append(usuario1)
            print(f"{usuario1} e {usuario2} são mais que amigos, são friends!")

    def criar_post(self, usuario, conteudo):
            self.posts.append({"usuario": usuario, "conteudo": conteudo, "comentarios": []})
            print(f"{usuario} compartilhou: {conteudo}")


    def comentar_no_post(self, usuario, post_id, comentario):
        try:
            self.posts[post_id]["comentarios"].append({"usuario": usuario, "comentario": comentario})
            print(f"{usuario} comentou: {comentario}")
            if self.posts == "kanye West comentario":
                print('Calma lá amigão')
        except:
            print("Não encontrado") 

    def procurar_usuario(self, nome):
        if nome in self.usuarios:
            print(f"{nome} localizado")
        else:
            print(f"{nome} não encontrado.")



rede_social = RedeSocial()

rede_social.cadastrar_usuario("amos", "amos@email.com", 25, "01/01/1922")
rede_social.cadastrar_usuario("stradinho", "sssss@email.com", 22, "02/02/2002")

rede_social.adicionar_amizade("amos", "stradinho")


rede_social.criar_post("amos", "eu gosto assim")
rede_social.criar_post("stradinho", "amostradinho")


rede_social.comentar_no_post("amos", 0, "salve")
rede_social.comentar_no_post("stradinho", 1, "Bom dia Marinalva")


rede_social.procurar_usuario("Joao")
rede_social.procurar_usuario("Carlos")
