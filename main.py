'''Esporte Educa é um projeto de extensão do IFSP que visa promover a inclusão social
 e o desenvolvimento humano por meio do esporte e da educação.
 O sistema será uma plataforma de cadastro de times e atletas, incluindo tabelas e chaveamento das competições
 Podendo ser elas: futebol, vôlei, basquete, handebol, entre outros.
 O sistema será desenvolvido em Python, utilizando o framework Flet para a interface gráfica.'''

"""
Observaões =>
    Você pode criar uma interface de usuário (UI) para o seu programa com os controles Flet, baseados no Flutter do Google.
    O Flet vai além de simplesmente encapsular widgets do Flutter. Ele adiciona seu próprio toque combinando widgets menores, simplificando complexidades, 
    implementando as melhores práticas de UI e aplicando padrões sensatos. 
    Isso garante que seus aplicativos tenham uma aparência elegante e refinada, sem exigir esforços adicionais de design da sua parte.

    O Flet foi criado em 2017, ou seja, não possui muito suporte. Além de que o python não é voltado para essa área de atuação, sendo majoritariamente para análise de dados, backend e etc.
    Diversas ferramentas que eu tentei fazer com que funcionassem não deram certo pois não consegui nada nem com suporte de IA e nem com suporte que encontrei na internet, tais como a própria documentação do flet
    Um exemplo é o NavBar/rodapé, eu queria usá-lo para navegação que estão explicitas nele, mas por não conseguir desenvolver eu optei por deixar assim mesmo, deixar por estilo, achei bonito.

""" 

import flet as ft
from database import esportes
from time import sleep

def main(page: ft.Page):
    # Essa é a lista de campeonatos ativos que serão expostos na tela
    # É uma variável global que armazena o esporte
    list_campeonatos_ativos = []
    # Essa é uma lista igual a de cima, com a diferença de ser para cadastro de times
    list_times_cad = []
    # escolha_esporte é um ft.Dropdown que vai exibir pro usuário as opções de esportes (ou não esportes) para iniciar um campeonato
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
            title=ft.Text("Iniciar um campeonato", size=20),
            actions=[
                ft.TextButton("Iniciar", on_click=salvar_esporte),
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
                    tooltip="Adicionar Time"
                    
            )   for c in list_campeonatos_ativos
                
        ])
        else:
            lista = ft.Text("Nenhum campeonato ativo.")

        exibir = ft.AlertDialog(
            title=ft.Text("Campeonatos Ativos"),
            content=lista
        )
        page.open(exibir)
    def configuracoes(e):
        page.clean()
        page.add(appbar, navigation_bar)
    def salvar_esporte(e):
        esporte_ativo = {
            "esporte": escolha_esporte.value,
        }
        v_esp = esporte_ativo["esporte"]
        alerta = ft.AlertDialog(
            content= ft.Text(f"Campeonato de {v_esp} Iniciado!", size=13))
        list_campeonatos_ativos.append(esporte_ativo)
        page.open(alerta)
    def adicionar_times(e):
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

        def salvar_time(e):
            time = {
                "nome_time": nome_time.value,
                "capitao": nome_capitao.value,
                "jogadores": [j.strip() for j in nomes_jogadores.value.split('\n') if j.strip()]
            }
            list_times_cad.append(time["nome_time"])
            print(time)
            sleep(1)
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
                ft.TextButton("Sair", on_click=lambda e: page.close(dlg)),
            ],
        )
        page.open(dlg)
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
    appbar = ft.AppBar(
        leading=ft.Icon(ft.icons.SPORTS),
        leading_width=50,
        title=ft.Text("Esporte Educa"),
        center_title=True,
        bgcolor=ft.colors.BLUE_900,
        actions=[
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                tooltip="Configurações",
                on_click=configuracoes
            ),
        ],
    )

    #Criando o rodapé
    # Essa barra de navegação vai servir pra navegar pelas funcionalidades do app
    # Vai navegar pela página inicial, campeonatos que estão acontecendo e pelas tabelas
    navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationDestination(icon=ft.icons.CAR_CRASH, label="Início"),
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
    page.add(appbar, lista_esporte, navigation_bar)
ft.app(target=main)