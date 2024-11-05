import matplotlib.pyplot as plt
import seaborn as sns

# Function to annotate bar charts
def annotate_bars(ax, fontsize=12):
    """
    Annotates each bar in a bar plot with its height (count).

    Parameters:
    - ax : matplotlib Axes object
        The Axes object containing the bar plot.
    - fontsize : int, optional (default=12)
        Font size for the annotations.

    Returns:
    None
    """
    # Iterate through each bar in the plot
    for p in ax.patches:
        height = round(p.get_height(),2)  # Get the height of the bar
        width = p.get_width()  # Get the width of the bar
        x, y = p.get_xy()  # Get the position of the bar
        
        # Annotate the count at the top of each bar
        ax.annotate(f'{height}', (x + width/2, height), ha='center', va='bottom', fontsize=fontsize)
