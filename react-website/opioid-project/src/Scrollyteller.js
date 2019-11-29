import React, { Component } from "react";
import './style.css';
import SlideOne from './components/SlideOne.js';
import SlideOneDuplicate from './components/SlideOneDuplicate.js';
import PillsByCounty from './components/SlideTwo.js';
import TopPillDistributors from './components/SlideThree.js';
import TopPillManufacturers from './components/SlideFour.js';
import PillDeathsByCounty from './components/SlideFive.js';
import PillsPerPersonByCounty from './components/SlideSix.js';
import injectSheet from 'react-jss';
import { Scrollama, Step } from 'react-scrollama';

class Scrollyteller extends Component {
  constructor() {
    super();
    this.props = {};
    this.state = {
      steps: [<SlideOne/>, <SlideOneDuplicate/>, <PillsByCounty/>, <TopPillDistributors/>,
        <TopPillManufacturers/>, <PillDeathsByCounty/>, <PillsPerPersonByCounty/>
      ],
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
