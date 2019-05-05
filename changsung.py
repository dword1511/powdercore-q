#!/usr/bin/env python3

# Datasheet from http://changsung.com/_new/wp-content/uploads/2018/11/core_1809_small.pdf

import material


# Unusual model: P = B ^ a (b * f + c * f ^ d), P in mW/cm3, B in kGauss, f in kHz.
# Probably gives inaccurate Q just like ABC model, but at least frequency coverage should be better.
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

    pv = (bpk ** self._a) * (self._b * freq + self._c * (freq ** self._d))

    return self._pv_to_unit(pv, 'cm', l_unit, 'mW', p_unit)


class _HS_HighU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.269, b = 3.677, c = 0.0411, d = 1.930)

class _HP_LowU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 1.878, b = 2.277, c = 0.0053, d = 2.135)

class _FineFlux(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.265, b = 4.168, c = 0.0234, d = 2.027)

class _MPP_LowU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.183, b = 2.485, c = 0.0125, d = 2.099)

class _MPP_MedU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.026, b = 0.865, c = 0.2634, d = 1.712)

class _HighFlux_HighU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.104, b = 2.117, c = 0.1131, d = 1.899)

class _Sendust_HighU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.207, b = 4.518, c = 0.0244, d = 1.967)

class _MegaFlux_HighU(_ChangSung):
  def __init__(self, ur):
    super().__init__(ur = ur, a = 2.145, b = 8.874, c = 0.0632, d = 1.980)


# HS (new material replacement for Sendust and Amorphous)

class HS_60u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 60, a = 2.275, b = 2.830, c = 0.0312, d = 1.953)

class HS_75u(_HS_HighU):
  def __init__(self):
    super().__init__(ur = 75)

class HS_90u(_HS_HighU):
  def __init__(self):
    super().__init__(ur = 90)

# KS (new material replacement for High Flux)

class KS_26u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 26, a = 2.219, b = 8.295, c = 0.0623, d = 1.990)

class KS_40u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 40, a = 2.219, b = 7.465, c = 0.0561, d = 1.990)

class KS_60u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 60, a = 2.231, b = 7.370, c = 0.0315, d = 2.086)

# KH (new material replacement for High Flux with characteristics comparable to Sendust, MPP, and Ferrosilicon)

class KH_26u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 26, a = 2.164, b = 7.613, c = 0.0183, d = 2.169)

class KH_40u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 40, a = 2.241, b = 7.190, c = 0.0182, d = 2.156)

class KH_60u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 60, a = 2.284, b = 6.615, c = 0.0310, d = 2.066)

class KH_90u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 90, a = 2.229, b = 4.861, c = 0.1374, d = 1.849)

# HP (new material replacement for MPP)

class HP_19u(_HP_LowU):
  def __init__(self):
    super().__init__(ur = 19)

class HP_26u(_HP_LowU):
  def __init__(self):
    super().__init__(ur = 26)

class HP_60u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 60, a = 2.083, b = 1.398, c = 0.0195, d = 1.955)

# Fine Flux (new material replacement for Sendust)

class FineFlux_26u(_FineFlux):
  def __init__(self):
    super().__init__(ur = 26)

class FineFlux_40u(_FineFlux):
  def __init__(self):
    super().__init__(ur = 40)

class FineFlux_60u(_FineFlux):
  def __init__(self):
    super().__init__(ur = 60)

# MPP

class MPP_26u(_MPP_LowU):
  def __init__(self):
    super().__init__(ur = 26)

class MPP_60u(_MPP_LowU):
  def __init__(self):
    super().__init__(ur = 60)

class MPP_125u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 125, a = 2.028, b = 1.197, c = 0.1865, d = 1.750)

class MPP_147u(_MPP_MedU):
  def __init__(self):
    super().__init__(ur = 147)

class MPP_160u(_MPP_MedU):
  def __init__(self):
    super().__init__(ur = 160)

class MPP_173u(_MPP_MedU):
  def __init__(self):
    super().__init__(ur = 173)

class MPP_200u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 200, a = 2.045, b = 0.848, c = 0.3513, d = 1.716)

# HighFlux

class HighFlux_26u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 26, a = 2.252, b = 4.081, c = 0.0006, d = 2.736)

class HighFlux_60u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 60, a = 2.284, b = 3.050, c = 0.0023, d = 2.397)

class HighFlux_125u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 125, a = 2.165, b = 1.736, c = 0.1793, d = 1.780)

class HighFlux_147u(_HighFlux_HighU):
  def __init__(self):
    super().__init__(ur = 147)

class HighFlux_160u(_HighFlux_HighU):
  def __init__(self):
    super().__init__(ur = 160)

# Sendust

class Sendust_26u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 26, a = 2.048, b = 4.245, c = 0.0215, d = 1.990)

class Sendust_60u(_Sendust_HighU):
  def __init__(self):
    super().__init__(ur = 60)

class Sendust_75u(_Sendust_HighU):
  def __init__(self):
    super().__init__(ur = 75)

class Sendust_90u(_Sendust_HighU):
  def __init__(self):
    super().__init__(ur = 90)

class Sendust_125u(_Sendust_HighU):
  def __init__(self):
    super().__init__(ur = 125)

# MegaFlux

class MegaFlux_26u(_ChangSung):
  def __init__(self):
    super().__init__(ur = 26, a = 2.166, b = 9.918, c = 0.0519, d = 2.061)

class MegaFlux_50u(_MegaFlux_HighU):
  def __init__(self):
    super().__init__(ur = 50)

class MegaFlux_60u(_MegaFlux_HighU):
  def __init__(self):
    super().__init__(ur = 60)

class MegaFlux_75u(_MegaFlux_HighU):
  def __init__(self):
    super().__init__(ur = 75)

class MegaFlux_90u(_MegaFlux_HighU):
  def __init__(self):
    super().__init__(ur = 90)
