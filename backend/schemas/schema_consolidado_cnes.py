import pandas as pd
import pandera as pa
from pandera.typing import Series


class SchemaDGP_CNES_Input(pa.DataFrameModel):
    """
    Modelos de esquema do Pandera para validação de dados
    do final da pipeline de dados da DGP-CNES
    que será responsável por alimentar a base de dados.

    Attributes:
        MATRICULA: Matrícula do funcionário, identificador único.
        PREFIXO: Prefixo associado ao cargo do funcionário.
        NOME: Nome completo do funcionário, campo obrigatório.
        CPF: Cadastro de Pessoa Física, identificador único e obrigatório.
        EXERCICIO: Data do exercício, pode ser nula.
        CARGOPROV: Cargo do funcionário, pode ser nulo.
        JORNADA: Tipo de jornada de trabalho, pode ser nulo.
        DTINICIO: Data de início do vínculo, pode ser nula.
        DTFIM: Data de fim do vínculo, pode ser nula.
        SETOR: Código do setor, pode ser nulo.
        NOMESETOR: Nome do setor, pode ser nulo.
        SIGLA: Sigla do setor, pode ser nulo.
        REGIME: Regime de trabalho do funcionário, pode ser nulo.
        TIPO_VINCULO: Tipo de vínculo do funcionário, pode ser nulo.
        sigla_unidade: Sigla da unidade onde o funcionário está alocado, pode ser nula.
        DESCRICAO_AFAST: Descrição do afastamento, se aplicável, pode ser nula.
        DATA_INICIO_AFAST: Data de início do afastamento, pode ser nula.
        DATA_FIM_AFAST: Data de fim do afastamento, pode ser nula.
        tempo_afastamento: Duração do afastamento em dias,
        pode ser um número decimal e nulo.
        status: Status atual do funcionário, pode ser nulo.
        _merge: Indica a origem dos dados.
        situacao: Situação atual do funcionário, campo obrigatório.
        data_atualizacao: Data da atualização dos dados, campo obrigatório.
        CENTRO_DE_CUSTO: Centro de custo associado ao funcionário, pode ser nulo.
        ERGON: Valor associado ao sistema ERGON, pode ser nulo.
    """

    MATRICULA: Series[pa.String] = pa.Field(nullable=True)
    PREFIXO: Series[float] = pa.Field(nullable=True, coerce=True)
    NOME: Series[pa.String] = pa.Field(nullable=False)
    CPF: Series[int] = pa.Field(nullable=False)
    EXERCICIO: Series[pa.DateTime] = pa.Field(nullable=True)
    CARGOPROV: Series[pa.String] = pa.Field(nullable=True)
    JORNADA: Series[pa.String] = pa.Field(nullable=True)
    DTINICIO: Series[pa.DateTime] = pa.Field(nullable=True)
    DTFIM: Series[pa.DateTime] = pa.Field(nullable=True)
    SETOR: Series[float] = pa.Field(nullable=True)
    NOMESETOR: Series[pa.String] = pa.Field(nullable=True)
    SIGLA: Series[pa.String] = pa.Field(nullable=True)
    REGIME: Series[pa.String] = pa.Field(nullable=True)
    TIPO_VINCULO: Series[pa.String] = pa.Field(nullable=True)
    sigla_unidade: Series[pa.String] = pa.Field(nullable=True)
    DESCRICAO_AFAST: Series[pa.String] = pa.Field(nullable=True)
    DATA_INICIO_AFAST: Series[pa.DateTime] = pa.Field(nullable=True)
    DATA_FIM_AFAST: Series[pa.DateTime] = pa.Field(nullable=True)
    tempo_afastamento: Series[float] = pa.Field(nullable=True)
    status: Series[pa.String] = pa.Field(nullable=True)
    _merge: Series[pa.String] = pa.Field(
        isin=["left_only", "right_only", "both"], nullable=False, coerce=True
    )
    situacao: Series[pa.String] = pa.Field(nullable=False)
    data_atualizacao: Series[pa.String] = pa.Field(nullable=False)
    CENTRO_DE_CUSTO: Series[pa.String] = pa.Field(nullable=True)
    ERGON: Series[float] = pa.Field(nullable=True)

    class Config:
        """
        Configuração do Schema.
        """

        coerce = True
        strict = True
        ordered = True
        unique = None
        unique_column_names = True
        add_missing_columns = False


class SchemaDGP_CNES_Output(pa.DataFrameModel):
    """
    Modelos de esquema do Pandera para validação de dados
    do final da pipeline de dados da DGP-CNES
    que será responsável por alimentar a base de dados.

    Attributes:
        matricula: Matrícula do funcionário.
        prefixo: Prefixo associado ao cargo do funcionário.
        nome: Nome completo do funcionário.
        cpf: Cadastro de Pessoa Física.
        exercicio: Data de admissão do funcionário.
        cargoprov: Cargo do funcionário.
        jornada: Tipo de jornada de trabalho.
        dtinicio: Data de início da função dentro da unidade.
        dtfim: Data de fim do vínculo.
        setor: Código do setor.
        nomesetor: Nome do setor.
        sigla: Sigla do setor (padrão do Sistema ERGON).
        regime: Regime de trabalho do funcionário.
        tipo_vinculo: Tipo de vínculo do funcionário.
        sigla_unidade: Sigla da unidade (padrão da equipe de BI).
        descricao_afast: Descrição do afastamento.
        data_inicio_afast: Data de início do afastamento.
        data_fim_afast: Data de fim do afastamento.
        tempo_afastamento: Duração do afastamento em dias.
        status: Status referente a metrícula do funcionário.
        origem: Indica a origem dos dados.
        situacao: Campo que descreve o que deve ser feito com a matrícula do funcionário.
        data_atualizacao: Data da atualização dos dados.
        centro_de_custo: Centro de custo associado a unidade (padrão da DGP).
        ergon: Código referente ao setor do sistema ERGON (padrão da DGP).
        parametrizado_cnes: Indica se houve comparação com a base do CNES.
        periodo_vigencia: Período de vigência do dado.
        servidor: Indica se o funcionário é terceirizado ou não.
    """

    matricula: Series[pa.String] = pa.Field(nullable=True)
    prefixo: Series[pd.Int64Dtype] = pa.Field(nullable=True, coerce=True)
    nome: Series[pa.String] = pa.Field(nullable=False)
    cpf: Series[pa.String] = pa.Field(nullable=False)
    exercicio: Series[pa.DateTime] = pa.Field(nullable=True)
    cargoprov: Series[pa.String] = pa.Field(nullable=True)
    jornada: Series[pa.String] = pa.Field(nullable=True)
    dtinicio: Series[pa.DateTime] = pa.Field(nullable=True)
    dtfim: Series[pa.DateTime] = pa.Field(nullable=True)
    setor: Series[pa.String] = pa.Field(nullable=True)
    nomesetor: Series[pa.String] = pa.Field(nullable=True)
    sigla: Series[pa.String] = pa.Field(nullable=True)
    regime: Series[pa.String] = pa.Field(nullable=True)
    tipo_vinculo: Series[pa.String] = pa.Field(nullable=True)
    sigla_unidade: Series[pa.String] = pa.Field(nullable=True)
    descricao_afast: Series[pa.String] = pa.Field(nullable=True)
    data_inicio_afast: Series[pa.DateTime] = pa.Field(nullable=True)
    data_fim_afast: Series[pa.DateTime] = pa.Field(nullable=True)
    tempo_afastamento: Series[pd.Int64Dtype] = pa.Field(nullable=True)
    status: Series[pa.String] = pa.Field(nullable=True)
    origem: Series[pa.String] = pa.Field(
        isin=["ergon", "cnes", "ergon_cnes"], nullable=False, coerce=True
    )
    situacao: Series[pa.String] = pa.Field(nullable=False)
    data_atualizacao: Series[pa.String] = pa.Field(nullable=False)
    centro_de_custo: Series[pa.String] = pa.Field(nullable=True)
    ergon: Series[pa.String] = pa.Field(nullable=True)
    parametrizado_cnes: Series[pa.String] = pa.Field(nullable=True)
    periodo_vigencia: Series[pa.String] = pa.Field(nullable=True)
    servidor: Series[pa.String] = pa.Field(nullable=True)

    class Config:
        """
        Configuração do Schema.
        """

        coerce = True
        strict = True
        ordered = True
        unique = None
        unique_column_names = True
        add_missing_columns = False
