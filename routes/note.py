from bson import ObjectId
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi import APIRouter
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity
from fastapi.templating import Jinja2Templates

note = APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.notes.notes.find({})
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),
            "title": doc.get("title", "(no title)"),
            "desc": doc.get("desc", ""),
            "important": doc.get("important", False)
        })
    return templates.TemplateResponse(request=request, name="index.html", context={"newDocs": newDocs})


@note.post("/")
async def create_item(request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    inserted_note = conn.notes.notes.insert_one(formDict)
    return {"Success": True, "id": str(inserted_note.inserted_id)}

@note.put("/{id}")
async def update_item(id: str, request: Request):
    form = await request.form()
    formDict = dict(form)
    formDict["important"] = True if formDict.get("important") == "on" else False
    updated_note = conn.notes.notes.update_one({"_id": ObjectId(id)}, {"$set": formDict})
    return {"Success": True, "updated_count": updated_note.modified_count}

@note.delete("/{id}")
async def delete_item(id: str):
    deleted_note = conn.notes.notes.delete_one({"_id": ObjectId(id)})
    return {"Success": True, "deleted_count": deleted_note.deleted_count}