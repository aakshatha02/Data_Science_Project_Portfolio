import openai
from fastapi import Depends, File, UploadFile, HTTPException, Body, APIRouter
from sqlalchemy.orm import Session
from document_processing import extract_text_from_pdf
from utils.db import get_db
from models.all_models import User, LearningStyle, Conversation
import os
from configs.load_config import get_config

router = APIRouter()
_, openai_conf, _ = get_config()

@router.post("/ask_gpt/")
async def ask_gpt(
        message: str = Body(..., embed=True),
        pre_message: str = Body(None, embed=True),
        user_id: str = Body(..., embed=True),
        document: UploadFile = File(None),
        db: Session = Depends(get_db)
):

    user_data = db.query(User).filter(User.id == user_id).first()
    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    learning_style = db.query(LearningStyle).filter(LearningStyle.id == user_data.learning_style_id).first()
    if not learning_style:
        raise HTTPException(status_code=404, detail="Learning style not found for user")

    demographic_info = f"""
    My name is: {user_data.name}
    My age is: {user_data.age}
    My gender is: {user_data.gender}
    My study program (major) is: {user_data.course_program_study}
    My employment status is: {user_data.employment_status}
    My civil status is: {user_data.civil_status}
    My Learning Style is: {learning_style.learning_style_name}. {learning_style.description}.
    """

    full_message = demographic_info

    if pre_message:
        if pre_message[-1] != ".":
            pre_message += "."
        pre_message += "\n"

        full_message += pre_message

    full_message += message

    if document:
        try:
            with open(document.filename, "wb") as f:
                f.write(document.file.read())

            document_text = extract_text_from_pdf(document.filename)
            full_message += f"\nDocument Content:\n{document_text}\n"

        except Exception as e:
            return {"error": f"Error processing document: {str(e)}"}

        finally:
            os.remove(document.filename)

    response = openai.Completion.create(engine=openai_conf["engine"], prompt=full_message, max_tokens=150)
    answer = response.choices[0].text.strip()

    conversation = Conversation(user_id=user_id, user_question=message, gpt_answer=answer)
    db.add(conversation)
    db.commit()

    return {"chagpt_answer": answer, "question": message, "full_message": full_message}
