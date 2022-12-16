{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
      "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://0.0.0.0:1234/ (Press CTRL+C to quit)\n",
      " * Restarting with inotify reloader\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/share/anaconda3/lib/python3.7/site-packages/IPython/core/interactiveshell.py:3339: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, Response, render_template\n",
    "from jinja2.utils import Markup\n",
    "import os\n",
    "from joblib import load\n",
    "# from werkzeug import secure_filename\n",
    "from werkzeug.utils import secure_filename\n",
    "import pandas as pd\n",
    "\n",
    "app = Flask(__name__)\n",
    "PATH = os.getcwd()\n",
    "\n",
    "def load_Model():\n",
    "  clf = load(PATH + '/pickle/model.pkl')\n",
    "  return clf\n",
    "\n",
    "model = load_Model()\n",
    "\n",
    "@app.route('/predict', methods=['GET','POST'])\n",
    "def predict():\n",
    "    \n",
    "    file = request.files['file']\n",
    "\n",
    "    data = pd.read_csv(file)\n",
    "\n",
    "    y_pred = model.predict(data)\n",
    "    data['y_pred'] = y_pred\n",
    "\n",
    "    if request.form.get(\"Display\"):\n",
    "      return render_template('result.html', data=data.to_dict(orient=\"records\"))\n",
    "    else:\n",
    "      return Response(data.to_csv(), mimetype=\"text/csv\", headers={\"Content-disposition\":\"attachment; filename=result.csv\"})    \n",
    "\n",
    "if __name__==\"__main__\":\n",
    "    app.run(host=\"0.0.0.0\", port=1234, debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
