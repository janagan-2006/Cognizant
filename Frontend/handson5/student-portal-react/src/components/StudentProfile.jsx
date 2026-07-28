import { useState } from 'react';

function StudentProfile() {
  const [profile, setProfile] = useState({
    name: '',
    email: '',
    semester: ''
  });

  function handleChange(e) {
    const { name, value } = e.target;
    setProfile((prev) => ({ ...prev, [name]: value }));
  }

  return (
    <section id="profile" className="profile-section">
      <h2>Student Profile</h2>
      <form>
        <label>
          Name
          <input
            type="text"
            name="name"
            value={profile.name}
            onChange={handleChange}
            placeholder="Your name"
          />
        </label>

        <label>
          Email
          <input
            type="email"
            name="email"
            value={profile.email}
            onChange={handleChange}
            placeholder="you@example.com"
          />
        </label>

        <label>
          Semester
          <input
            type="number"
            name="semester"
            value={profile.semester}
            onChange={handleChange}
            placeholder="e.g. 6"
            min="1"
            max="8"
          />
        </label>
      </form>

      <div className="profile-preview">
        <p><strong>Name:</strong> {profile.name || '—'}</p>
        <p><strong>Email:</strong> {profile.email || '—'}</p>
        <p><strong>Semester:</strong> {profile.semester || '—'}</p>
      </div>
    </section>
  );
}

export default StudentProfile;