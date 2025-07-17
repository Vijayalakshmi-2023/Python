# Hashtag Trend Tracker

# Daily sets of hashtags from the last 3 days
day1_hashtags = {"#fun", "#sun", "#vacation", "#travel"}
day2_hashtags = {"#work", "#focus", "#travel", "#motivation"}
day3_hashtags = {"#fun", "#health", "#wellness", "#motivation"}

# Combine all daily hashtags into a weekly trending set using update()
weekly_trending = set()
weekly_trending.update(day1_hashtags)
weekly_trending.update(day2_hashtags)
weekly_trending.update(day3_hashtags)

print("Weekly trending hashtags:", weekly_trending)

# Find hashtags unique to only one day

# Calculate hashtags used more than once by intersecting pairs
day1_day2 = day1_hashtags.intersection(day2_hashtags)
day2_day3 = day2_hashtags.intersection(day3_hashtags)
day1_day3 = day1_hashtags.intersection(day3_hashtags)

# Combine all repeated hashtags
repeated_hashtags = day1_day2.union(day2_day3, day1_day3)

# Unique hashtags used only one day = all - repeated
unique_one_day = weekly_trending.difference(repeated_hashtags)

print("Hashtags used only on one day:", unique_one_day)
