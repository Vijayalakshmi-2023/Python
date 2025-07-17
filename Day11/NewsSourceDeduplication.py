# News Source Deduplication

# Headlines fetched from two different news APIs
api1_headlines = {
    "Global markets rally amid economic optimism",
    "New species discovered in the Amazon",
    "Tech companies report record earnings",
    "Sports team wins championship"
}

api2_headlines = {
    "Tech companies report record earnings",
    "New species discovered in the Amazon",
    "Political tensions rise in Europe",
    "Health officials warn about flu season"
}

# Find duplicate headlines (intersection)
duplicate_headlines = api1_headlines.intersection(api2_headlines)
print("Duplicate headlines:", duplicate_headlines)

# Combine all unique headlines (union)
unique_headlines = api1_headlines.union(api2_headlines)
print("\nAll unique headlines combined:")
for headline in unique_headlines:
    print("-", headline)
