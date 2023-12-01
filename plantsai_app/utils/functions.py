import plantsai_app.config as config


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in config.allowed_extensions
