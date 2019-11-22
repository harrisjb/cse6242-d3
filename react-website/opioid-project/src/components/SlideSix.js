import React, { Component } from "react";

class PillsPerPersonByCounty extends Component {
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

                //<div id='legend-container_s3'></div>
                //<div id='map-container_s3'></div>

        //<script>

            //// set the dimensions and margins of the graph
            //var margin = {top: 20, bottom: 40, left: 40, right: 80},
                //width = 1000 - margin.left - margin.right,
                //height = 600 - margin.top - margin.bottom;


            //var svg_s3 = d3.select("#map-container_s3").append("svg")
                //.attr("width", width + margin.left + margin.right)
                //.attr("height", height + margin.top + margin.bottom)
                //.append("g")
                //.attr("transform", "translate(" + (margin.left -130) + "," + margin.top + ")");

            //var tool_tip_s3 = d3.tip()
                //.attr("class", "d3-tip")
                //.offset([-8, 0])
                //.html(function (d) {
                    //county_id = d['id'];
                    //pill_data = pills_s3[county_id];
                    //count = pill_data[0];
                    //state = pill_data[1];
                    //county = pill_data[2];
                    //return "Location: " + county + ", "+state+"<br/>Deaths: " + count;
                //});


            //svg_s3.call(tool_tip_s3);

            //pills_s3 = {};

            //var projection_s3 = d3.geoAlbersUsa();
            //var path_s3 = d3.geoPath().projection(projection_s3);

            ////DPH FIX ME Set this later
            //max_pills_s3 = 150;
            //min_pills_s3 = 1;
            //var promises_s3 = [
                //d3.json("./data/counties-10m.json"),
                //d3.csv("./data/pills_per_person_average_2006_2012.csv", function (d) {
                    ////County_cd,State_nm,County_nm,avgerage_pills
                    //pills_s3[d.County_cd]=[d['avgerage_pills'],d['State_nm'],d['County_nm']];
                //})
            //];

            //colorScheme_s3 = ['#e5e49e','#dcce05','#d9b70b','#d6a011','#d28917','#cf721d','#c84429','#c52d2f','#bf003b'];
            //colorScheme_s3 = ['#ffffff','#f8f8f8','#e2e2e2','#d2d2d2','#e2d5ea','#ebe3f3','#ce99c4','#953d4d','#753037'];
            ////colorScheme = ['#4d004b','#810f7c','#88419d','#8c6bb1','#8c96c6','#9ebcda','#bfd3e6','#e0ecf4','#f7fcfd']

            //Promise.all(promises_s3).then(ready_s3);

            //function ready_s3(promise_data){
               //us = promise_data[0];
               //render_chart_s3()
            //}

            //function render_chart_s3() {


                //mapScale_s3 = d3.scaleLog()
                    //.domain([min_pills_s3, max_pills_s3])
                    //.range([0, 8]);

                //svg_s3.append("g")
                    //.attr("class", "states")
                    //.attr("class", "counties")
                    //.selectAll("path")
                    //.data(topojson.feature(us, us.objects.counties).features)
                    //.enter()
                    //.append("path")
                    //.on('mouseover', tool_tip_s3.show)
                    //.on('mouseout', tool_tip_s3.hide)
                    //.attr("fill", function (d) {
                        //state = d['id'];
                        //pill_data = pills_s3[state];
                        //count=0;
                        //if (typeof(pill_data) !== "undefined"){
                           //count = pill_data[0];
                        //}
                        ////console.log(count)
                        //log = 0;
                        //log = Math.round(mapScale_s3(count));
                        //log = log === -Infinity ? 0 : log;

                        //if (typeof count === 'undefined'){
                            //log=0
                        //}
                        //if (log >8){
                            //log=8
                        //}
                        ////console.log("State="+state+" count="+count+" log="+log+" color="+colorScheme[log]);

                        //return colorScheme_s3[log];
                    //})
                    //.attr("d", path_s3);

                //svg_s3.append("path")
        //            .datum(topojson.mesh(us, us.objects.states, function(a, b) { return a !== b; }))
        //            .attr("class", "states")			//Mesh state boundaries to prevent duplicate paths for borders
        //            .attr("d", path_s3);

                //svg_s3.append("path")
                    //.data(topojson.feature(us, us.objects.nation).features)
        //            .attr("class", "states")
        //            .attr("d", path_s3);


            //}

            //grid_size_s3 = 30;

            //var legend_s3 = svg_s3.append("g")
                //.attr("transform", "translate(" + (width + margin.left + margin.right) + "," + margin.top + ")")
                //.selectAll(".legend")
                //.data([0, 1, 10, 15, 25, 50, 75, 100, 150])
                //.enter();

            //legend_s3.append("rect")
                //.attr("x", -150)
                //.attr("y", function (d, i) {
                    //return (grid_size_s3 * i) + 160;
                //})
                //.attr("width", grid_size_s3)
                //.attr("height", grid_size_s3)
                //.style("fill", function (d, i) {
                    //return colorScheme_s3[i];
                //});

            //legend_s3.append("text")
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
                    //return (grid_size_s3 * i) + 180;
                //});

            //legend_s3.append("text")
                //.attr("text-anchor", "middle")
                //.attr("font-family", "sans-serif")
                //.attr("font-size", "16px")
                //.attr("font-weight", "500")
                ////.attr("transform", "translate("+ (grid_size+10) +","+(height-10)+")")
                //.attr("x", -120)
                //.attr("y", 150)
                //.text("Pills");

        //</script>


    return (
      <div>

        <section className="section section bg-2" id="slide3a">
            <div className="section-title">
                <h2>Number of Pills Per Person Per Year</h2>
                <p>Average County yearly total 2006 - 2012</p>
            </div>
          <div className="container">

        </div>
        </section>
      </div>
    )
  }
}

export default PillsPerPersonByCounty;