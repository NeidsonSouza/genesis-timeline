import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gn_characters_pt.csv')

# Create a new figure
# fig, ax = plt.subplots(figsize=(10, 6))
# fig_height_pixels = fig.get_figheight() * fig.dpi
# pixel_per_row = fig_height_pixels/len(df)

# Initialize a counter for the y-coordinate of bars
y = 0
list_of_height = []
# Iterate through each row in the DataFrame without sorting
for index, row in df.iterrows():
    index += 1
    name = row['name'].capitalize()
    parenting_age = row['parenting_age']
    lifetime = row['lifetime']
    if y > 0:
        before_born_bar = plt.hlines(y=index, xmin=0, xmax=y, colors='gray', lw=1)
        text_x = y / 2
        text_y = index
        plt.text(
            text_x,
            text_y,
            y,
            ha='center',
            va='bottom',
            color='black',
            fontsize=8
        )

    # Plot the first part of the bar (years until parenting age)
    # plt.barh(name, parenting_age, left=y, color='lightblue')
    parenting_age_bar = plt.barh(index, parenting_age, left=y, color='lightblue')
    x = y + lifetime
    plt.axvline(
        x = x,
        # ymax = 0.04 + (0.037 * (len(df) - (index - 1))), # 0.077
        ymax = 1/23,
        color='red',
        linestyle='--',
        label='Vertical Line',
        linewidth=0.4,
    )


    # Add text inside the bar
    if parenting_age > 0:
        text_x = y + (parenting_age / 2)
        text_y = index
        plt.text(
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
    # plt.barh(name, bar_length, left=y, color='lightgreen')
    after_parenting_age_bar = plt.barh(index, bar_length, left=y, color='lightgreen')

    # Add text inside the bar
    text_x = y + bar_length / 2
    text_y = index
    plt.text(
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
    plt.text(
        text_x,
        text_y,
        f'{name}',
        ha='left',
        va='center',
        color='black',
        fontsize=10
    )
    children = plt.gca().get_children()[index]
    if isinstance(children, plt.Rectangle):
        height = children.get_height()
        print(height)

# Set labels and title
plt.tick_params(axis='x', rotation=45)
plt.gca().invert_yaxis()
plt.gca().set_xticks(list(range(100, 2500, 100)))
plt.gca().set_yticks(list(range(1, 24)))

plt.legend(
    [before_born_bar, parenting_age_bar, after_parenting_age_bar],
    ['Anos antes de nascer', 'Anos antes do nascimento do filho especificado na próxima linha', 'Anos depois do nascimento do filho']
    )
# Display the Gantt chart
plt.tight_layout()
plt.show()
