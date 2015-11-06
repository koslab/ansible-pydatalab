import json
import uuid

script = '''
element.append("<h3>%(title)s</h3><div id='barchart-%(id)s'></div>");

setTimeout(function (){ 
    var data = %(data)s;
    var svg = dimple.newSvg("#barchart-%(id)s", 590, 400);
    var myChart = new dimple.chart(svg, data);
    myChart.setBounds(60, 30, 510, 305)
    var x = myChart.addCategoryAxis("x", "%(xAxis)s");
    var y = myChart.addMeasureAxis("y", "%(yAxis)s");
    x.addOrderRule("%(orderBy)s", %(orderDesc)s);
    var series = myChart.addSeries(null, dimple.plot.bar);
    myChart.draw();
}, 1000);

'''

def bar(data, xAxis, yAxis, orderBy=None, orderDesc=True, title=None):

    return script % {
        'data': json.dumps(data),
        'title': title or '',
        'xAxis': xAxis,
        'yAxis': yAxis,
        'orderBy': orderBy or xAxis,
        'orderDesc': 'true' if orderDesc else 'false',
        'id': uuid.uuid4().get_hex()
    }
