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
        print(data)
        return data


class Visualize():
    @staticmethod
    def visualization(data):
        data['Price'] = pandas.to_numeric(data['Price'], errors='coerce')
        data['Date'] = pandas.to_datetime(
            data['Date'], unit='s').dt.strftime('%Y-%m-%d')
        data['Companies'] = data['Company'] + '\n' + \
            data['Location'] + '\n' + data['Date']
        grouped = data.groupby(['Companies'])[
            'Price'].mean()
        grouped.plot(kind='bar', figsize=(8, 6))

        plt.ylabel('Price')
        plt.title('Prices by Location')
        plt.xticks(rotation=45)
        plt.legend(title='Company')
        plt.tight_layout()
        plt.show()


def main():
    importer = Import('test.csv')
    data = importer.read_data()
    Visualize.visualization(data)


if __name__ == '__main__':
    main()
