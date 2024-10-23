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











# Check if pos_id is in the list of imp_ids
df['is_aligned'] = df.apply(lambda row: str(row['pos_ids']) in row['imp_ids'], axis=1)

# Calculate the frequency of transitions per plan
transition_counts = df.groupby(['pos_ids', 'is_aligned']).size().unstack(fill_value=0)

# Plot the distribution of aligned vs. not aligned per plan
transition_counts.plot(kind='bar', stacked=True, figsize=(8, 6), color=['red', 'green'])
plt.title('Distribution of Aligned vs Not Aligned Plans by POS ID')
plt.xlabel('POS ID (Chosen Plan)')
plt.ylabel('Frequency')
plt.legend(['Not Aligned', 'Aligned'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate the percentage of transitions into aligned plans for each POS ID
transition_percentage = transition_counts.div(transition_counts.sum(axis=1), axis=0) * 100

# Plot the percentage of aligned transitions
transition_percentage['Aligned'].plot(kind='bar', figsize=(8, 6), color='green')
plt.title('Percentage of Aligned Transitions per POS ID')
plt.xlabel('POS ID (Chosen Plan)')
plt.ylabel('Percentage of Aligned Transitions')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
