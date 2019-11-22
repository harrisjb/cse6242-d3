import React, { Component } from "react";

class PillDeathsByCounty extends Component {
  constructor() {
    super();
    this.state = { };
  }

  componentDidMount() { }

  render() {

            //<style>
                //.states {
                    //fill: none;
                    //stroke: #000;
                    //stroke-linejoin: round;
                //}

                //.counties {
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

            //<script src="../static/js/d3.v5.min.js"></script>
            //<script src="../static/js/d3-scale-chromatic.v1.min.js"></script>
            //<script src="../static/js/topojson.v2.min.js"></script>
            //<script src="../static/js/d3-tip.min.js"></script>

                //<div id='legend-container-s4'></div>
                //<div id='map-container-s4'></div>

        //<script>

            //// set the dimensions and margins of the graph
            //var margin = {top: 20, bottom: 40, left: 40, right: 80},
                //width = 1000 - margin.left - margin.right,
                //height = 600 - margin.top - margin.bottom;


            //var svg_s4 = d3.select("#map-container-s4").append("svg")
                //.attr("width", width + margin.left + margin.right)
                //.attr("height", height + margin.top + margin.bottom)
                //.append("g")
                //.attr("transform", "translate(" + (margin.left -130) + "," + margin.top + ")");

            //var tool_tip_s4 = d3.tip()
                //.attr("class", "d3-tip")
                //.offset([-8, 0])
                //.html(function (d) {
                    //county_id = d['id'];
                    //pill_data = pills_s4[county_id];
                    //count = pill_data[0];
                    //state = pill_data[1];
                    //county = pill_data[2];
                    //return "Location: " + county + ", "+state+"<br/>Deaths: " + count;
                //});


            ////svg_s4.call(tool_tip_s4);

            //pills_s4 = {};

            //var projection_s4 = d3.geoAlbersUsa();
            //var path_s4 = d3.geoPath().projection(projection_s4);

            ////DPH FIX ME Set this later
            //max_pills_s4 = 40;
            //min_pills_s4 = 1;
            //var promises_s4 = [
                //d3.json("./data/counties-10m.json"),
                //d3.csv("./data/Mortality_2006_2012.csv", function (d) {
                    //pills_s4[d.county_id]=[d['deaths'],d['state'],d['county']];
                //})
            //];

            //colorScheme_s4 = ['#e5e49e','#dcce05','#d9b70b','#d6a011','#d28917','#cf721d','#c84429','#c52d2f','#bf003b'];
            //colorScheme_s4 = ['#ffffff','#f8f8f8','#feeff8','#c2c5e0','#95b0d4','#5a9ac5','#478ebe','#0f6756','#083629'];
            ////colorScheme = ['#4d004b','#810f7c','#88419d','#8c6bb1','#8c96c6','#9ebcda','#bfd3e6','#e0ecf4','#f7fcfd']

            //Promise.all(promises_s4).then(ready);

            //function ready(promise_data){
               //us = promise_data[0];
               //render_chart()
            //}

            //function render_chart() {

                //mapScale_s4 = d3.scaleLog()
                    //.domain([min_pills_s4, max_pills_s4])
                    //.range([0, 8]);

                //svg_s4.append("g")
                    //.attr("class", "states")
                    //.attr("class", "counties")
                    //.selectAll("path")
                    //.data(topojson.feature(us, us.objects.counties).features)
                    //.enter()
                    //.append("path")
                    //.on('mouseover', tool_tip_s4.show)
                    //.on('mouseout', tool_tip_s4.hide)
                    //.attr("fill", function (d) {
                        //state = d['id'];
                        //pill_data = pills_s4[state];
                        //count=0;
                        //if (typeof(pill_data) !== "undefined"){
                           //count = pill_data[0];
                        //}
                        ////console.log(count)
                        //log = 0;
                        //log = Math.round(mapScale_s4(count));
                        //log = log === -Infinity ? 0 : log;

                        //if (typeof count === 'undefined'){
                            //log=0
                        //}
                        //if (log >8){
                            //log=8
                        //}
                        ////console.log("State="+state+" count="+count+" log="+log+" color="+colorScheme[log]);

                        //return colorScheme_s4[log];
                    //})
                    //.attr("d", path_s4);

                //svg_s4.append("path")
        //            .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
        //            .attr("class", "states")	//Mesh state boundaries to prevent duplicate paths for borders
        //            .attr("d", path_s4);

                //svg_s4.append("path")
                    //.data(topojson.feature(us, us.objects.nation).features)
        //            .attr("class", "states")
        //            .attr("d", path_s4);

            //}

            //grid_size_s4 = 30;

            //var legend_s4 = svg_s4.append("g")
                //.attr("transform", "translate(" + (width + margin.left + margin.right) + "," + margin.top + ")")
                //.selectAll(".legend")
                //.data([0, 1, 10, 15, 20, 25, 30, 35, 40])
                //.enter();

            //legend_s4.append("rect")
                //.attr("x", -150)
                //.attr("y", function (d, i) {
                    //return (grid_size_s4 * i) + 160;
                //})
                //.attr("width", grid_size_s4)
                //.attr("height", grid_size_s4)
                //.style("fill", function (d, i) {
                    //return colorScheme_s4[i];
                //});

            //legend_s4.append("text")
                //.attr("class", "mono")
                //.text(function (d,i) {
                    //ret_val = d3.format(",")(d);
                    //if(i===8){
                        //ret_val = ret_val + ' +'
                    //}
                    //return ret_val
                //})
                //.attr("x", -110)
                //.attr("y", function (d, i) {
                    //return (grid_size_s4 * i) + 180;
                //});

            //legend_s4.append("text")
                //.attr("text-anchor", "middle")
                //.attr("font-family", "sans-serif")
                //.attr("font-size", "16px")
                //.attr("font-weight", "500")
                ////.attr("transform", "translate("+ (grid_size+10) +","+(height-10)+")")
                //.attr("x", -120)
                //.attr("y", 150)
                //.text("Deaths");

        //</script>


    return (
      <div>
        <section className="section section bg-2" id="slide4a">
            <div className="section-title">
                <h2>Opioid Deaths</h2>
                <p>Cumulative Opioid death rate 2006 - 2012</p>
            </div>
          <div className="container">
        </div>
        </section>
      </div>
    )
  }
}

export default PillDeathsByCounty;
