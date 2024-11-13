import { expect } from 'chai';
import sinon from 'sinon';
import { Utils } from './utils.js';  // Named import
import { sendPaymentRequestToApi } from './3-payment.js';

describe('sendPaymentRequestToApi', function () {
  it('should call Utils.calculateNumber with the correct arguments', function () {
    const spy = sinon.spy(Utils, 'calculateNumber');
    
    // Call the function to test
    sendPaymentRequestToApi(100, 20);
    
    // Validate the spy was called correctly
    expect(spy.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    
    // Restore the spy after the test
    spy.restore();
  });
});