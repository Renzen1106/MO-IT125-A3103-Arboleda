{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "2c8e8dce-9e18-4416-9d05-10524cada6df",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Code for Social Media Interactions Exploratory Data\n",
    "# Assuming df is already defined and loaded with the dataset\n",
    "print(df['InteractionDate'].describe())\n",
    "print(df['Platform'].value_counts())\n",
    "print(df['InteractionType'].value_counts())\n",
    "print(df['Sentiment'].value_counts())\n",
    "df['InteractionDate'].plot(kind='box')\n",
    "plt.title('Boxplot of Interaction Dates')\n",
    "plt.show()\n",
    "\n",
    "# Code for Customer Transactions Exploratory Data\n",
    "print(df['Amount'].describe())\n",
    "print(df['ProductCategory'].value_counts())\n",
    "print(df['PaymentMethod'].value_counts())\n",
    "sns.boxplot(x=df['Amount'])\n",
    "plt.title('Boxplot of Transaction Amounts')\n",
    "plt.show()\n",
    "\n",
    "# Code for Customer Demographics Exploratory Data\n",
    "print(df['Age'].describe())\n",
    "print(df['IncomeLevel'].value_counts(dropna=False))\n",
    "print(df['Gender'].value_counts(dropna=False))\n",
    "\n",
    "# Convert SignupDate to datetime and describe\n",
    "df['SignupDate'] = pd.to_datetime(df['SignupDate'], errors='coerce')\n",
    "print(df['SignupDate'].describe())\n",
    "\n",
    "# Boxplot for Age\n",
    "sns.boxplot(x=df['Age'])\n",
    "plt.title('Boxplot of Age')\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
