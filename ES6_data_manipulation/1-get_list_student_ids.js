export default function getListStudentIds(arrayOfObjects) {
  if (typeof arrayOfObjects !== 'object' || arrayOfObjects === null) {
    return [];
  }
  return arrayOfObjects.map((value) => value.id);
}
