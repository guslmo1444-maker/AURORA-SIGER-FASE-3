"""
================================================================================
SISTEMA INTELIGENTE DE GERENCIAMENTO ENERGÉTICO DA COLÔNIA MARTE
================================================================================
Versão: 2.0
Autor: Sistema de Automação Colonial
Descrição: Monitora, analisa e toma decisões sobre o consumo energético
           da colônia em tempo real.
================================================================================
"""

# ==========================================
# 1. IMPORTAÇÃO DE BIBLIOTECAS
# ==========================================

from datetime import datetime
import random

# ==========================================
# 2. ORGANIZAÇÃO DOS DADOS (ESTRUTURA PRINCIPAL)
# ==========================================

colonia = {
    "energia": {
        "solar": 40,        # kW - geração dos painéis solares
        "eolica": 30,       # kW - geração das turbinas eólicas
        "reserva": 20       # kW - baterias/estoque de emergência
    },
    
    "consumo": {
        "suporte_vida": 35,  # kW - oxigênio, água, pressurização
        "laboratorio": 20,   # kW - pesquisas, computadores, equipamentos
        "iluminacao": 15,    # kW - iluminação geral da colônia
        "aquecimento": 0     # kW - será calculado dinamicamente
    },
    
    "clima": {
        "vento": 11,          # km/h - velocidade do vento
        "temperatura": -20,   # °C - temperatura externa
        "radiacao_solar": 65  # % - eficiência dos painéis (0-100)
    },
    
    "historico": [],          # lista para armazenar eventos importantes
    "alertas": []             # lista para armazenar alertas gerados
}

# ==========================================
# 3. FUNÇÕES AUXILIARES (REGRAS DE NEGÓCIO)
# ==========================================

def calcular_aquecimento(temperatura):
    """
    Calcula a necessidade de aquecimento baseado na temperatura externa.
    Regra: abaixo de -10°C, liga aquecimento (10kW)
          abaixo de -20°C, liga aquecimento intensificado (18kW)
    
    Parâmetros:
        temperatura (float): temperatura externa em °C
    
    Retorna:
        int: consumo de aquecimento em kW
    """
    if temperatura <= -20:
        return 18  # aquecimento intenso
    elif temperatura < -10:
        return 10  # aquecimento moderado
    else:
        return 0   # sem necessidade de aquecimento


def registrar_evento(mensagem, tipo="INFO"):
    """
    Registra eventos importantes no histórico da colônia.
    
    Parâmetros:
        mensagem (str): descrição do evento
        tipo (str): INFO, ALERTA, CRITICO, SUGESTAO
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    evento = f"[{timestamp}] [{tipo}] {mensagem}"
    colonia["historico"].append(evento)
    
    # Se for alerta, também adiciona à lista de alertas
    if tipo in ["ALERTA", "CRITICO"]:
        colonia["alertas"].append(evento)
    
    print(evento)


def atualizar_consumo_dinamico():
    """
    Atualiza os consumos que dependem de condições variáveis.
    Retorna o consumo total atualizado.
    """
    # Calcula necessidade de aquecimento baseado na temperatura
    aquecimento = calcular_aquecimento(colonia["clima"]["temperatura"])
    colonia["consumo"]["aquecimento"] = aquecimento
    
    # Retorna soma total
    return sum(colonia["consumo"].values())


def calcular_geracao_eolica(velocidade_vento):
    """
    Calcula a geração de energia eólica baseada na velocidade do vento.
    Usa regressão linear: energia = 2.5 * velocidade
    
    Parâmetros:
        velocidade_vento (float): velocidade do vento em km/h
    
    Retorna:
        float: energia gerada em kW
    """
    coeficiente = 2.5
    geracao = coeficiente * velocidade_vento
    return min(geracao, 45)  # Limite máximo de 45 kW (proteção)


def calcular_geracao_solar(radiacao, base=40):
    """
    Calcula a geração solar considerando a radiação atual.
    
    Parâmetros:
        radiacao (float): percentual de radiação solar (0-100)
        base (int): geração máxima em kW
    
    Retorna:
        float: energia gerada em kW
    """
    return base * (radiacao / 100)


def regressao_linear_previsao(dados_vento, dados_energia):
    """
    Calcula a regressão linear para previsão de energia eólica.
    Método dos mínimos quadrados.
    
    Parâmetros:
        dados_vento (list): valores históricos de velocidade do vento
        dados_energia (list): valores históricos de geração eólica
    
    Retorna:
        tuple: (coeficiente_angular, coeficiente_linear)
    """
    n = len(dados_vento)
    media_vento = sum(dados_vento) / n
    media_energia = sum(dados_energia) / n
    
    # Calcula coeficiente angular (a)
    numerador = sum((dados_vento[i] - media_vento) * (dados_energia[i] - media_energia) for i in range(n))
    denominador = sum((dados_vento[i] - media_vento) ** 2 for i in range(n))
    
    a = numerador / denominador if denominador != 0 else 0
    
    # Calcula coeficiente linear (b)
    b = media_energia - a * media_vento
    
    return a, b


def determinar_nivel_alerta(geracao, consumo):
    """
    Determina o nível de alerta baseado na relação geração/consumo.
    
    Parâmetros:
        geracao (float): energia gerada total
        consumo (float): energia consumida total
    
    Retorna:
        str: nível do alerta (VERDE, AMARELO, VERMELHO)
    """
    if geracao < 0.6 * consumo:
        return "🔴 CRÍTICO"
    elif geracao < 0.9 * consumo:
        return "🟡 ATENÇÃO"
    else:
        return "🟢 NORMAL"


def gerenciar_reserva(geracao, consumo, reserva_atual):
    """
    Gerencia o uso da reserva energética quando necessário.
    
    Parâmetros:
        geracao (float): energia gerada total
        consumo (float): energia consumida total
        reserva_atual (float): energia disponível na reserva
    
    Retorna:
        tuple: (nova_reserva, acao_tomada)
    """
    if consumo > geracao:
        deficit = consumo - geracao
        if reserva_atual >= deficit:
            nova_reserva = reserva_atual - deficit
            acao = f"Usado {deficit:.1f} kW da reserva. Reserva restante: {nova_reserva:.1f} kW"
            return nova_reserva, acao
        else:
            acao = f"CRÍTICO: Reserva insuficiente! Déficit de {deficit - reserva_atual:.1f} kW"
            return 0, acao
    else:
        # Se há excesso, armazena 80% na reserva (20% é perdido/descartado)
        excesso = geracao - consumo
        acrescimo = excesso * 0.8
        nova_reserva = min(reserva_atual + acrescimo, 100)  # Limite máximo de 100 kW
        acao = f"Excedente de {excesso:.1f} kW. {acrescimo:.1f} kW armazenados na reserva"
        return nova_reserva, acao


# ==========================================
# 4. DADOS HISTÓRICOS PARA PREVISÃO
# ==========================================

# Dados coletados nos últimos dias
historico_vento = [8, 10, 12, 11, 9, 13, 10]      # km/h
historico_energia_eolica = [20, 25, 30, 28, 22, 32, 25]  # kW

# ==========================================
# 5. PROCESSAMENTO PRINCIPAL
# ==========================================

print("\n" + "="*70)
print(" SISTEMA INTELIGENTE DA COLÔNIA - INICIANDO ANÁLISE ".center(70, "="))
print("="*70)

# 5.1. Registrar início da operação
registrar_evento("Sistema iniciado", "INFO")
registrar_evento(f"Temperatura externa: {colonia['clima']['temperatura']}°C", "INFO")

# 5.2. Atualizar consumos dinâmicos
consumo_total = atualizar_consumo_dinamico()

# 5.3. Calcular gerações atualizadas
colonia["energia"]["solar"] = calcular_geracao_solar(colonia["clima"]["radiacao_solar"])
colonia["energia"]["eolica"] = calcular_geracao_eolica(colonia["clima"]["vento"])
geracao_total = colonia["energia"]["solar"] + colonia["energia"]["eolica"]

# ==========================================
# 6. RELATÓRIO DE STATUS
# ==========================================

print("\n" + "📊 STATUS OPERACIONAL DA COLÔNIA".center(70))
print("-"*70)

print(f"\n🔋 GERAÇÃO DE ENERGIA:")
print(f"   • Energia Solar: {colonia['energia']['solar']:.1f} kW")
print(f"   • Energia Eólica: {colonia['energia']['eolica']:.1f} kW")
print(f"   • TOTAL GERADO: {geracao_total:.1f} kW")
print(f"   • Reserva Disponível: {colonia['energia']['reserva']:.1f} kW")

print(f"\n💡 CONSUMO DE ENERGIA:")
for sistema, consumo in colonia["consumo"].items():
    if consumo > 0:
        print(f"   • {sistema.replace('_', ' ').title()}: {consumo} kW")
print(f"   • TOTAL CONSUMIDO: {consumo_total} kW")

print(f"\n🌦️ CONDIÇÕES CLIMÁTICAS:")
print(f"   • Vento: {colonia['clima']['vento']} km/h")
print(f"   • Temperatura: {colonia['clima']['temperatura']}°C")
print(f"   • Radiação Solar: {colonia['clima']['radiacao_solar']}%")

# ==========================================
# 7. PREVISÃO DE ENERGIA EÓLICA
# ==========================================

print("\n" + "🌬️ PREVISÃO DE ENERGIA EÓLICA".center(70))
print("-"*70)

# Método 1: Regressão linear simples
coeficiente_simples = 2.5
previsao_simples = coeficiente_simples * colonia["clima"]["vento"]
print(f"📈 Método Simples (coef. fixo 2.5): {previsao_simples:.1f} kW")

# Método 2: Regressão linear com dados históricos
a, b = regressao_linear_previsao(historico_vento, historico_energia_eolica)
previsao_avancada = a * colonia["clima"]["vento"] + b
print(f"📊 Método Avançado (regressão histórica): {previsao_avancada:.1f} kW")
print(f"   → Equação: energia = {a:.2f} × vento + {b:.2f}")

# ==========================================
# 8. ANÁLISE ENERGÉTICA E DECISÕES
# ==========================================

print("\n" + "⚡ ANÁLISE ENERGÉTICA".center(70))
print("-"*70)

# 8.1. Verificar equilíbrio energético
diferenca = geracao_total - consumo_total

if diferenca > 0:
    print(f"✅ EXCEDENTE ENERGÉTICO: sobra de {diferenca:.1f} kW")
    registrar_evento(f"Excedente de {diferenca:.1f} kW gerado", "SUGESTAO")
elif diferenca < 0:
    print(f"⚠️ DÉFICIT ENERGÉTICO: falta de {abs(diferenca):.1f} kW")
    registrar_evento(f"Déficit de {abs(diferenca):.1f} kW detectado", "ALERTA")
else:
    print("⚖️ SISTEMA EQUILIBRADO: geração = consumo")
    registrar_evento("Sistema perfeitamente equilibrado", "INFO")

# 8.2. Determinar nível de alerta
nivel = determinar_nivel_alerta(geracao_total, consumo_total)
print(f"\n🚨 NÍVEL DE ALERTA: {nivel}")

# 8.3. Gerenciar reserva energética
nova_reserva, mensagem_reserva = gerenciar_reserva(
    geracao_total, 
    consumo_total, 
    colonia["energia"]["reserva"]
)
colonia["energia"]["reserva"] = nova_reserva
print(f"\n🔋 GERENCIAMENTO DA RESERVA:")
print(f"   → {mensagem_reserva}")

# ==========================================
# 9. REGRAS DE DECISÃO AUTOMÁTICAS
# ==========================================

print("\n" + "🤖 DECISÕES AUTOMÁTICAS".center(70))
print("-"*70)

# Regra 1: Ativar modo economia
if geracao_total < 50 and consumo_total > 60:
    print("🔌 ATIVANDO MODO ECONOMIA:")
    print("   • Reduzindo iluminação em 50%")
    print("   • Otimizando sistemas de suporte")
    registrar_evento("Modo economia ativado", "ALERTA")

# Regra 2: Prioridade para sistemas essenciais
if consumo_total > geracao_total + colonia["energia"]["reserva"]:
    print("\n⚠️ CRISE ENERGÉTICA DETECTADA!")
    print("   → Desligando sistemas NÃO ESSENCIAIS:")
    print("   • Laboratório de pesquisas (20 kW)")
    print("   • Iluminação reduzida (15 kW → 5 kW)")
    registrar_evento("Sistemas não essenciais desligados devido a crise", "CRITICO")
    
    # Simula desligamento
    consumo_total -= (20 + 10)  # laboratório + redução iluminação
    print(f"   → Novo consumo total: {consumo_total} kW")
    
    # Verifica se resolveu
    if consumo_total <= geracao_total + colonia["energia"]["reserva"]:
        print("   ✅ Crise controlada!")
        registrar_evento("Crise energética controlada após desligamentos", "INFO")
    else:
        print("   ❌ Crise PERSISTE! Necessário suporte externo!")
        registrar_evento("Crise energética NÃO controlada - Emergência!", "CRITICO")

# Regra 3: Sugestões proativas
if geracao_total > consumo_total:
    sobra = geracao_total - consumo_total
    if sobra > 15:
        print(f"\n💡 SUGESTÃO: Excedente de {sobra:.1f} kW disponível")
        print("   → Recomendado: carregar veículos ou processar dados")
        registrar_evento(f"Grande excedente de {sobra:.1f} kW disponível", "SUGESTAO")
    else:
        print(f"\n💡 SUGESTÃO: Pequeno excedente de {sobra:.1f} kW")
        print("   → Recomendado: armazenar para momentos críticos")

# ==========================================
# 10. RELATÓRIO FINAL E ESTATÍSTICAS
# ==========================================

print("\n" + "📋 RELATÓRIO FINAL".center(70))
print("="*70)

print(f"\n📊 ESTATÍSTICAS DO DIA:")
print(f"   • Geração total: {geracao_total:.1f} kW")
print(f"   • Consumo total: {consumo_total} kW")
print(f"   • Saldo: {geracao_total - consumo_total:+.1f} kW")
print(f"   • Reserva final: {colonia['energia']['reserva']:.1f} kW")
print(f"   • Eficiência energética: {(geracao_total/consumo_total)*100:.1f}%" if consumo_total > 0 else "   • Eficiência: N/A")

print(f"\n📜 HISTÓRICO DE EVENTOS ({len(colonia['historico'])} eventos):")
print("-"*70)
for evento in colonia["historico"][-5:]:  # Mostra últimos 5 eventos
    print(f"   {evento}")

if colonia["alertas"]:
    print(f"\n⚠️ ALERTAS ATIVOS ({len(colonia['alertas'])}):")
    print("-"*70)
    for alerta in colonia["alertas"][-3:]:  # Mostra últimos 3 alertas
        print(f"   {alerta}")

# ==========================================
# 11. RECOMENDAÇÕES PARA O OPERADOR
# ==========================================

print("\n" + "🎯 RECOMENDAÇÕES PARA O OPERADOR".center(70))
print("="*70)

if consumo_total > geracao_total:
    if colonia["energia"]["reserva"] > 0:
        print("✅ Ação: Continuar usando reserva energética")
        print("✅ Monitorar: Recarga da reserva nas próximas horas")
    else:
        print("⚠️ Ação URGENTE: Reduzir consumo em 20%")
        print("⚠️ Prioridade: Verificar integridade dos geradores")
else:
    print("✅ Situação confortável: Geração suficiente")
    print("✅ Recomendação: Aumentar processamento científico")
    
    if colonia["energia"]["reserva"] < 30:
        print("✅ Sugestão: Priorizar recarga da reserva")

print("\n" + "="*70)
print(" SISTEMA ENCERRADO - ANÁLISE COMPLETA ".center(70, "="))
print("="*70 + "\n")

# ==========================================
# 12. FUNÇÃO PARA SIMULAÇÃO DE TEMPO REAL (OPCIONAL)
# ==========================================

def simular_proximo_dia():
    """
    Função opcional para simular a evolução da colônia ao longo dos dias.
    Útil para testes e demonstrações.
    """
    print("\n🔄 INICIANDO SIMULAÇÃO DO PRÓXIMO DIA...")
    
    # Altera condições climáticas aleatoriamente
    colonia["clima"]["vento"] += random.randint(-3, 3)
    colonia["clima"]["temperatura"] += random.randint(-5, 5)
    colonia["clima"]["radiacao_solar"] += random.randint(-15, 15)
    
    # Garante valores dentro dos limites realistas
    colonia["clima"]["vento"] = max(0, min(25, colonia["clima"]["vento"]))
    colonia["clima"]["temperatura"] = max(-40, min(20, colonia["clima"]["temperatura"]))
    colonia["clima"]["radiacao_solar"] = max(0, min(100, colonia["clima"]["radiacao_solar"]))
    
    print("✅ Condições climáticas atualizadas para o novo dia")
    print("👉 Execute o programa novamente para analisar o novo dia")

# Descomente a linha abaixo para executar a simulação
# simular_proximo_dia()

"""
================================================================================
EXPLICAÇÃO DAS PRINCIPAIS MELHORIAS:
================================================================================

1. FUNÇÕES MODULARIZADAS:
   - Cada tarefa tem sua própria função (calcular_aquecimento, gerenciar_reserva, etc.)
   - Código mais organizado, reutilizável e testável

2. HISTÓRICO E ALERTAS:
   - Sistema registra todos os eventos importantes
   - Alertas são categorizados e armazenados separadamente

3. PREVISÃO AVANÇADA:
   - Duas formas de previsão (simples e com regressão real)
   - Usa dados históricos para melhor precisão

4. GERENCIAMENTO INTELIGENTE DA RESERVA:
   - Reserva é usada automaticamente quando necessário
   - Excedente é armazenado (com limite máximo)
   - Tomada de decisão clara

5. NÍVEIS DE ALERTA (VERDE/AMARELO/VERMELHO):
   - Sistema de semáforo para fácil interpretação
   - Baseado em porcentagens de segurança

6. TOMADA DE DECISÃO AUTÔNOMA:
   - Desliga sistemas não essenciais em crise
   - Dá sugestões proativas baseadas no cenário

7. RELATÓRIOS DETALHADOS:
   - Mostra estatísticas completas
   - Histórico de eventos para auditoria
   - Recomendações claras para o operador

8. SIMULAÇÃO DE TEMPO REAL (opcional):
   - Permite avançar dias para testar cenários diferentes
   - Útil para demonstração e testes

================================================================================
COMO TESTAR DIFERENTES CENÁRIOS:
================================================================================

Para simular uma CRISE ENERGÉTICA:
   Altere colonia["energia"]["solar"] = 10
   Altere colonia["energia"]["eolica"] = 5
   Altere colonia["consumo"]["suporte_vida"] = 50

Para simular EXCEDENTE:
   Altere colonia["energia"]["solar"] = 80
   Altere colonia["clima"]["vento"] = 25

Para simular TEMPERATURA EXTREMA:
   Altere colonia["clima"]["temperatura"] = -35
   (O sistema automaticamente aumentará o aquecimento)

================================================================================
"""