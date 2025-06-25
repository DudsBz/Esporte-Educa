'''Esporte Educa é um projeto de extensão do IFSP que visa promover a inclusão social
 e o desenvolvimento humano por meio do esporte e da educação.
 O sistema será uma plataforma de cadastro de times e atletas, incluindo tabelas e chaveamento das competições
 Podendo ser elas: futebol, vôlei, basquete, handebol, entre outros.
 O sistema será desenvolvido em Python, utilizando o framework Flet para a interface gráfica.'''

import flet as ft
from database import esportes

def main(page: ft.Page):
    list_campeonatos_ativos = []
    escolha_esporte = ft.Dropdown(
            options=[
                ft.dropdown.Option(esporte['nome'], 
                #key=esporte['id']
                )
                for esporte in esportes
            ],
            width=250,
            label="Selecione um esporte",
            hint_text="Selecione um esporte",
        )
    def iniciar_campeonato(e):
        dlg = ft.AlertDialog(
            content=ft.Container(
                width=400,
                height=250,
                content=ft.Column(
                    [
                        ft.Text("Selecione o esporte:", size=12),
                        escolha_esporte,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ),
            title=ft.Text("Cadastrar Time", size=20),
            actions=[
                ft.TextButton("Iniciar", on_click=cadastrar_time),
                ft.TextButton("Fechar", on_click=lambda e: page.close(dlg)),
            ],
        )
        

        page.open(dlg)
    def exibir_campeonatos(e):
        print(list_campeonatos_ativos)
        if list_campeonatos_ativos:
            lista = ft.Column([
                ft.TextButton(
                    f"{c['esporte']}",
                    on_click=adicionar_times,
            )   for c in list_campeonatos_ativos
                
        ])
        else:
            lista = ft.Text("Nenhum campeonato ativo.")

        exibir = ft.AlertDialog(
            title=ft.Text("Campeonatos Ativos"),
            content=lista
        )
        page.open(exibir)
    def cadastrar_time(e):
        # Função para iniciar o cadastro de time
        # Campos do formulário
        nome_time = ft.TextField(label="Nome do Time", width=300)
        nome_capitao = ft.TextField(label="Nome do Capitão", width=300)
        nomes_jogadores = ft.TextField(
            label="Nomes dos Jogadores (um por linha)", 
            multiline=True, 
            min_lines=4, 
            max_lines=10, 
            width=300
        )
        

        def salvar_time(ev):
            time = {
                "esporte": escolha_esporte.value,
                "nome_time": nome_time.value,
                "capitao": nome_capitao.value,
                "jogadores": [j.strip() for j in nomes_jogadores.value.split('\n') if j.strip()]
            }
            list_campeonatos_ativos.append(time)
            print("Time cadastrado:", time)
            page.close(dlg)
            
            # Aqui você pode adicionar o time a uma lista ou banco de dados


        dlg = ft.AlertDialog(
            content=ft.Container(
                width=400,
                height=350,
                content=ft.Column(
                    [
                        ft.Text("Preencha os dados do time:", size=12),
                        nome_time,
                        nome_capitao,
                        nomes_jogadores,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ),
            title=ft.Text("Cadastro de Time", size=20),
            actions=[
                ft.TextButton("Salvar", on_click=salvar_time),
                ft.TextButton("Cancelar", on_click=lambda e: page.close(dlg)),
            ],
        )

        page.open(dlg)
    
    def adicionar_times(e):
        pass
    def mostrardescricao(e):
        # Função para mostrar a descrição do esporte
        # Aqui você pode implementar a lógica para exibir mais informações sobre o esporte
        # Por exemplo, abrir um diálogo com detalhes
        # next é uma função que retorna o primeiro item de um iterável que satisfaz a condição
        # Se não houver nenhum item que satisfaça a condição, retorna None
        # e.control.parent.key é a chave do componente que disparou o evento

        esporte = next((esporte for esporte in esportes if esporte['id'] == e.control.parent.key), None)
        dlg = ft.AlertDialog(
            title=ft.Text(esporte['detalhes'], size=12),
            actions=[
                ft.TextButton("Fechar", on_click=lambda e: page.close(dlg)),
            ],
        )
        page.open(dlg)
        

    page.title = "Esporte Educa"
    page.window.width = 550
    page.window.height = 650

    # Criar os objetos da página
    #Criando o appbar
    page.appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SPORTS),
        leading_width=50,
        title=ft.Text("Esporte Educa"),
        center_title=True,
        bgcolor=ft.colors.BLUE_900,
        actions=[
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                tooltip="Configurações",
                #on_click=lambda e: print("Configurações clicadas")
            ),
        ],
    )

    #Criando o rodapé
    # Essa barra de navegação vai servir pra navegar pelas funcionalidades do app
    # Vai navegar pela página inicial, campeonatos que estão acontecendo e pelas tabelas
    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Início"),
            ft.NavigationDestination(icon=ft.icons.SPORTS, label="Campeonatos Ativos"),
            ft.NavigationDestination(icon=ft.icons.TABLE_CHART, label="Tabelas"),
        ],
        selected_index=0,
    )
    #Criando o corpo da página do início
    lista_esporte = ft.Column(
        scroll=ft.ScrollMode.ALWAYS,
        expand=True, 
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER
    )
    # Para cada esporte em esportes(database), faça...
    for esporte in esportes:
        # Cria um componente ListTile para cada esporte
        # e adiciona à lista de esportes
        # A imagem do esporte deve ser definida corretamente no dicionário esportes
        esporte_componente = ft.ListTile(
            #ListTile é um componente que exibe uma linha com informações
            #leading é a imagem do esporte
            leading=ft.Image(
                src=esporte["foto"],
                #fit é o modo como a imagem será exibida
                fit=ft.ImageFit.COVER,
                # repeat é como a imagem será repetida
                repeat=ft.ImageRepeat.NO_REPEAT,
                width=130,
                height=250,
                border_radius=ft.border_radius.all(5),
            ),

            title=ft.Text(f"{esporte['nome']} - {esporte['participantes_max_por_time']} participante(s) por time", size=13),
            subtitle=ft.Text(f"Modalidade: {esporte['modalidade']}", size=10),
            trailing=ft.PopupMenuButton(
                key=esporte['id'],
                icon=ft.icons.MORE_VERT,
                items=[
                    ft.PopupMenuItem(
                        text="Ver Detalhes",
                        icon=ft.icons.INFO,
                        on_click=mostrardescricao,
                    ),
                    ft.PopupMenuItem(
                        text="Iniciar Campeonato",
                        icon=ft.icons.SPORTS_FOOTBALL,
                        on_click=iniciar_campeonato,
                    ),
                    ft.PopupMenuItem(
                        text="Campeonatos Ativos",
                        icon=ft.icons.SPORTS_GYMNASTICS,
                        on_click=exibir_campeonatos
                    ),
                ],
            ),
        )
        # Adiciona o componente ListTile à lista de esportes
        # A lista de esportes é uma coluna que contém todos os esportes
        # assim, cada esporte será exibido como um item na lista
        # A lista de esportes é uma coluna que contém todos os esportes
        # e será exibida na página principal
        lista_esporte.controls.append(esporte_componente)
    page.add(lista_esporte)
ft.app(target=main)