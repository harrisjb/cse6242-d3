import React, { Component } from "react";

class SlideThree extends Component {
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
          //<td>{{ report_line['total_count'] }}</td>
          //<td>{{ report_line['percentage'] }}</td>
        //</tr>
      //{% endfor %}

    return (
      <div>
        <section class="section feature" id="slide2">
          <div class="container">
            <div class="row">
              <div class="col-12">
                <div class="section-title">
                  <h2>Top Pill Distributors</h2>
                  <p>From 2006 through 2012</p>
                </div>
              </div>
            </div>
            <div class="card"  style={{width:'100%'}} >
              <div class="card-body" >
                <table id="distributors" class="table table-striped table-bordered" style={{width: '90%'}}>

                    <thead class="mdb-color lighten-4">
                        <tr>
                            <th class="th-lg">Distributor</th>
                            <th class="no-sort th-lg">Pills</th>
                            <th class="th-lg">Percent of Market</th>

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

export default SlideThree;
