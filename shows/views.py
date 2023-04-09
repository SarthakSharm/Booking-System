from flask import Blueprint, request, render_template
from .models import Show
from datetime import datetime
from website import db

show  = Blueprint("show", __name__, url_prefix="/show")