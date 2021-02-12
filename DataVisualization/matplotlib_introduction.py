Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
>>> import numpy as np
>>> x = np.array([3,4,5,5,4,6,8,8,3,2])
>>> y = x ** 2
>>> x
array([3, 4, 5, 5, 4, 6, 8, 8, 3, 2])
>>> y
array([ 9, 16, 25, 25, 16, 36, 64, 64,  9,  4], dtype=int32)
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000260FF2B0F28>]
>>> plt.show()
>>> x = np.linspace(1,50)
>>> y = x ** 2
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000260FFED5320>]
>>> plt.show()
>>> y = x ** 3
>>> plt.plot(x,y)
[<matplotlib.lines.Line2D object at 0x00000260FFDB5518>]
>>> plt.show()
>>> plt.scatter(x,y)
<matplotlib.collections.PathCollection object at 0x0000026081BC1E10>
>>> plt.show()
>>> plt.scatter(x,y,color='red')
<matplotlib.collections.PathCollection object at 0x0000026081D69518>
>>> plt.show()
>>> data = {"names" : ["BJP","CONG","AAP","OTHERS"], "seats" : [340,120,54,23]}
>>> plt.pie(data["names"])
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    plt.pie(data["names"])
  File "C:\Python37\lib\site-packages\matplotlib\pyplot.py", line 2805, in pie
    data is not None else {}))
  File "C:\Python37\lib\site-packages\matplotlib\__init__.py", line 1810, in inner
    return func(ax, *args, **kwargs)
  File "C:\Python37\lib\site-packages\matplotlib\axes\_axes.py", line 2799, in pie
    x = np.array(x, np.float32)
ValueError: could not convert string to float: 'BJP'
>>> plt.pie(data["seats"])
([<matplotlib.patches.Wedge object at 0x0000026081DEF278>, <matplotlib.patches.Wedge object at 0x0000026081DEF828>, <matplotlib.patches.Wedge object at 0x0000026081DEFCF8>, <matplotlib.patches.Wedge object at 0x0000026081EBB208>], [Text(-0.4468223593865701, 1.0051615686804878, ''), Text(-0.03538796233246417, -1.0994306217865484, ''), Text(0.9170671768293235, -0.6074436543271274, ''), Text(1.0900570806938779, -0.1475654459185513, '')])
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"])
([<matplotlib.patches.Wedge object at 0x0000026081F33588>, <matplotlib.patches.Wedge object at 0x0000026081F33A90>, <matplotlib.patches.Wedge object at 0x0000026081F33F60>, <matplotlib.patches.Wedge object at 0x0000026081F3F470>], [Text(-0.4468223593865701, 1.0051615686804878, 'BJP'), Text(-0.03538796233246417, -1.0994306217865484, 'CONG'), Text(0.9170671768293235, -0.6074436543271274, 'AAP'), Text(1.0900570806938779, -0.1475654459185513, 'OTHERS')])
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90)
([<matplotlib.patches.Wedge object at 0x0000026081F72A20>, <matplotlib.patches.Wedge object at 0x0000026081F72F28>, <matplotlib.patches.Wedge object at 0x0000026081F7C438>, <matplotlib.patches.Wedge object at 0x0000026081F7C908>], [Text(-1.0051615686804878, -0.44682235938656983, 'BJP'), Text(1.0994306217865484, -0.03538796233246424, 'CONG'), Text(0.6074436543271274, 0.9170671768293235, 'AAP'), Text(0.1475654459185514, 1.0900570806938779, 'OTHERS')])
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=True)
([<matplotlib.patches.Wedge object at 0x00000260820E1E48>, <matplotlib.patches.Wedge object at 0x00000260820EB390>, <matplotlib.patches.Wedge object at 0x00000260820EB860>, <matplotlib.patches.Wedge object at 0x00000260820EBD30>], [Text(-1.0051615686804878, -0.44682235938656983, 'BJP'), Text(1.0994306217865484, -0.03538796233246424, 'CONG'), Text(0.6074436543271274, 0.9170671768293235, 'AAP'), Text(0.1475654459185514, 1.0900570806938779, 'OTHERS')])
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=False)
([<matplotlib.patches.Wedge object at 0x0000026081F855F8>, <matplotlib.patches.Wedge object at 0x0000026081F2B748>, <matplotlib.patches.Wedge object at 0x0000026081F2BA90>, <matplotlib.patches.Wedge object at 0x0000026081F2B1D0>], [Text(1.0051615686804878, -0.44682235938657006, 'BJP'), Text(-1.0994306217865484, -0.0353879623324641, 'CONG'), Text(-0.6074436543271273, 0.9170671768293235, 'AAP'), Text(-0.14756544591855125, 1.0900570806938779, 'OTHERS')])
>>> plt.show()
>>> plt.title("Election Results 2021")
Text(0.5, 1.0, 'Election Results 2021')
>>> plt.legend()
No handles with labels found to put in legend.
<matplotlib.legend.Legend object at 0x0000026081D62668>
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=False)
([<matplotlib.patches.Wedge object at 0x0000026081D7C860>, <matplotlib.patches.Wedge object at 0x0000026081D7C4A8>, <matplotlib.patches.Wedge object at 0x0000026081EFAA20>, <matplotlib.patches.Wedge object at 0x0000026081D84390>], [Text(1.0051615686804878, -0.44682235938657006, 'BJP'), Text(-1.0994306217865484, -0.0353879623324641, 'CONG'), Text(-0.6074436543271273, 0.9170671768293235, 'AAP'), Text(-0.14756544591855125, 1.0900570806938779, 'OTHERS')])
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000026081F48A90>
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=False, autopct='%1.2f%%')
([<matplotlib.patches.Wedge object at 0x00000260FFDBEA90>, <matplotlib.patches.Wedge object at 0x00000260FFDCECF8>, <matplotlib.patches.Wedge object at 0x00000260FFDCE048>, <matplotlib.patches.Wedge object at 0x00000260FFDB5438>], [Text(1.0051615686804878, -0.44682235938657006, 'BJP'), Text(-1.0994306217865484, -0.0353879623324641, 'CONG'), Text(-0.6074436543271273, 0.9170671768293235, 'AAP'), Text(-0.14756544591855125, 1.0900570806938779, 'OTHERS')], [Text(0.5482699465529933, -0.24372128693812908, '63.31%'), Text(-0.5996894300653899, -0.019302524908616777, '22.35%'), Text(-0.3313329023602512, 0.5002184600887218, '10.06%'), Text(-0.08049024322830067, 0.5945765894693879, '4.28%')])
>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000026081F3FDA0>
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=False, autopct='%1.2f%%', explode=(0,0,0.3,0))
([<matplotlib.patches.Wedge object at 0x00000260FF30D940>, <matplotlib.patches.Wedge object at 0x00000260FF2BCA20>, <matplotlib.patches.Wedge object at 0x00000260FF2BC4A8>, <matplotlib.patches.Wedge object at 0x00000260F7111A90>], [Text(1.0051615686804878, -0.44682235938657006, 'BJP'), Text(-1.0994306217865484, -0.0353879623324641, 'CONG'), Text(-0.7731101055072529, 1.1671764068736845, 'AAP'), Text(-0.14756544591855125, 1.0900570806938779, 'OTHERS')], [Text(0.5482699465529933, -0.24372128693812908, '63.31%'), Text(-0.5996894300653899, -0.019302524908616777, '22.35%'), Text(-0.49699935354037683, 0.7503276901330828, '10.06%'), Text(-0.08049024322830067, 0.5945765894693879, '4.28%')])

>>> plt.legend()
<matplotlib.legend.Legend object at 0x0000026081D69F28>
>>> plt.show()
>>> plt.pie(data["seats"], labels=data["names"], startangle=90, counterclock=False, autopct='%1.2f%%', explode=(0,0,0.3,0), shadow=True)
([<matplotlib.patches.Wedge object at 0x00000260FFDAD5F8>, <matplotlib.patches.Wedge object at 0x00000260FFDC1048>, <matplotlib.patches.Wedge object at 0x00000260FFDC19E8>, <matplotlib.patches.Wedge object at 0x00000260FFDD13C8>], [Text(1.0051615686804878, -0.44682235938657006, 'BJP'), Text(-1.0994306217865484, -0.0353879623324641, 'CONG'), Text(-0.7731101055072529, 1.1671764068736845, 'AAP'), Text(-0.14756544591855125, 1.0900570806938779, 'OTHERS')], [Text(0.5482699465529933, -0.24372128693812908, '63.31%'), Text(-0.5996894300653899, -0.019302524908616777, '22.35%'), Text(-0.49699935354037683, 0.7503276901330828, '10.06%'), Text(-0.08049024322830067, 0.5945765894693879, '4.28%')])
>>> plt.show()
>>> plt.bar(data['names'], data['labels'])
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    plt.bar(data['names'], data['labels'])
KeyError: 'labels'
>>> plt.bar(data['names'], data['seats'])
<BarContainer object of 4 artists>
>>> plt.show()
>>> plt.hist(data['seats'])
(array([2., 0., 0., 1., 0., 0., 0., 0., 0., 1.]), array([ 23. ,  54.7,  86.4, 118.1, 149.8, 181.5, 213.2, 244.9, 276.6,
       308.3, 340. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> age = [4,5,3,12,34,45,33,6,8,9,16,18,91,23,4,6,8,9,12,45,32,56,76]
>>> plt.hist(age)
(array([10.,  4.,  1.,  3.,  2.,  0.,  1.,  0.,  1.,  1.]), array([ 3. , 11.8, 20.6, 29.4, 38.2, 47. , 55.8, 64.6, 73.4, 82.2, 91. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> plt.hist(age, width=0.9)
(array([10.,  4.,  1.,  3.,  2.,  0.,  1.,  0.,  1.,  1.]), array([ 3. , 11.8, 20.6, 29.4, 38.2, 47. , 55.8, 64.6, 73.4, 82.2, 91. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> plt.hist(age, width=9)
(array([10.,  4.,  1.,  3.,  2.,  0.,  1.,  0.,  1.,  1.]), array([ 3. , 11.8, 20.6, 29.4, 38.2, 47. , 55.8, 64.6, 73.4, 82.2, 91. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> plt.hist(age, width=7)
(array([10.,  4.,  1.,  3.,  2.,  0.,  1.,  0.,  1.,  1.]), array([ 3. , 11.8, 20.6, 29.4, 38.2, 47. , 55.8, 64.6, 73.4, 82.2, 91. ]), <a list of 10 Patch objects>)
>>> plt.show()
>>> 
