🚀 Sistema Inteligente da Colônia em Marte
https://img.shields.io/badge/Python-3.7+-blue.svg

Sistema autônomo para gerenciamento energético de colônias espaciais, capaz de tomar decisões inteligentes em tempo real.

📋 Índice
Sobre o Projeto

Funcionalidades

Como Funciona

Exemplo de Uso

Como Executar

🎯 Sobre o Projeto
Este sistema foi desenvolvido para gerenciar de forma inteligente a energia de uma colônia em Marte. Ele monitora consumo, geração e condições climáticas, tomando decisões automáticas para evitar crises energéticas.

⚡ Funcionalidades
Funcionalidade	Descrição
Organização Hierárquica	Dados estruturados em dicionários com subsistemas (solar/eólico/suporte_vida)
Tomada de Decisão	Regras IF/ELSE que priorizam suporte à vida sobre sistemas não essenciais
Previsão por Regressão	Estima geração eólica baseada em velocidade do vento usando mínimos quadrados
Gestão de Reserva	Armazena excedente e usa reserva automaticamente em déficit
Sistema de Alertas	Níveis VERDE/AMARELO/VERMELHO baseados na situação energética
Histórico de Eventos	Registra todas as ações e decisões para auditoria
Adaptação Climática	Ajusta aquecimento automaticamente baseado na temperatura externa
🔧 Como Funciona
1. Organização dos Dados
Os dados são organizados em um dicionário hierárquico:

python
colonia = {
    "energia": {
        "solar": 40,      # kW - geração dos painéis solares
        "eolica": 30,     # kW - geração das turbinas eólicas
        "reserva": 20     # kW - baterias de emergência
    },
    "consumo": {
        "suporte_vida": 35,  # kW - oxigênio, água, pressurização
        "laboratorio": 20,   # kW - pesquisas científicas
        "iluminacao": 15     # kW - iluminação geral
    },
    "clima": {
        "vento": 11,          # km/h - velocidade do vento
        "temperatura": -20    # °C - temperatura externa
    }
}
2. Regras de Decisão
O sistema aplica regras lógicas para tomar decisões:

python
# Regra 1: Ativar economia em crise
if geracao_total < 50 and consumo_total > 60:
    ativar_modo_economia()

# Regra 2: Priorizar sistemas essenciais
if consumo_total > geracao_total + reserva:
    desligar_laboratorio()    # Não essencial
    manter_suporte_vida()      # Essencial

# Regra 3: Aproveitar excedente
if geracao_total > consumo_total:
    armazenar_excedente()
3. Previsão com Regressão Linear
Usamos mínimos quadrados para prever energia eólica:

python
# Dados históricos
vento = [8, 10, 12]      # km/h
energia = [20, 25, 30]   # kW

# Equação da reta: energia = 2.5 × vento
previsao = 2.5 * vento_atual

# Exemplo: vento = 11 km/h → previsão ≈ 27.5 kW
4. Análise Energética
Compara geração e consumo para gerar ações:

Situação	Ação do Sistema
Consumo > Geração	⚠️ ALERTA: ativar reserva
Geração > Consumo	💡 SUGESTÃO: armazenar excedente
Geração < 60% do Consumo	🔴 CRÍTICO: desligar não essenciais
📊 Exemplo de Entrada e Saída
ENTRADA (Dados da Colônia)
Parâmetro	Valor
Geração Solar	40 kW
Geração Eólica	30 kW
Geração Total	70 kW
Consumo Suporte Vida	35 kW
Consumo Laboratório	20 kW
Consumo Iluminação	15 kW
Consumo Total	70 kW
Velocidade do Vento	11 km/h
Temperatura Externa	-20°C
SAÍDA (Decisões do Sistema)
text
======================================================================
 SISTEMA INTELIGENTE DA COLÔNIA - INICIANDO ANÁLISE
======================================================================

📊 STATUS OPERACIONAL DA COLÔNIA
----------------------------------------------------------------------

🔋 GERAÇÃO DE ENERGIA:
   • Energia Solar: 40.0 kW
   • Energia Eólica: 30.0 kW
   • TOTAL GERADO: 70.0 kW
   • Reserva Disponível: 20.0 kW

💡 CONSUMO DE ENERGIA:
   • Suporte Vida: 35 kW
   • Laboratorio: 20 kW
   • Iluminacao: 15 kW
   • TOTAL CONSUMIDO: 70 kW

🌦️ CONDIÇÕES CLIMÁTICAS:
   • Vento: 11 km/h
   • Temperatura: -20°C

⚡ ANÁLISE ENERGÉTICA
----------------------------------------------------------------------
✅ SISTEMA EQUILIBRADO: geração = consumo

🚨 NÍVEL DE ALERTA: 🟢 NORMAL

🤖 DECISÕES AUTOMÁTICAS
----------------------------------------------------------------------
✅ Situação confortável: Geração suficiente
✅ Recomendação: Aumentar processamento científico

======================================================================
 SISTEMA ENCERRADO - ANÁLISE COMPLETA
======================================================================
