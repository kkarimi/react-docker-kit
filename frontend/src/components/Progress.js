import React, { Component } from 'react';
import { findDOMNode } from 'react-dom';

import classSet from '../utils/classSet';

export default class Progress extends Component {
  componentDidUpdate() {
    var percent = parseInt(this.props.status);
    var deg = 360*percent/100 ;
    var element = findDOMNode(this.refs.progress);
    element.style.transform = 'rotate(-'+ deg +'deg)';
  }

  render() {
    const { status, result } = this.props;
    const percent = Math.floor(status);
    const classes = classSet({
      "progress-pie-chart": true,
      "gt-50": percent > 50
    });

    return (
      <div className="flex flex-center">
        <div className="mx-auto">
          <div className={classes}>
            <div className="ppc-progress">
              <div className="ppc-progress-fill" ref="progress"></div>
            </div>
            <div className="ppc-percents">
              <div className="pcc-percents-wrapper">
                <span>{percent + '%'}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
