import uuid
import json

script = '''
element.append('<h3>%(title)s</h3><div id="wordcloud-%(id)s"></div>');

setTimeout(function () {
  var data = %(words)s
  var domain = %(domain)s
  var fill = d3.scale.category20();
  var fontSize = function (count) {
      return d3.scale.linear().domain(domain)(count) * 100;
  }
  d3.layout.cloud().size([600,600])
      .words(data.map(function (x) { 
          var b = JSON.parse(JSON.stringify(x))
          b.size = fontSize(b.size);
          return b;
      }))
      .rotate(function() { return ~~(Math.random() * 2) * 90; })
      .font("Impact")
      .fontSize(function(d) { return d.size; })
      .on("end", draw)
      .start();

  function draw(words) {
    d3.select("#wordcloud-%(id)s").append("svg")
        .attr("width", 600)
        .attr("height", 600)
      .append("g")
        .attr("transform", "translate(300,300)")
      .selectAll("text")
        .data(words)
      .enter().append("text")
        .style("font-size", function(d) { return d.size + "px"; })
        .style("font-family", "Impact")
        .style("fill", function(d, i) { return fill(i); })
        .attr("text-anchor", "middle")
        .attr("transform", function(d) {
          return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
        })
        .text(function(d) { return d.text; });
  }
}, 1000)'''

def wordcloud(data, title, textField, sizeField):
    # sort data
    data = list(sorted(data, key=lambda x:x[sizeField]))
    smallest = data[0][sizeField]
    largest = data[-1][sizeField]
    data = [{'text': i[textField], 'size': i[sizeField]} for i in data]
    return script % {
        'title': title,
        'id': uuid.uuid4().get_hex(),
        'words': json.dumps(data),
        'domain': json.dumps([smallest, largest])
    }
