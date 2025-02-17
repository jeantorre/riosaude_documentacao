# Versionamento

- Versão v0.1.5 - 12/02/2025
    - Adicionado o site do Núcleo de Inteligência de Dados & Negócios na capa.
    - Novos Drills Adicionados:
        - Produtividade Profissional - Atendimento
            - Exibe o total de atendimentos de todos os profissionais, permitindo filtro por nome ou tipo de unidade, com separação entre "mês atual" e "meses anteriores".
        - Produtividade Profissional - Procedimento
            - Apresenta o total de exames realizados por todos os profissionais, com filtros por nome ou tipo de unidade, também segmentado em "mês atual" e "meses anteriores".
        - Produtividade Exames - Profissional
            - Lista todos os procedimentos realizados pelo profissional selecionado.
    - Novo Botão "Visualizar Percentuais": Adicionado na opção "Ver Detalhes" do Atendimento, exibe as taxas de pacientes classificados, redirecionados e atendidos em relação ao total de registros.
    - Check-Up da Unidade: Criado um filtro para especialidade e período.  

- Versão v0.1.4 - 22/01/2025
    - Adicionada a View 'tb_ultima_atualizacao' que mostra a data das últimas atualizações das principais tabelas utilizadas nessa aplicação.

- Versão v0.1.3 - 23/12/2024
    - Adicionada métricas referentes as Estatística do Censo de acordo com a query enviada pela Vitai para garantir que os resultados mostrados nos paineis sejam os mesmos que são extraídos do PEP.

    Query Vitai | DAX Power BI
    -|-
    leito_instalado | Quant Leitos Oficiais Ocupados Diário
    leito_extra | Quant Leitos Extras Ocupados Diário
    leito_dia | Quant Leitos Ocupados Diário
    paciente_dia | Quant Pacientes Admitidos Diário
    leito_livre | Quant Leitos Livres
    media_paciente_dia | Quant Média Paciente Dia
    internado | Quant Admissão Censo
    transferencia_entrada | Quant Transferência Censo
    alta | Quant Alta Censo
    obito | Quant Obito Censo
    obito_maior_24 | Quant Óbito Maior 24h Censo
    obito_menor_24 | Quant Óbito Menor 24h Censo
    transferencia_saida | Quant Transferência Saida Censo
    transf_externa | Quant Transferência Externa Censo
    saida_unidade_operacional | Quant Saida Operacional Censo
    entrada_unidade_operacional | Quant Entrada Operacional Censo

- Versão v0.1.2 - 25/10/2024
    - Adicionada métricas referentes aos indicares, que serão utilizadas tanto nos indicadores da SUBHUE quanto nos do Contrato de Gestão.  
    Atualmente serão encontrados os valores :  
        - Admissão Sala Amarela Adulto
        - Admissão Sala Amarela Pediátrica
        - Admissão Sala Vermelha Adulto
        - Admissão Sala Vermelha Pediátrica
        - Permanência Sala Amarela por até 24h
        - Permanência Sala Amarela entre 1 e 5 dias
        - Permanência Sala Amarela por mais de 5 dias
        - Permanência Sala Vermelha por até 24h
        - Permanência Sala Vermelha entre 1 e 5 dias
        - Permanência Sala Vermelha por mais de 5 dias
        - Quantidade de Pacientes com CID I21 (IAM)
        - Quantidade de Pacientes com CID I64 (AVE)
        - Quantidade de Pacientes com CID A419 (Sepse)
        - Quantidade de Pacientes com CID I64 (AVE) que foi solicitado Tomografia
        - Divisão de Pacientes com CID I64 (AVE) que foi solicitado Tomografia por Pacientes com CID I64 (AVE)
    - Adicionada a coluna de 'meta' na fat_boletim_consolidado.
    - Contabilizado a quantidade de pacientes de risco azul que foram redirecionados
    - Alterado a formula de calcular o tempo de óbito do paciente na unidade para:
        - data_obito - data_internacao
    - Adicionada métrica [Quant Exame Realizado por BAM]
    - Adicionada métrica [Quant Exame Prescrito e Cancelado]
        - Com isso foi retirado o status 'Cancelado' da métrica [Quant Exame Não Realizado]
    - Adicionada métrica [Quant Admissão após Atendimento]
    - Estava ocorrendo um erro na fórmula de métricas para mês atual, identificado como "M 0", e mês anterior, identificado como "M -1". Como estão sendo utilizados apenas dias completos no primeiro dia do mês a fórmula apresentou erro. Todas as fórmulas de "M 0" e "M -1" serão adaptadas.
    - Adicionada todos os cálculos de estatística de internação baseados na *query* enviada pelo Mussi - desenvolvedor da aplicação. Dessa forma garantimos que as informações do PEP e do painel sejam iguais.
    - Para cáluclo de produtividade dos exames laboratoriais, foi utilizado como referência no Power BI (`USERELATIONSHIP`) a coluna que contém a data de realização do exame (`fat_exame_item`).
    - Para cáluclo de período de óbito, foi utilizado como referência no Power BI (`USERELATIONSHIP`) a coluna que contém a data de óbito `fat_alta`.

- Versão v0.1.1 - 09/10/2024
    - O tempo de internação é calculado pela tabela fat_boletim, anteriormente calculado pela tabela fat_internacao.
    - Retirada as ‘tipo_internacao’ da tabela ‘fat_internacao’, visto que conceitualmente não deve-se fazer a divisão de observação ou internação pelo tempo que o paciente fica hospedado e sim pelo leito que ele se encontra.
    - Adicionadas as tabelas
        - fat_historico_leito
            - Na tabela fat_historico_leito foi utilizada a coluna 'hil_data' para pegar os dados consolidados. Com isso são mostrados todas as movimentações do ano 2024.
        - dim_leito
        - dim_tipo_movimentacao_leito
        - dim_tipo_leito
        - fat_censo_ativo
    - A tabela fat_censo_ativo está sendo utilizada apenas para saber quais leitos estão ativos no momento
    - Adicionado métricas referentes as admissões:
        - tx de ocupação
        - tx de uso de leito extra/dia
        - quant admissões
        - quant saída
    - Adiciona métricas referente aos óbitos:
        - tx. mortalidade
        - tx. mortalidade institucional
    - Atualização na forma que se calcula o TME 1º atendimento. Não foram mapeados os pacientes que foram atendidos antes de uma internação e atualmente eles são contabilizados.
    - Adicionado as colunas com os tempos de espera do último atendimento até a internação (fat_tempos) e também do registro até a internação (fat_boletim)

- Versão inicial - v0.1.0 - 08/10/2024
    - Cálculo de métricas referente aos atendimentos:
        - Quantidade de registros
        - Quantidade de classificados
        - Quantidade de atendimentos
        - Quantidade de reavaliados
        - Quantidade de exames prescritos
        - Quantidade de exames realizados
        - Quantidade de admitidos
        - Quantidade de mortalidade
    - Cálculos de métricas referentes a todos os tempos percorridos pelos pacientes dentro de um fluxo de atendimento dentro de uma unidade  

    **Todas as métricas possuem período de comparação MoM**
