#!/usr/bin/env python3

from q_plotter import QPlotter

import changsung


if __name__ == '__main__':
  plotter   = QPlotter()

  f         = {'MHz': [10, 5, 2, 1], 'kHz': [500, 300, 200, 100, 50, 20, 10]}
  colors    = ['#6f4527', '#c5341c', '#bc95c4', '#927530', '#313491', '#de4a26', '#f7941e', '#7e287e', '#313491', '#1f99d5', '#22b24c']
  styles    = ['-'] * len(colors)
  bpk_range = [10, 1000]
  q_range   = [ 1, 1000]
  log       = {'b': True, 'q': True}
  size      = (3, 2)
  units     = {'l': 'cm', 'p': 'mW', 'b': 'mT'}

  for material in [ \
    changsung.HS_60u(), changsung.HS_75u(), changsung.HS_90u(), \
    \
    changsung.KS_26u(), changsung.KS_40u(), changsung.KS_60u(), \
    \
    changsung.KH_26u(), changsung.KH_40u(), changsung.KH_60u(), changsung.KH_90u(), \
    \
    changsung.HP_19u(), changsung.HP_26u(), changsung.HP_60u(), \
    \
    changsung.FineFlux_26u(), changsung.FineFlux_40u(), changsung.FineFlux_60u(), \
    \
    changsung.MPP_26u(), changsung.MPP_60u(), changsung.MPP_125u(), changsung.MPP_147u(), \
    changsung.MPP_160u(), changsung.MPP_173u(), changsung.MPP_200u(), \
    \
    changsung.HighFlux_26u(), changsung.HighFlux_60u(), changsung.HighFlux_125u(), \
    changsung.HighFlux_147u(), changsung.HighFlux_160u(), \
    \
    changsung.Sendust_26u(), changsung.Sendust_60u(), changsung.Sendust_75u(), \
    changsung.Sendust_90u(), changsung.Sendust_125u(), \
    \
    changsung.MegaFlux_26u(), changsung.MegaFlux_50u(), changsung.MegaFlux_60u(), \
    changsung.MegaFlux_75u(), changsung.MegaFlux_90u(), \
  ]:
    print(material.__class__.__name__)
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, q_range, log, size, units)
