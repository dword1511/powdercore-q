#!/usr/bin/env python3

# Datasheet from http://changsung.com/_new/wp-content/uploads/2018/11/core_1809_small.pdf

import material


# Unusual model: P = B ^ a (b * f + c * f ^ d), P in mW/cm3, B in kGauss, f in kHz.
class _ChangSung(material.Material):

  def __init__(self, ur, a, b, c, d):
    self._a = a
    self._b = b
    self._c = c
    self._d = d
    super().__init__(ur)

  # It is unclear whether B is in peak value.
  def get_pv(self, freq, bpk, f_unit = 'Hz', b_unit = 'T', p_unit = 'W', l_unit = 'm'):
    freq  = self._f_to_unit(freq, f_unit, 'kHz')
    bpk   = self._b_to_unit(bpk , b_unit, 'kG')

    pv = (bpk ** self._a) * (freq ** self._c)

    return self._pv_to_unit(pv, 'cm', l_unit, 'mW', p_unit)

class _MPP_LowU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 0.29, b = 2.23, c = 1.63)

class _MPP_MediumHighU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 0.41, b = 2.03, c = 1.64)


# MPP (Ni-Fe-Mo)

class MPP_26u(_MPP_LowU):
  def __init__(self):
    super().__init__(ur = 26)

class MPP_60u(_MPP_LowU):
  def __init__(self):
    super().__init__(ur = 60)

class MPP_125u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 125, a = 0.33, b = 1.98, c = 1.64)

class MPP_147u(_MPP_MediumHighU):
  def __init__(self):
    super().__init__(ur = 147)

class MPP_160u(_MPP_MediumHighU):
  def __init__(self):
    super().__init__(ur = 160)

class MPP_173u(_MPP_MediumHighU):
  def __init__(self):
    super().__init__(ur = 173)

class MPP_200u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 200, a = 0.46, b = 2.05, c = 1.65)

