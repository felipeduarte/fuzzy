class Fuzzy(object):

    def inicializar_valores(self):
        self.valor = [2500, 4000, 5000, 9000, 16000, 23000, 30000, 37000, 
                        42000, 60000]
        self.muito_baixo = [1, 0.7, 0.5, 0.2, 0, 0, 0, 0, 0, 0]
        self.baixo = [0, 0.4, 0.5, 0.9, 0.9, 0.3, 0, 0, 0, 0]
        self.alto = [0, 0, 0, 0, 0.2, 0.8, 1, 0.8, 0.4, 0]
        self.muito_alto = [0, 0, 0, 0, 0, 0, 0, 0.2, 0.7, 1]
       
    def inicializar_periodos(self):
        self.periodo = [1, 3, 6, 8, 12,
                        24]
        self.curto = [1, 0.8, 0.5, 0.3, 0, 0]
        self.medio = [0.3, 0.5, 1, 1, 0.5, 0.2]
        self.longo = [0, 0, 0.2, 0.6, 0.8, 1]

    def inicializar_rendimentos(self):
        self.rendimento = [1, 5, 10, 30, 50, 100]
        self.alto = [0, 0, 0.2, 0.3, 0.5, 1]
        self.baixo = [1, 0.8, 0.5, 0.4, 0, 0]

    def aplicar_regra1(self, valor):
        x = 0
        val = 0
        rendimento = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.muito_baixo[x]
        for x in range(0, 6):
            if val == self.alto[x]:
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra1 = rendimento
        self.peso_regra1 = val
        
    def aplicar_regra2(self, valor, periodo):
        x = 0
        val = 0
        rendimento = 0
        per = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.baixo[x]
                break
        for x in range(0, 6):
            if periodo == self.periodo[x]:
                per = self.longo[x]
        if val < per:
            per = val
        for x in range(0, 6):
            if per == self.alto[x]
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra2 = rendimento
        self.peso_regra2 = per
        
    def aplicar_regra3(self, valor, periodo):
        x = 0
        val = 0
        rendimento = 0
        per = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.baixo[x]
        for x in range(0, 6):
            if periodo == self.periodo[x]:
                per = self.curto[x]
        if val < per:
            per = val
        if per == 0.3:
            per = 0
        for x in range(0, 6):
            if per = self.baixo[x]:
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra3 = rendimento
        self.peso_regra3 = per

    def aplicar_regra4(self, valor, periodo):
        x = 0
        val = 0
        rendimento = 0
        per = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.alto[x]
        for x in range(0, 6):
            if periodo == self.periodo[x]:
                per = self.curto[x]
        if val < per:
            per = val
        for x in range(0, 6):
            if per == self.baixo[x]:
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra4 = rendimento
        self.peso_regra4 = per

    def aplicar_regra5(self, valor, periodo):
        x = 0
        val = 0
        rendimento = 0
        per = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.valor[x]
        for x in range(0, 6):
            if periodo == self.periodo[x]:
                per = self.longo[x]
        if val < per:
            per = val
        for x in range(0, 6):
            if per == self.alto[x]:
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra5 = rendimento
        self.peso_regra5 = per

    def aplicar_regra6(self, valor):
        x = 0
        val = 0
        rendimento = 0
        for x in range(0, 10):
            if valor == self.valor[x]:
                val = self.muito_alto[x]
        for x in range(0, 6):
            if val == self.alto[x]:
                rendimento = self.rendimento[x]
                break
        self.rendimento_regra6 = rendimento
        self.peso_regra6 = val
        
if __name__ == "__main__":
    pass