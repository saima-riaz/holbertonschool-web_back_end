// "./2-get_students_by_loc.js"
export default function getStudentsByLocation(studentsList, city) {
  return studentsList.filter(student => student.location === city);
}
