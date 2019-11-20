import React, { Component } from "react";

class SlideOne extends Component {
  constructor() {
    super();
    this.state = { };
  }

  componentDidMount() { }

  render() {
    return (
      <div>
        <section className="banner bg-1" id="home">
          <div className="container">
            <div className="row">
              <div className="col-md-8 align-self-center">
                <div className="content-block">
                  <h1>Analysis of the pain pill Crisis</h1>
                  <h5>Due to increases in opioid prescriptions for pain management and its abuse, the opioid epidemic
                              has become a major public health problem in the United States of America (USA)[1,2].
                              In 2014, 61% of 47,055 total drug overdose deaths involved opioids[3].</h5>
                </div>
              </div>

            </div>
          </div>
        </section>
      </div>
    )
  }
}

export default SlideOne;
