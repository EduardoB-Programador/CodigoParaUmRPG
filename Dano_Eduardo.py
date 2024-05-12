class Player():
    acoes = int()
    vida = int()
    escudo = int()
    energia = int()
    arma_primaria = None
    arma_secundaria = None
    arma_corpo_a_corpo = None

    @classmethod
    def __init__(cls, vida, escudo, energia, acoes = 4):
        cls.acoes = acoes
        cls.vida = vida
        cls.escudo = escudo
        cls.energia = energia

    @classmethod
    def mostrar_tudo(cls, vida_base, escudo_base, energia_base, acoes_base, arma1_usos_base, arma2_usos_base):
        print(f"\n---------------------------------------------\nSeus atributos são:\n\nVida = {cls.vida}/{vida_base}\nEscudo = {cls.escudo}/{escudo_base}\nEnergia = {cls.energia}/{energia_base}\nAções base = {cls.acoes}/{acoes_base}\n\n---------------------------------------------\nSuas armas são:\n\nArma primária: {cls.arma_primaria} - Usos: {cls.arma_primaria.usos}/{arma1_usos_base}\nArma secundária: {cls.arma_secundaria} - Usos: {cls.arma_secundaria.usos}/{arma2_usos_base}\nArma corpo a corpo: {cls.arma_corpo_a_corpo}\n\n---------------------------------------------\n")

    @classmethod
    def quantidade_acoes_alterada(cls):
        quantidade = int(input("\nQual a quantidade de ações que foi definida?\n"))
        cls.acoes = quantidade

        quantidade_turnos = int(input("\nPor quantos turnos essa quantidade de ações foi definida?\n"))

        return quantidade_turnos, quantidade

    @classmethod
    def energia_alterada(cls):
        tipo = input("\n---------------------------------------------\n1 - Recebeu energia\n2 - Roubaram sua energia\n3 - Não alterar\n---------------------------------------------\n\nQual o tipo de alteração na energia?\n")

        if (tipo == "1"):
            valor = int(input("\nDigite a quantidade de energia que foi recebida:\n"))

            cls.energia += valor

        elif (tipo == "2"):
            valor = int(input("\nDigite a quantidade de energia que foi roubada:\n"))

            cls.energia -= valor

        elif (tipo == "3"):
            print("\nAção cancelada.\n")

            return

        else:
            print(f"\nO valor {tipo} não corresponde a nenhuma opção.\n")

            cls.energia_alterada()

    @classmethod
    def vida_alterada(cls):
        
        tipo = input("\n---------------------------------------------\n1 - Levou dano\n2 - Cura na vida\n3 - Cura no escudo\n4 - Cura no escudo e vida\n5 - Aumento de vida máxima\n6 - Não alterar\n---------------------------------------------\n\nQual o tipo de alteração na vida?\n")

        if (tipo == "1"):
            valor = int(input("\nQuanto de dano foi recebido?\n"))
            direto_na_vida = int(input("\nO dano foi direto na vida?(0 - não/1 - sim)\n"))

            if (direto_na_vida == 1):
                cls.vida -= valor
                print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

            else:
                if (cls.escudo != 0):
                    cls.escudo -= valor

                else:
                    cls.vida -= valor

                print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

        elif (tipo == "2"):
            valor = int(input("\nQual o valor de cura na vida recebida?\n"))

            cls.vida += valor

            print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

        elif (tipo == "3"):
            valor = int(input("\nQual o valor de cura no escudo recebida?\n"))

            cls.escudo += valor

            print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

        elif (tipo == "4"):
            valor1 = int(input("\nQual o valor de cura na vida recebida?\n"))
            valor2 = int(input("\nQual o valor de cura no escudo recebida?\n"))

            cls.vida += valor1
            cls.escudo += valor2

            print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

        elif (tipo == "5"):
            valor = input("\nQual é o valor de sobrevida recebida?\n")

            cls.vida += valor

            print(f"\nSua vida atual é: {cls.vida}\nSeu escudo atual é: {cls.escudo}")

        elif (tipo == "6"):
            print("\nAção cancelada.\n")

            return

        else:
            print(f"\nO dígito {tipo} não corresponde a nenhuma opção. Tente novamente.\n")
            cls.vida_alterada()

        return

    @classmethod
    def verifica_acoes(cls):

        if (cls.acoes <= 0):
            print("\nAcabaram suas ações.\n")

        return cls.acoes

    @classmethod
    def usa_acoes(cls, custoAcao = 1):
        cls.acoes -= custoAcao
    
    @classmethod
    def usa_habilidade(cls):
        
        if (cls.verifica_acoes() == 0):
            return

        custo = int(input("\nQual o custo da habilidade?(se não quiser mais usar habilidade digite 0)\n"))

        if (custo > cls.energia):
            print(f"\nEnergia insuficiente.\nEnergia restante é {cls.energia}")
            cls.usa_habilidade()
            return

        elif (custo == 0):
            print(f"\nUso de habilidade cancelada. Energia restante é {cls.energia}")
            return

        cls.usa_acoes()
        cls.energia -= custo
        print(f"\nA habilidade foi usada.\nEnergia restante é {cls.energia}")

    @classmethod
    def movimentar(cls):

        if (cls.verifica_acoes() == 0):
            return

        print("\nVocê se moveu.\n")        
        cls.usa_acoes()
        return cls.verifica_acoes()

    @classmethod
    def definir_armas(cls):
        
        cls.arma_primaria = Arma.cria_arma_primaria()
        cls.arma_secundaria = Arma.cria_arma_secundaria()
        cls.arma_corpo_a_corpo = Arma.cria_arma_perto()

class Arma():
    usos = int()
    recarregar = True

    def __init__(self, usos = -1):
        # usos = -1 significa que não possui munição
        self.usos = usos

    def recarregar_arma(self, custo_acao_recarga = 1):

        if (Player.verifica_acoes() == 0):
            return
        
        recarregar_p = int(input("\nVocê deseja recarregar?(0 = não/ 1 = sim)\n"))
        if (recarregar_p == 0):
            self.recarregar = False

        elif (recarregar_p == 1):
            self.recarregar = True

        else:
                        
            print(f"\nA ação {recarregar_p} não corresponde a nenhuma opção informada\n")
            self.recarregar_arma()

        if (Player.verifica_acoes() < custo_acao_recarga):

            self.recarregar = False
            
            print(f"\nAções insuficientes para recarregar, você possui {Player.verifica_acoes()} ações e esse equipamento requer {custo_acao_recarga} ações para ser recarregado\n")

            return False
        
        else:
            
            if (self.recarregar == False):
                print("\nA arma não foi recarregada")
                return False
            
            else:
                print("\nA arma foi recarregada")
                Player.usa_acoes(custo_acao_recarga)
                return True   
    
    def mostra_dano(self, dano, usos, acoes):
        print(f"\n---------------------------------------------\nO dano final causado é igual a {dano}.\nA quantidade de usos desse equipamento é igual a {usos}.\nA quantidade de ações restantes é {acoes}\n---------------------------------------------\n")

    def usa_usos(self):
        self.usos -= 1

    def verifica_usos(self):

        if (self.usos <= 0):
            print("\nAcabaram os usos desse equipamento, procure munição\n")
            return True
        
        else:
            return False
        
    @classmethod
    def cria_arma_primaria(cls):
        decisao = input("\n---------------------------------------------\n1 - Grakata\n2 - Braton\n---------------------------------------------\nQual arma primária você deseja?\n")

        if (decisao == "1"):
            arma_primaria = Grakata()
            
            return arma_primaria
        
        elif (decisao == "2"):
            arma_primaria = Braton()

            return arma_primaria
        
        else:
            print(f"\nA opção {decisao} não se refere a nenhuma das opções mencionadas. Tente novamente.\n")

            return cls.cria_arma_primaria()

    @classmethod
    def cria_arma_secundaria(cls):
        decisao = input("\n---------------------------------------------\n1 - Hikou\n2 - Grakatas duplas\n---------------------------------------------\nQual arma secundária você deseja?\n")

        if (decisao == "1"):
            arma_secundaria = Hikou()
            
            return arma_secundaria
        
        elif (decisao == "2"):
            arma_secundaria = Grakatas_duplas()

            return arma_secundaria
        
        else:
            print(f"\nA opção {decisao} não se refere a nenhuma das opções mencionadas. Tente novamente.\n")

            return cls.cria_arma_secundaria()

    @classmethod
    def cria_arma_perto(cls):
        decisao = input("\n---------------------------------------------\n1 - Skana\n2 - Bo\n---------------------------------------------\nQual arma corpo a corpo você deseja?\n")

        if (decisao == "1"):
            arma_perto = Skana()
            
            return arma_perto
        
        elif (decisao == "2"):
            arma_perto = Bo()

            return arma_perto
        
        else:
            print(f"\nA opção {decisao} não se refere a nenhuma das opções mencionadas. Tente novamente.\n")

            return cls.cria_arma_perto()

class Grakata(Arma):
    custo_acao_recarga = 1
    #Com split chamber, infested clip e heavy caliber

    def __init__(self, usos = 10):
        super().__init__(usos)

    def causar_dano(self, dado_acerto):
        
        if (Player.verifica_acoes() == 0 or super().verifica_usos()):
            return

        if (not self.recarregar):
            if (not super().recarregar_arma(self.custo_acao_recarga)):
                return
            
        if (Player.verifica_acoes() == 0):
            return
        
        super().usa_usos()
        self.recarregar = False
        Player.usa_acoes()

        print(f"\n---------------------------------------------\nO dano final causado é igual a {dado_acerto * 4} ignorando o escudo.\nCaso o inimigo seja de blindagem o dano final é igual a {dado_acerto * 8}.\n\nQuantidade de usos agora é {self.usos}\n---------------------------------------------\n")

class Braton(Arma):
    custo_acao_recarga = 1
    #Sem mods

    def __init__(self, usos = 12):
        super().__init__(usos)

    def causar_dano(self, dado_acerto):
        
        if (Player.verifica_acoes() == 0 or super().verifica_usos()):
            return

        if (not self.recarregar):
            if (not super().recarregar_arma(self.custo_acao_recarga)):
                return
            
        if (Player.verifica_acoes() == 0):
            return
        
        super().usa_usos()
        self.recarregar = False
        Player.usa_acoes()
        
        if (dado_acerto > 33):
            valor = int(input(f"\nO dano foi crítico, verifique o dano jogando {dado_acerto}d2.\n"))

            super().mostra_dano(valor, self.usos, Player.verifica_acoes())

        else:
            super().mostra_dano(dado_acerto, self.usos, Player.verifica_acoes())
    
class Hikou(Arma):
    custo_acao_recarga = 1
    #Com target cracker

    def __init__(self, usos = 12):
        super().__init__(usos)

    def causar_dano(self, dado_acerto):

        if (Player.verifica_acoes() == 0 or super().verifica_usos()):
            return

        if (not self.recarregar):
            if (not super().recarregar_arma(self.custo_acao_recarga)):
                return
            
        if (Player.verifica_acoes() == 0):
            return
        
        dado_dano = int(input(f"\nRode um {dado_acerto}d2 para computar o dano\n"))
            
        if (dado_acerto > 15):
            dado_dano *= 4
            #Dano crítico

        super().usa_usos()
        self.recarregar = False
        Player.usa_acoes()

        super().mostra_dano(dado_dano, self.usos, Player.verifica_acoes)

class Grakatas_duplas(Arma):
    custo_acao_recarga = 2
    #Com Hornet Strike

    def __init__(self, usos = 5):
        super().__init__(usos)

    def causar_dano(self, dado_acerto):

        if (Player.verifica_acoes() == 0 or super().verifica_usos()):
            return

        if (not self.recarregar):
            if (not super().recarregar_arma(self.custo_acao_recarga)):
                return
            
        if (Player.verifica_acoes() == 0):
            return
        
        super().usa_usos()
        self.recarregar = False
        Player.usa_acoes()

        dado_acerto += (dado_acerto / 2)
        super().mostra_dano(dado_acerto, self.usos, Player.verifica_acoes)

class Skana(Arma):
    #Com Fury

    def mostra_dano(self, dano, acoes):
        print(f"\n---------------------------------------------\nO dano final causado é igual a {dano}.\nA quantidade de ações restantes é {acoes}\n---------------------------------------------\n")
    
    def causar_dano(self, dado_acerto):

        if (Player.verifica_acoes() == 0):
            return
        
        Player.usa_acoes()

        if (dado_acerto > 18):
            #Dano crítico
            valor = int(input(f"\nO dano causado é critico rode {dado_acerto}d2 para obter o dano crítico.\n"))
            
            self.mostra_dano(valor, Player.verifica_acoes())

        else:
            self.mostra_dano(dado_acerto, Player.verifica_acoes())

class Bo(Arma):
    #Sem mods

    def mostra_dano(self, dano, acoes):
        print(f"\n---------------------------------------------\nO dano final causado é igual a {dano}.\nA quantidade de ações restantes é {acoes}\n---------------------------------------------\n")

    def causar_dano(self, dado_acerto):

        if (Player.verifica_acoes() == 0):
            return
        
        Player.usa_acoes()

        if (dado_acerto == 20):
            valor = int(input(f"\nO dano causado é critico rode {dado_acerto}d2 para obter o dano crítico.\n"))

            self.mostra_dano(valor, Player.verifica_acoes())

        else:
            self.mostra_dano(dado_acerto, Player.verifica_acoes())

class Jogando():

    @staticmethod
    def cria_personagem():
        vida = int(input("\n---------------------------------------------\n\nDefina a quantidade de vida base do seu personagem:\n"))
        escudo = int(input("\nDefina a quantidade de escudo base do seu personagem:\n"))
        energia = int(input("\nDefina a quantidade de energia base do seu personagem:\n"))
        print("---------------------------------------------\n")

        player = Player(vida, escudo, energia)
        player.definir_armas()

        return player
    
    @staticmethod
    def meu_turno(vida_base, escudo_base, energia_base, acoes_base, arma1_usos_base, arma2_usos_base, player = Player):

        player.mostrar_tudo(vida_base, escudo_base, energia_base, acoes_base, arma1_usos_base, arma2_usos_base)

        while True:
            acao = input("\n---------------------------------------------\n1 - Movimentar para perto do inimigo\n2 - Usar habilidade\n3 - Causar dano\n4 - Mostar situação do personagem\n5 - Turno encerrado\n---------------------------------------------\nO que deseja fazer?\n")

            if (acao == "1"):
                player.movimentar()
    
            elif (acao == "2"):
                player.usa_habilidade()

            elif (acao == "3"):
                arma = input("\n---------------------------------------------\n1 - Arma primária\n2 - Arma Secundária\n3 -  Arma corpo a corpo\n---------------------------------------------\nQual arma você deseja usar?\n")

                if (arma == "1"):
                    dado = int(input("\nQual é o valor do dado de acerto?\n"))
                    player.arma_primaria.causar_dano(dado)

                elif (arma == "2"):
                    dado = int(input("\nQual é o valor do dado de acerto?\n"))
                    player.arma_secundaria().causar_dano(dado)

                elif (arma == "3"):
                    dado = int(input("\nQual é o valor do dado de acerto?\n"))
                    player.arma_corpo_a_corpo().causar_dano(dado)

                else:
                    print(f"\nA ação {arma} não corresponde a nenhuma opção informada\n")
                    Jogando.meu_turno(player)

            elif (acao == "4"):
                player.mostrar_tudo(vida_base, escudo_base, energia_base, acoes_base, arma1_usos_base, arma2_usos_base)

            elif (acao == "5"):
                break
        
            else:
                print(f"\nA ação {acao} não corresponde a nenhuma opção informada\n")
                
            
    @staticmethod
    def main():

        print("\n---------------------------------------------\nBem vindo ao sistema de dano em turnos feito por mim para o RPG que estamos jogando.\nSerão requeridos algumas informações base do seu personagem.\n---------------------------------------------\n")

        player = Jogando.cria_personagem()

        acao_base = player.acoes
        tempo = 0
        quantidade_temp = int()
        vida_base = player.vida
        escudo_base = player.escudo
        energia_base = player.energia
        arma1_usos_base = player.arma_primaria.usos
        arma2_usos_base = player.arma_secundaria.usos
        

        while True:

            acao = input("\n---------------------------------------------\n1 - Lore/Periodo sem batalha\n2 - Alteração na vida (Dano recebido ou cura recebida)\n3 - Alteração na energia (energia drenada ou recuperação de energia)\n4 - Alteração na quantidade de ações\n5 - Mostrar situação do personagem\n6 - Meu turno\n7 - Sessão encerrada\n---------------------------------------------\nDigite qualquer uma das opções acima para continuar:\n")

            
            if (acao == "1"):
                input("\nAperte Enter para sair da parte do período sem batalha.\n")

            elif (acao == "2"):
                player.vida_alterada()

            elif (acao == "3"):
                player.energia_alterada()

            elif (acao == "4"):
                tempo, quantidade_temp = player.quantidade_acoes_alterada()

            elif (acao == "5"):
                player.mostrar_tudo(vida_base, escudo_base, energia_base, acao_base, arma1_usos_base, arma2_usos_base)
                input("\nAperte Enter para continuar.\n")

            elif (acao == "6"):
                Jogando.meu_turno(vida_base, escudo_base, energia_base, acao_base, arma1_usos_base, arma2_usos_base, player)

                tempo -= 1
                
                if (tempo > 0):
                    Player.acoes = quantidade_temp

                else:
                    Player.acoes = acao_base

                print(f"\nVocê terá {player.acoes} ações no próximo turno.\n")

            elif (acao == "7"):
                break

            else:
                print(f"\nA opção {acao} não corresponde a nenhuma opção informada. Tente Novamente\n")

Jogando().main()

# auto-py-to-exe