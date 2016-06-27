import autobind from 'autobind-decorator';
import React, { Component } from 'react';
import io from 'socket.io-client';
import Progress from './components/Progress';

import { serverUrl, port } from './config';
let socket = io.connect(`${serverUrl}:${port}/cruncher`);

export default class App extends Component {
  constructor () {
    super();
    socket.on('server:event', data => {
      this.setState({data})
    });
  }

  state = {
    progress: 0
  };

  componentDidMount() {
    socket.on('connected', this._connected);
    socket.on('progress', this._progress);
  }


  @autobind
  _connected(e) {
    console.info('action: connected');
    if (e) {
      console.info(e);
    }
  }

  @autobind
  _progress(e) {
    console.info(e);
    if (e && e.status) {
     this.setState({
       progress: e.status
     });
    }
    if (e && e.status === 100) {
      this.setState({
       result: e.result
     });
    }
  }

  @autobind
  _reset() {
    this.setState({
      result: 0
    });
  }

  @autobind
  _doAction(e) {
    if (e) {
      this._reset();
      const { n1, n2 } = this.refs;
      fetch(`${serverUrl}:${port}/add/${n1.value}/${n2.value}`, {
        method: 'post'
      }).then(function(response) {
        console.info(response);
      }).catch(function(err) {
        console.info(err);
      });
        console.info('sending action: do crunching');
      }
  }

  renderCalc() {
    return (
      <div>
        <input type="text" ref="n1" defaultValue="0" className="flex-auto m1 field-light rounded-left"/>
        <span>+</span>
        <input type="text" ref="n2" defaultValue="1" className="flex-auto m1 field-light rounded-left"/>
        <button onClick={this._doAction}>Do it!</button>
      </div>
    );
  }

  renderProgress(){
    if (this.state.progress > 0 && this.state.progress < 100) {
      return (
        <Progress status={this.state.progress} result={this.state.result} />
      );
    }
    if (this.state.result > 0) {
      return (
        <div className="flex flex-center p2">
          <div className="col-6 mx-auto">
            <p className="m1">
              Result: {this.state.result}
            </p>
          </div>
        </div>
      );
    }
  }

  render() {
    return (
      <div className="flex flex-center p2" style={{ minHeight: '100vh' }}>
          <div className="bold p2 mx-auto bg-silver">
            <h1 className="center">Number Cruncher</h1>
            {this.renderCalc()}
            {this.renderProgress()}
          </div>
      </div>
    );
  }
}
