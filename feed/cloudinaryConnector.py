import cloudinary
# Import the cloudinary.api for managing assets
import cloudinary.api
# Import the cloudinary.uploader for uploading assets
import cloudinary.uploader

cloudinary.config(
    cloud_name="devogzino",
    api_key="423542217966864",
    api_secret="cLRCG2AAlSOi43Vc6gHsNTgdzNc",
    secure=True,
)

# cloudinary.uploader.upload("https://upload.wikimedia.org/wikipedia/commons/a/ae/Olympic_flag.jpg", 
#   public_id = "olympic_flag")