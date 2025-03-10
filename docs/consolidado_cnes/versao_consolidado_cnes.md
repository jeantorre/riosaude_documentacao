# Versionamento

- Versão v0.1.3 - 10/03/2025
    - Adicionada a coluna 'estabelecimento_gid' que parametriza todas as unidades de gestão parcial e plena.
    - Allterada as informações da coluna 'parametrizado_cnes'. Anteriormente os valores eram 'sim' ou 'nao' e atualmente serão 'GESTÃO PLENA' e 'GESTÃO PARCIAL'.  

    Essas alterações se dão porque foram adicionado os dados do CNES provenientes da gestão parcial e agora todas as unidades de RH do RioSaúde terão acesso a um *dashboard* para acompanhamento de quantos profissionais estão na folha de pagamento da RioSaúde *versus* profissionais cadastrados no CNES.

- Versão v0.1.2 - 03/02/2025
    - Adicionada as colunas 'periodo_vigencia' e 'servidor' nas tabelas. Essas são responsáveis por:
        - 'periodo_vigencia': período de vigência do profissional.
        - 'servidor': indica se o profissional é servidor RIOSAUDE, TERCEIRIZADO ou CEDIDO.  

    Com a nova parametrização de servidores, a regra de negócio para saber se sua matrícula está correta também foi alterada, pois servidores terceirizados ou cedidos não aparecem na lista do ERGON e necessariamente precisam aparecer na base do CNES.  

- Versão v0.1.1 - 27/12/2024
    - Adição da coluna "parametrizado_cnes", que indica se houve comparação com a base do CNES proveniente do setor de Controle e Avaliação (Qualidade em TI).
    - Parametrização da unidade:
        - Sede

- Versão Inicial - v0.1.0 - 23/12/2024
    - Parametrização das unidades:
        - CER Barra da Tijuca
        - CER Campo Grande
        - Hospital Municipal Rocha Faria
        - Hospital Municipal Ronaldo Gazolla
        - Maternidade Rocinha
        - UPA Costa Barros
        - UPA Cidade de Deus
        - UPA Del Castilho
        - UPA Engenho de Dentro
        - UPA João XXIII
        - UPA Magalhães Bastos
        - UPA Madureira
        - UPA Paciência
        - UPA Rocha Miranda
        - UPA Senador Camará
        - UPA Sepetiba
        - UPA Vila Kennedy
    - Comparação entre os dados do CNES, proveniente do setor de Controle e Avaliação, com os dados do sistema ERGON (lista de colaboradores e lista de afastados), fornecido pela DGP da RioSaúde.
