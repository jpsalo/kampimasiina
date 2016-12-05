# -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 23:02:40 2016

@author: HP
"""


from random import randint
import subprocess

subprocess.call(['python', 'kampi_ui.py'])

koenumero = 1

# while (koenumero < 3):
#     koenumero = randint(0, 2)
#     if (koenumero == 0):
#         subprocess.call(['python', 'KampiPos.py'])
#     if (koenumero == 1):
#         subprocess.call(['python', 'KampiNeg.py'])
#     if (koenumero == 2):
#         subprocess.call(['python', 'KampiNeutr.py'])
