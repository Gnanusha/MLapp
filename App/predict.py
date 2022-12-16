{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['age', 'workclass', 'education', 'marital-status', 'occupation',\n",
      "       'relationship', 'race', 'gender', 'capital-gain', 'capital-loss',\n",
      "       'hours-per-week', 'native-country', 'y_pred'],\n",
      "      dtype='object')\n",
      "   age  workclass     education      marital-status         occupation  \\\n",
      "0   25    Private          11th       Never-married  Machine-op-inspct   \n",
      "1   38    Private       HS-grad  Married-civ-spouse    Farming-fishing   \n",
      "2   28  Local-gov    Assoc-acdm  Married-civ-spouse    Protective-serv   \n",
      "3   44    Private  Some-college  Married-civ-spouse  Machine-op-inspct   \n",
      "4   18          ?  Some-college       Never-married                  ?   \n",
      "\n",
      "  relationship   race  gender  capital-gain  capital-loss  hours-per-week  \\\n",
      "0    Own-child  Black    Male             0             0              40   \n",
      "1      Husband  White    Male             0             0              50   \n",
      "2      Husband  White    Male             0             0              40   \n",
      "3      Husband  Black    Male          7688             0              40   \n",
      "4    Own-child  White  Female             0             0              30   \n",
      "\n",
      "  native-country y_pred  \n",
      "0  United-States  <=50K  \n",
      "1  United-States  <=50K  \n",
      "2  United-States  <=50K  \n",
      "3  United-States   >50K  \n",
      "4  United-States  <=50K  \n",
      "Accuracy =  0.8467792370231395\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "from joblib import load\n",
    "import pandas as pd\n",
    "from sklearn.metrics import accuracy_score, recall_score\n",
    "\n",
    "PATH = os.getcwd()\n",
    "\n",
    "clf = load(PATH + '/pickle/model.pkl')\n",
    "\n",
    "data = pd.read_excel(PATH+\"/Data/adult_train.csv\")\n",
    "data = data.drop(['fnlwgt', 'educational-num'], axis=1)\n",
    "\n",
    "y = data['income']\n",
    "\n",
    "data.drop('income', axis=1, inplace=True)\n",
    "\n",
    "y_pred = clf.predict(data)\n",
    "\n",
    "data[\"y_pred\"] = y_pred\n",
    "\n",
    "print(data.columns)\n",
    "\n",
    "data.columns\n",
    "\n",
    "print(data.head())\n",
    "print(\"Accuracy = \", accuracy_score(y, y_pred))\n"
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
