from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import shutil
import uuid
from slugify import slugify
import PyPDF2

#Initialize FastAPI app
app = FastAPI()

#Directory for storing uploaded files
UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

MAX_FILE_SIZE = 10 * 1024 * 1024

def is_valid_pdf(file_path):
	"""Check if the file is valid PDF."""
	try: 
		with open(file_path, "rb") as f:
			PyPDF2.PdfReader(f)
		return True
	except Exception:
		return False

@app.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File(...)):
	if file.content_type != "application/pdf":
		raise HTTPException(status_code=400, detail="Only PDFs are allowed")
	
	# Read the content to check file size
	content = await file.read()
	if len(content) > MAX_FILE_SIZE:
		raise HTTPException(status_code=413, detail="File too large.")
	
	# Generate a safe filename
	filename = f"{uuid.uuid4()}-{slugify(file.filename)}"
	file_location = os.path.join(UPLOAD_DIR, filename)

	# Save the file
	with open(file_location, "wb") as buffer:
		buffer.write(content)

	# Validate PDF
	if not is_valid_pdf(file_location):
		os.remove(file_location)
		raise HTTPException(status_code=400, detail="Uploaded file is not a valid PDF.")
	
	return {"info": f"File '{filename}' has been uploaded succesfully."}

# Define root for the home page
@app.get("/")
def read_root():
	return {"message": "Hello, FastAPI!"}

# Define another route that accepts a path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}




