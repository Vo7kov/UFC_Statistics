# UFC Statistics Backend

This backend is built with FastAPI and provides analysis of UFC fight durations based on the "Ultimate UFC Dataset."

## API Endpoints Description

### 1. `/distribution/fight-time`
Returns a histogram of fight times (`TotalFightTimeSecs`) with a fitted normal distribution curve overlaid.
- **Response:** PNG image with the plot.
- **Purpose:** Visualizes the distribution of fight durations.

### 2. `/confidence-interval/fight-time`
Calculates the mean fight time and the 95% confidence interval.
- **Response:** JSON with fields `mean_fight_time` and `confidence_interval_95%`.
- **Purpose:** Provides a statistical summary of the average fight duration with a confidence range.

### 3. `/clt/fight-time`
Demonstrates the Central Limit Theorem by sampling 1000 sub-samples of 30 fights, calculating their means, and plotting the distribution of these means.
- **Response:** PNG image with the plot.
- **Purpose:** Shows how the distribution of sample means approximates a normal distribution.

---

## General Structure

- Uses UFC dataset loaded via `kagglehub`.
- Each analytical function is separated into its own service module.
- Plots are generated using `matplotlib` and returned as images.
- Designed for easy scaling and future feature extensions.

---
