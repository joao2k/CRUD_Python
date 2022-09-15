class Aluno:
    cod=0
    def __init__(self,nome,idade,sexo):
        self.__nome=nome
        self.__idade=idade
        self.__sexo=sexo
        self.__nota1=None
        self.__nota2=None
        Aluno.cod+=1
        self.__matricula=Aluno.cod
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def sexo(self):
        return self.__sexo
    @property
    def nota1(self):
        return self.__nota1
    @property
    def nota2(self):
        return self.__nota2
    @property
    def matricula(self):
        return self.__matricula

    @nome.setter
    def nome(self,nome):
        self.__nome=nome

    @idade.setter
    def idade(self,idade):
        self.__idade=idade

    @nota1.setter
    def nota1(self,nota1):
        self.__nota1=nota1

    @nota2.setter
    def nota2(self,nota2):
        self.__nota2=nota2
    def imprime(self):
        print(f"{self.nome.title()}, idade:{self.idade}, sexo:{self.sexo}, matricula:{self.matricula}, AV1:{self.nota1} AV2:{self.nota2} ")
#Main
aluno=None
turma={}
while(True):
    print("\t ____ M E N U ____\n")
    print("\t1-Criar Estudante.")
    print("\t2-Remover Estudante.")
    print("\t3-listar Estudantes.")
    print("\t4-Procurar por matricula.")
    print("\t5-Adicionar nota:")
    print("\t6-Sair.")
    op=input("\tDigite uma opção:")
    #Menu
    match op:
        case "1":
            nome=input("Digite o nome do aluno:")
            idade=int(input("digite a idade do aluno:"))
            sexo=input("digite o sexo do aluno(Masculino ou Feminino): ")
            aluno=Aluno(nome,idade,sexo)
            turma.update({aluno.matricula:aluno})
            print(f"Aluno criado com sucesso.")
            print("esse aluno tem alguma nota para cadastrar?(s/n)")
            resp=input()
            resp.lower()
            if resp=="s":
                nota=float(input("digita a nota:"))
                resp=input("escolha em qual avaliação AV1 ou AV2:")
                print(resp)
                match resp:
                    case "AV1"| "av1":
                        aluno.nota1=nota
                        print("nota castrada")
                        resp=input("deseja castrar a AV2?(s/n)")
                        if resp=="s":
                            nota=float(input("digita a nota:"))
                            aluno.nota2=nota
                    case "AV2"| "av2":
                        aluno.nota2 = nota
                        print("nota cadastrada")
                    case _:
                        print("alternativa invalida (nota nao cadastrada)")
        case "2":
            matricula=input("digite a matriculado aluno a ser removido:")
            if matricula.isdigit():
                print(f"{turma[int(matricula)].nome} foi removido")
                del turma[int(matricula)]

            else:
                print("matricula invalida")
        case "3":
            for i in turma.values():
                i.imprime()
        case "4":
            matricula=input("Digite a matricula do estudante:")
            if matricula.isdigit():
                turma[int(matricula)].imprime()
            else:
                print("digite um numero valido")
        case "5":
            nota = float(input("digita a nota:"))
            resp = input("escolha em qual avaliação AV1 ou AV2:")
            print(resp)
            match resp:
                case "AV1" | "av1":
                    aluno.nota1 = nota
                    print("nota castrada")
                    resp = input("deseja castrar a AV2?(s/n)")
                    if resp == "s":
                        nota = float(input("digita a nota:"))
                        aluno.nota2 = nota
                case "AV2" | "av2":
                    aluno.nota2 = nota
                    print("nota cadastrada")
                case _:
                    print("alternativa invalida (nota nao cadastrada)")
        case "6":
            print("Programa finalizado.")
            break
        case _:
            print("Digite uma opção válida.")