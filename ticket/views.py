from flask import Blueprint, request, render_template
from .models import Ticket
from datetime import datetime
from flask_login import login_user, login_required, logout_user, current_user
from website import db
from venue.models import Venue

ticket = Blueprint("ticket", __name__, url_prefix="/ticket")

