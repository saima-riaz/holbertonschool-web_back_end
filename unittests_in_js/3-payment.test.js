const sinon = require('sinon');
const { expect } = require('chai');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with the correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    
    // Call the function to test
    sendPaymentRequestToApi(100, 20);
    
    // Verify that calculateNumber was called correctly
    expect(spy.calledOnceWithExactly('sum', 100, 20)).to.be.true;
    
    // Restore the spy
    spy.restore();
  });
});