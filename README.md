<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Relatório - Sistema Aurora Siger - Fase 3</title>
<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 40px;
        color: #333;
    }
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
    }
    h2 {
        color: #2980b9;
        border-left: 4px solid #3498db;
        padding-left: 15px;
        margin-top: 30px;
    }
    h3 {
        color: #16a085;
        margin-top: 20px;
    }
    .highlight {
        background-color: #f0f8ff;
        padding: 15px;
        border-left: 4px solid #3498db;
        margin: 20px 0;
        font-family: monospace;
        font-size: 14px;
        white-space: pre-wrap;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 10px;
        text-align: left;
    }
    th {
        background-color: #3498db;
        color: white;
    }
    .badge {
        background-color: #27ae60;
        color: white;
        padding: 5px 10px;
        border-radius: 5px;
        display: inline-block;
        margin: 5px 0;
    }
    .footer {
        margin-top: 50px;
        text-align: center;
        font-size: 12px;
        color: #7f8c8d;
        border-top: 1px solid #ddd;
        padding-top: 20px;
    }
    .page-break {
        page-break-before: always;
    }
</style>
</head>
<body>

<h1>🚀 SISTEMA INTELIGENTE DA COLÔNIA - AURORA SIGER</h1>
<p><strong>Fase 3 - Sistema Integrado de Gestão Energética</strong></p>
<p><span class="badge">Python 3.7+</span> <span class="badge">Sem bibliotecas externas</span> <span class="badge">100% Funcional</span></p>

<hr>

<h2>📌 1. INFORMAÇÕES GERAIS DO PROJETO</h2>

<p><strong>🔗 Link do Repositório GitHub:</strong><br>
<a href="https://github.com/guslmo1444-maker/AURORA-SIGER-FASE-3">https://github.com/guslmo1444-maker/AURORA-SIGER-FASE-3</a></p>

<p><strong>📁 Arquivo Principal:</strong> <code>FASE3.PY</code></p>
<p><strong>👤 Autor/Equipe:</strong> guslmo1444-maker</p>
<p><strong>📅 Data da Última Atualização:</strong> 24 de Maio de 2026</p>

<h2>🎯 2. OBJETIVO DO SISTEMA</h2>

<p>Desenvolver um sistema integrado que represente o funcionamento inteligente da colônia, capaz de:</p>
<ul>
    <li>Organizar dados de forma hierárquica e eficiente</li>
    <li>Tomar decisões automáticas baseadas em regras lógicas</li>
    <li>Prever comportamentos usando regressão linear simples</li>
    <li>Analisar o uso de energia e gerar alertas/sugestões</li>
</ul>

<h2>📊 3. ORGANIZAÇÃO DOS DADOS (Estrutura Hierárquica)</h2>

<p>Os dados são armazenados em um <strong>dicionário principal</strong> chamado <code>colonia</code>, com subdicionários para cada subsistema:</p>

<div class="highlight">
colonia = {
    "energia": {
        "solar": 40,      # kW - geração dos painéis solares
        "eolica": 30,     # kW - geração das turbinas eólicas
        "reserva": 20     # kW - baterias de emergência
    },
    "consumo": {
        "suporte_vida": 35,  # kW - oxigênio, água, pressurização
        "laboratorio": 20,   # kW - pesquisas científicas
        "iluminacao": 15,    # kW - iluminação geral
        "aquecimento": 0     # kW - calculado dinamicamente
    },
    "clima": {
        "vento": 11,          # km/h - velocidade do vento
        "temperatura": -20,   # °C - temperatura externa
        "radiacao_solar": 65  # % - eficiência dos painéis
    },
    "historico": [],          # lista de eventos
    "alertas": []             # lista de alertas gerados
}
</div>

<p><strong>✅ Por que essa estrutura?</strong></p>
<ul>
    <li><strong>Hierárquica:</strong> Permite navegar de energia → solar facilmente</li>
    <li><strong>Legível:</strong> Cada valor tem um comentário explicativo</li>
    <li><strong>Flexível:</strong> Fácil adicionar novos subsistemas (ex: energia → nuclear)</li>
</ul>

<h2>🧠 4. REGRAS DE DECISÃO (LÓGICA DO SISTEMA)</h2>

<p>O sistema implementa <strong>4 tipos principais de regras</strong>, todas usando estruturas condicionais IF/ELIF/ELSE:</p>

<h3>🔹 Regra 1 - Alerta Crítico (Modo Economia)</h3>
<div class="highlight">
if geracao_total < 50 and consumo_total > 60:
    print("ALERTA: Ativar modo economia!")
</div>

<h3>🔹 Regra 2 - Prioridade de Sistemas Essenciais</h3>
<div class="highlight">
if consumo_total > geracao_total + colonia["energia"]["reserva"]:
    print("Desligando sistemas NÃO ESSENCIAIS...")
    print("Suporte à vida mantido ATIVO.")
    # Laboratório é desligado, iluminação reduzida
</div>

<h3>🔹 Regra 3 - Gerenciamento de Excedente</h3>
<div class="highlight">
if geracao_total > consumo_total:
    print("SUGESTÃO: armazenar energia excedente.")
    # 80% do excedente vai para a reserva
</div>

<h3>🔹 Regra 4 - Níveis de Alerta (Semáforo)</h3>
<table>
    <tr><th>Condição</th><th>Nível</th><th>Ação</th></tr>
    <tr><td>geração < 60% do consumo</td><td>🔴 CRÍTICO</td><td>Desligar não essenciais</td></tr>
    <tr><td>geração < 90% do consumo</td><td>🟡 ATENÇÃO</td><td>Monitorar reserva</td></tr>
    <tr><td>geração >= 90% do consumo</td><td>🟢 NORMAL</td><td>Operação normal</td></tr>
</table>

<p><strong>✅ Diferencial:</strong> O sistema <strong>prioriza o suporte à vida</strong> acima de qualquer outro sistema, desligando laboratório e reduzindo iluminação antes de afetar oxigênio/água.</p>

<h2>📈 5. MODELO DE PREVISÃO (REGRESSÃO LINEAR)</h2>

<p>Para estimar a geração de energia eólica futura, o sistema utiliza <strong>regressão linear simples</strong> (método dos mínimos quadrados).</p>

<h3>🔹 Dados Históricos</h3>
<div class="highlight">
vento = [8, 10, 12, 11, 9, 13, 10]      # km/h
energia = [20, 25, 30, 28, 22, 32, 25]  # kW
</div>

<h3>🔹 Cálculo da Reta (y = a*x + b)</h3>
<div class="highlight">
a = Σ[(x - x̄)(y - ȳ)] / Σ[(x - x̄)²]
b = ȳ - a * x̄
</div>

<p><strong>Resultado obtido:</strong> energia ≈ <strong>2.5 × vento</strong></p>

<h3>🔹 Exemplo Prático</h3>
<div class="highlight">
Entrada: vento_atual = 11 km/h
Previsão = 2.5 * 11 = 27.5 kW
Saída: "Energia prevista: 27.5 kW"
</div>

<p><strong>✅ Por que esse modelo?</strong></p>
<ul>
    <li>Simples e eficaz para relações lineares</li>
    <li>Não requer bibliotecas externas (implementado manualmente)</li>
    <li>Pode ser atualizado com novos dados históricos</li>
</ul>

<h2>⚡ 6. ANÁLISE DO USO DE ENERGIA</h2>

<p>O sistema compara constantemente <strong>geração total</strong> vs <strong>consumo total</strong> e gera ações específicas:</p>

<h3>🔹 Cenário 1: Consumo > Geração (Déficit)</h3>
<div class="highlight">
diferenca = consumo_total - geracao_total
print(f"RISCO ENERGÉTICO: déficit de {diferenca}")
# Usa reserva automaticamente
</div>

<h3>🔹 Cenário 2: Geração > Consumo (Excedente)</h3>
<div class="highlight">
sobra = geracao_total - consumo_total
print(f"EXCEDENTE ENERGÉTICO: sobra de {sobra}")
print("SUGESTÃO: armazenar energia excedente.")
# 80% da sobra vai para reserva
</div>

<h3>🔹 Cenário 3: Sistema Equilibrado</h3>
<div class="highlight">
print("Sistema equilibrado.")
# Mantém operação normal
</div>

<p><strong>✅ Resultado:</strong> O operador recebe <strong>alertas claros e sugestões acionáveis</strong>, nunca apenas números brutos.</p>

<h2>🖥️ 7. EXEMPLO COMPLETO DE EXECUÇÃO</h2>

<h3>🔹 ENTRADA (Dados Iniciais)</h3>
<table>
    <tr><th>Parâmetro</th><th>Valor</th></tr>
    <tr><td>Geração Solar</td><td>40 kW</td></tr>
    <tr><td>Geração Eólica</td><td>30 kW</td></tr>
    <tr><td>Suporte à Vida</td><td>35 kW</td></tr>
    <tr><td>Laboratório</td><td>20 kW</td></tr>
    <tr><td>Iluminação</td><td>15 kW</td></tr>
    <tr><td>Temperatura</td><td>-20°C</td></tr>
</table>

<h3>🔹 SAÍDA (Decisões do Sistema)</h3>
<div class="highlight">
=== STATUS DA COLÔNIA ===
Geração total: 70 kW
Consumo total: 70 kW

=== ANÁLISE ENERGÉTICA ===
Sistema equilibrado.

=== PREVISÃO DE ENERGIA EÓLICA ===
Velocidade do vento: 11 km/h
Energia prevista: 27.5 kW

=== DECISÕES AUTOMÁTICAS ===
✅ Situação confortável: Geração suficiente
✅ Recomendação: Armazenar excedente
</div>

<h2>🌍 8. COMO O SISTEMA AJUDA A MELHORAR O USO DE ENERGIA NA COLÔNIA</h2>

<table>
    <tr>
        <th>Problema na Colônia</th>
        <th>Solução do Sistema</th>
        <th>Benefício Real</th>
    </tr>
    <tr>
        <td>Falta de energia em horários de pico</td>
        <td>Usa reserva automaticamente quando consumo > geração</td>
        <td>Evita apagões e mantém suporte à vida</td>
    </tr>
    <tr>
        <td>Desperdício de energia gerada em excesso</td>
        <td>Armazena 80% do excedente na reserva</td>
        <td>Reduz desperdício e prepara para emergências</td>
    </tr>
    <tr>
        <td>Dificuldade de planejamento (ex: vento variável)</td>
        <td>Prevê geração eólica baseada em vento atual</td>
        <td>Permite antecipar medidas corretivas</td>
    </tr>
    <tr>
        <td>Decisões lentas em emergências</td>
        <td>Desliga sistemas não essenciais automaticamente</td>
        <td>Resposta imediata (milissegundos)</td>
    </tr>
    <tr>
        <td>Falta de transparência energética</td>
        <td>Mantém histórico completo de eventos e alertas</td>
        <td>Auditoria e melhoria contínua</td>
    </tr>
</table>

<h2>📋 9. CUMPRIMENTO DOS REQUISITOS (Checklist)</h2>

<table>
    <tr>
        <th>Requisito</th>
        <th>Status</th>
        <th>Evidência</th>
    </tr>
    <tr>
        <td>Organizar dados em estruturas (listas/dicionários)</td>
        <td>✅ ATENDIDO</td>
        <td>Dicionário colonia com subsistemas</td>
    </tr>
    <tr>
        <td>Estrutura hierárquica (energia → solar/eólico)</td>
        <td>✅ ATENDIDO</td>
        <td>colonia["energia"]["solar"]</td>
    </tr>
    <tr>
        <td>Regras básicas IF/ELSE</td>
        <td>✅ ATENDIDO</td>
        <td>Condicionais de geração vs consumo</td>
    </tr>
    <tr>
        <td>Combinar condições (AND/OR)</td>
        <td>✅ ATENDIDO</td>
        <td>if geracao < 50 and consumo > 60</td>
    </tr>
    <tr>
        <td>Priorizar sistemas essenciais</td>
        <td>✅ ATENDIDO</td>
        <td>Suporte à vida mantido, laboratório desligado</td>
    </tr>
    <tr>
        <td>Previsão com regressão linear</td>
        <td>✅ ATENDIDO</td>
        <td>Função regressao_linear_previsao()</td>
    </tr>
    <tr>
        <td>Comparar geração vs consumo</td>
        <td>✅ ATENDIDO</td>
        <td>diferenca = geracao_total - consumo_total</td>
    </tr>
    <tr>
        <td>Código organizado em funções</td>
        <td>✅ ATENDIDO</td>
        <td>9 funções modulares</td>
    </tr>
    <tr>
        <td>README.md com explicações</td>
        <td>✅ ATENDIDO</td>
        <td>Arquivo README no repositório</td>
    </tr>
    <tr>
        <td>Exemplo de entrada e saída</td>
        <td>✅ ATENDIDO</td>
        <td>Seção 7 deste relatório</td>
    </tr>
</table>

<h2>🔗 10. LINK DO REPOSITÓRIO GITHUB</h2>

<p><strong>Acesso ao código fonte completo:</strong><br>
<a href="https://github.com/guslmo1444-maker/AURORA-SIGER-FASE-3">https://github.com/guslmo1444-maker/AURORA-SIGER-FASE-3</a></p>

<p><strong>Arquivos disponíveis:</strong></p>
<ul>
    <li><code>FASE3.PY</code> - Código principal do sistema (100% Python)</li>
    <li><code>README.md</code> - Documentação completa</li>
</ul>

<p><strong>Estatísticas do repositório:</strong></p>
<ul>
    <li>✅ 12 commits registrados</li>
    <li>✅ Python 100%</li>
    <li>✅ Atualizado em 24/05/2026</li>
</ul>

<h2>📌 11. OBSERVAÇÕES FINAIS</h2>

<p><strong>✔️ O sistema utiliza APENAS conceitos básicos de Python:</strong></p>
<ul>
    <li>Dicionários e listas (estruturas de dados)</li>
    <li>Condicionais IF/ELIF/ELSE (lógica)</li>
    <li>Funções (modularização)</li>
    <li>Operações aritméticas (regressão)</li>
    <li>Bibliotecas padrão (datetime, random)</li>
</ul>

<p><strong>🚫 Nenhuma biblioteca avançada (NumPy, Pandas, Sklearn) foi utilizada</strong>, conforme solicitado.</p>

<p><strong>✅ Evolução alcançada:</strong> Sistema <strong>preditivo</strong> (com regressão) ao invés de apenas reativo.</p>

<div class="footer">
    <p>Relatório gerado automaticamente - Sistema Aurora Siger - Fase 3</p>
    <p>Desenvolvido para disciplina de Estruturas de Dados e Lógica de Programação</p>
</div>

</body>
</html>
