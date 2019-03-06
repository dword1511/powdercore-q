#!/usr/bin/env python3

from pv_plotter import PvPlotter

import micrometals


if __name__ == '__main__':
  plotter   = PvPlotter()

  f         = {'MHz': [10, 5, 2, 1], 'kHz': [500, 200, 100, 50, 10, 1]}
  colors    = ['#a50021', '#cc0000', '#ff5050', '#ff9999', '#3366ff', '#0000cc', '#00cc66', '#006400', '#ff3399', '#cc0099']
  styles    = ['--'     , '-'      , ':'      , '-.'     , '--'     , '-.'     , '--'     , '--'     , ':'      , '-'      ]
  bpk_range = [1 , 10000]
  pv_range  = [10, 10000]
  log       = {'b': True, 'p': True}
  size      = (3.5, 2)
  units     = {'l': 'cm', 'p': 'mW', 'b': 'G'}
  material  = micrometals.Mix_1()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  # As in datasheet. Commenting bpk_range and f out gives more informative graph
  bpk_range = [10, 10000]
  f         = {'kHz': [500, 250, 100, 50, 25, 10, 5, 1], 'Hz': [400, 60]}
  material  = micrometals.Mix_2()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_3()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_4()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_6()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_7()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_8()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_10()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_14()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_15()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_17()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_18()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_19()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_26()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_30()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_34()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_35()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_38()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_40()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_45()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_52()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_60()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_61()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_63()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_65()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_66()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_70()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)

  material  = micrometals.Mix_M125()
  plotter.plot_one_mat(material, f, colors, styles, bpk_range, pv_range, log, size, units)
