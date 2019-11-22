import React, { Component } from "react";

class PillsByCounty extends Component {
  constructor() {
    super();
    this.state = { };
  }

  componentDidMount() { }

  render() {
            //<style>
                //.states_s5 {
                    //fill: none;
                    //stroke: #000;
                    //stroke-linejoin: round;
                //}

                //.counties_s5 {
                    //fill: none;
                    //stroke: #fff;
                    //stroke-linejoin: round;
                //}

                //.d3-tip {
                    //line-height: 1;
                    //padding: 6px;
                    //background: rgba(0, 0, 0, 0.8);
                    //color: #fff;
                    //border-radius: 4px;
                    //font-size: 12px;
                //}

                //.d3-tip:after {
                    //box-sizing: border-box;
                    //display: inline;
                    //font-size: 10px;
                    //width: 100%;
                    //line-height: 1;
                    //color: rgba(0, 0, 0, 0.8);
                    //content: "\25BC";
                    //position: absolute;
                    //text-align: center;
                //}

                //.d3-tip.n:after {
                    //margin: -2px 0 0 0;
                    //top: 100%;
                    //left: 0;
                //}

            //</style>

            //<script src="./js/d3.v5.min.js"></script>
            //<script src="./js/d3-scale-chromatic.v1.min.js"></script>
            //<script src="./js/topojson.v2.min.js"></script>
            //<script src="./js/d3-tip.min.js"></script>



                //<div id='dropbox-container-s5'></div>
                //<div id='legend-container-s5'></div>
                //<div id='map-container-s5'></div>
        //<script>
        //{
            //// set the dimensions and margins of the graph
            //var margin = {top: 20, bottom: 40, left: 40, right: 80},
                //width = 1000 - margin.left - margin.right,
                //height = 600 - margin.top - margin.bottom;


            //var svg_s5 = d3.select("#map-container-s5").append("svg")
                //.attr("width", width + margin.left + margin.right )
                //.attr("height", height + margin.top + margin.bottom)
                //.append("g")
                //.attr("transform", "translate(" + (margin.left - 130)+ "," + margin.top + ")");

            //var tool_tip_s5 = d3.tip()
                //.attr("class", "d3-tip")
                //.offset([-8, 0])
                //.html(function (d) {
                    ////county = d.properties['name'];
                    //county_cd = d['id'];
                    //counts = pillsMap[county_cd];
                    //count = counts[current_year - 2006];
                    //state = counts[7];
                    //county = counts[8];
                    //return county + ", "+state+"<br/>Pills: " + numberWithCommas(count);
                //});

            //function numberWithCommas(x) {
                    //return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            //}

            //// Dropdown selection
            //d3.select("#dropbox-container-s5")
                    //.append("text")
                    //.style("font-size", "20px")
                    //.text("Year: ");

            //svg_s5.call(tool_tip_s5);

            //var pillsMap = {};
            //var current_year = 2006;

            //var projection = d3.geoAlbersUsa();
            //var path = d3.geoPath().projection(projection);

            ////DPH FIX ME Set this later
            //var max_pills_s5 = 425;
            //var min_pills_s5 = 1;
            //var promises_s5 = [
                //d3.json("./data/counties-10m.json"),
                //d3.csv("./data/pills_sold_by_county_and_years.csv", function (d) {
                    //pillsMap[d.County_cd]=[+d[2006],+d[2007],+d[2008],+d[2009],+d[2010],+d[2011],+d[2012],d.State_nm,d.County_nm];
                //})
            //];

            //var colorScheme_s5 = ['#f7fcfd','#e0ecf4','#bfd3e6','#9ebcda','#8c96c6','#8c6bb1','#88419d','#810f7c','#4d004b'];
            ////colorScheme_s5 = ['#4d004b','#810f7c','#88419d','#8c6bb1','#8c96c6','#9ebcda','#bfd3e6','#e0ecf4','#f7fcfd']

            //Promise.all(promises_s5).then(ready_s5);

            //function ready_s5(promise_data){
               //us = promise_data[0];
               //render_chart_s5(current_year)
            //}

            //function render_chart_s5(map_year) {
                //current_year = map_year;

                //mapScale_s5 = d3.scaleLog()
                    //.domain([min_pills_s5, max_pills_s5])
                    //.range([0, 8]);

                //svg_s5.append("g")
                    //.attr("class", "counties_s5")
                    //.selectAll("path")
                    //.data(topojson.feature(us, us.objects.counties).features)
                    //.enter()
                    //.append("path")
                    //.on('mouseover', tool_tip_s5.show)
                    //.on('mouseout', tool_tip_s5.hide)
                    //.attr("fill", function (d) {
                        //state = d['id'];
                        //counts = pillsMap[state];
                        //count = counts[map_year - 2006]
                        //log = 0;
                        //log = Math.round(mapScale_s5(count));
                        //log = log === -Infinity ? 0 : log;

                        //if (typeof count === 'undefined'){
                            //log=0
                        //}
                        //if (log >8){
                            //log=8
                        //}
                        ////console.log("State="+state+" count="+count+" log="+log+" color="+colorScheme_s5[log]);

                        //return colorScheme_s5[log];
                    //})
                    //.attr("d", path);

                //svg_s5.append("path")
        //            .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
        //            .attr("class", "states_s5")			//Mesh state boundaries to prevent duplicate paths for borders
        //            .attr("d", path);

                //svg_s5.append("path")
                    //.data(topojson.feature(us, us.objects.nation).features)
        //            .attr("class", "states_s5")
        //            .attr("d", path);


            //}

            //var grid_size = 30;

            //var legend = svg_s5.append("g")
                //.attr("transform", "translate(" + (width + margin.left + margin.right) + "," + margin.top + ")")
                //.selectAll(".legend")
                //.data([0, 5, 10, 20, 50, 75, 100, 125, 150])
                //.enter();

            //legend.append("rect")
                //.attr("x", -150)
                //.attr("y", function (d, i) {
                    //return (grid_size * i) +160;
                //})
                //.attr("width", grid_size)
                //.attr("height", grid_size)
                //.style("fill", function (d, i) {
                    //return colorScheme_s5[i];
                //});

            //legend.append("text")
                //.attr("class", "mono")
                //.text(function (d) {
                    //// Hack fix later
                    //if (d === 150) {
                        //return '150+'
                    //}
                    //return d3.format(",")(d)
                //})
                //.attr("x", -110)
                //.attr("y", function (d, i) {
                    //return (grid_size * i) + 180;
                //});

            //legend.append("text")
                //.attr("text-anchor", "middle")
                //.attr("font-family", "sans-serif")
                //.attr("font-size", "16px")
                //.attr("font-weight", "500")
                //.attr("x", -130)
                //.attr("y", 140)

                //.text("Pills");


            //var dropdownChange = function() {
                    //var range = d3.select(this).property('value');
                    //years = [2006,2007,2008,2009,2010,2011,2012]
                    //render_chart_s5(range)

            //};

            //var dropdown = d3.select("#dropbox-container-s5")
                    //.append("select")
                    //.on("change", dropdownChange)
                    //.selectAll("option")
                    //.data([2006,2007,2008,2009,2010,2011,2012]).enter()
                    //.append("option")
                    //.text(function (d) { return d; });

        //}
        //</script>

    return (
      <div>

        <section className="section section bg-2" id="slide5a">
          <div className="section-title">
              <h2>Pills Sold by County</h2>
              <p>Pills per person per year</p>
          </div>
          <div className="container">
          </div>
        </section>

      </div>
    )
  }
}

export default PillsByCounty;
