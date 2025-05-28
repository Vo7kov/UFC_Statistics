import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_fight_time_distribution(df):
  times = df["TotalFightTimeSecs"].dropna()
  mu, std = norm.fit(times)

  fig, ax = plt.subplots()
  ax.hist(times, bins=30, density=True, alpha=0.6, color='g')

  xmin, xmax = times.min(), times.max()
  x = np.linspace(xmin, xmax, 100)
  p = norm.pdf(x, mu, std)
  ax.plot(x, p, 'k', linewidth=2)
  ax.set_title("Fight Time Distribution with Normal Curve")

  return times, fig
