from django.db import models


class Coleta_Organica(models.Model):
    cep_inicio = models.CharField(max_length=9, help_text="CEP inicial da faixa atendida (ex: 74000-000)")
    cep_fim = models.CharField(max_length=9, help_text="CEP final da faixa atendida (ex: 74999-999)")
    
    dia_semana = models.CharField(
        max_length=84,
        help_text="Dia da semana em que a coleta ocorre, caso seja mais de um preencher com vírgula (ex: Segunda-feira, Quarta-feira, Sexta-feira)"
    )
    
    turno = models.CharField(
        max_length=7,
        help_text="Período do dia (Diurno ou Noturno, somente um dos dois)"
    )

    def __str__(self):
        return f"(CEP: {self.cep_inicio} - {self.cep_fim})"
    

class Coleta_Seletiva(models.Model):
    cep_inicio = models.CharField(max_length=9, help_text="CEP inicial da faixa atendida (ex: 74000-000)")
    cep_fim = models.CharField(max_length=9, help_text="CEP final da faixa atendida (ex: 74999-999)")
    
    dia_semana = models.CharField(
        max_length=86,
        help_text="Dia da semana em que a coleta ocorre, caso seja mais de um preencher com vírgula (ex: Segunda-feira, Quarta-feira, Sexta-feira)"
    )
    
    turno = models.CharField(
        max_length=7,
        help_text="Período do dia (Diurno ou Noturno, somente um dos dois)"
    )

    def __str__(self):
        return f"(CEP: {self.cep_inicio} - {self.cep_fim})"
    

class Eco_pontos(models.Model):

    Nome = models.CharField(max_length=50, help_text="Nome do ecoponto (ex: Ecoponto do Setor Bueno)")
    Dias_funcionamento = models.CharField(max_length=30, help_text="Dias de funcionamento do ecoponto (ex: Segunda-feira a Sexta-feira)")
    Horario_funcionamento = models.CharField(max_length=15, help_text="Horário de funcionamento do ecoponto (ex: 08:00 às 18:00)")
    endereco = models.CharField(max_length=84, help_text="Endereço do ecoponto")
    cep = models.CharField(max_length=9, help_text="CEP do ecoponto (ex: 74000-000)")
    
    def __str__(self):
        return f"{self.Nome} - {self.cep}"


