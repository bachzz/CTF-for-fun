import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug import secure_filename
from hashlib import md5
from subprocess32 import run, STDOUT, PIPE, CalledProcessError

UPLOAD_FOLDER = '/tmp/data/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def getfilename(filename):
    name = secure_filename(filename)
    return md5(name + os.urandom(0x10)).hexdigest()

@app.route("/upload", methods=['POST'])
def upload():
    try:
        gif_file = request.files['gif_file']
        args_file = request.files['args_file']
        if gif_file and args_file:
            gif_filename = getfilename(gif_file.filename)
            gif_filename = os.path.join(app.config['UPLOAD_FOLDER'], gif_filename)
            gif_file.save(gif_filename)
            args_filename = getfilename(args_file.filename)
            args_filename = os.path.join(app.config['UPLOAD_FOLDER'], args_filename)
            args_file.save(args_filename)
            out_gif = os.path.join(app.config['UPLOAD_FOLDER'], getfilename("chung96vn"))
            try:
                command = '/home/gifremake/gifremake' + " " + gif_filename + " " + out_gif + " " + args_filename
                result = run(['su', 'gifremake', '-c', command], stdout=PIPE, stderr=STDOUT, timeout=4).stdout
                try:
                    os.unlink(out_gif)
                    os.unlink(gif_filename)
                    os.unlink(args_filename)
                except:
                    pass
                if "Successfully" in result:
                    return "Running complete Successfully!"
                else: return "Running complete!"
            except:
                try:
                    os.unlink(out_gif)
                    os.unlink(gif_filename)
                    os.unlink(args_filename)
                except:
                    pass
                return "Error when run program????"
            return "Upload Done"
    except:
        return "Upload False"

@app.route("/", methods=['GET'])       
def index():
    return render_template("/index.html")
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)