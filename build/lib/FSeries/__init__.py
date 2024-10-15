"""
FSeries - A library for calculating Fourier coefficients.

This package provides tools to compute Fourier coefficients for periodic functions.
"""
__version__ = '0.1.0'

import numpy as np
import scipy.integrate as integrate

import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)
logger.info('FSeries package initialized, have fun :)')