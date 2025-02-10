import pandas as pd
import pandera as pa
from pandera.typing import Series


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
