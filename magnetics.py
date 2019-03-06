#!/usr/bin/env python3

import material


class _Magnetics(material.Material):

  def __init__(self, ur, khz_break, a1, b1, c1, a2, b2, c2):
    self._a1    = a1
    self._b1    = b1
    self._c1    = c1
    self._fbk   = khz_break
    self._a2    = a2
    self._b2    = b2
    self._c2    = c2
    super().__init__(ur)

  # It is unclear whether B is in peak value.
  def get_pv(self, freq, bpk, f_unit = 'Hz', b_unit = 'T', p_unit = 'W', l_unit = 'm'):
    freq  = self._f_to_unit(freq, f_unit, 'kHz')
    bpk   = self._b_to_unit(bpk , b_unit, 'T')

    if freq < self._fbk:
      pv = self._a1 * (bpk ** self._b1) * (freq ** self._c1)
    else:
      pv = self._a2 * (bpk ** self._b2) * (freq ** self._c2)

    return self._pv_to_unit(pv, 'cm', l_unit, 'mW', p_unit)

class _KoolMuMax_MediumLowU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 10, a1 = 170.17, b1 = 1.774, c1 = 1.03, a2 = 45.48, b2 = 1.774, c2 = 1.46)

class _KoolMuMax_MediumHighU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 10, a1 = 338.51, b1 = 2.022, c1 = 1.05, a2 = 146.81, b2 = 2.022, c2 = 1.33)

class _KoolMuMax_HighU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 10, a1 = 94.674, b1 = 1.998, c1 = 1.402, a2 = 86.005, b2 = 1.998, c2 = 1.402)

class _MPP_MediumLowU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 10, a1 = 254.26, b1 = 2.222, c1 = 1.17, a2 = 87.07, b2 = 2.222, c2 = 1.56)

class _MPP_MediumHighU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 10, a1 = 320.32, b1 = 2.322, c1 = 1.19, a2 = 115.52, b2 = 2.322, c2 = 1.59)

class _HighFlux_MediumU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 25, a1 = 151.44, b1 = 1.585, c1 = 1.09, a2 = 47.51, b2 = 1.585, c2 = 1.43)

class _HighFlux_HighU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 25, a1 = 883.51, b1 = 2.163, c1 = 1.09, a2 = 203.61, b2 = 2.163, c2 = 1.52)

class _XFlux_HighU(_Magnetics):
  def __init__(self, ur):
    super().__init__(ur = ur, khz_break = 9, a1 = 862.34, b1 = 2.018, c1 = 1.02, a2 = 566.54, b2 = 2.018, c2 = 1.17)


# Sendust (Fe-Si-Al)

class KoolMu_14u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 14, khz_break = 10, a1 = 40.18, b1 = 1, c1 = 1.22, a2 = 21.49, b2 = 1, c2 = 1.33)

class KoolMu_26u(_KoolMuMax_MediumLowU):
  def __init__(self):
    super().__init__(ur = 26)

class KoolMu_40u(_KoolMuMax_MediumLowU):
  def __init__(self):
    super().__init__(ur = 40)

class KoolMu_60u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 60, khz_break = 9, a1 = 136.93, b1 = 1.781, c1 = 1.12, a2 = 62.65, b2 = 1.781, c2 = 1.36)

class KoolMu_75u(_KoolMuMax_MediumHighU):
  def __init__(self):
    super().__init__(ur = 75)

class KoolMu_90u(_KoolMuMax_MediumHighU):
  def __init__(self):
    super().__init__(ur = 90)

class KoolMu_125u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 125, khz_break = 10, a1 = 228.46, b1 = 1.928, c1 = 1.05, a2 = 71.93, b2 = 1.928, c2 = 1.47)

# Next-gen Sendust (Fe-Si-Al)

class KoolMuMax_19u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 19, khz_break = 25, a1 = 468.978, b1 = 2.141, c1 = 1.067, a2 = 149.797, b2 = 2.141, c2 = 1.381)

class KoolMuMax_26u(_KoolMuMax_HighU):
  def __init__(self):
    super().__init__(ur = 26)

class KoolMuMax_40u(_KoolMuMax_HighU):
  def __init__(self):
    super().__init__(ur = 40)

class KoolMuMax_60u(_KoolMuMax_HighU):
  def __init__(self):
    super().__init__(ur = 60)

# 75-series Sendust has no formular available

# MPP (Ni-Fe-Mo)

class MPP_14u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 14, khz_break = 10, a1 = 64.02, b1 = 1.074, c1 = 1.11, a2 = 21.06, b2 = 1.074, c2 = 1.38)

class MPP_26u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 26, khz_break = 10, a1 = 361.62, b1 = 2, c1 = 1.08, a2 = 109.17, b2 = 2, c2 = 1.37)

class MPP_60u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 60, khz_break = 10, a1 = 80.12, b1 = 1.585, c1 = 1.04, a2 = 31.32, b2 = 1.585, c2 = 1.37)

class MPP_125u(_MPP_MediumLowU):
  def __init__(self):
    super().__init__(ur = 125)

class MPP_147u(_MPP_MediumLowU):
  def __init__(self):
    super().__init__(ur = 147)

class MPP_160u(_MPP_MediumLowU):
  def __init__(self):
    super().__init__(ur = 160)

class MPP_173u(_MPP_MediumLowU):
  def __init__(self):
    super().__init__(ur = 173)

class MPP_200u(_MPP_MediumHighU):
  def __init__(self):
    super().__init__(ur = 200)

class MPP_300u(_MPP_MediumHighU):
  def __init__(self):
    super().__init__(ur = 300)

class MPP_500u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 500, khz_break = 10, a1 = 303.43, b1 = 1.999, c1 = 1.09, a2 = 96.89, b2 = 1.999, c2 = 1.54)

# High-flux (Ni-Fe)

class HighFlux_14u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 14, khz_break = 0, a1 = 0, b1 = 0, c1 = 0, a2 = 181.14, b2 = 1.386, c2 = 1.21)

class HighFlux_26u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 26, khz_break = 25, a1 = 1550.54, b1 = 2.17, c1 = 1.05, a2 = 532.55, b2 = 2.17, c2 = 1.35)

class HighFlux_40u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 40, khz_break = 25, a1 = 2021.58, b1 = 2.28, c1 = 1.05, a2 = 1707.09, b2 = 2.28, c2 = 1.14)

class HighFlux_60u(_HighFlux_MediumU):
  def __init__(self):
    super().__init__(ur = 60)

class HighFlux_125u(_HighFlux_MediumU):
  def __init__(self):
    super().__init__(ur = 125)

class HighFlux_147u(_HighFlux_HighU):
  def __init__(self):
    super().__init__(ur = 147)

class HighFlux_160u(_HighFlux_HighU):
  def __init__(self):
    super().__init__(ur = 160)

# Ferrosilicon (Fe-Si)

class XFlux_26u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 26, khz_break = 25, a1 = 1187.96, b1 = 1.977, c1 = 1.05, a2 = 761.36, b2 = 1.977, c2 = 1.21)

class XFlux_40u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 40, khz_break = 9, a1 = 1274.93, b1 = 1.934, c1 = 1.06, a2 = 804.88, b2 = 1.934, c2 = 1.14)

class XFlux_60u(_Magnetics):
  def __init__(self):
    super().__init__(ur = 60, khz_break = 10, a1 = 670.26, b1 = 1.909, c1 = 1.06, a2 = 454.56, b2 = 1.909, c2 = 1.19)

class XFlux_75u(_XFlux_HighU):
  def __init__(self):
    super().__init__(ur = 75)

class XFlux_90u(_XFlux_HighU):
  def __init__(self):
    super().__init__(ur = 90)
