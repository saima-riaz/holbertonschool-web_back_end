export default function createInt8TypedArray(length, position, value) {
  if (position > length) {
    throw Error('Position outside range');
  }

  const int8View = new Int8Array(length);
  int8View[position] = value;
  const { buffer } = int8View;
  return new DataView(buffer, 0, length);
}
