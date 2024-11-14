export function calculateNumber(type, a, b) {
  // Round the numbers before performing the operation
  const roundedA = Math.round(a);
  const roundedB = Math.round(b);

  if (type === 'SUM') {
    return roundedA + roundedB;
  }
  if (type === 'SUBTRACT') {
    return roundedA - roundedB;
  }
  if (type === 'DIVIDE') {
    if (roundedB === 0) {
      return 'Error';
    }
    // Perform division and round the result
    return Math.floor(roundedA / roundedB); // Use Math.floor to ensure no fractional result
  }
}
