import { calculateNumber } from './2-calcul_chai.js';
import { expect } from 'chai';

describe('calculateNumber', () => {
  it('should return the sum when type is SUM', () => {
    expect(calculateNumber('SUM', 1.4, 2.6)).to.equal(4);  // 1.4 + 2.6 = 4
  });

  it('should return the difference when type is SUBTRACT', () => {
    expect(calculateNumber('SUBTRACT', 5.5, 2.2)).to.equal(4);  // 5.5 - 2.2 = 3.3 -> rounded to 4
  });

  it('should return the division result when type is DIVIDE', () => {
    expect(calculateNumber('DIVIDE', 4.5, 2)).to.equal(2);  // 4.5 / 2 = 2.25 -> rounded to 2 (Math.floor)
  });

  it('should return "Error" when dividing by zero', () => {
    expect(calculateNumber('DIVIDE', 5, 0)).to.equal('Error');  // Division by zero
  });
});
