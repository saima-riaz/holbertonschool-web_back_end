import { expect } from 'chai';
import { calculateNumber } from './2-calcul_chai.js'; // Use named import

describe('calculateNumber', function () {
  describe('SUM', function () {
    it('should return 6 when inputs are (SUM, 1.4, 4.5)', function () {
      expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
  });

  describe('SUBTRACT', function () {
    it('should return -4 when inputs are (SUBTRACT, 1.4, 4.5)', function () {
      expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
  });

  describe('DIVIDE', function () {
    it('should return 0.2 when inputs are (DIVIDE, 1.4, 4.5)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });

    it('should return "Error" when inputs are (DIVIDE, 1.4, 0)', function () {
      expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
  });
});
