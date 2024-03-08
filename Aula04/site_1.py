
import flet as ft

# função principal
def main(pagina):
    
    # add o texto titulo na pagina
    texto = ft.Text("Hashzap", size=20)

    # cria o chat, Column() significa que os 'filhos' desse componente dserão empilhados como um coluna
    chat = ft.Column()

    # função 'soquete' que é executada em todos os clientes conectados
    def mensagem_tunel(mensagem):
        chat.controls.append(mensagem) # add a mensagem do parametro no chat
        pagina.update() # atualiza a pagina



    pagina.pubsub.subscribe(mensagem_tunel)# criando o 'socket'

    

    # função para enviar a mensagem no chat
    def enviar_msg(evento):
        print("Enviando")
        texto_remetente = ft.Text(f"{nome_usuario.value} diz: ", italic=True)
        texto_enviado = ft.Text(campo_mensagem.value)
        linha_chat = ft.Row([texto_remetente, texto_enviado])
        pagina.pubsub.send_all(linha_chat)#envia a mensagem para o 'socket'
        campo_mensagem.value = ""
        pagina.update()

    def sair_chat(evento):
        botao_iniciar.visible = True
        texto_sair = ft.Text(f"{nome_usuario.value} saiu do chat", italic=True)
        linha_enviar.visible = False
        pagina.pubsub.send_all(texto_sair)
        
        #pagina.update()

    # cria os campos de interagir no chat
    campo_mensagem = ft.TextField(label="Digite sua mensagem", on_submit=enviar_msg)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_msg)
    botao_sair = ft.ElevatedButton("Sair do chat", on_click=sair_chat, color="red")
    linha_enviar = ft.Row([campo_mensagem, botao_enviar, botao_sair])

    
    
    # função para o cliente entrar no chat
    def entrar_chat(evento):
        print("Entrando no chat...")
        popup.open = False
        botao_iniciar.visible = False
        pagina.add(chat)
        texto_bemvindo = ft.Text(f"{nome_usuario.value} entrou no chat", italic=True)
        pagina.add(linha_enviar)
        linha_enviar.visible = True
        pagina.pubsub.send_all(texto_bemvindo)# envia mensagem de boas vindas no chat avisando quem entrou
        pagina.update()

    # função que cancela o popup de entrar no chat
    def cancelar_chat(evento):
        print("Fechando o chat")
        popup.open = False
        pagina.update()


    # campos da popup
    titulo_pop = ft.Text("Bem vindo ao chat")
    nome_usuario = ft.TextField(label="Digite seu nome")
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
    botao_cancelar = ft.ElevatedButton("Cancelar", on_click=cancelar_chat)

    # cria a popup
    popup = ft.AlertDialog(
        open=True,
        modal=True,
        title=titulo_pop,
        content=nome_usuario,
        actions=[botao_entrar, botao_cancelar]
    )

    # função para abrir a popup de entrar no chat
    def abrir_popup(evento):
        print("Abrindo tela de login no chat")
        pagina.dialog = popup
        popup.open = True
        pagina.update()
    
    # botão para abrir a popup
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=abrir_popup)

    # add o titlo da pagina e o botao de iniciar chat
    pagina.add(texto)
    pagina.add(botao_iniciar)

# inicia o app como wesite
ft.app(target=main, view=ft.WEB_BROWSER, port=8000)