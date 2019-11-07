//import React from 'react';
//import ReactDOM from 'react-dom';
//import './index.css';
//import App from './App';
//import * as serviceWorker from './serviceWorker';

//ReactDOM.render(<App />, document.getElementById('root'));

//// If you want your app to work offline and load faster, you can change
//// unregister() to register() below. Note this comes with some pitfalls.
//// Learn more about service workers: https://bit.ly/CRA-PWA
//serviceWorker.unregister();

import React, { PureComponent } from 'react';
import ReactDOM from 'react-dom';
import injectSheet from 'react-jss';
import { Scrollama, Step } from 'react-scrollama';

const styles = {
  main: {
    padding: '70vh 2vw',
    display: 'flex',
    fontFamily: 'Helvetica',
    justifyContent: 'space-between',
  },
  graphic: {
    flexBasis: '60%',
    position: 'sticky',
    width: '100%',
    padding: '5rem 0',
    top: '160px',
    alignSelf: 'flex-start',
    backgroundColor: '#aaa',
    '& p': {
      fontSize: '5rem',
      textAlign: 'center',
      color: '#fff',
    },
  },
  scroller: {
    flexBasis: '35%',
  },
  step: {
    margin: '0 auto 2rem auto',
    paddingTop: 200,
    paddingBottom: 200,
    border: '1px solid #333',
    '& p': {
      textAlign: 'center',
      padding: '1rem',
      fontSize: '1.5rem',
    },
    '&:last-child': {
      marginBottom: 0,
    },
  },
};

class Graphic extends PureComponent {
  state = {
    data: 0,
    steps: [10, 20, 30],
  };

  onStepEnter = ({ element, data }) => {
    element.style.backgroundColor = 'lightgoldenrodyellow';
    this.setState({ data });
  };

  onStepExit = ({ element }) => {
    element.style.backgroundColor = '#fff';
  };

  render() {
    const { data, steps } = this.state;
    const { classes } = this.props;

    return (
      <div className={classes.main}>
        <div className={classes.scroller}>
          <Scrollama onStepEnter={this.onStepEnter} onStepExit={this.onStepExit} offset={0.33} debug>
            {steps.map(value => (
              <Step data={value} key={value}>
                <div className={classes.step}>
                  <p>step value: {value}</p>
                </div>
              </Step>
            ))}
          </Scrollama>
        </div>
        <div className={classes.graphic}>
          <p>{data}</p>
        </div>
      </div>
    );
  }
}

const StyledGraphic = injectSheet(styles)(Graphic);

ReactDOM.render(<StyledGraphic />, document.getElementById('root'));
