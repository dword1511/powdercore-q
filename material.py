#!/usr/bin/env python3

import abc


class Material(abc.ABC):
  _f_to_khz = {'Hz': 1e-3, 'kHz': 1  , 'MHz': 1e3}
  _b_to_mt  = {'G' : 0.1 , 'kG' : 100, 'T'  : 1e3, 'mT' : 1  }
  _p_to_mw  = {'mW': 1   , 'W'  : 1e3, 'kW' : 1e6}
  _l_to_cm  = {'mm': 0.1 , 'cm' : 1  , 'm'  : 100}

  def __init__(self, ur):
    self._ur = ur

  # Use SI unit by default. Internally uses kHz, mT, mW, and cm.
  @abc.abstractmethod
  def get_pv(self, freq, bpk, f_unit = 'Hz', b_unit = 'T', p_unit = 'W', l_unit = 'm'):
    pass

  def get_q(self, freq, bpk, f_unit = 'Hz', b_unit = 'T'):
    p_unit = 'mW'
    l_unit = 'cm'
    pv = self.get_pv(freq, bpk, f_unit, b_unit, p_unit, l_unit)
    return 2.5 * \
      self._f_to_unit(freq, f_unit, 'kHz') * (self._b_to_unit(bpk, b_unit, 'mT') ** 2) \
      / (self._ur * pv)

  def get_ur(self):
    return self._ur

  def _f_to_unit(self, f, unit_in, unit_out):
    return f * self._f_to_khz[unit_in] / self._f_to_khz[unit_out]

  def _b_to_unit(self, b, unit_in, unit_out):
    return b * self._b_to_mt[unit_in] / self._b_to_mt[unit_out]

  def _p_to_unit(self, p, unit_in, unit_out):
    return p * self._p_to_mw[unit_in] / self._p_to_mw[unit_out]

  def _l_to_unit(self, l, unit_in, unit_out):
    return l * self._l_to_cm[unit_in] / self._l_to_cm[unit_out]

  def _v_to_unit(self, v, l_unit_in, l_unit_out):
    return v * (self._l_to_unit(1, l_unit_in, l_unit_out) ** 3)

  def _pv_to_unit(self, pv, l_unit_in, l_unit_out, p_unit_in, p_unit_out):
    return pv * self._p_to_unit(1, p_unit_in, p_unit_out) / self._v_to_unit(1, l_unit_in, l_unit_out)
