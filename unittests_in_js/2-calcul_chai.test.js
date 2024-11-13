const { expect } = require('chai');
const calculateNumber = require('./0-calcul.js');

describe('calculateNumber', function () {
  it('should return 4 when inputs are (1, 3)', function () {
    expect(calculateNumber(1, 3)).to.equal(4);
  });

  it('should return 5 when inputs are (1, 3.7)', function () {
    expect(calculateNumber(1, 3.7)).to.equal(5);
  });

  it('should return 5 when inputs are (1.2, 3.7)', function () {
    expect(calculateNumber(1.2, 3.7)).to.equal(5);
  });

  it('should return 6 when inputs are (1.5, 3.7)', function () {
    expect(calculateNumber(1.5, 3.7)).to.equal(6);
  });

  it('should handle edge cases with negative numbers', function () {
    expect(calculateNumber(-1.4, -3.6)).to.equal(-5);
  });
});
