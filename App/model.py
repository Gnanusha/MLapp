{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      " Saved Pipeline(steps=[('preprocessor',\n",
      "                 ColumnTransformer(transformers=[('num',\n",
      "                                                  Pipeline(steps=[('imputer',\n",
      "                                                                   SimpleImputer()),\n",
      "                                                                  ('scaler',\n",
      "                                                                   StandardScaler())]),\n",
      "                                                  ['age', 'capital-gain',\n",
      "                                                   'capital-loss',\n",
      "                                                   'hours-per-week']),\n",
      "                                                 ('cat',\n",
      "                                                  Pipeline(steps=[('imputer',\n",
      "                                                                   SimpleImputer(strategy='most_frequent')),\n",
      "                                                                  ('onehot',\n",
      "                                                                   OneHotEncoder(handle_unknown='ignore'))]),\n",
      "                                                  ['workclass', 'race',\n",
      "                                                   'education',\n",
      "                                                   'marital-status',\n",
      "                                                   'occupation', 'relationship',\n",
      "                                                   'gender',\n",
      "                                                   'native-country'])])),\n",
      "                ('classifier',\n",
      "                 DecisionTreeClassifier(max_depth=5, min_samples_leaf=5,\n",
      "                                        random_state=100))]) pipeline to file: /home/5062b121/course end devops/pickle/model.pkl\n"
     ]
    }
   ],
   "source": [
    "import os\n",
    "import configparser\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
    "from sklearn.compose import ColumnTransformer\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.pipeline import Pipeline\n",
    "from joblib import dump\n",
    "\n",
    "PATH = os.getcwd()\n",
    "df = pd.read_excel(\"Data/adult_train.csv\",na_values =[\"?\"])\n",
    "df = df.apply(lambda x: x.fillna(x.value_counts().index[0]))\n",
    "df = df.drop(['fnlwgt', 'educational-num'], axis=1)\n",
    "cat_Attr_Names = ['workclass', 'race', 'education', 'marital-status', 'occupation',\n",
    "                'relationship', 'gender', 'native-country', 'income']\n",
    "num_Attr_Names = ['age', 'capital-gain', 'capital-loss', 'hours-per-week']\n",
    "\n",
    "df[cat_Attr_Names] = df[cat_Attr_Names].apply(lambda col: col.astype('category'))\n",
    "df[num_Attr_Names] = df[num_Attr_Names].apply(lambda col: col.astype('int64'))\n",
    "\n",
    "X = df.drop('income', axis=1)\n",
    "y = np.array(df['income'])\n",
    "\n",
    "cat_Attr_Names.remove('income')\n",
    "\n",
    "numeric_transformer = Pipeline(steps=[\n",
    "    ('imputer', SimpleImputer(strategy='mean')),\n",
    "    ('scaler', StandardScaler())])\n",
    "\n",
    "categorical_transformer = Pipeline(steps=[\n",
    "    ('imputer', SimpleImputer(strategy='most_frequent')),\n",
    "    ('onehot', OneHotEncoder(handle_unknown='ignore'))])\n",
    "\n",
    "preprocessor = ColumnTransformer(\n",
    "    transformers=[\n",
    "        ('num', numeric_transformer, num_Attr_Names),\n",
    "        ('cat', categorical_transformer, cat_Attr_Names)])\n",
    "\n",
    "classifier = DecisionTreeClassifier(criterion = \"gini\",\n",
    "                                     random_state = 100,\n",
    "                                     max_depth = 5,\n",
    "                                     min_samples_leaf = 5)\n",
    "\n",
    "clf = Pipeline(steps=[\n",
    "    ('preprocessor', preprocessor), \n",
    "    ('classifier', classifier)])\n",
    "\n",
    "clf.fit(X, y)\n",
    "\n",
    "dump_file = PATH + '/pickle/model.pkl'\n",
    "dump(clf, dump_file, compress=1)\n",
    "\n",
    "print('\\n Saved %s pipeline to file: %s' % (clf, dump_file))\n"
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
