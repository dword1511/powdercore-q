#!/usr/bin/env python3

import math

import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

import numpy as np


class QPlotter:

  def __init__(self):
    font = {'family': 'Arial', 'size': 9}
    matplotlib.rc('font', **font)
    self._formatter = matplotlib.ticker.FuncFormatter(lambda x, p: format(x, ',.0f'))

  def _fullname(self, o):
    # https://stackoverflow.com/a/2020083/6520528
    module = o.__class__.__module__
    if module is None or module == str.__class__.__module__:
      return o.__class__.__name__
    else:
      return module + '.' + o.__class__.__name__

  def _sanitize_name(self, s):
    return s.replace('.', ' ').replace('_', '-').title()

  def _get_ticks(self, bpk_range, q_range, log, pts):
    b_min = min(bpk_range)
    b_max = max(bpk_range)
    q_min = min(q_range)
    q_max = max(q_range)

    if log['b']:
      b_min = round(math.log10(b_min))
      b_max = round(math.log10(b_max))
      b = np.linspace(start = b_min, stop = b_max, num = pts)
      b = 10 ** b
    else:
      b = np.linspace(start = b_min, stop = b_max, num = pts)

    if log['q']:
      q_min = round(math.log10(q_min))
      q_max = round(math.log10(q_max))
      q = np.linspace(start = q_min, stop = q_max, num = pts)
      q = 10 ** q
    else:
      q = np.linspace(start = q_min, stop = q_max, num = pts)

    return {'bpk': b, 'q': q}


  def plot_one_mat(self, material, f, colors, styles, bpk_range, q_range, log, size, units):
    name      = self._fullname(material)
    f_units   = list(f.keys())
    b_unit    = units['b']
    ticks     = self._get_ticks(bpk_range, q_range, log, 1000)
    x         = ticks['bpk']

    fig       = plt.figure(figsize = size)
    ax        = plt.subplot(1, 1, 1)
    plot      = ax.plot
    if log['b'] and log['q']:
      plot = ax.loglog
    elif log['b']:
      plot = ax.semilogx
    elif log['q']:
      plot = ax.semilogy

    i = 0
    for f_unit in f_units:
      for freq in f[f_unit]:
        color     = colors[i]
        linestyle = styles[i]
        i += 1
        y = [material.get_q(freq, bpk, f_unit, b_unit) for bpk in x]
        plot(x, y, color = color, linewidth = 1.0, linestyle = linestyle, label = '{:>3,d} {:>3}'.format(freq, f_unit))

    ax.xaxis.set_major_formatter(self._formatter)
    ax.yaxis.set_major_formatter(self._formatter)
    ax.legend(loc = 'upper right', fancybox = 'False', shadow = 'False', labelspacing = 0.1, prop = {'family': 'monospace', 'size': 'x-small'})
    plt.xlim(bpk_range)
    plt.ylim(q_range)
    plt.xlabel(r'$B_{{pk}}$ ({})'.format(b_unit))
    plt.ylabel(r'$Q_{{core}}$')
    plt.grid(color = '#c0c0c0', which = 'both', linestyle = '-', linewidth = 0.2)
    plt.title(r'{}, $\mu_r$ = {}'.format(self._sanitize_name(name), material.get_ur()))

    fig.savefig('q_{}.pdf'.format(name), bbox_inches = 'tight')
    plt.close(fig)
