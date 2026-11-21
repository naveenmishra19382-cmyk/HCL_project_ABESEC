import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Data Load Karein
print("Loading dataset...")
df = pd.read_csv('28_tournament_match_stats.csv')

# 2. Data Cleaning (Duplicates aur Missing Values hatana)
print(f"Original rows: {len(df)}")
df.drop_duplicates(subset=['Match_ID'], keep='first', inplace=True)
df['Player_Points'] = df['Player_Points'].fillna(df['Player_Points'].mean())
df['Match_Duration_Mins'] = df['Match_Duration_Mins'].fillna(df['Match_Duration_Mins'].median())
print(f"Cleaned rows: {len(df)}\n")

# 3. Basic Summary & Statistics
print("--- DATASET SUMMARY ---")
print(df.info())
print("\n--- STATISTICAL OVERVIEW ---")
print(df.describe())

# 4. Key Insights Nikalna
print("\n--- KEY INSIGHTS ---")
# Top 5 Players by Total Points
top_players = df.groupby('Player_Name')['Player_Points'].sum().sort_values(ascending=False).head(5)
print("Top 5 Players (Total Points):\n", top_players)

# Team Performance (Wins, Losses, Draws)
team_results = pd.crosstab(df['Team'], df['Result'])
print("\nTeam Match Results:\n", team_results)

# 5. Data Visualization (Charts Banana)
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Sports Match Data Analysis Dashboard', fontsize=16, fontweight='bold')

# Chart 1: Team-wise Match Results (Win/Loss/Draw)
team_results.plot(kind='bar', stacked=True, ax=axes[0, 0], colormap='viridis')
axes[0, 0].set_title('Match Results by Team')
axes[0, 0].set_ylabel('Number of Matches')
axes[0, 0].tick_params(axis='x', rotation=45)

# Chart 2: Top 5 Players by Total Points
sns.barplot(x=top_players.values, y=top_players.index, ax=axes[0, 1], palette='magma', hue=top_players.index, legend=False)
axes[0, 1].set_title('Top 5 Scorers (Total Points)')
axes[0, 1].set_xlabel('Total Points')

# Chart 3: Match Duration Distribution
sns.histplot(df['Match_Duration_Mins'], bins=20, kde=True, ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Match Duration Distribution (Mins)')
axes[1, 0].set_xlabel('Duration (Minutes)')

# Chart 4: Average Points by Match Type
avg_points_type = df.groupby('Match_Type')['Player_Points'].mean().reset_index()
sns.barplot(data=avg_points_type, x='Match_Type', y='Player_Points', ax=axes[1, 1], palette='coolwarm', hue='Match_Type', legend=False)
axes[1, 1].set_title('Average Player Points by Match Type')
axes[1, 1].set_ylabel('Average Points')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('dashboard_output.png')  # Chart ko image ke roop mein save karega
print("\nDashboard saved as 'dashboard_output.png'!")
plt.show()