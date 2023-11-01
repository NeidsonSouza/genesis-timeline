import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gn_characters_pt.csv')

# Create a new figure
fig, ax = plt.subplots(figsize=(10, 6))

# Initialize a counter for the y-coordinate of bars
y = 0
# Iterate through each row in the DataFrame without sorting
for index, row in df.iterrows():
    index += 1
    name = row['name'].capitalize()
    parenting_age = row['parenting_age']
    lifetime = row['lifetime']
    if y > 0:
        before_born_bar = ax.hlines(y=index, xmin=0, xmax=y, colors='gray', lw=1)
        text_x = y / 2
        text_y = index
        ax.text(
            text_x,
            text_y,
            y,
            ha='center',
            va='bottom',
            color='black',
            fontsize=8
        )

    # Plot the first part of the bar (years until parenting age)
    # ax.barh(name, parenting_age, left=y, color='lightblue')
    parenting_age_bar = ax.barh(index, parenting_age, left=y, color='lightblue')
    x = y + lifetime
    # ax.axvline(
    #     x=x,
    #     ymax=0.043,
    #     color='red',
    #     linestyle='--',
    #     label='Vertical Line',
    #     linewidth=0.4,
    # )

    # Add text inside the bar
    if parenting_age > 0:
        text_x = y + (parenting_age / 2)
        text_y = index
        ax.text(
            text_x,
            text_y,
            f'{parenting_age}',
            ha='center',
            va='center',
            color='black',
            fontsize=8
        )


    # Plot the second part of the bar (remaining years)
    y += parenting_age
    bar_length = lifetime - parenting_age
    # ax.barh(name, bar_length, left=y, color='lightgreen')
    after_parenting_age_bar = ax.barh(index, bar_length, left=y, color='lightgreen')

    # Add text inside the bar
    text_x = y + bar_length / 2
    text_y = index
    ax.text(
        text_x,
        text_y,
        f'{bar_length}',
        ha='center',
        va='center',
        color='black',
        fontsize=8
    )

    text_x = y + bar_length + 10
    text_y = index
    ax.text(
        text_x,
        text_y,
        f'{name}',
        ha='left',
        va='center',
        color='black',
        fontsize=10
    )

# Set labels and title
ax.set_xticks(list(range(100, 2500, 100)))
ax.set_yticks(list(range(1, 24)))
ax.tick_params(axis='x', rotation=45)
ax.set_xlabel('Years Since Creation')
ax.set_ylabel('Characters')
ax.set_title('Genesis Timeline')

# Invert chart
ax.invert_yaxis()


ax.legend(
    [before_born_bar, parenting_age_bar, after_parenting_age_bar],
    ['Anos antes de nascer', 'Anos antes do nascimento do filho especificado na próxima linha', 'Anos depois do nascimento do filho']
    )
# Display the Gantt chart
plt.tight_layout()
plt.show()
