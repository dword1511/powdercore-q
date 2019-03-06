#!/usr/bin/env python3

from q_plotter import QPlotter

import arnold


if __name__ == '__main__':
  plotter   = QPlotter()

  f         = {'MHz': [10, 5, 2, 1], 'kHz': [800, 500, 250, 100, 50, 25]}
  colors    = ['#a50021', '#cc0000', '#ff5050', '#ff9999', '#3366ff', '#0000cc', '#00cc66', '#006400', '#ff3399', '#cc0099']
  styles    = ['--'     , '-'      , ':'      , '-.'     , '--'     , '-.'     , '--'     , '--'     , ':'      , '-'      ]
  bpk_range = [1, 10000]
  q_range   = [1, 1000 ]
  log       = {'b': True, 'q': True}
  size      = (6, 4)
  units     = {'b': 'G'}

  for material in [ \
    arnold.MS_14u(), arnold.MS_26u(), arnold.MS_40u(), \
    arnold.MS_60u(), arnold.MS_75u(), arnold.MS_90u(), \
    arnold.MS_125u(), arnold.MS_147u(), arnold.MS_160u(), \
    \
    arnold.SH_26u(), arnold.SH_60u(), arnold.SH_125u(), \
    \
    arnold.MP_14u(), arnold.MP_26u(), arnold.MP_60u(), \
    arnold.MP_125u(), arnold.MP_147u(), arnold.MP_160u(), \
    arnold.MP_173u(), arnold.MP_205u(), \
    \
    arnold.FS_14u(), arnold.FS_26u(), arnold.FS_40u(), \
    arnold.FS_60u(), arnold.FS_75u(), arnold.FS_90u(), \
    \
    arnold.HF_14u(), arnold.HF_26u(), arnold.HF_60u(), \
    arnold.HF_125u(), arnold.HF_147u(), arnold.HF_160u(), \
    \
    arnold.OP_14u(), arnold.OP_26u(), arnold.OP_40u(), \
    arnold.OP_60u(), arnold.OP_75u(), arnold.OP_90u(), \
    arnold.OP_125u(), \
  ]:
    plotter.plot_one_mat(material, f, colors, styles, bpk_range, q_range, log, size, units)

