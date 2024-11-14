function calculateNumber(type, a, b) {

  // Round both numbers
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  switch(type){
      case 'sum' :
          return roundedA + roundedB;
      case 'sub' :
          return roundedA - roundedB;
      case 'division' :
          if(roundedB === 0) {
              return "Error";
          }
          return roundedA / roundedB;
      default:
          throw new Error('Invalid operation type');
  }
}
module.exports = calculateNumber;