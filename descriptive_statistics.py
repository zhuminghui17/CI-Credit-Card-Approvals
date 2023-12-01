{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'pandas'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32m/Users/minghuizhu/Library/CloudStorage/Dropbox/Duke/Fall 2023/IDS706 - Data Engineering/Projects/CI-Credit-Card-Approvals/descriptive_statistics.ipynb Cell 1\u001b[0m line \u001b[0;36m1\n\u001b[0;32m----> <a href='vscode-notebook-cell:/Users/minghuizhu/Library/CloudStorage/Dropbox/Duke/Fall%202023/IDS706%20-%20Data%20Engineering/Projects/CI-Credit-Card-Approvals/descriptive_statistics.ipynb#W0sZmlsZQ%3D%3D?line=0'>1</a>\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mlib\u001b[39;00m\n",
      "File \u001b[0;32m~/Library/CloudStorage/Dropbox/Duke/Fall 2023/IDS706 - Data Engineering/Projects/CI-Credit-Card-Approvals/lib.py:1\u001b[0m\n\u001b[0;32m----> 1\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mpandas\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mpd\u001b[39;00m\n\u001b[1;32m      2\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mnumpy\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mnp\u001b[39;00m\n\u001b[1;32m      3\u001b[0m \u001b[39mimport\u001b[39;00m \u001b[39mmatplotlib\u001b[39;00m\u001b[39m.\u001b[39;00m\u001b[39mpyplot\u001b[39;00m \u001b[39mas\u001b[39;00m \u001b[39mplt\u001b[39;00m\n",
      "\u001b[0;31mModuleNotFoundError\u001b[0m: No module named 'pandas'"
     ]
    }
   ],
   "source": [
    "import lib"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Read Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = lib.read_data('credit_card_approvals.csv')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "EDA"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "lib.describe_data(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
