from fastapi import APIRouter, File, UploadFile

router = APIRouter()


@router.post("/send")
async def upload(file: UploadFile = File(...)):
    file_info = {
        "filename": file.filename,
        "content_type": file.content_type,
        "file_headers": file.headers,
    }

    return file_info


@router.post("/upload")
async def send_multiple_files(files: list[UploadFile] = File(...)):
    files_uploaded = []

    for file in files:
        file_info = {
            "filename": file.filename,
            "content_type": file.content_type,
            "file_size": file.size,
        }
        files_uploaded.append(file_info)

    return files_uploaded
