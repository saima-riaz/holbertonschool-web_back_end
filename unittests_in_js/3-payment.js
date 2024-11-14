const Utils = require('./utils');

function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const result = Utils.calculateNumber('sum', totalAmount, totalShipping);
  console.log(`The total is: ${result}`);
}

module.exports = sendPaymentRequestToApi;
