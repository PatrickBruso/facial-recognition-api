import os

from insightface.app import FaceAnalysis

from ..config import Config
from .cosine_similarity import *

face_app = FaceAnalysis(root=os.path.join(Config.PROJECT_DIR, "assets"))
face_app.prepare(ctx_id=0, det_size=(640, 640))
