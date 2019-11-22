import React, { Component } from "react";

class TopPillDistributors extends Component {
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

      //{% for report_line in ui_data.slide2 %}
        //<tr>
          //<th scope="row">{{ report_line['distributor'] }}</th>
          //<td>{{ report_line['total_dosage'] }}</td>
          //<td>{{ report_line['percent_dosage'] }}</td>
          //<td>{{ report_line['total_gms'] }}</td>
          //<td>{{ report_line['percent_gms'] }}</td>
        //</tr>
      //{% endfor %}

    return (
      <div>
        <section className="cta-download bg-3 overlay" id="slide2">
          <div className="container">
            <div className="row">
              <div className="col-12">
                <div className="section-title">
                  <h2 style={{color:"white"}}>Top Pill Distributors</h2>
                  <p style={{color:"black"}}>Only six companies distributed 75.8% of the pills during this seven year period:
                                McKesson Corp., Walgreens, Cardinal Health, AmerisourceBergen, CVS and Walmart.
                            </p>
                </div>
              </div>
            </div>
            <div className="card"  style={{width:"90%"}}>
              <div className="card-body" >
                <table id="distributors" className="table table-striped table-bordered" >
                    <thead className="mdb-color lighten-4">
                        <tr>
                            <th className="th-lg">Distributor</th>
                            <th className="no-sort th-lg">Units</th>
                            <th className="th-lg">Units pct</th>
                            <th className="no-sort th-lg">Dosage gms</th>
                            <th className="th-lg">Dosage pct</th>
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

export default TopPillDistributors;
