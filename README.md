# AURORA-SIGER-FASE-3
# Sistema Inteligente da Colônia em Marte

> Sistema autônomo para gerenciamento energético de colônias espaciais, capaz de tomar decisões inteligentes em tempo real.

## 📋 Índice

- Sobre o Projeto
- Funcionalidades
- Como Funciona
- Exemplo de Uso
- Estrutura do Código
- Como Executar
- Tecnologias Utilizadas
- Contribuição
- Equipe

---

## Sobre o Projeto

Este sistema foi desenvolvido para **gerenciar de forma inteligente** a energia de uma colônia em Marte. Ele monitora consumo, geração e condições climáticas, tomando **decisões automáticas** para evitar crises energéticas e otimizar o uso dos recursos disponíveis.

### Problema que resolve
Em uma colônia espacial, a energia é um recurso crítico. Falhas no gerenciamento podem levar a:
- ❌ Desligamento de sistemas de suporte à vida
- ❌ Perda de pesquisas científicas
- ❌ Risco à vida dos colonos

### Nossa solução
- ✅ Monitoramento contínuo em tempo real
- ✅ Decisões automáticas baseadas em regras inteligentes
- ✅ Previsão de geração usando dados históricos
- ✅ Priorização automática de sistemas essenciais

---

## ⚡ Funcionalidades

| Funcionalidade | Descrição |
|----------------|-----------|
| 📊 **Organização Hierárquica** | Dados estruturados em dicionários com subsistemas (solar/eólico/suporte_vida) |
| 🧠 **Tomada de Decisão** | Regras IF/ELSE que priorizam suporte à vida sobre sistemas não essenciais |
| 📈 **Previsão por Regressão** | Estima geração eólica baseada em velocidade do vento usando mínimos quadrados |
| 🔋 **Gestão de Reserva** | Armazena excedente e usa reserva automaticamente em déficit |
| 🚨 **Sistema de Alertas** | Níveis VERDE/AMARELO/VERMELHO baseados na situação energética |
| 📝 **Histórico de Eventos** | Registra todas as ações e decisões para auditoria |
| 🌡️ **Adaptação Climática** | Ajusta aquecimento automaticamente baseado na temperatura externa |

---

## 🔧 Como Funciona

### 1. Organização dos Dados

Os dados são organizados em um **dicionário hierárquico** para fácil navegação:

```python
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
📊 Exemplo de Uso
Entrada (Dados da Colônia)
python
Geração Solar: 40 kW
Geração Eólica: 30 kW
Geração Total: 70 kW

Consumo Suporte Vida: 35 kW
Consumo Laboratório: 20 kW
Consumo Iluminação: 15 kW
Consumo Total: 70 kW

Velocidade do Vento: 11 km/h
Temperatura Externa: -20°C
Saída (Decisões do Sistema)
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
   • Aquecimento: 18 kW
   • TOTAL CONSUMIDO: 88 kW

🌦️ CONDIÇÕES CLIMÁTICAS:
   • Vento: 11 km/h
   • Temperatura: -20°C

⚡ ANÁLISE ENERGÉTICA
----------------------------------------------------------------------
⚠️ DÉFICIT ENERGÉTICO: falta de 18.0 kW

🚨 NÍVEL DE ALERTA: 🔴 CRÍTICO

🔋 GERENCIAMENTO DA RESERVA:
   → Usado 18.0 kW da reserva. Reserva restante: 2.0 kW

🤖 DECISÕES AUTOMÁTICAS
----------------------------------------------------------------------
⚠️ CRISE ENERGÉTICA DETECTADA!
   → Desligando sistemas NÃO ESSENCIAIS:
   • Laboratório de pesquisas (20 kW)
   • Iluminação reduzida (15 kW → 5 kW)
   → Novo consumo total: 68 kW
   ✅ Crise controlada!

======================================================================
 SISTEMA ENCERRADO - ANÁLISE COMPLETA
======================================================================
📁 Estrutura do Código
text
sistema-colonia-marte/
│
├── colonia_marte.py          # Código principal do sistema
│   ├── Dicionários (dados)   # Organização hierárquica
│   ├── Funções               # Regras de decisão e cálculos
│   ├── Regressão Linear      # Previsão de energia eólica
│   └── Sistema de Alertas    # Níveis e históricos
│
├── README.md                  # Documentação (este arquivo)
│
└── relatorio.pdf              # Relatório detalhado do projeto
Funções Implementadas
Função	Responsabilidade
calcular_aquecimento()	Define necessidade de aquecimento baseado na temperatura
regressao_linear_previsao()	Calcula coeficientes da reta usando mínimos quadrados
gerenciar_reserva()	Usa ou armazena energia da reserva automaticamente
determinar_nivel_alerta()	Classifica situação como VERDE/AMARELO/VERMELHO
registrar_evento()	Mantém histórico de todas as ações
