from flask import Blueprint, request, render_template
from .models import Venue
from datetime import datetime
from website import db

venue = Blueprint("venue", __name__, url_prefix="/venue")