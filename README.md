# Esporte Educa

Este projeto é uma aplicação desenvolvida em Python utilizando o framework [Flet], que permite criar interfaces gráficas modernas e responsivas. O objetivo do sistema é gerenciar campeonatos esportivos, permitindo o cadastro de esportes, times, jogadores e a visualização dos campeonatos ativos.

## Funcionalidades

- **Cadastro de Campeonatos:** O usuário pode iniciar um novo campeonato selecionando um esporte disponível.
- **Cadastro de Times:** Para cada campeonato, é possível cadastrar times, informando nome do time, nome do capitão e nomes dos jogadores.
- **Visualização de Campeonatos Ativos:** Todos os campeonatos iniciados ficam disponíveis para consulta em uma lista.
- **Interface Intuitiva:** Utiliza componentes visuais como Dropdowns, AlertDialogs, Columns e Buttons para facilitar a navegação.

## Estrutura do Projeto

- `main.py`: Arquivo principal da aplicação, onde estão implementadas as funções de cadastro, exibição e navegação.
- `database.py`: Contém a lista de esportes disponíveis para cadastro de campeonatos.
- `README.md`: Este arquivo de documentação.

## Como Executar

1. Instale as dependências necessárias:
   
   Python e Flet (com o python intalado, no terminal insira => pip install flet )
   

2. Execute 

*Como Usar*
 - Iniciar Campeonato: Clique no botão para iniciar um campeonato, selecione o esporte desejado e confirme.
 - Cadastrar Time: Após iniciar um campeonato, cadastre times informando os dados solicitados.
 - Visualizar Campeonatos Ativos: Acesse o botão de campeonatos ativos para ver todos os campeonatos cadastrados.

*Observações*
O projeto utiliza listas em memória para armazenar os dados. Ao fechar o programa, os dados são perdidos.
O Flet é um framework relativamente novo, então algumas limitações podem ser encontradas na documentação ou suporte.
Contribuição
Sinta-se à vontade para sugerir melhorias ou reportar problemas!

### ATENÇÃO!!
    O projeto não está completo, ainda falta ajustar os cadastros de times novos e adicionar a funcionalidade de chaveamento de campeonato. Além disso, esportes em dupla ou individuais terão de ser ajustados para a modalidade que lhe confere.