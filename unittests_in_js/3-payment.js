import { Utils } from './utils.js';  // Named import

export function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const total = Utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${total}`);
  console.log(Utils);
}
