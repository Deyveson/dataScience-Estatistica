import pandas as pd
import numpy
import seaborn
import scipy

dados = pd.read_csv('dados.csv')

# print(sorted(dados['Anos de Estudo'].unique()))
#
#
# classes = [dados.Altura.min(), 1.65, 1.75, dados.Altura.max()]
# labels = ['1 - Baixa', '2 - Média', '3 - Alta']
#
# frequencia = pd.value_counts(
#     pd.cut(
#         x = dados.Altura,
#         bins = classes,
#         labels = labels,
#         include_lowest = True
#     )
# )
#
# percentual = pd.value_counts(
#     pd.cut(
#         x = dados.Altura,
#         bins = classes,
#         labels = labels,
#         include_lowest = True
#     ), normalize = True
# ) * 100
#
# dist_freq_altura = pd.DataFrame(
#     {'Frequência': frequencia, 'Porcentagem (%)': percentual}
# )
#
# dist_freq_altura.rename_axis('Estaturas', axis= 'columns', inplace = True)
#
# dist_freq_altura.sort_index(ascending = True, inplace = True)
#
# print(dist_freq_altura)

dataset = pd.DataFrame({
    'Sexo': ['H', 'M', 'M', 'M', 'M', 'H', 'H', 'H', 'M', 'M'],
    'Idade': [53, 72, 54, 27, 30, 40, 58, 32, 44, 51]
})

# print(dataset['Idade'].mean())

print(dataset.groupby('Sexo').mean().loc['H'])

