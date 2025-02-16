from sqlalchemy.orm import Session
from .models import Solution

def add_solution_to_db(db: Session, problem_id: str, file_path: str, language: str, user_id: str):
    solution = Solution(
        problem_id=problem_id,
        file_path=file_path,
        language=language,
        user_id=user_id
    )
    db.add(solution)
    db.commit()
    db.refresh(solution)