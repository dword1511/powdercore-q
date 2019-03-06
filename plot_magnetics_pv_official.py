#!/usr/bin/env python3

from pv_plotter import PvPlotter

import magnetics


if __name__ == '__main__':
  plotter   = PvPlotter()

  f         = {'kHz': [500, 300, 200, 100, 50, 40, 20, 10, 5, 2, 1]}
  colors    = ['#6f4527', '#c5341c', '#bc95c4', '#927530', '#313491', '#de4a26', '#f7941e', '#7e287e', '#313491', '#1f99d5', '#22b24c']
  styles    = ['-'] * len(colors)
  bpk_range = [10, 1000]
  pv_range  = [1 , 5000]
  log       = {'b': True, 'p': True}
  size      = (4, 2)
  units     = {'l': 'cm', 'p': 'mW', 'b': 'mT'}

  for material in [ \
    magnetics.KoolMu_14u(), magnetics.KoolMu_26u(), magnetics.KoolMu_40u(), \
    magnetics.KoolMu_60u(), magnetics.KoolMu_75u(), magnetics.KoolMu_90u(), \
    magnetics.KoolMu_125u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  f         = {'kHz': [300, 200, 100, 50, 40, 25, 10, 5, 1]}

  for material in [ \
    magnetics.KoolMuMax_19u(), magnetics.KoolMuMax_26u(), magnetics.KoolMuMax_40u(), \
    magnetics.KoolMuMax_60u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  f         = {'kHz': [300, 200, 100, 50, 40, 20, 10, 5, 2, 1], 'Hz': [500]}

  for material in [ \
    magnetics.MPP_14u(), magnetics.MPP_26u(), magnetics.MPP_60u(), \
    magnetics.MPP_125u(), magnetics.MPP_147u(), magnetics.MPP_160u(), \
    magnetics.MPP_173u(), magnetics.MPP_200u(), magnetics.MPP_300u(), \
    magnetics.MPP_500u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  f         = {'kHz': [100, 50, 40, 20, 10, 5, 2, 1], 'Hz': [500, 100, 60]}

  for material in [ \
    magnetics.HighFlux_14u(), magnetics.HighFlux_26u(), magnetics.HighFlux_40u(), \
    magnetics.HighFlux_60u(), magnetics.HighFlux_125u(), magnetics.HighFlux_147u(), \
    magnetics.HighFlux_160u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  f         = {'kHz': [200, 100, 50, 40, 20, 10, 5, 2, 1], 'Hz': [500, 60]}

  for material in [ \
    magnetics.XFlux_26u(), magnetics.XFlux_40u(), magnetics.XFlux_60u(), \
    magnetics.XFlux_75u(), magnetics.XFlux_90u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

