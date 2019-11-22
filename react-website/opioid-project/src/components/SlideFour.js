import React, { Component } from "react";

class TopPillManufacturers extends Component {
  constructor() {
    super();
    this.state = { };
  }

  componentDidMount() { }

  render() {

      //<style>
            //.table-wrapper-2 {
            //display: block;
            //max-height: 300px;
            //overflow-y: auto;
            //-ms-overflow-style: -ms-autohiding-scrollbar;
        //}
      //</style>

          //{% for report_line in ui_data.slide5 %}
            //<tr>
              //<th scope="row">{{ report_line['manufacturer'] }}</th>
              //<td>{{ report_line['total_count'] }}</td>
              //<td>{{ report_line['percentage'] }}</td>
            //</tr>
          //{% endfor %}


    return (
      <div>
        <section className="section team bg-shape-two" id="slide5">
          <div className="container">
            <div className="row">
              <div className="col-12">
                <div className="section-title">
                  <h2 >Top Pill Manufacturers</h2>
                  <p >Five companies produced approximately 95% percent of the opioids:
                                Mallinckrodt; Allergan, Inc.; Endo Pharmaceuticals, Inc., Purdue Pharma LP
                                and Amneal Pharmaceuticals, Inc..</p>
                </div>
              </div>
            </div>
            <div className="card"  style={{width:"90%"}}>
              <div className="card-body" >
                            <table id="manufacturer" className="table table-striped table-bordered" >

                                <thead className="mdb-color lighten-4">
                                    <tr>
                                        <th className="th-lg">Manufacturer</th>
                                        <th className="no-sort th-lg">Pills</th>
                                        <th className="th-lg">Percent of Market</th>

                                    </tr>
                                </thead>
                                <tbody>
                                </tbody>
                            </table>
              </div>
            </div>
          </div>
        </section>
      </div>
    )
  }
}

export default TopPillManufacturers;
