import matplotlib as plt
import seaborn as sns
sns.set(style="darkgrid")


def plot_stocks(stocks, title='Stocks of xyz', y_label='Price USD', x_label='Days'):
   
   #plots basic plot
    #parameter :
    #dataframe :stocks
    #title     :title of the plot
    # y_label  :ylabel taken from df
    # x_lbel   :xlabel taken from df
    

    sns.relplot(data=stocks, x="Item", y="Close", height=5, aspect=2, kind="line"
                ).set(title=title, ylabel=y_label, xlabel=x_label)



def plot_predstock(actual, pred, title='Stocks of xyz', y_label='Price USD', x_label='Trading Days'):
    
    # Plots train, test and prediction
    fig = plt.figure()
    ax = fig.add_subplot()

    # Plot actual and predicted close values

    plt.plot(actual, 'red', label='Adjusted Close')
    plt.plot(pred, 'blue', label='Predicted Close')

    # Set title, label
    plt.ylabel(y_label)
    plt.xlabel(x_label)

    ax.set_title(title)
    ax.legend(loc='upper left')

    plt.show()
