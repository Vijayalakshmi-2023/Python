# Format: {resume_id: {"skills": [...], "experience": ...}}
resumes = {
    101: {"skills": ["Python", "Django", "SQL"], "experience": 3},
    102: {"skills": ["JavaScript", "React", "Node.js"], "experience": 5},
    103: {"skills": ["Python", "Flask", "SQL"], "experience": 2},
    104: {"skills": ["Java", "Spring", "SQL"], "experience": 4},
    105: {"skills": ["C++", "Python", "Machine Learning"], "experience": 6},
}
# Search resumes with required skills
def search_by_skills(required_skills):
    matched_resumes = []
    for resume_id, resume_info in resumes.items():
        if all(skill in resume_info["skills"] for skill in required_skills):
            matched_resumes.append(resume_id)
    return matched_resumes

# Filter resumes by experience range
def filter_by_experience(min_exp, max_exp):
    matched_resumes = [resume_id for resume_id, resume_info in resumes.items()
                       if min_exp <= resume_info["experience"] <= max_exp]
    return matched_resumes

# Search and filter resumes based on skills and experience
def search_resumes(required_skills, min_exp, max_exp):
    # Get resumes that match the skills
    skill_matches = search_by_skills(required_skills)
    # Filter these resumes by experience
    experience_matches = [resume_id for resume_id in skill_matches
                          if resumes[resume_id]["experience"] >= min_exp and resumes[resume_id]["experience"] <= max_exp]
    return experience_matches
# Search resumes with required skills
required_skills = ["Python", "SQL"]
print("Resumes matching required skills:", search_by_skills(required_skills))

# Filter resumes by experience range (e.g., 3 to 5 years)
print("\nResumes with experience between 3 and 5 years:", filter_by_experience(3, 5))

# Search resumes with both required skills and experience range
required_skills = ["Python", "SQL"]
print("\nResumes matching skills and experience (3-5 years):", search_resumes(required_skills, 3, 5))
