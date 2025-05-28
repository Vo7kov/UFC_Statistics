def get_confidence_interval(df):
  times = df["TotalFightTimeSecs"].dropna()
  mean = times.mean()
  sem = times.sem()
  ci95 = 1.96 * sem

  return {
    "mean_fight_time": mean,
    "confidence_interval_95%": [mean - ci95, mean + ci95],
  }
