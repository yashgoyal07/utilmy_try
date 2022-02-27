import pandas
from utilmy.viz import vizhtml 

dataframe = pandas.read_csv('data.csv')

# create html file 
my_html = vizhtml.htmlDoc(title='utilmy_output')

# html file design

# heading h1
my_html.h2('Table Plot')
my_html.table(dataframe, format='orange_light', table_id='table')

my_html.hr()

new_dataframe = pandas.read_csv('histogram.csv')

print(new_dataframe.head())

my_html.h2('Histogram Plot')

my_html.plot_histogram(new_dataframe, col='a', mode='highcharts')

my_html.save('table_html_file.html')