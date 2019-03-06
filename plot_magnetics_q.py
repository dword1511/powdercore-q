#!/usr/bin/env python3

from q_plotter import QPlotter

import magnetics


if __name__ == '__main__':
  plotter   = QPlotter()

  f         = {'MHz': [10, 5, 2, 1], 'kHz': [800, 500, 250, 100, 50, 25]}
  colors    = ['#a50021', '#cc0000', '#ff5050', '#ff9999', '#3366ff', '#0000cc', '#00cc66', '#006400', '#ff3399', '#cc0099']
  styles    = ['--'     , '-'      , ':'      , '-.'     , '--'     , '-.'     , '--'     , '--'     , ':'      , '-'      ]
  bpk_range = [10, 1000]
  q_range   = [1 , 1000]
  log       = {'b': True, 'q': True}
  size      = (6, 4)
  units     = {'b': 'G'}

  for material in [ \
    magnetics.KoolMu_14u(), magnetics.KoolMu_26u(), magnetics.KoolMu_40u(), \
    magnetics.KoolMu_60u(), magnetics.KoolMu_75u(), magnetics.KoolMu_90u(), \
    magnetics.KoolMu_125u(), \
    \
    magnetics.KoolMuMax_19u(), magnetics.KoolMuMax_26u(), magnetics.KoolMuMax_40u(), \
    magnetics.KoolMuMax_60u(), \
    \
    magnetics.MPP_14u(), magnetics.MPP_26u(), magnetics.MPP_60u(), \
    magnetics.MPP_125u(), magnetics.MPP_147u(), magnetics.MPP_160u(), \
    magnetics.MPP_173u(), magnetics.MPP_200u(), magnetics.MPP_300u(), \
    magnetics.MPP_500u(), \
    \
    magnetics.HighFlux_14u(), magnetics.HighFlux_26u(), magnetics.HighFlux_40u(), \
    magnetics.HighFlux_60u(), magnetics.HighFlux_125u(), magnetics.HighFlux_147u(), \
    magnetics.HighFlux_160u(), \
    \
    magnetics.XFlux_26u(), magnetics.XFlux_40u(), magnetics.XFlux_60u(), \
    magnetics.XFlux_75u(), magnetics.XFlux_90u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, q_range, log, size, units)

