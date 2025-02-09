# Versionamento

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
