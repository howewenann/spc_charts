import seaborn as sns
from matplotlib import pyplot as plt

def plot_control_chart(data, index, obs, UCL, center, LCL, drawstyle='steps-mid', title=None, ylab=None, xlab=None, all_dates=True, rot=45):

    fig, ax = plt.subplots(figsize=(15,5))
    sns.relplot(x=index, y=obs, data=data, kind='line', ax=ax, color='blue', marker='o')
    sns.lineplot(x=index, y=UCL, data=data, drawstyle=drawstyle, ax=ax, color='red')
    sns.lineplot(x=index, y=LCL, data=data, drawstyle=drawstyle, ax=ax, color='red')
    sns.relplot(x=index, y=center, data=data, kind='line', ax=ax, color='black')

    plt.close()
    plt.close()

    if title is not None:
        plt.title(title)

    if ylab is not None:
        plt.ylabel(ylab)

    if xlab is not None:
        plt.xlabel(xlab)

    if all_dates:
        ax.set(xticks=data[index].values)
        
    plt.xticks(rotation=rot)

    return None


if __name__ == "__main__":
    pass