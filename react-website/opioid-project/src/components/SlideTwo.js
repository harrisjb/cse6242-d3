import React, { Component } from "react";

class SlideTwo extends Component {
  constructor() {
    super();
    this.state = { };
  }

  componentDidMount() { }

  render() {

            //<style>
                //.states {
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


        //<script>
        //{
            //// set the dimensions and margins of the graph
            //var margin = {top: 70, bottom: 40, left: 40, right: 80},
                //width = 1000 - margin.left - margin.right,
                //height = 600 - margin.top - margin.bottom;


            //var svg = d3.select("#map-container-s1").append("svg")
                //.attr("width", width + margin.left + margin.right + 500)
                //.attr("height", height + margin.top + margin.bottom)
                //.append("g")
                //.attr("transform", "translate(" + margin.left + "," + margin.top + ")");

            //var tool_tip = d3.tip()
                //.attr("class", "d3-tip")
                //.offset([-8, 0])
                //.html(function (d) {
                    //state = d.properties['name'];
                    //count = pills[state];
                    //return "State: " + state + "<br/>Pills: " + numberWithCommas(count);
                //});

            //function numberWithCommas(x) {
                    //return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            //}

            //svg.call(tool_tip);

            //var pillsMap = {};
            //var pills = {};

            //var projection = d3.geoAlbersUsa();
            //var path = d3.geoPath().projection(projection);

            ////DPH FIX ME Set this later
            //var max_pills = 30000;
            //var min_pills = 7000000;
            //var promises = [
                //d3.json("./data/states-10m.json"),
                //d3.csv("./data/pills_by_state.csv", function (d) {


                    //pillsMap[d.state]=[+d[2006],+d[2007],+d[2008],+d[2009],+d[2010],+d[2011],+d[2012]];
                //})
            //];

            ////var colorScheme = ['#f7fcfd','#e0ecf4','#bfd3e6','#9ebcda','#8c96c6','#8c6bb1','#88419d','#810f7c','#4d004b'];
            //var colorScheme = ['#4d004b','#810f7c','#88419d','#8c6bb1','#8c96c6','#9ebcda','#bfd3e6','#e0ecf4','#f7fcfd']

            //Promise.all(promises).then(ready);

            //function ready(promise_data){
               //us = promise_data[0];
               //render_chart(2006)
            //}

            //function render_chart(map_year) {
                //console.log("map_year="+map_year)
                //pills = {};
                //Object.keys(pillsMap).forEach(function(key) {
                    //value = pillsMap[key];
                    //index = map_year- 2006
                    //pills[key]=value[index]
                //});


                //var mapScale = d3.scaleLog()
                    //.domain([min_pills, max_pills])
                    //.range([0, 8]);

                //svg.append("g")
                    //.attr("class", "states")
                    //.selectAll("path")
                    //.data(topojson.feature(us, us.objects.states).features)
                    //.enter()
                    //.append("path")
                    //.on('mouseover', tool_tip.show)
                    //.on('mouseout', tool_tip.hide)
                    //.attr("fill", function (d) {
                        //state = d.properties['name'];
                        //count = pills[state];
                        //log = 0;
                        //log = Math.round(mapScale(count));
                        //log = log === -Infinity ? 0 : log;


                        ////console.log("State="+state+" count="+count+" log="+log+" color="+colorScheme[log]);
                        //return colorScheme[log];
                    //})
                    //.attr("d", path);
            //}

            //var grid_size = 30;

            //var legend = svg.append("g")
                //.attr("transform", "translate(" + (width + margin.left + margin.right) + "," + margin.top + ")")
                //.selectAll(".legend")
                //.data([1, 5, 10, 50, 100, 500, 1000, 2000, 10000])
                //.enter();

            //legend.append("rect")
                //.attr("x", 0)
                //.attr("y", function (d, i) {
                    //return (grid_size * i) + 30;
                //})
                //.attr("width", grid_size)
                //.attr("height", grid_size)
                //.style("fill", function (d, i) {
                    //return colorScheme[i];
                //});

            //legend.append("text")
                //.attr("class", "mono")
                //.text(function (d) {
                    //return d3.format(",")(d)
                //})
                //.attr("x", 40)
                //.attr("y", function (d, i) {
                    //return (grid_size * i) + 50;
                //});

            //legend.append("text")
                //.attr("text-anchor", "middle")
                //.attr("font-family", "sans-serif")
                //.attr("font-size", "16px")
                //.attr("font-weight", "500")
                ////.attr("transform", "translate("+ (grid_size+10) +","+(height-10)+")")
                //.text("Pills");

            //// when the input range changes update the rectangle
            //d3.select("#timeslide-s1")
                  //.on("input", function() {
                    //update_slider(+this.value);
                //});

            //function update_slider(value) {
                //console.log("slider val="+value)
                //years = [2006,2007,2008,2009,2010,2011,2012]
                //document.getElementById("range-s1").innerHTML=years[value];
                //render_chart(years[value])
            //}
        //}
        //</script>

    return (
      <div>

        <section className="about section bg-2" id="slide1">
          <div className="section-title">
              <h2>Pills Sold by State</h2>
              <p>This does <b>not consider population</b> it is just RAW pill count by state.</p>
          </div>

          <div className="container">
            <div id='title-container-s1'></div>
            <div id='dropbox-container-s1'>
                <input id="timeslide-s1" type="range" min="0" max="6" value="0" step="1"/>
                <br/>
                Year: <span id="range-s1">2006</span>
            </div>
            <div id='legend-container-s1'></div>
            <div id='map-container-s1'></div>
          </div>
        </section>
      </div>
    )
  }
}

export default SlideTwo;
