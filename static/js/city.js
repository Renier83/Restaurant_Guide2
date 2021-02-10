var csvfile = d3.select("#city_id").property("value");
csvfile = csvfile.replace(/\s+/g, '');

console.log("csvfile");
console.log("../static/data / " + csvfile + ".csv");

x_label = []
y_label = []

d3.csv("../static/data/" + csvfile + ".csv").then((data) => {
    data.forEach(function (d) {
        y_label.push(d.Type);
        x_label.push(d.Total)
    });

    console.log("y_label")
    console.log(y_label);

    var bar_trace = {
        y: y_label.slice(0, 10).reverse(),
        x: x_label.slice(0, 10).reverse(),
        // text: x_label.slice(0, 10).reverse(),
        type: "bar",
        orientation: "h",
    };

    var data = [bar_trace];

    var bar_layout = {
        title: "Number of Restaurants",
        margin: { t: 30, l: 150 }
    };

    Plotly.newPlot("bar", data, bar_layout);

});

