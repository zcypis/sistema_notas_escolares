from processadores import *
from dados import *
from helpers import *
from rich import print
from rich.panel import Panel


# --- Main | Menu interativo --------
def main():
    cadastro = carregar_dados()

    while True:
        print(
            Panel(
                "[yellow][1][/] - Registrar aluno.\n"
                "[yellow][2][/] - Buscar aluno.\n"
                "[yellow][3][/] - Listar alunos.\n"
                "[yellow][4][/] - Finalizar.",
                title=":books: [white]Gestão Acadêmica[/] ",
                border_style="cyan",
                width=40,
            )
        )

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            nome = ler_nome("Nome: ")

            if nome.strip() in carregar_dados():
                print(
                    Panel(
                        f"Aluno [blue]{nome.title()}[/] já registrado nos [green]Dados dos alunos[/], informe um nome diferente.",
                        title="[red] Falha ao Registrar",
                        width=40,
                    )
                )
                continue

            qtd_notas = ler_quantidade_nota("Quantas notas quer informar: ")
            notas = ler_nota("Nota: ", qtd_notas)

            try:
                registrar_aluno(cadastro, nome, notas)

            except ValueError as error:
                print(error)
                continue

            print(
                "",
                Panel(
                    f"Aluno [blue]{nome}[/] registrado no Banco de dados do SGA.",
                    title=":file_folder: [white]Registro concluido ",
                    border_style="yellow",
                    width=40,
                ),
            )

        elif opcao == "2":
            aluno = ler_nome("Informe o nome do Aluno: ")
            try:
                resultado = buscar_aluno(cadastro, aluno)

            except ValueError as error:
                print(error)
                continue

            print(
                "",
                Panel(
                    f"Aluno: [blue]{resultado['nome']}[/]\n"
                    f"Notas: [blue]{resultado['notas']}[/]",
                    title="[white]Resultado da Busca :magnifying_glass_tilted_left:[/]",
                    border_style="green",
                    width=40,
                ),
            )

        elif opcao == "3":
            try:
                listagem = listar_alunos(cadastro)

            except ValueError as error:
                print(error)
                continue

            for num, aluno in enumerate(listagem):
                print(
                    "",
                    Panel(
                        f'Aluno: {aluno["nome"]}\n'
                        f'Media: {aluno["media"]}\n'
                        f'Situacao: {aluno["situacao"]}',
                        title=f":child: [white]Aluno {num + 1} ",
                        border_style="green",
                        width=40,
                    ),
                )

        elif opcao == "4":
            salvar_dados(cadastro)
            print(
                "",
                Panel(
                    "Finalizado com [green]sucesso[/], Dados salvos em formato json",
                    title=":closed_book:[white] Encerrado ",
                    border_style="red",
                    width=40,
                ),
            )

            break

        else:
            print("\n[red]Opcao invalida. Tente novamente.[/]\n")


if __name__ == "__main__":
    main()
