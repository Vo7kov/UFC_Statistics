import matplotlib.pyplot as plt

def get_clt_distribution(df):
  times = df["TotalFightTimeSecs"].dropna()
  sample_means = []
  for _ in range(1000):
    sample = times.sample(30, replace=True)
    sample_means.append(sample.mean())

  fig, ax = plt.subplots()
  ax.hist(sample_means, bins=30, density=True, alpha=0.7, color='b')
  ax.set_title("Central Limit Theorem Distribution (samples of 30)")

  return sample_means, fig
