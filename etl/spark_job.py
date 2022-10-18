from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = (
    SparkSession.builder
    .appName("AWS Datalake")
    .getOrCreate()
)

rais = (
    spark.read.format("csv")
    .option("inferSchema", True)
    .option("header", True)
    .option("delimiter", ";")
    .load('s3://datalake-edc-bt/raw-data/rais')
)

# rais_modified = (
#     rais
#     .withColumnRenamed('Bairros SP', 'bairros_sp')
#     .withColumnRenamed('Bairros Fortaleza', 'bairros_fortaleza')
#     .withColumnRenamed('Bairros RJ', 'bairros_rj')
#     .withColumnRenamed('Causa Afastamento 1', 'causa_afastamento_1')
#     .withColumnRenamed('Causa Afastamento 2', 'causa_afastamento_2')
#     .withColumnRenamed('Causa Afastamento 3', 'causa_afastamento_3')
#     .withColumnRenamed('Motivo Desligamento', 'motivo_desligamento')
#     .withColumnRenamed(rais.columns[7], 'cbo_ocupacao_2002')
#     .withColumnRenamed('CNAE 2.0 Classe', 'cnae_2_0_classe')
#     .withColumnRenamed('CNAE 95 Classe', 'cnae_95_classe')
#     .withColumnRenamed('Distritos SP', 'distritos_sp')
#     .withColumnRenamed(rais.columns[11], 'vinculo_ativo_31_12')
#     .withColumnRenamed(rais.columns[12], 'faixa_etaria')
#     .withColumnRenamed('Faixa Hora Contrat', 'faixa_hora_contrat')
#     .withColumnRenamed('Faixa Remun Dezem (SM)', 'faixa_remun_dezem_sm')
#     .withColumnRenamed(rais.columns[15], 'faixa_remun_media_sm')
#     .withColumnRenamed('Faixa Tempo Emprego', 'faixa_tempo_emprego')
#     .withColumnRenamed(rais.columns[17], 'escolaridade_apos_2005')
#     .withColumnRenamed('Qtd Hora Contr', 'qtd_hora_contr')
#     .withColumnRenamed('Idade', 'idade')
#     .withColumnRenamed('Ind CEI Vinculado', 'ind_cei_vinculado')
#     .withColumnRenamed('Ind Simples', 'ind_simples')
#     .withColumnRenamed(rais.columns[22], 'mes_admissao')
#     .withColumnRenamed(rais.columns[23], 'mes_desligamento')
#     .withColumnRenamed('Mun Trab', 'mun_trab')
#     .withColumnRenamed(rais.columns[25], 'municipio')
#     .withColumnRenamed('Nacionalidade', 'nacionalidade')
#     .withColumnRenamed(rais.columns[27], 'natureza_juridica')
#     .withColumnRenamed('Ind Portador Defic', 'ind_portador_defic')
#     .withColumnRenamed('Qtd Dias Afastamento', 'qtd_dias_afastamento')
#     .withColumnRenamed(rais.columns[30], 'raca_cor')
#     .withColumnRenamed(rais.columns[31], 'regioes_adm_df')
#     .withColumnRenamed('Vl Remun Dezembro Nom', 'vl_remun_dezembro_nom')
#     .withColumnRenamed('Vl Remun Dezembro (SM)', 'vl_remun_dezembro_sm')
#     .withColumnRenamed(rais.columns[34], 'vl_remun_media_nom')
#     .withColumnRenamed(rais.columns[35], 'vl_remun_media_sm')
#     .withColumnRenamed('CNAE 2.0 Subclasse', 'cnae_2_0_subclasse')
#     .withColumnRenamed('Sexo Trabalhador', 'sexo_trabalhador')
#     .withColumnRenamed('Tamanho Estabelecimento', 'tamanho_estabelecimento')
#     .withColumnRenamed('Tempo Emprego', 'tempo_emprego')
#     .withColumnRenamed(rais.columns[40], 'tipo_admissao')
#     .withColumnRenamed('Tipo Estab41', 'tipo_estab41')
#     .withColumnRenamed('Tipo Estab42', 'tipo_estab42')
#     .withColumnRenamed('Tipo Defic', 'tipo_defic')
#     .withColumnRenamed(rais.columns[44], 'tipo_vinculo')
#     .withColumnRenamed('IBGE Subsetor', 'ibge_subsetor')
#     .withColumnRenamed('Vl Rem Janeiro SC', 'vl_rem_janeiro_sc')
#     .withColumnRenamed('Vl Rem Fevereiro SC', 'vl_rem_fevereiro_sc')
#     .withColumnRenamed(rais.columns[48], 'vl_rem_marco_sc')
#     .withColumnRenamed('Vl Rem Abril SC', 'vl_rem_abril_sc')
#     .withColumnRenamed('Vl Rem Maio SC', 'vl_rem_maio_sc')
#     .withColumnRenamed('Vl Rem Junho SC', 'vl_rem_junho_sc')
#     .withColumnRenamed('Vl Rem Julho SC', 'vl_rem_julho_sc')
#     .withColumnRenamed('Vl Rem Agosto SC', 'vl_rem_agosto_sc')
#     .withColumnRenamed('Vl Rem Setembro SC', 'vl_rem_setembro_sc')
#     .withColumnRenamed('Vl Rem Outubro SC', 'vl_rem_outubro_sc')
#     .withColumnRenamed('Vl Rem Novembro SC', 'vl_rem_novembro_sc')
#     .withColumnRenamed('Ano Chegada Brasil', 'ano_chegada_brasil')
#     .withColumnRenamed('Ind Trab Intermitente', 'ind_trab_intermitente')
#     .withColumnRenamed('Ind Trab Parcial', 'ind_trab_parcial')
#     .withColumn('uf', 
#     col('municipio')
#     .cast('string')
#     .substr(1,2)
#     .cast('int'))
# )

(
    rais
    .write
    .mode("overwrite")
    .format("parquet")
    .save("s3://datalake-edc-bt/staging-zone/rais")
)
