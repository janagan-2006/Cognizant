function CourseCard({ name, code, credits, grade, hideButton = false }) {
  return (
    <article className="course-card">
      <h3>{name}</h3>
      <p>{code}</p>
      <span className="credits">{credits} credits</span>
      <span className="grade">Grade: {grade}</span>
      {!hideButton && (
        <button type="button" className="enroll-btn-inline">Enroll</button>
      )}
    </article>
  );
}

export default CourseCard;
