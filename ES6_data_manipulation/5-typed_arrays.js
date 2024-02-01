export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) throw new Error('Position outside range');
  return new DataView(new ArrayBuffer(length)).setInt8(position, value);
}
