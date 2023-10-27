def student_photo_upload(instance, filename):
    return f"student_photos/{instance.id}/{filename}"


def student_resume_upload(instance, filename):
    return f"student_resumes/{instance.id}/{filename}"
