#import simplegui
import simpleplot

dataset1 = {3: 5, 8: 2, 1: 3, 4:4}
#dataset2 = [(1, 2), (4, 7), (2, 5), (7, 6)]
dataset2 = [(1, 2), (2, 5), (4, 7), (7, 6)]
simpleplot.plot_lines('We are the champions', 600, 400, 'x', 'y', [dataset1, dataset2], True, ['dataset-1', 'dataset-2'])
