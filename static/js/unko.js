createsvg();

function createsvg() {
  var svg = d3.select("#chart").append("svg")
    .attr({
      width: 640,
      height: 480,
    });

  var c1 = [
    "2017-10-23 12:00:00",
    "2017-10-23 12:01:00",
    "2017-10-23 12:02:00",
    "2017-10-23 12:03:00",
    "2017-10-23 12:04:00",
    "2017-10-23 12:05:00",
    "2017-10-23 12:06:00"
  ]

  var c2 = [143.0, 143.1, 143.2, 143.3, 143.4, 143.5, 143.6];

  var carray = [c1, c2]

  var line = d3.line()
    .x(function(d) { return d[0];})
    .y(function(d) { return d[1];});

  var path = svg.append("path")
    .attr({
      "d": line(carray),
      "stroke": "lightgreen",
      "stroke-width": 5,
    });
};
