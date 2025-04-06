#!/usr/bin/env python
"""
--------------------------------
project: code
created: 11/04/2018 18:15
---------------------------------

"""

import sys
import os

"""Añade el directorio 'code' al sys.path. El sys.path es una lista de cadenas que especifica
 los directorios donde Python buscará los módulos cuando se encuentra una instrucción import."""
sys.path.append("/Users/camilonunez/Desktop/Internship-2025/reinforcement_learning_an_introduction/code")

import constants as c
import plotting

import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

###Debug, borrar
print(f"Contenido del módulo constants (c): {dir(c)}")


# Make the charts asked for in the thing
# also make some charts of how the values converge as the real ones move
# but for this you'll need the samples!


def load_file(name):
#Utiliza la función read_pickle de la biblioteca pandas para cargar un objeto
#(presumiblemente un DataFrame) desde el archivo especificado.
    return pd.read_pickle(
#Construye la ruta completa al archivo que se va a cargar. Asume que hay una 
#variable paths dentro del módulo constants (al que accedemos como c), que tiene
#un atributo output que representa el directorio de salida principal. Luego, une
#ese directorio con el subdirectorio 'ex_2_5' y el name del archivo.
            os.path.join(c.paths.output, 'ex_2_5', name),
#Después de cargar el DataFrame, esta parte renombra las columnas del DataFrame
#convirtiéndolas a tipo entero (int)
    ).rename(columns=int)

#Esta es una construcción estándar en Python que asegura que el código dentro de
# este bloque solo se ejecute cuando el script analysis.py se ejecuta directamente
# (no cuando se importa como un módulo en otro script).
if __name__ == '__main__':
    epsilon = 0.1
    estimator_type = 'ExponentialRecencyWeightedEstimator'.lower()

    all_exponential_choices = load_file(
            r'choices_{}_eps{}.pkl'.format(
                    'ExponentialRecencyWeightedEstimator'.lower(),
                    epsilon
            )
    )

    all_average_choices = load_file(
            r'choices_{}_eps{}.pkl'.format('sampleaverageestimator', epsilon)
    )

    all_optimal = load_file(r'optimal.pkl')

    perc_average_optimal = all_average_choices.eq(all_optimal).expanding().mean()
    perc_exponential_optimal = all_exponential_choices.eq(all_optimal).expanding().mean()

    with plt.rc_context(plotting.rc()):
        fig, ax = plt.subplots(1)
        ax.plot(perc_average_optimal.mean(1), label='Sample Average Method')
        ax.plot(perc_exponential_optimal.mean(1), label='Exponential Recency Weighted Method')
        print('ready')

        ax.grid(alpha=0.25)
        ax.legend(loc='lower right')
        ax.set_title('Comparison of Estimation Methods on 10-Bandit Test Bed')
        ax.set_xlabel(r'Number of Iterations')
        ax.set_ylabel(r'% Optimal Choices (Cumulative)')
        plt.tight_layout()
        fig.savefig(
                os.path.join(
                        c.paths.output,
                        'ex_2_5',
                        'learning_curve.png'
                )
        )
