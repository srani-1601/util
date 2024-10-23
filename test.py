# Check if pos_id is in the list of imp_ids
df['is_aligned'] = df.apply(lambda row: str(row['pos_ids']) in row['imp_ids'], axis=1)

# Count aligned and not aligned
alignment_counts = df['is_aligned'].value_counts()

# Plot the distribution
plt.figure(figsize=(6, 4))
alignment_counts.plot(kind='bar', color=['green', 'red'])
plt.title('Distribution of Aligned vs Not Aligned User Plans')
plt.xlabel('Plan Alignment')
plt.ylabel('Frequency')
plt.xticks(ticks=[0, 1], labels=['Aligned', 'Not Aligned'], rotation=0)
plt.show()
