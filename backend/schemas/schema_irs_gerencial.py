import pandas as pd
import pandera as pa
from pandera.typing import Series


class SchemaIRS_Fat_Alta_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando Pandera para as informações extraídas do
    banco de dados referentes à alta de pacientes.

    Attributes:
        alta_gid: Chave única do registro de alta hospitalar.
        boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
        estabelecimento_gid: Chave única do estabelecimento de saúde.
        mal_id: Chave única dos motivos de alta.
        motivo_saida: Motivo pelo qual o paciente recebeu alta.
        alta_administrativa: Data/hora que paciente recebe alta através do sistema TIMed.
        status: Indica se a alta foi efetuada ou cancelada.
    """

    alta_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    estabelecimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    mal_id: Series[int] = pa.Field(nullable=False, coerce=True)
    motivo_saida: Series[str] = pa.Field(nullable=True, coerce=True)
    alta_administrativa: Series[pd.Timestamp] = pa.Field(nullable=True, coerce=True)
    status: Series[str] = pa.Field(nullable=False, coerce=True)


class SchemaIRS_Fat_Atendimento_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando Pandera para as informações extraídas do
    banco de dados referentes ao atendimento do paciente.

    Attributes:
        atendimento_gid: Chave única para identificação de cada atendimento.
        matd_id: Chave única dos tipos de atendimento.
        boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
        estabelecimento_gid: Chave única do estabelecimento de saúde.
        cid_id: Chave única dos diferentes tipos de CID.
        esp_id: Chave única das especialidades.
        data_inicio: Data/hora de início do atendimento.
        data_fim: Data/hora do fim do atendimento.
        fat_paciente_rede_id: Chave única que identifica cada paciente no banco.
        prf_id: Chave única que identifica cada profissional no banco.
    """

    atendimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    matd_id: Series[str] = pa.Field(nullable=False, coerce=True)
    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    estabelecimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    cid_id: Series[int] = pa.Field(nullable=False, coerce=True)
    esp_id: Series[int] = pa.Field(nullable=False, coerce=True)
    data_inicio: Series[pd.Timestamp] = pa.Field(nullable=False, coerce=True)
    data_fim: Series[pd.Timestamp] = pa.Field(nullable=False, coerce=True)
    fat_paciente_rede_id: Series[int] = pa.Field(nullable=False, coerce=True)
    prf_id: Series[int] = pa.Field(nullable=False, coerce=True)


class SchemaIRS_Fat_Boletim_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando a biblioteca Pandera
    para as informações extraídas do banco de dados referentes ao boletim de
    atendimento médico do paciente.

    Attributes:
       boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
       tpa_id: Chave única do tipo de atendimento médico.
       estabelecimento_gid: Chave única do estabelecimento de saúde.
       data_entrada: Data/hora de entrada do paciente na unidade de saúde.
       data_internacao: Data/hora do início da internação.
       tpu_id: Chave única do tipo de Unidade.
       tpe_id: Chave única do tipo de Registro.
       interno: Identificador se o paciente é interno ou externo.
       esp_id: Chave única do tipo de especialidade médica.
    """

    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    tpa_id: Series[int] = pa.Field(nullable=False, coerce=True)
    estabelecimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    data_entrada: Series[pd.Timestamp] = pa.Field(nullable=False, coerce=True)
    data_internacao: Series[pd.Timestamp] = pa.Field(nullable=False, coerce=True)
    tpu_id: Series[int] = pa.Field(nullable=False, coerce=True)
    tpe_id: Series[int] = pa.Field(nullable=False, coerce=True)
    interno: Series[int] = pa.Field(nullable=False, coerce=True)
    esp_id: Series[int] = pa.Field(nullable=False, coerce=True)


class SchemaIRS_Fat_Censo_Ativo_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando a biblioteca Pandera para as informações
    extraídas do banco de dados relacionadas às internações em tempo real.

    Attributes:
        leito_gid: Chave única do leito.
        estabelecimento_gid: Chave única do estabelecimento de saúde.
        boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
        fat_paciente_rede_id: Chave única que identifica cada paciente no banco.
        leito_extra: Indica se o leito referenciado é extra ou não.
        leito_estado: Indica ocupação do leito.
        leito_nome: Descreve o nome do leito.
        motivo_atendimento_nome: Indicador de motivação para atendimento.
        esp_id: Chave única de especialidade médica.
    """

    leito_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    estabelecimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    fat_paciente_rede_id: Series[int] = pa.Field(nullable=False, coerce=True)
    leito_extra: Series[pd.CategoricalDtype] = pa.Field(
        pd.CategoricalDtype(categories=["S", "N"], ordered=False),
        nullable=True,
        coerce=True,
    )
    leito_estado: Series[str] = pa.Field(str, nullable=True, coerce=True)
    leito_nome: Series[str] = pa.Field(str, nullable=True, coerce=True)
    motivo_atendimento_nome: Series[str] = pa.Field(str, nullable=True, coerce=True)
    esp_id: Series[int] = pa.Field(int, nullable=True, coerce=True)


class SchemaIRS_Fat_Descritor_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando a biblioteca Pandera para as informações
    extraídas do banco de dados relacionadas à descrição da
    classificação de risco do paciente.

    Attributes:
        boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
        risco: Identificador de classificação de risco.
        descritor: Descrição de risco.
    """

    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    risco: Series[str] = pa.Field(str, nullable=False, coerce=True)
    descritor: Series[str] = pa.Field(nullable=False, coerce=True)


class SchemaIRS_Fat_Diagnostico_Publico(pa.DataFrameModel):
    """
    Esquema de validação de dados utilizando a biblioteca Pandera para as informações
    extraídas do banco de dados relacionadas ao diagnóstico do paciente.

    Attributes:
        diagnostico_gid: Chave única do Diagnóstico.
        boletim_gid: Chave única do Boletim de Atendimento Médico (BAM).
        cid_id: Chave que enumera os diferentes tipos de CID.
        estabelecimento_gid: Chave única do estabelecimento de saúde.
        data_diagnostico: Data/hora do diagnóstico.
        tpd_id: Chave única dos tipos de diagnósticos.
    """

    diagnostico_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    boletim_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    cid_id: Series[int] = pa.Field(nullable=False, coerce=True)
    estabelecimento_gid: Series[str] = pa.Field(str, nullable=False, coerce=True)
    data_diagnosticco: Series[pd.Timestamp] = pa.Field(nullable=False, coerce=True)
    tdp_id: Series[int] = pa.Field(nullable=False, coerce=True)
