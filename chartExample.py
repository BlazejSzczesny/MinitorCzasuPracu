2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen, QFont
from PyQt5.QtCore import Qt


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DonutChart Example")
        self.setGeometry(100, 100, 1280, 600)

        self.show()

        self.create_donutchart()

    def create_donutchart(self):
        series = QPieSeries()
        series.setHoleSize(0.35)
        series.append("Protein 4.2%", 4.2)
        slice = QPieSlice()
        slice = series.append("Fat 15.6%", 15.6)
        slice.setExploded()
        slice.setLabelVisible()
        series.append("Other 23.8%", 23.8);
        series.append("Carbs 56.4%", 56.4);

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)

        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("DonutChart Example")
        chart.setTheme(QChart.ChartThemeBlueCerulean)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())