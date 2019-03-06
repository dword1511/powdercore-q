#!/usr/bin/env python3

import material


class _Arnold(material.Material):

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

class _MS_MediumU(_Arnold):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 7.890e9, b = 7.111e8, c = 8.98e6, d = 2.846e-14)

class _MP_LowU(_Arnold):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 1.914e9, b = 4.349e8, c = 4.331e6, d = 8.85e-14)

class _MP_HighU(_Arnold):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 3.167e10, b = 1.206e9, c = 9.656e6, d = 5.636e-14)

class _HF_LowU(_Arnold):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.058e9, b = 3.239e8, c = 3.003e6, d = 1.233e-13)

class _HF_HighU(_Arnold):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 4.299e10, b = 6.671e8, c = 3.114e6, d = 8.003e-14)


# Sendust (Fe-Si-Al)

class MS_14u(_Arnold):
  def __init__(self):
    super().__init__(ur = 14, a = 1e9, b = 4.213e8, c = 1.032e7, d = 2.297e-14)

class MS_26u(_Arnold):
  def __init__(self):
    super().__init__(ur = 26, a = 1e6, b = 4.969e8, c = 3.993e6, d = 2.867e-14)

class MS_40u(_Arnold):
  def __init__(self):
    super().__init__(ur = 40, a = 1e6, b = 6.961e8, c = 5.397e6, d = 4.127e-14)

class MS_60u(_MS_MediumU):
  def __init__(self):
    super().__init__(ur = 60)

class MS_75u(_MS_MediumU):
  def __init__(self):
    super().__init__(ur = 75)

class MS_90u(_MS_MediumU):
  def __init__(self):
    super().__init__(ur = 90)

class MS_125u(_Arnold):
  def __init__(self):
    super().__init__(ur = 125, a = 1.394e10, b = 1.034e9, c = 1.244e7, d = 4.007e-14)

class MS_147u(_Arnold):
  def __init__(self):
    super().__init__(ur = 147, a = 5.176e8, b = 1.028e9, c = 9.893e6, d = 2.852e-14)

class MS_160u(_Arnold):
  def __init__(self):
    super().__init__(ur = 160, a = 3.679e10, b = 1.15e9, c = 1.004e7, d = 2.851e-14)

# High-frequency Sendust (Fe-Si-Al)

class SH_26u(_Arnold):
  def __init__(self):
    super().__init__(ur = 26, a = 1e6, b = 3.287e8, c = 5.779e6, d = 1.24e-14)

class SH_60u(_Arnold):
  def __init__(self):
    super().__init__(ur = 60, a = 1e6, b = 8.801e8, c = 5.421e6, d = 1.033e-14)

class SH_125u(_Arnold):
  def __init__(self):
    super().__init__(ur = 125, a = 7.985e9, b = 1.378e9, c = 4.041e6, d = 7.891e-15)

# MPP (Ni-Fe-Mo)

class MP_14u(_MP_LowU):
  def __init__(self):
    super().__init__(ur = 14)

class MP_26u(_MP_LowU):
  def __init__(self):
    super().__init__(ur = 26)

class MP_60u(_Arnold):
  def __init__(self):
    super().__init__(ur = 60, a = 9.919e9, b = 9.488e8, c = 4.486e6, d = 3.238e-14)

class MP_125u(_Arnold):
  def __init__(self):
    super().__init__(ur = 125, a = 2.193e10, b = 1.308e9, c = 9.301e6, d = 3.087e-14)

class MP_147u(_MP_HighU):
  def __init__(self):
    super().__init__(ur = 147)

class MP_160u(_MP_HighU):
  def __init__(self):
    super().__init__(ur = 160)

class MP_173u(_MP_HighU):
  def __init__(self):
    super().__init__(ur = 173)

class MP_205u(_Arnold):
  def __init__(self):
    super().__init__(ur = 205, a = 1.143e10, b = 2.045e9, c = 1.156e7, d = 8.981e-14)

# Ferrosilicon (Fe-Si)

class FS_14u(_Arnold):
  def __init__(self):
    super().__init__(ur = 14, a = 1e6, b = 6.131e7, c = 2.047e6, d = 6.095e-14)

class FS_26u(_Arnold):
  def __init__(self):
    super().__init__(ur = 26, a = 1e6, b = 1.812e8, c = 3.251e6, d = 6.158e-14)

class FS_40u(_Arnold):
  def __init__(self):
    super().__init__(ur = 40, a = 1e6, b = 3.071e8, c = 3.524e6, d = 5.634e-14)

class FS_60u(_Arnold):
  def __init__(self):
    super().__init__(ur = 60, a = 1e6, b = 3.903e8, c = 3.785e6, d = 5.229e-14)

class FS_75u(_Arnold):
  def __init__(self):
    super().__init__(ur = 75, a = 1.883e8, b = 5.098e8, c = 1.162e6, d = 5.024e-14)

class FS_90u(_Arnold):
  def __init__(self):
    super().__init__(ur = 90, a = 1e6, b = 5.648e8, c = 7.44e4, d = 6.942e-14)

# High-flux (Ni-Fe)

class HF_14u(_HF_LowU):
  def __init__(self):
    super().__init__(ur = 14)

class HF_26u(_HF_LowU):
  def __init__(self):
    super().__init__(ur = 26)

class HF_60u(_Arnold):
  def __init__(self):
    super().__init__(ur = 60, a = 8.579e9, b = 7.879e8, c = 1.65e6, d = 1.019e-13)

class HF_125u(_Arnold):
  def __init__(self):
    super().__init__(ur = 125, a = 3.54e10, b = 6.826e8, c = 2.688e6, d = 6.077e-14)

class HF_147u(_HF_HighU):
  def __init__(self):
    super().__init__(ur = 147)

class HF_160u(_HF_HighU):
  def __init__(self):
    super().__init__(ur = 160)

# Optilloy

class OP_14u(_Arnold):
  def __init__(self):
    super().__init__(ur = 14, a = 1e6, b = 2.387e8, c = 5.595e6, d = 7e-14)

class OP_26u(_Arnold):
  def __init__(self):
    super().__init__(ur = 26, a = 1e6, b = 4.732e8, c = 5.789e6, d = 7e-14)

class OP_40u(_Arnold):
  def __init__(self):
    super().__init__(ur = 40, a = 3.471e9, b = 6.469e8, c = 5.242e6, d = 7.252e-14)

class OP_60u(_Arnold):
  def __init__(self):
    super().__init__(ur = 60, a = 1e6, b = 1.329e9, c = 3.531e6, d = 5e-14)

class OP_75u(_Arnold):
  def __init__(self):
    super().__init__(ur = 75, a = 1.442e7, b = 1.864e9, c = 1.825e6, d = 5e-14)

class OP_90u(_Arnold):
  def __init__(self):
    super().__init__(ur = 90, a = 3.715e9, b = 1.852e9, c = 2.019e6, d = 5e-14)

class OP_125u(_Arnold):
  def __init__(self):
    super().__init__(ur = 125, a = 3.954e9, b = 2.598e9, c = 3.654e6, d = 5e-14)

