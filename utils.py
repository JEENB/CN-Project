def stats_summary(df):
	data = df["x"]
	tot  = len(df)
	maxi = data.max()
	mini = data.min()
	mean = data.mean()
	medi = data.median()
	sd   = data.std()

	return tot, maxi, mini, mean, medi, sd