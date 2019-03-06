#!/usr/bin/env python3

from pv_plotter import PvPlotter

import changsung


if __name__ == '__main__':
  plotter   = PvPlotter()

  f         = {'kHz': [300, 200, 100, 50, 25]}
  colors    = ['#6f4527', '#c5341c', '#bc95c4', '#927530', '#313491', '#de4a26', '#f7941e', '#7e287e', '#313491', '#1f99d5', '#22b24c']
  styles    = ['-'] * len(colors)
  bpk_range = [10 , 5000 ]
  pv_range  = [0.1, 10000]
  log       = {'b': True, 'p': True}
  size      = (3.5, 2)
  units     = {'l': 'cm', 'p': 'mW', 'b': 'G'}

  for material in [ \
    changsung.MPP_26u(), changsung.MPP_60u(), changsung.MPP_125u(), \
    changsung.MPP_147u(), changsung.MPP_160u(), changsung.MPP_173u(), \
    changsung.MPP_200u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)
