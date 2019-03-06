#!/usr/bin/env python3

import material


class _Micrometals(material.Material):

  def __init__(self, ur, a, b, c, d, exp_a = 3, exp_b = 2.3, exp_c = 1.65):
    self._a     = a
    self._b     = b
    self._c     = c
    self._d     = d
    self._exp_a = exp_a
    self._exp_b = exp_b
    self._exp_c = exp_c
    super().__init__(ur)

  def get_pv(self, freq, bpk, f_unit = 'Hz', b_unit = 'T', p_unit = 'W', l_unit = 'm'):
    freq  = self._f_to_unit(freq, f_unit, 'Hz')
    bpk   = self._b_to_unit(bpk , b_unit, 'G')

    t_a   = self._a / (bpk ** self._exp_a)
    t_b   = self._b / (bpk ** self._exp_b)
    t_c   = self._c / (bpk ** self._exp_c)

    t_1   = freq / (t_a + t_b + t_c)
    t_2   = self._d * (bpk ** 2) * (freq ** 2)

    pv = t_1 + t_2
    return self._pv_to_unit(pv, 'cm', l_unit, 'mW', p_unit)

class _TypeI(_Micrometals):
  def __init__(self, ur, d):
    super().__init__(ur = ur, a = 1.9e9, b = 2e8, c = 9e5, d = d)

class _TypeII(_Micrometals):
  def __init__(self, ur, d):
    super().__init__(ur = ur, a = 4e9, b = 3e8, c = 2.7e6, d = d)


# Carbonyl Iron, Type I

class Mix_1(_TypeI):
  def __init__(self):
    super().__init__(ur = 20, d = 4.3e-15)

class Mix_3(_TypeI):
  def __init__(self):
    super().__init__(ur = 35, d = 4.3e-15)

class Mix_8(_TypeI):
  def __init__(self):
    super().__init__(ur = 35, d = 5e-15)

class Mix_15(_TypeI):
  def __init__(self):
    super().__init__(ur = 25, d = 5e-15)

# Carbonyl Iron, Type II

class Mix_2(_TypeII):
  def __init__(self):
    super().__init__(ur = 10, d = 9.6e-16)

class Mix_4(_TypeII):
  def __init__(self):
    super().__init__(ur = 9, d = 8e-15)

class Mix_6(_TypeII):
  def __init__(self):
    super().__init__(ur = 8.5, d = 8.9e-16)

class Mix_7(_TypeII):
  def __init__(self):
    super().__init__(ur = 9, d = 9.6e-16)

class Mix_10(_TypeII):
  def __init__(self):
    super().__init__(ur = 6, d = 8e-16)

class Mix_17(_TypeII):
  def __init__(self):
    super().__init__(ur = 4, d = 4.4e-16)

# Iron, Type II

class Mix_14(_TypeII):
  def __init__(self):
    super().__init__(ur = 14, d = 1.92e-15)

# Iron, Others

class Mix_18(_Micrometals):
  def __init__(self):
    super().__init__(ur = 55, a = 8e8, b = 1.7e8, c = 9e5, d = 3.1e-14)

class Mix_19(_Micrometals):
  def __init__(self):
    super().__init__(ur = 55, a = 1.9e9, b = 8.4e7, c = 2.1e6, d = 5e-14)

class Mix_26(_Micrometals):
  def __init__(self):
    super().__init__(ur = 75, a = 1e9, b = 1.1e8, c = 1.9e6, d = 1.9e-13)

class Mix_30(_Micrometals):
  def __init__(self):
    super().__init__(ur = 22, a = 3.3e8, b = 2e7, c = 2e6, d = 1.1e-13)

class Mix_34(_Micrometals):
  def __init__(self):
    super().__init__(ur = 33, a = 1.1e9, b = 3.3e7, c = 2.5e6, d = 7.7e-14)

class Mix_35(_Micrometals):
  def __init__(self):
    super().__init__(ur = 33, a = 3.7e8, b = 2.2e7, c = 2.2e6, d = 1.1e-13)

class Mix_38(_Micrometals):
  def __init__(self):
    super().__init__(ur = 85, a = 1.2e9, b = 1.3e8, c = 1.9e6, d = 3.2e-13)

class Mix_40(_Micrometals):
  def __init__(self):
    super().__init__(ur = 60, a = 1.1e9, b = 3.3e7, c = 2.5e6, d = 3.1e-13)

class Mix_45(_Micrometals):
  def __init__(self):
    super().__init__(ur = 100, a = 1.2e9, b = 1.3e8, c = 2.4e6, d = 1.2e-13)

class Mix_52(_Micrometals):
  def __init__(self):
    super().__init__(ur = 75, a = 1e9, b = 1.1e8, c = 2.1e6, d = 6.9e-14)

# Ferrosilicon (Fe-Si)

class Mix_60(_Micrometals):
  def __init__(self):
    super().__init__(ur = 55, a = 5.3e8, b = 1.4e8, c = 1.2e6, d = 2.7e-14)

class Mix_61(_Micrometals):
  def __init__(self):
    super().__init__(ur = 38, a = 4e8, b = 1.1e8, c = 5.1e5, d = 2.4e-14)

class Mix_63(_Micrometals):
  def __init__(self):
    super().__init__(ur = 35, a = 9.94e8, b = 2.56e8, c = 1e4, d = 3.34e-15)

class Mix_65(_Micrometals):
  def __init__(self):
    super().__init__(ur = 42, a = 6.9e9, b = 6e7, c = 1.1e6, d = 2.5e-14)

class Mix_66(_Micrometals):
  def __init__(self):
    super().__init__(ur = 66, a = 1.72e10, b = 4.96e7, c = 1.23e6, d = 1.73e-14)

# High Flux (Ni-Fe)

class Mix_70(_Micrometals):
  def __init__(self):
    super().__init__(ur = 100, a = 1e10, b = 1.3e9, c = 7.9e6, d = 4.2e-14)

# MPP (Ni-Fe-Mo)

class Mix_M125(_Micrometals):
  def __init__(self):
    super().__init__(ur = 125, a = 3.1e10, b = 2.7e9, c = 3.3e6, d = 5.3e-14)
