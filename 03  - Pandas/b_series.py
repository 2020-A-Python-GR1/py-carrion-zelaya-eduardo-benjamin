# -*- coding: utf-8 -*-

# b_series.py

import numpy as np
import pandas as pd

lista_numeros = [1, 2, 3, 4]
tupla_numeros = [1, 2, 3, 4]
np_numeros = np.array((1, 2, 3, 4))

series_a = pd.Series(
    lista_numeros
)

series_b = pd.Series(
    tupla_numeros
)


series_c = pd.Series(
    np_numeros
)
