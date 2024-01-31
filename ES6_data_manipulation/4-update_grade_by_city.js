export default function updateStudentGradeByCity(studentsList, city, newGrades) {
  return studentsList
    .filter((student) => student.location === city)
    .map((student) => ({
      ...student,
      grade: (newGrades.find((grade) => grade.studentId === student.id) || {}).grade || 'N/A',
    }));
}
