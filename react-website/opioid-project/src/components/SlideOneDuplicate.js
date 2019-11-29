import React, { Component } from "react";

class SlideOneDuplicate extends Component {
  constructor() {
    super();
    this.state = {
      data: "The opioid crisis in america"
    };
  }

  componentDidMount() {
  }

  render() {
    return (
      <div>
        <section className="banner " id="home">
          <div className="container">
            <div className="row">
              <div className="col-md-8 align-self-center">
              </div>
                <div className="" style={{position: 'sticky', textAlign: 'center', backgroundColor: 'yellow', border: '1px solid', zIndex: '999'}}>
                  THIS IS A BOX WITH CONTENT CENTERED IN THE MIDDLE OF THE SCREEN.
                </div>

            </div>
          </div>
        </section>
      </div>
    )
  }
}

export default SlideOneDuplicate;
