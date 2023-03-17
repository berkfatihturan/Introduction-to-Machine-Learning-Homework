import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff

timesData = pd.read_csv("data/timesData.csv")
print(timesData.head())

def Scatter3d():
    global timesData
    dataframe = timesData[timesData.year == 2015]

    trace1 = go.Scatter3d(
        x=dataframe.world_rank,  # x eksenine dünya sıralaması eklenir.
        y=dataframe.research,  # y eksenine research skoru eklenir.
        z=dataframe.citations,  # z eksenine citations skoru eklenir.
        mode='markers',  # marker -> nokta demektir.
        marker=dict(
            size=dataframe.teaching,  # size eklenerek 4 boyutlu yapılır.
            color='rgb(255,0,0)',  # renk eklenir.
        )
    )

    data = [trace1]  # trace1 listenin içerisine koyulur.

    layout = go.Layout(
        margin=dict(  # kenarlardan bırakılan boşluktur.
            l=0,
            r=0,
            b=0,
            t=0  # hepsi 0 verildiği için kenarlardan boşluk bırakılmaz.
        )

    )
    fig = go.Figure(data=data,
                    layout=layout)  # data parametresine data değişkeni, layout parametresine layout değişkeni atanarak figür oluşturulur.

    iplot(fig)  # figür plot edilir.

def BarPlot():
    global timesData
    df2014 = timesData[timesData.year == 2014].iloc[:3,
             :]  # 2014 yılındaki ilk 3 üniversite seçilerek bir filtre oluşturulur, bu filtre dataya uygulanır.
    print(df2014)

    # create trace1
    trace1 = go.Bar(  # Bar türü seçilir.
        x=df2014.university_name,  # x eksenine üniversite isimleri koyulur.
        y=df2014.citations,  # y eksenine alıntı değerleri koyulur.
        name="citations",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 174, 255, 0.5)',  # renk ve saydamlık verilir.
                    line=dict(color='rgb(0,0,0)', width=1.5)),  # bar plotun çevresindeki renk ve çevresinin kalınlığı
        text=df2014.country)  # değerin üzerine gelindiğinde hoverda ülke adı yazır.

    # create trace2
    trace2 = go.Bar(
        x=df2014.university_name,  # x eksenine üniversite isimleri koyulur.
        y=df2014.teaching,  # y eksenine öğretme değerleri koyulur.
        name="teaching",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 255, 128, 0.5)',  # renk ve saydamlık verilir.
                    line=dict(color='rgb(0,0,0)', width=1.5)),  # bar plotun çevresindeki renk ve çevresinin kalınlığı
        text=df2014.country)  # değerin üzerine gelindiğinde hoverda ülke adı yazır.

    data = [trace1, trace2]  # trace1 ve trace2 data değişkenine liste olarak atanır.

    layout = go.Layout(barmode="group")  # barmode -> trace1 ve trace2'nin nasıl koyulacağının modudur.
    # group moduyla iki trace yan yana koyulur.

    fig = go.Figure(data=data,
                    layout=layout)  # data parametresine data değişkeni, layout parametresine layout değişkeni atanarak figür oluşturulur.

    iplot(fig)  # figür plot edilir.

def BoxPlot():
    global timesData
    x2015 = timesData[timesData.year == 2015]
    international = [float(each) for each in x2015.international]
    trace0 = go.Box(  # box plot türü seçilir.
        y=x2015.international,  # y eksen
        name='international score of universities in 2015',
        marker=dict(
            color='rgb(12, 12, 140)',
        )
    )
    trace1 = go.Box(
        y=x2015.research,
        name='research of universities in 2015',
        marker=dict(
            color='rgb(12, 128, 128)',
        )
    )
    data = [trace0, trace1]
    iplot(data)


def ScatterPlotMatrix():
    global timesData

    dataframe = timesData[timesData.year == 2015]
    data2015 = dataframe.loc[:, ["research", "citations", "teaching"]]
    data2015["index"] = np.arange(1, len(data2015) + 1)

    print(data2015.head())

    fig = ff.create_scatterplotmatrix(  # plotly'ın figure factory kütüphanesinden scatter plot matrix çağrılır.
        data2015,  # data verilir.
        diag='box',  # diagonal dikdörtgenin bir köşesinden diğer köşesine çizilen çizgidir. box plot türü seçilmiştir.
        index='index',  # index olarak oluşturulan index sütunu seçilir.
        colormap='Portland',  # derece arttıkça maviden kırmızıya giden bir colormap
        colormap_type='cat',
        # cat -> categorical demektir ve indeksteki her kategoriye renk haritasından bir renk atanır.
        height=700, width=700)  # boyut verildi.
    iplot(fig)  # figür plot edilir.

def ScatterPlot():
    global timesData
    df2014 = timesData[timesData.year == 2014].iloc[:100,
             :]  # timesData'daki 2014 yılındaki ilk 100 üniversiteden bir filtre oluşturulup,bu filtre dataya uygulanır.
    df2015 = timesData[timesData.year == 2015].iloc[:100,
             :]  # timesData'daki 2015 yılındaki ilk 100 üniversiteden bir filtre oluşturulup,bu filtre dataya uygulanır.
    df2016 = timesData[timesData.year == 2016].iloc[:100,
             :]  # timesData'daki 2016 yılındaki ilk 100 üniversiteden bir filtre oluşturulup,bu filtre dataya uygulanır.

    # creating trace1 -> 2014,2015 ve 2016 olmak üzere üç farklı data olduğundan 3 farklı trace yaratılacaktır.
    trace1 = go.Scatter(  # scatter türü seçilir.
        x=df2014.world_rank,  # x eksenine 2014 yılındaki ilk 100 üniversite koyulur.
        y=df2014.citations,  # y eksenine 2014 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2014",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 128, 255, 0.8)'),  # renk ve saydamlık verilir.
        text=df2014.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    # creating trace2
    trace2 = go.Scatter(
        x=df2015.world_rank,  # x eksenine 2015 yılındaki ilk 100 üniversite koyulur.
        y=df2015.citations,  # y eksenine 2015 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2015",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 128, 2, 0.8)'),  # renk ve saydamlık verilir.
        text=df2015.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    # creating trace3
    trace3 = go.Scatter(
        x=df2016.world_rank,  # x eksenine 2016 yılındaki ilk 100 üniversite koyulur.
        y=df2016.citations,  # y eksenine 2016 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2016",  # trace'in adı verilir.
        marker=dict(color='rgba(0, 255, 200, 0.8)'),  # renk ve saydamlık verilir.
        text=df2016.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    data = [trace1, trace2, trace3]  # trace1, trace2 ve trace3 data değişkenine liste olarak atanır.

    layout = dict(title='Citation vs world rank of top 100 universities with 2014, 2015 and 2016 years',
                  xaxis=dict(title='World Rank', ticklen=5, zeroline=False),
                  yaxis=dict(title='Citation', ticklen=5, zeroline=False)
                  # başlık, x ve y ekseninin bilgisi dictionary olarak layout değişkenine atanır.
                  )
    fig = dict(data=data,
               layout=layout)  # data parametresine data değişkeni, layout parametresine layout değişkeni atanarak figür oluşturulur.

    iplot(fig)  # figür plot edilir.

    # creating trace1 -> 2014,2015 ve 2016 olmak üzere üç farklı data olduğundan 3 farklı trace yaratılacaktır.
    trace1 = go.Scatter(  # scatter türü seçilir.
        x=df2014.world_rank,  # x eksenine 2014 yılındaki ilk 100 üniversite koyulur.
        y=df2014.total_score,  # y eksenine 2014 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2014",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 128, 255, 0.8)'),  # renk ve saydamlık verilir.
        text=df2014.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    # creating trace2
    trace2 = go.Scatter(
        x=df2015.world_rank,  # x eksenine 2015 yılındaki ilk 100 üniversite koyulur.
        y=df2015.total_score,  # y eksenine 2015 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2015",  # trace'in adı verilir.
        marker=dict(color='rgba(255, 128, 2, 0.8)'),  # renk ve saydamlık verilir.
        text=df2015.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    # creating trace3
    trace3 = go.Scatter(
        x=df2016.world_rank,  # x eksenine 2016 yılındaki ilk 100 üniversite koyulur.
        y=df2016.total_score,  # y eksenine 2016 yılındaki alıntı değerleri koyulur.
        mode="markers",  # marker modu seçilir, yani nokta şekli
        name="2016",  # trace'in adı verilir.
        marker=dict(color='rgba(0, 255, 200, 0.8)'),  # renk ve saydamlık verilir.
        text=df2016.university_name)  # bir değerin üzerine gelindiğinde üniversite adı gözükür.

    data = [trace1, trace2, trace3]  # trace1, trace2 ve trace3 data değişkenine liste olarak atanır.

    layout = dict(title='Total score vs world rank of top 100 universities with 2014, 2015 and 2016 years',
                  xaxis=dict(title='World Rank', ticklen=5, zeroline=False),
                  yaxis=dict(title='Total Score', ticklen=5, zeroline=False)
                  # başlık, x ve y ekseninin bilgisi dictionary olarak layout değişkenine atanır.
                  )
    fig = dict(data=data,
               layout=layout)  # data parametresine data değişkeni, layout parametresine layout değişkeni atanarak figür oluşturulur.

    iplot(fig)  # figür plot edilir.


Scatter3d()
BarPlot()
BoxPlot()
ScatterPlotMatrix()
ScatterPlot()