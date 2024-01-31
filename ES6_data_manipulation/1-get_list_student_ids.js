export default function getListStudentIds(Object) {
    if (!Array.isArray(Object)) {
      return [];
    }
    return Object.map((Object) => Object.id);
  }