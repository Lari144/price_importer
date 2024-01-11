import argparse
import pandas
import matplotlib.pyplot as plt


class Import():
    def __init__(self, file):
        self.file = file

    def read_data(self):
        data = pandas.read_csv(
            self.file, sep='[,;]\s*', engine='python', header=None)
        data.drop(data.columns[-1], axis=1, inplace=True)
        data.columns = ['Company', 'Date',
                        'Price', 'Currency', 'Location']
        return data


class Visualize():
    @staticmethod
    def visualization(data, plot_type):
        data['Price'] = pandas.to_numeric(data['Price'], errors='coerce')
        data['Date'] = pandas.to_datetime(
            data['Date'], unit='s').dt.strftime('%Y-%m-%d')

        if plot_type == 'bar':
            grouped = data.groupby(['Company', 'Location'])[
                'Price'].mean().unstack()
            ax = grouped.plot(kind='bar', figsize=(10, 6))
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')

        elif plot_type == 'pie':
            grouped = data.groupby(['Company', 'Location'])['Price'].mean()
            grouped.plot(kind='pie', figsize=(8, 6),
                         labels=grouped.index, autopct='%1.1f%%', legend=False)

        elif plot_type == 'time_series':
            fig, ax = plt.subplots(figsize=(10, 6))

            for (company, location), group in data.groupby(['Company', 'Location']):
                group.sort_values('Date', inplace=True)
                ax.plot(group['Date'], group['Price'], marker='o',
                        linestyle='-', label=f"{company}, {location}")

            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.title('Price Time Series by Company and Location')
            plt.xticks(rotation=45)
            plt.legend(title='Company - Location')

        plt.tight_layout()
        plt.show()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('path')
    parser.add_argument(
        'plot_type', choices=['bar', 'pie', 'time_series'])
    args = parser.parse_args()

    importer = Import('test.csv')
    data = importer.read_data()
    Visualize.visualization(data, args.plot_type)


if __name__ == '__main__':
    main()
