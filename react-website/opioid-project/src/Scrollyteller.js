import React, { Component } from "react";
import './style.css';
import SlideOne from './components/SlideOne.js';
import SlideTwo from './components/SlideTwo.js';
import SlideThree from './components/SlideThree.js';
import injectSheet from 'react-jss';
import { Scrollama, Step } from 'react-scrollama';

class Scrollyteller extends Component {
  constructor() {
    super();
    this.props = {};
    this.state = {
      data: <SlideOne/>,
      steps: [<SlideOne/>, <SlideTwo />, <SlideThree />],
    };
    //this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount() {
  }

  onStepEnter = ({ element, data }) => {
    //element.style.backgroundColor = 'lightgoldenrodyellow';
    this.setState({ data });
  };

  onStepExit = ({ element }) => {
    element.style.backgroundColor = '#fff';
  };

  render() {
    const { data, steps } = this.state;

    return (
      <div className='main'>
        <div className='scroller'>
          <Scrollama onStepEnter={this.onStepEnter} onStepExit={this.onStepExit} offset={0.33} >
            {steps.map(value => (
              <Step data={value} key={value}>
                <div className='current'>
                  {value}
                </div>
              </Step>
            ))}
          </Scrollama>
        </div>
      </div>
    );
  }
}

export default Scrollyteller;
