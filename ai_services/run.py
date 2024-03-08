import os
import sys

#Get current dir path
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to sys.path.
sys.path.append(parent)

from ai_services import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)