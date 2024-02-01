export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || !set.size || !startString) return '';

  return [...set].filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length))
    .join('-');
}
