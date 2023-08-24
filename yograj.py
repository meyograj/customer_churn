{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "95699656-fb2a-40c7-ae05-a98c5ee596ff",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f267ca78-7e20-4db9-869a-105eb874d5ad",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "df = pd.read_csv('customer_churn_large_dataset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6c141e05-146a-49f9-bb83-8fe8f26f9ab7",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Location</th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Customer_1</td>\n",
       "      <td>63</td>\n",
       "      <td>Male</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Customer_2</td>\n",
       "      <td>62</td>\n",
       "      <td>Female</td>\n",
       "      <td>New York</td>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Customer_3</td>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Customer_4</td>\n",
       "      <td>36</td>\n",
       "      <td>Female</td>\n",
       "      <td>Miami</td>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Customer_5</td>\n",
       "      <td>46</td>\n",
       "      <td>Female</td>\n",
       "      <td>Miami</td>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CustomerID        Name  Age  Gender     Location  \\\n",
       "0           1  Customer_1   63    Male  Los Angeles   \n",
       "1           2  Customer_2   62  Female     New York   \n",
       "2           3  Customer_3   24  Female  Los Angeles   \n",
       "3           4  Customer_4   36  Female        Miami   \n",
       "4           5  Customer_5   46  Female        Miami   \n",
       "\n",
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Churn  \n",
       "0                          17         73.36             236      0  \n",
       "1                           1         48.76             172      0  \n",
       "2                           5         85.47             460      0  \n",
       "3                           3         97.94             297      1  \n",
       "4                          19         58.14             266      0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "a0d1ea0a-b0c1-4ba3-aa78-f502f6ce591f",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100000, 9)"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "29a8d3eb-93ad-4b71-a5db-5486f1b4f9cd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['CustomerID', 'Name', 'Age', 'Gender', 'Location',\n",
       "       'Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB',\n",
       "       'Churn'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "300e1ff1-bb04-43f1-b789-e6ec2136eb9a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Name', 'Gender', 'Location'], dtype='object')\n"
     ]
    }
   ],
   "source": [
    "categorical_columns = df.select_dtypes(include=['object']).columns\n",
    "print(categorical_columns)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c95cbcc2-db8f-45c7-8794-13c07e8f74aa",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Customer_1' 'Customer_2' 'Customer_3' ... 'Customer_99998'\n",
      " 'Customer_99999' 'Customer_100000']\n",
      "['Male' 'Female']\n",
      "['Los Angeles' 'New York' 'Miami' 'Chicago' 'Houston']\n"
     ]
    }
   ],
   "source": [
    "print(df['Name'].unique())\n",
    "print(df['Gender'].unique())\n",
    "print(df['Location'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "57a42fd6-2000-4b46-b624-1a1cc9e7ce2a",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "CustomerID                    0\n",
       "Name                          0\n",
       "Age                           0\n",
       "Gender                        0\n",
       "Location                      0\n",
       "Subscription_Length_Months    0\n",
       "Monthly_Bill                  0\n",
       "Total_Usage_GB                0\n",
       "Churn                         0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f4b5163c-6c3e-497a-aa82-abb27aa42210",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "      <td>100000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>50000.500000</td>\n",
       "      <td>44.027020</td>\n",
       "      <td>12.490100</td>\n",
       "      <td>65.053197</td>\n",
       "      <td>274.393650</td>\n",
       "      <td>0.497790</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>28867.657797</td>\n",
       "      <td>15.280283</td>\n",
       "      <td>6.926461</td>\n",
       "      <td>20.230696</td>\n",
       "      <td>130.463063</td>\n",
       "      <td>0.499998</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>50.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>25000.750000</td>\n",
       "      <td>31.000000</td>\n",
       "      <td>6.000000</td>\n",
       "      <td>47.540000</td>\n",
       "      <td>161.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>50000.500000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>65.010000</td>\n",
       "      <td>274.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>75000.250000</td>\n",
       "      <td>57.000000</td>\n",
       "      <td>19.000000</td>\n",
       "      <td>82.640000</td>\n",
       "      <td>387.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>100000.000000</td>\n",
       "      <td>70.000000</td>\n",
       "      <td>24.000000</td>\n",
       "      <td>100.000000</td>\n",
       "      <td>500.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "          CustomerID            Age  Subscription_Length_Months  \\\n",
       "count  100000.000000  100000.000000               100000.000000   \n",
       "mean    50000.500000      44.027020                   12.490100   \n",
       "std     28867.657797      15.280283                    6.926461   \n",
       "min         1.000000      18.000000                    1.000000   \n",
       "25%     25000.750000      31.000000                    6.000000   \n",
       "50%     50000.500000      44.000000                   12.000000   \n",
       "75%     75000.250000      57.000000                   19.000000   \n",
       "max    100000.000000      70.000000                   24.000000   \n",
       "\n",
       "        Monthly_Bill  Total_Usage_GB          Churn  \n",
       "count  100000.000000   100000.000000  100000.000000  \n",
       "mean       65.053197      274.393650       0.497790  \n",
       "std        20.230696      130.463063       0.499998  \n",
       "min        30.000000       50.000000       0.000000  \n",
       "25%        47.540000      161.000000       0.000000  \n",
       "50%        65.010000      274.000000       0.000000  \n",
       "75%        82.640000      387.000000       1.000000  \n",
       "max       100.000000      500.000000       1.000000  "
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "73ec34be-90d7-4064-b9e6-3d2c61af4034",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Name</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Location</th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Customer_1</td>\n",
       "      <td>63</td>\n",
       "      <td>Male</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Customer_2</td>\n",
       "      <td>62</td>\n",
       "      <td>Female</td>\n",
       "      <td>New York</td>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Customer_3</td>\n",
       "      <td>24</td>\n",
       "      <td>Female</td>\n",
       "      <td>Los Angeles</td>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Customer_4</td>\n",
       "      <td>36</td>\n",
       "      <td>Female</td>\n",
       "      <td>Miami</td>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Customer_5</td>\n",
       "      <td>46</td>\n",
       "      <td>Female</td>\n",
       "      <td>Miami</td>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   CustomerID        Name  Age  Gender     Location  \\\n",
       "0           1  Customer_1   63    Male  Los Angeles   \n",
       "1           2  Customer_2   62  Female     New York   \n",
       "2           3  Customer_3   24  Female  Los Angeles   \n",
       "3           4  Customer_4   36  Female        Miami   \n",
       "4           5  Customer_5   46  Female        Miami   \n",
       "\n",
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Churn  \n",
       "0                          17         73.36             236      0  \n",
       "1                           1         48.76             172      0  \n",
       "2                           5         85.47             460      0  \n",
       "3                           3         97.94             297      1  \n",
       "4                          19         58.14             266      0  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "3875aaac-1ee0-4299-b9b6-626457a0c3a2",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "final_dataset = df[['Subscription_Length_Months', 'Monthly_Bill', 'Total_Usage_GB', 'Age', 'Churn', 'CustomerID','Gender']]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d3ddb6e2-adf3-4b10-bf5b-d6ef5c535da2",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Age</th>\n",
       "      <th>Churn</th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Gender</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>Male</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>36</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>46</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>Female</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Age  Churn  \\\n",
       "0                          17         73.36             236   63      0   \n",
       "1                           1         48.76             172   62      0   \n",
       "2                           5         85.47             460   24      0   \n",
       "3                           3         97.94             297   36      1   \n",
       "4                          19         58.14             266   46      0   \n",
       "\n",
       "   CustomerID  Gender  \n",
       "0           1    Male  \n",
       "1           2  Female  \n",
       "2           3  Female  \n",
       "3           4  Female  \n",
       "4           5  Female  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "ca1a963b-c8e8-401d-b164-484dd4d889b9",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "final_dataset = pd.get_dummies(final_dataset, drop_first=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "db8eb908-c6f1-49e4-bbee-707414657805",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Age</th>\n",
       "      <th>Churn</th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Gender_Male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>36</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>46</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Age  Churn  \\\n",
       "0                          17         73.36             236   63      0   \n",
       "1                           1         48.76             172   62      0   \n",
       "2                           5         85.47             460   24      0   \n",
       "3                           3         97.94             297   36      1   \n",
       "4                          19         58.14             266   46      0   \n",
       "\n",
       "   CustomerID  Gender_Male  \n",
       "0           1            1  \n",
       "1           2            0  \n",
       "2           3            0  \n",
       "3           4            0  \n",
       "4           5            0  "
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bd040e84-4fde-4d6f-9f32-f6219012a080",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6f614064-cdc7-4bf6-968d-a23669fbf70b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.PairGrid at 0x2489b004650>"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "text/plain": [
       "<Figure size 1750x1750 with 56 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.pairplot(final_dataset)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "0731353c-a7a6-46da-8b31-28e6bb95e5fd",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "fc8c2371-938c-4bad-b022-2d394457e541",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Axes: >"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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N2PGjElZWVmF1wqFQhYvXlwr4QAAAAAA6kqhpPDlnVgt1ajwfeqpp2bHHXfMgw8+mM6dO1e4ySUAAAAAANSnGhW+R48enXvuuSddunSp7TwAAAAAALBSSmpy0Ne//vW8/fbbtZ0FAAAAAABWWo1WfH//+9/PD37wg0ycODFbb711GjZsWOH1bbbZplbCAQAAAABAddWo8H3YYYclSY4//vjytkKhkLKyMje3BAAAAACgXtWo8P3ee+/Vdg4AAAAAgP+pQkmhviNQR2pU+F5//fVrOwcAAAAAANSKGhW+k+Sdd97JgAED8sYbb6RQKORrX/ta/t//+3/ZeOONazMfAAAAAABUS0lNDnr00UezxRZb5MUXX8w222yTrbbaKi+88EK23HLLDBo0qLYzAgAAAABAldVoxfcFF1yQs88+O1dccUWl9vPPPz/7779/rYQDAAAAAIDqqtGK7zfeeCMnnHBCpfbjjz8+r7/++kqHAgAAAACAmqrRiu/27dtn5MiR2WSTTSq0jxw5Mh06dKiVYAAAAAAAdalQUqjvCNSRGhW+TzrppJx88sl59913s9tuu6VQKOSZZ57JlVdemR/84Ae1nREAAAAAAKqsRoXvn/zkJ2nZsmV+9atfpV+/fkmStdZaKz/72c9y5pln1mpAAAAAAACojhoVvguFQs4+++ycffbZmTVrVpKkZcuWtRoMAAAAAABqokaF789T8AYAAAAAYFVSrcL3vvvuW6V+TzzxRI3CAAAAAADAyqpW4fupp57K+uuvn4MPPjgNGzasq0wAAAAAAHWuUFKo7wjUkWoVvq+44orcdttt+dvf/pajjjoqxx9/fLbaaqu6ygYAAAAAANVWUp3O5513Xl5//fX885//zKxZs7L77rtn5513zvXXX5+PP/64rjICAAAAAECVVavw/aldd901N954YyZMmJDvfe97ueWWW7LWWmspfgMAAAAAUO9qVPj+1PDhw/P000/njTfeyFZbbWXfbwAAAAAA6l21C98ffvhhLrvssmy66aY5/PDD07Zt27zwwgsZOnRomjZtWhcZAQAAAACgyqp1c8sePXrkySefTPfu3fPLX/4yBx98cEpLq3UKAAAAAIBVQqGkUN8RqCOFsrKysqp2LikpSefOndOhQ4cUCssfFMOHD69+kNN2qfYxsCr58/Uz6jsCwFean8WzuluypL4T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unwLAAAAAACooE5vA1WL980EAAAAAKhVhZLl38+Q1Zt7bgMAAAAAUFQUvgEAAAAAKCoK3wAAAAAAFBWFbwAAAAAAikqdFr7XX3/9NGzYsC7fAgAAAAAAKihdmYMXLFiQyZMnZ8mSJRXa11tvvSTJq6++ujKnBwAAAACoM4WSQn1HoI7UqPA9evToHH/88XnuuecqtJeVlaVQKGTx4sW1Eg4AAAAAAKqrRoXvY489NqWlpXnggQfSuXPnFAp+MgIAAAAAwKqhRoXvkSNHZtiwYdl8881rOw8AAAAAAKyUGt3ccosttsjUqVNrOwsAAAAAAKy0GhW+r7zyypx33nl56qmnMm3atHz88ccVHgAAAAAAUF9qtNXJfvvtlyTp1q1bhXY3twQAAAAAVhfuXVi8alT4fvLJJ2s7BwAAAAAA1IoaFb733nvv2s4BAAAAAAC1okaF7yT56KOPcvPNN+eNN95IoVDIFltskeOPPz6tW7euzXwAAAAAAFAtNbq55UsvvZSNN944/fv3z/Tp0zN16tRcc8012XjjjTN8+PDazggAAAAAAFVWoxXfZ599dg455JDceOONKS1deopFixblxBNPzFlnnZXBgwfXakgAAAAAAKiqGhW+X3rppQpF7yQpLS3Neeedlx133LHWwgEAAAAA1JVCSaG+I1BHarTVSatWrTJ27NhK7ePGjUvLli1XOhQAAAAAANRUjQrfRx55ZE444YTcfffdGTduXD744IPcddddOfHEE/Od73yntjMCAAAAAECV1Wirk6uvvjqFQiFHH310Fi1alCRp2LBhTjvttFxxxRW1GhAAAAAAAKqjRoXvRo0a5de//nUuv/zyvPPOOykrK0uXLl3SrFmz2s4HAAAAAADVUqPC96eaNWuWrbfeurayAAAAAADASqty4btPnz657bbb0qpVq/Tp02eFfe+9996VDgYAAAAAADVR5cJ369atUygUkiStWrUq/zMAAAAAwOqoUKLGWayqXPi+9dZby/9822231UUWAAAAAABYaSU1OWjffffNRx99VKn9448/zr777ruymQAAAAAAoMZqVPh+6qmnsmDBgkrt8+bNy5AhQ1Y6FAAAAAAA1FSVtzpJkpdffrn8z6+//nomTpxY/nzx4sV55JFHsvbaa9deOgAAAAAAqKZqFb67du2aQqGQQqGwzC1NmjZtmt/85je1Fg4AAAAAAKqrWoXv9957L2VlZdloo43y4osvpn379uWvNWrUKB06dEiDBg1qPSQAAAAAQG0rlBTqOwJ1pFqF7/XXXz9JsmTJkjoJAwAAAAAAK6tahe/Pe/PNN/Ob3/wmb7zxRgqFQjbffPOcccYZ2XzzzWszHwAAAAAAVEtJTQ665557stVWW2XYsGHZdttts80222T48OHZeuut87e//a22MwIAAAAAQJXVaMX3eeedl379+uWSSy6p0H7RRRfl/PPPz7e+9a1aCQcAAAAAANVVoxXfEydOzNFHH12p/f/+7/8yceLElQ4FAAAAAAA1VaMV3/vss0+GDBmSLl26VGh/5plnsueee9ZKMAAAAACAulRSo2XBrA5qVPg+5JBDcv7552fYsGHZZZddkiRDhw7N3/72t1x88cW5//77K/QFAAAAAID/lUJZWVlZdQ8qqeKPQgqFQhYvXly1vqftUt0YsEr58/Uz6jsCwFdaaY1+nA+rjiVL6jsBrDyr5ljdmYtZ3X178Zv1HWG1s84Nh9Z3hNXOByf/o74jVEmN/ou4xL8EAAAAAACsovw8HgAAAACAolLlFd/XXnttTj755DRp0iTXXnvtCvueeeaZKx0MAAAAAABqosqF7/79++eoo45KkyZN0r9//+X2KxQKCt8AAAAAwCqvQaFQ3xGoI1UufL/33nvL/DMAAAAAAKxKqr3H98KFC7PRRhvl9ddfr4s8AAAAAACwUqpd+G7YsGHmz5+fgl8DAAAAAABgFVTtwneSfP/738+VV16ZRYsW1XYeAAAAAABYKVXe4/vzXnjhhTz++OMZOHBgtt566zRv3rzC6/fee2+thAMAAAAAgOqqUeF7jTXWyGGHHVbbWQAAAAAA/mcalNjOuVjVqPB966231nYOAAAAAACoFTXa4/u9997L6NGjK7WPHj0677///spmAgAAAACAGqtR4fvYY4/Nc889V6n9hRdeyLHHHruymQAAAAAAoMZqVPgeMWJEdt9990rtu+yyS0aOHLmymQAAAAAAoMZqVPguFAqZNWtWpfaZM2dm8eLFKx0KAAAAAABqqkY3t9xzzz1z+eWX584770yDBg2SJIsXL87ll1+ePfbYo1YDAgAAAADUhQaFQn1HoI7UqPB91VVXZa+99spmm22WPffcM0kyZMiQfPzxx3niiSdqNSAAAAAAAFRHjbY62WKLLfLyyy/niCOOyOTJkzNr1qwcffTR+c9//pOtttqqtjMCAAAAAECV1WjFd5KstdZaueyyy2ozCwAAAAAArLQarfh+5JFH8swzz5Q//93vfpeuXbumb9++mTFjRq2FAwAAAACA6qpR4fuHP/xhPv744yTJK6+8knPOOSc9evTIu+++m3POOadWAwIAAAAAQHXUaKuT9957L1tssUWS5O9//3t69uyZyy67LMOHD0+PHj1qNSAAAAAAQF1oUKNlwawOavRX26hRo8ydOzdJ8thjj6V79+5JkrZt25avBAcAAAAAgPpQoxXfe+yxR84555zsvvvuefHFF3P33XcnSd56662ss846tRoQAAAAAACqo0Yrvn/729+mtLQ099xzT6677rqsvfbaSZKHH344Bx54YK0GBAAAAACA6qjRiu/11lsvDzzwQKX2/v37r3QgAAAAAABYGTUqfCfJ4sWL849//CNvvPFGCoVCNt988/Tu3TulpTU+JQAAAAAArLQaValfffXVHHLIIZk0aVI222yzJEv3927fvn3uv//+bL311rUaEgAAAACgtjUoFOo7AnWkRnt8n3jiidlqq63ywQcfZPjw4Rk+fHjGjRuXbbbZJieffHJtZwQAAAAAgCqr0YrvUaNG5aWXXkqbNm3K29q0aZNLL700O+20U62FAwAAAACA6qrRiu/NNtsskyZNqtQ+efLkdOnSZaVDAQAAAABATVW58P3xxx+XPy677LKceeaZueeee/LBBx/kgw8+yD333JOzzjorV155ZV3mBQAAAACAFaryVidrrLFGCp/b7L2srCxHHHFEeVtZWVmSpGfPnlm8eHEtxwQAAAAAgKqpcuH7ySefrMscAAAAAAD/Uw0+t9CX4lLlwvfee+9dlzkAAAAAAKBWVLnw/XmDBw9e4et77bVXjcIAAAAAAMDKqlHhe5999qnU9vn9v+3xDQAAAABAfSmpyUEzZsyo8Jg8eXIeeeSR7LTTThk4cGBtZwQAAAAAgCqr0Yrv1q1bV2rbf//907hx45x99tkZNmzYSgcDAAAAAICaqFHhe3nat2+fN998szZPCQAAAABQJxqUFL68E6ulGhW+X3755QrPy8rKMmHChFxxxRXZdtttayUYAAAAAADURI0K3127dk2hUEhZWVmF9l122SW33HJLrQQDAAAAAICaqFHh+7333qvw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7mkBAAAAACgiCxYsyLBhw9K9e/cK7d27d89zzz23zGN22223fPDBB3nooYdSVlaWSZMm5Z577snBBx9crfeu1h7fSXLPPffktttuS48ePfLWW29l8803z4MPPpiDDjooSdKhQ4ccddRR1T0tAAAAAACruPnz52f+/PkV2ho3bpzGjRtX6jt16tQsXrw4HTt2rNDesWPHTJw4cZnn32233fLnP/85Rx55ZObNm5dFixblkEMOyW9+85tq5az2iu8PP/ww2267bZJk0003TePGjdOlS5fy1zfddNPlhgYAAAAAWFU0KBQ8qvm4/PLL07p16wqPyy+/fIVf50KhUOF5WVlZpbZPvf766znzzDPz05/+NMOGDcsjjzyS9957L6eeemq1/m6rveJ78eLFadiw4WcnKC1NgwYNyp+XlJSkrKysuqcFAAAAAGAV169fv5xzzjkV2pa12jtJ2rVrlwYNGlRaKD158uRKq8A/dfnll2f33XfPD3/4wyTJNttsk+bNm2fPPffML37xi3Tu3LlKOatd+E6SRx99NK1bt06SLFmyJI8//nheffXVJMlHH31Uk1MCAAAAALCKW962JsvSqFGj7LDDDhk0aFAOPfTQ8vZBgwalV69eyzxm7ty5KS2tWLb+dOF1dRZc16jwfcwxx1R4fsopp1R4vrxl6gAAAAAAfHWcc845+e53v5sdd9wxu+66a2644YaMHTu2fOuSfv36Zfz48bn99tuTJD179sxJJ52U6667LgcccEAmTJiQs846KzvvvHPWWmutKr9vtQvfS5Ysqe4hAAAAAAB8BR155JGZNm1aLrnkkkyYMCFbbbVVHnrooay//vpJkgkTJmTs2LHl/Y899tjMmjUrv/3tb/ODH/wga6yxRvbdd99ceeWV1XrfQlkdb8h98MEH56abbvrSvVf+UtisLmNAnTvq1Db1HQFWyt03zajvCLBS/GweAICvum8vfrO+I6x2TnnixPqOsNr5w7431XeEKqnRVifVMXjw4HzyySd1/TYAAAAAANXSwI7NRaukvgMAAAAAAEBtUvgGAAAAAKCoKHwDAAAAAFBUFL4BAAAAACgqCt8AAAAAABSV0poeOGfOnDRv3vxL+1144YVp27ZtTd8GAAAAAKBOlBQK9R2BOlLjFd8dO3bM8ccfn2eeeWaF/fr165c11lijpm8DAAAAAADVUuPC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20pKKi/spThUu/Ddu3fvJMnIkSNzwAEHpEWLFuWvNWrUKBtssEEOO+ywWgsIAAAAAADVUe3C90UXXZQk2WCDDXLkkUemSZMmtR4KAAAAAABqqtqF708dc8wxSZIFCxZk8uTJWbJkSYXX11tvvZVLBgAAAAAANVDjwvfo0aNz/PHH57nnnqvQ/ulNLxcvXrzS4QAAAAAAoLpqXPg+9thjU1pamgceeCCdO3dOoWAjeAAAAAAA6l+NC98jR47MsGHDsvnmm9dmHgAAAACA/4kG1vIWrZKaHrjFFltk6tSptZkFAAAAAABWWo0L31deeWXOO++8PPXUU5k2bVo+/vjjCg8AAAAAAKgPNd7qZL/99kuSdOvWrUK7m1sCAAAAAFCfalz4fvLJJ2szBwAAAAAA1IoaF7733nvv2swBAAAAAAC1osaF7yT56KOPcvPNN+eNN95IoVDIFltskeOPPz6tW7eurXwAAAAAAHWipFDfCagrNb655UsvvZSNN944/fv3z/Tp0zN16tRcc8012XjjjTN8+PDazAgAAAAAAFVW4xXfZ599dg455JDceOONKS1deppFixblxBNPzFlnnZXBgwfXWkgAAAAAAKiqGhe+X3rppQpF7yQpLS3Neeedlx133LFWwgEAAAAAQHXVeKuTVq1aZezYsZXax40bl5YtW65UKAAAAAAAqKkaF76PPPLInHDCCbn77rszbty4fPDBB7nrrrty4okn5jvf+U5tZgQAAAAAgCqr8VYnV199dQqFQo4++ugsWrQoZWVladSoUU477bRcccUVtZkRAAAAAKDWNSjUdwLqSo0L340aNcqvf/3rXH755XnnnXdSVlaWLl26pFmzZrWZDwAAAAAAqqXahe/jjz++Sv1uueWWaocBAAAAAICVVe3C92233Zb1118/2223XcrKyuoiEwAAAAAA1Fi1C9+nnnpq7rrrrrz77rs5/vjj83//939p27ZtXWQDAAAAAIBqK6nuAb///e8zYcKEnH/++fnXv/6VddddN0cccUQeffRRK8ABAAAAAKh3Nbq5ZePGjfOd73wn3/nOdzJmzJjcdtttOf3007Nw4cK8/vrradGiRW3nBAAAAACoVSWFQn1HoI5Ue8X3FxUKhRQKhZSVlWXJkiW1kQkAAAAAAGqsRoXv+fPn584778z++++fzTbbLK+88kp++9vfZuzY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5JPy1xs0aJAbb7wxa6yxRq2HBAAAAACAqqryiu8bb7wxzz77bPnz+++/PyUlJWndunVat26dV155JQMGDKiLjAAAAAAAUGVVLnzfc8896du3b4W2q666KrfeemtuvfXWXH755bnvvvtqPSAAAAAAAFRHlQvf77zzTrp06VL+fLPNNkujRo3Kn2+77bYZPXp07aYDAAAAAIBqqvIe33Pnzs2CBQvKn7/00ksVXp8zZ06WLFlSe8kAAAAAAOpQSaFQ3xGoI1Ve8b3RRhtl+PDhy339pZdeyoYbblgroQAAAAAAoKaqXPg+9NBD8+Mf/zgTJ06s9NqECRNy0UUX5dBDD63VcAAAAAAAUF1V3urkvPPOy9///vdsuumm+e53v5tNN900hUIh//nPf3LHHXdk7bXXzvnnn1+XWQEAAAAA4EtVufDdsmXLPPvss+nXr1/uvPPOfPTRR0mSNdZYI3379s1ll12Wli1b1lVOAAAAAACokioXvpOkTZs2uf7663PddddlypQpSZL27dunsIxN4J999tnsuOOOady4ce0kBQAAAACAKqhW4ftThUIhHTp0WGGfgw46KCNHjsxGG21Uo2AAAAAAAHWpZBkLeikOVb65ZXWVlZXV1akBAAAAAGC56qzwDQAAAAAA9UHhGwAAAACAoqLwDQAAAABAUamzwnfBxvAAAAAAANSD0ro6sZtbAgAAAACrspKCDTGKVY0K34sWLcpTTz2Vd955J3379k3Lli3z4YcfplWrVmnRokWSZNasWbUaFAAAAAAAqqLahe8xY8bkwAMPzNixYzN//vzsv//+admyZa666qrMmzcv119/fV3kBAAAAACAKqn2Wv7/9//+X3bcccfMmDEjTZs2LW8/9NBD8/jjj9dqOAAAAAAAqK5qr/h+5pln8uyzz6ZRo0YV2tdff/2MHz++1oIBAAAAAEBNVHvF95IlS7J48eJK7R988EFatmxZK6EAAAAAAKCmql343n///TNgwIDy54VCIbNnz85FF12UHj161GY2AAAAAACotmpvddK/f/984xvfyBZbbJF58+alb9++GT16dNq1a5c777yzLjICAAAAANS6kkKhviNQR6pd+F5rrbUycuTI3HnnnRk+fHiWLFmSE044IUcddVSFm10CAAAAAEB9qHbhO0maNm2a448/Pscff3xt5wEAAAAAgJVS7cL3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6quvIicnp8Dy9evXx5w5c0qlKAAAAAAAKKkiT3Xywgsv5P33qFGjolatWnk/5+TkxJgxY2KPPfYo1eIAAAAAAKC4ihx89+/fPyIiUqlUnH322fmeq1ixYuyxxx5x1113lWpxAAAAAABlJSuVynQJlJEiB9+5ubkREdGqVav44IMPon79+mVWFAAAAAAAlFSRg+/vzZo1qyzqAAAAAACAUlHsm1tGRPzrX/+K448/Ptq0aRNt27aNE044IcaNG1fatQEAAAAAQLEVO/j+y1/+EkceeWRUq1YtLrvssrj00kujatWq0bt373jqqafKokYAAAAAACiyYk91csstt8Ttt98eV1xxRd6yX//61zFkyJD4n//5nxgwYECpFggAAAAAAMVR7BHfX375ZRx//PEFlp9wwgnm/wYAAAAAyo2sSHkU81FeFDv4btGiRYwZM6bA8jFjxkSLFi1KpSgAAAAAACipIk91cu6558Y999wTV111VVx22WUxadKk6NmzZ6RSqXjrrbfisccei3vuuacsawUAAAAAgO0qcvD9+OOPx6233hoXXXRRNG7cOO6666549tlnIyJi7733jhEjRkS/fv3KrFAAAAAAACiKIgff6XQ6779PPPHEOPHEE8ukIAAAAAAA2BHFmuM7lSo/k5cDAAAAALBrKvKI74iIvfbaa7vh95IlS3aoIAAAAACA/4QsA30Tq1jB90033RS1atUqq1oAAAAAAGCHFSv4PuOMM6Jhw4ZlVQsAAAAAAOywIs/xbX5vAAAAAADKgyIH3+l0uizrAAAAAACAUlHkqU5yc3PLsg4AAAAAACgVxZrjGwAAAAAgKbJSRZ4Qg3LGbxYAAAAAgDJz//33R6tWraJKlSrRtWvXGDdu3DbXX79+fVx33XXRsmXLqFy5cuy5557x6KOPFuuYRnwDAAAAAFAmRowYEZdffnncf//9cfDBB8cDDzwQRx99dEybNi123333Qrc57bTTYv78+fHII49EmzZtYsGCBbFp06ZiHVfwDQAAAABAmRgyZEicd9558ctf/jIiIoYOHRqjRo2KYcOGxeDBgwus/8orr8S//vWv+PLLL6Nu3boREbHHHnsU+7imOgEAAAAAoEjWr18fK1asyPdYv359oetu2LAhJkyYEH379s23vG/fvvH2228Xus0LL7wQ3bp1i9tvvz2aNWsWe+21V/zm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AAAAJIrgGwAAAACARBF8AwAAAACQKNmZLgAAAAAAICNyczNdAWXEiG8AAAAAABJF8A0AAAAAQKIIvgEAAAAASBTBNwAAAAAAiSL4BgAAAAAgUQTfAAAAAAAkiuAbAAAAANg1pXM9ivsogfvvvz9atWoVVapUia5du8a4ceOKtN348eMjOzs7unTpUuxjCr4BAAAAACgTI0aMiMsvvzyuu+66mDhxYvTq1SuOPvromD179ja3W758eZx11lnRu3fvEh1X8A0AAAAAQJkYMmRInHfeefHLX/4y9t577xg6dGi0aNEihg0bts3tLrjgghgwYED06NGjRMcVfAMAAAAAUCTr16+PFStW5HusX7++0HU3bNgQEyZMiL59++Zb3rdv33j77be3eow///nPMXPmzLjhhhtKXKfgGwAAAACAIhk8eHDUqlUr32Pw4MGFrrto0aLIycmJRo0a5VveqFGjmDdvXqHbfP7553HttdfGk08+GdnZ2SWus+RbAgAAAACwSxk0aFBceeWV+ZZVrlx5m9ukUql8P6fT6QLLIiJycnJiwIABcdNNN8Vee+21Q3UKvgEAAACAXVM6N9MVlDuVK1febtD9vfr160eFChUKjO5esGBBgVHgERErV66MDz/8MCZOnBiXXnppRETk5uZGOp2O7OzsePXVV+OII44o0rFNdQIAAAAAQKmrVKlSdO3aNUaPHp1v+ejRo6Nnz54F1q9Zs2ZMmTIlJk2alPe48MILo127djFp0qQ48MADi3xsI74BAAAAACgTV155Zfz85z+Pbt26RY8ePeLBBx+M2bNnx4UXXhgRm6dOmTNnTgwfPjyysrKiU6dO+bZv2LBhVKlSpcDy7RF8AwAAAABQJk4//fRYvHhx3HzzzTF37tzo1KlTvPTSS9GyZcuIiJg7d27Mnj271I+bSqfT6VLfawk8U6FdpksA2KXlmtaMci7LBG6Ucz87v06mS4Ad9uSflma6BNghrico787ImZHpEsqd9Nd3ZrqEcifV8jeZLqFInNIBAAAAAEgUU50AAAAAALsmf/6cWEZ8AwAAAACQKIJvAAAAAAASRfANAAAAAECiCL4BAAAAAEgUwTcAAAAAAImSnekCAAAAAAAyIjed6QooI0Z8AwAAAACQKIJvAAAAAAASRfANAAAAAECiCL4BAAAAAEgUwTcAAAAAAImSnekCAAAA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A66IJe9/nLdO1WaN46C/DIlK9WvH+oVLY8l7k2LMIaflHReK6ptnX47KdetEp99/18NTP4s3j/uhh6s2aRDVt+jhfx13fux316Boe/HmHv7o8lvi2+fz9/DbA66MfW++PPa5+bJYNfObePtn+Xu4brdOccTYJ/J+3n/I7yIiYtbjz8d75w6KdE5O1GjfOg4+68SoXL9ObFi8LBZ/OCXGHHZmrJj2RVm/LSTA9NsfiuyqlaP7/TdEpTq1YtF7k+P1vufGplWr89aptnuTSOfm5v286J2JMf6MK2Pf/7089v2fzb371ulXxOIf9e7sZ1+OyvXqRKfrL46q331m3jjmfOdfdtind2zu2W73be7Zxe9Njjd+mr9nq7doEvGjni3K+XZ75/mIiGYnHBEHPnpr3s8HPz00IiKm3nRvTL35voiIaHPBGdHphl/lrdP7X09FRMR7514bsx7/W+m+GZRLO/t5d8Y9j0eFKpVi/7sHReW6tWLp5E/j9T7nxqovS34vJChMt933jjeuvD/v57tPvTwiIh5758U4Z/j/ZKgqkiiT1w5FOfb2rh1y1q6P5if2jU43/iqyq1eLtXMXxtxR42LagCsid8PGMnnPgJ1bKl3gLgRFM3PmzBg6dGhMnz49UqlU7L333vHrX/869txzzxIV8mzFdiXaDnYWP/r/fiiX9DDlXZZZ0yjnnIdJgjMvrJPpEmCHPP3g0kyXADvkjJwZmS6h3FlzVd9Ml1DuVLvr1e2vtBMo0T8RR40aFR06dIj3338/9t133+jUqVO899570bFjxxg9enRp1wgAAAAAAEVWoqlOrr322rjiiivi1ltvLbD8mmuuiT59+pRKcQAAAAAAUFwlGvE9ffr0OO+88wosP/fcc2PatGk7XBQAAAAAAJRUiYLvBg0axKRJkwosnzRpUjRs2HBHawIAAAAAgBIr0VQnAwcOjPPPPz++/PLL6NmzZ6RSqXjrrbfitttui6uuuqq0awQAAAAAgCIrUfD93//931GjRo246667YtCgQRER0bRp07jxxhvjsssuK9UCAQAAAADKQjo3nekSKCMlmuoklUrFFVdcEd9++20sX748li9fHt9++238+te/jlQqVdo1AgAAAABQTt1///3RqlWrqFKlSnTt2jXGjRu31XWff/756NOnTzRo0CBq1qwZPXr0iFGjRhX7mCUKvo844ohYtmxZRETUqFEjatSoERERK1asiCOOOKIkuwQAAAAAIGFGjBgRl19+eVx33XUxceLE6NWrVxx99NExe/bsQtd/8803o0+fPvHSSy/FhAkT4ic/+Ukcf/zxMXHixGIdN5VOp4s9nj8rKyvmzZtX4EaWCxYsiGbNmsXGjRuLu8t4tmK7Ym8DO5Pc3ExXADtGD1PeZZXo63zYeTgPkwRnXlgn0yXADnn6waWZLgF2yBk5MzJdQrmz+oo+mS6h3Kl+9+hirX/ggQfG/vvvH8OGDctbtvfee0f//v1j8ODBRdpHx44d4/TTT4/rr7++yMct1hzfH3/8cd5/T5s2LebNm5f3c05OTrzyyivRrFmz4uwSAAAAAIByYv369bF+/fp8yypXrhyVK1cusO6GDRtiwoQJce211+Zb3rdv33j77beLdLzc3NxYuXJl1K1bt1h1Fiv47tKlS6RSqUilUoVOaVK1atW49957i1UAAAAAAADlw+DBg+Omm27Kt+yGG26IG2+8scC6ixYtipycnGjUqFG+5Y0aNco3qHpb7rrrrli9enWcdtppxaqzWMH3rFmzIp1OR+vWreP999+PBg0a5D1XqVKlaNiwYVSoUKFYBQAAAAAAZEROsWeB3uUNGjQorrzyynzLChvt/WOpVCrfz+l0usCywjz99NNx4403xsiRIwtMu709xQq+W7ZsGRGbh5cDAAAAALBr2dq0JoWpX79+VKhQocDo7gULFhQYBb6lESNGxHnnnRf/93//F0ceeWSx6yzRbaAef/zxePHFF/N+/u1vfxu1a9eOnj17xtdff12SXQIAAAAAkCCVKlWKrl27xujR+W+IOXr06OjZs+dWt3v66afjF7/4RTz11FNx7LHHlujYJQq+/9//+39RtWrViIh455134r777ovbb7896tevH1dccUWJCgEAAAAAIFmuvPLKePjhh+PRRx+N6dOnxxVXXBGzZ8+OCy+8MCI2T51y1lln5a3/9NNPx1lnnRV33XVXHHTQQTFv3ryYN29eLF++vFjHLdZUJ9/75ptvok2bNhER8fe//z1OOeWUOP/88+Pggw+Oww8/vCS7BAAAAAAgYU4//fRYvHhx3HzzzTF37tzo1KlTvPTSS3nTas+dOzdmz56dt/4DDzwQmzZtiksuuSQuueSSvOVnn312PPbYY0U+bomC79122y0WL14c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RESEihUrpgULFlimLViwQEWLFlWVKlUs0zJah2fNmqU33nhDu3btshzXO5+KOH/+vNq3by8fHx+VKVNGixYtSjHeq1evKleuXPruu++spv/000/y9fW1qrNpyZ07twoWLKiiRYvqkUceUZs2bbRjxw7L/KzSO/1+ULBgQcsnICBAJpPJatpXX32l0qVLK2fOnAoLC9MXX3xhWbZEiRKSpPbt28tkMlm+Hz58WG3btlVQUJD8/PxUvXp1rVy5MtP35bvvvlOFChUsPakbN26sq1evSrr9RFGTJk2UP39+BQQEqEGDBlZ1TpL279+vunXrysvLS+XKldPKlSuT9TY/ceKEOnfurDx58ihfvnxq27atjh49alN8r776qo4fP64tW7aoZ8+eqlixoh544AE98sgj+uqrr/T8889blffx8VHBggUVHBysBx98UP369UsWM7Knq1ev6ptvvlHfvn31yCOPJHtKbdGiRSpTpoy8vb3VqFEjzZ49O9mQU5s2bVL9+vXl7e2tokWLqn///pb6DmRU4pNnW7duVadOnRQaGqrw8HANHDhQmzdvtpRLq/2Q0hN8P/zwg1UbNfHv/YwZMyy9fA3DkMlk0rRp02xqm8A13K3O2XINGx0drW7duqlAgQLy9vZWmTJlNHPmTEmpXzfaeu3yzTffqF69evL29lb16tX1559/6rffflO1atUs11fnzp2z2qeZM2eqbNmy8vLy0gMPPKDJkyenuN6GDRvKy8tLX375ZarHJzAwUAULFlRoaKi6dOmijRs3qkCBAurbt29GDjvS6fnnn5e7u7u2bdumxx57TGXLllWFChXUsWNH/fzzz2rdurUkx+QBrl69qqeeekp+fn4KDg7WhAkTksUTHx+voUOHqnDhwvL19VXNmjWtcjuJ5+PFixerXLly8vT0tOkpQnvyALa0tZPKSLsaQNaV6YnvxJ6SP/zwg9XQAekxZMgQjR8/Xr/99psCAwPVpk0by53ofv36KS4uTuvXr9fvv/+u9957z9JD88SJE6pfv768vLy0evVqbd++Xb169dLNmzct6161apX27dunFStWaPHixanG8Prrr6tjx47atWuXnnjiCXXt2lX79u2TJG3dulWStHLlSp06dcoqeXinoUOH6vvvv9fs2bO1Y8cOhYSEqFmzZsl6wA8fPlwTJkzQtm3b5O7url69eqX/4P3LMAy1atVKp0+f1pIlS7R9+3ZFRETo4Ycfttr+4cOH9cMPP2jx4sVavHix1q1bp3fffdcyf+DAgdq4caMWLVqkFStWKDIy0uoPyYIFC1SkSBGNHj1ap06dskpsX7t2TePHj9cXX3yh9evX6/jx4xo8eLBd+9GrVy+rC/MZM2aoW7duypkzp1W5Dz74QBMmTND48eO1e/duNWvWTG3atNHBgwetyg0fPlyDBw9WVFSUQkND1bVrV928eVO1a9fWpEmTlCtXLst+3BnrhAkTVK1aNe3cuVPPP/+8+vbta+kB8uGHH2rRokX65ptvdODAAX355ZeWRFxW1rNnT0ujXLp9bJPWvYzW4c6dO2vQoEEKDw+3HNfOnTtblnvjjTf02GOPaffu3WrZsqW6deuW4hMivr6+6tKli1W80u2GfadOneTv72/3/v/5559as2aNatasafeyyFwLFy7UgAEDNGjQIO3Zs0fPPfecevbsqTVr1kiS5ebLzJkzderUKcv32NhYtWzZUitXrtTOnTvVrFkztW7dWsePH8+0WE+dOqWuXbuqV69e2rdvn9auXasOHTrIMAxJt28edu/eXZGRkdq8ebPKlCmjli1bWi4szGaz2rVrJx8fH23ZskWff/65hg8fbrWNa9euqVGjRvLz89P69eu1YcMGy8VufHx8mvGZzWbNnz9fTzzxhAoXLpximaQ3LO908eJFffvtt/xOXMT8+fMVFhamsLAwPfHEE5o5c6alrh49elSdOnVSu3btFBUVpeeeey5ZXfz999/VrFkzdejQQbt379b8+fO1YcMGvfDCC87YHbiYixcvatmyZerXr598fX2Tzb8zmW1r+yEthw4d0jfffKPvv//eKqnpiHUje7CnzqXl9ddf1x9//KGlS5dq3759mjJlivLnzy8p9etGW69dRo4cqddee007duyQu7u7unbtqqFDh+qDDz5QZGSkDh8+rBEjRljKT506VcOHD9fbb7+tffv26Z133tHrr79ulUCUpFdeeUX9+/fXvn371KxZM5uPmbe3t/r06aONGzfq7NmzNi+HjLtw4YJ++eWXVOurdLtN56g8wJAhQ7RmzRotXLhQv/zyi9auXavt27dbba9nz57auHGj5s2bp927d+vRRx9V8+bNrerxtWvXNGbMGE2bNk179+5VYGCgTftrax7gbm3tpDLSrgaQ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1alTR2+88YZ27typnDlzauHChZaY+vfvr5YtWyo8PFyenp46f/681TaOHz+uM2fOWKYl3WZERIQOHjyowMDAZOfzxAR8anLkyKHHHntMX375pU6cOJGu48DvJPu7efOm5syZowkTJigqKsry2bVrl4oXL665c+emWN+3bdtm9T0iIkJ79+5NVg8T/14AGZE3b141a9ZMn3zySYovTE16ky41BQoUUExMjNU6UrvmwP3Nljpn6zVsgQIF1KNHD3355ZeaNGmSPv/8c0kpXzc66tolqaCgIBUuXFh//fVXsnN04ks2M+r69ev6/PPPVb9+fZKE91i+fPnUpEkTffzxx2m+VNoReYCQkBB5eHikmJdJVKVKFd26dUtnz55Ntp07n2TMiLvlAaS7t7WTyki7GkDWluk9vi9cuKBHH31UvXr1UsWKFeXv769t27Zp7Nixatu2rby9vfXggw/q3XffVYkSJXT+/Hm99tprKa5r9OjRypcvn4KCgjR8+HDlz5/fchf+pZdeUosWLRQaGqro6GitXr3a0kB44YUX9NFHH6lLly4aNmyYAgICtHnzZtWoUcPm4TkSffvtt6pWrZrq1q2ruXPnauvWrZo+fbqk228Z9vb21rJly1SkSBF5eXklO0n6+vqqb9++GjJkiPLmzatixYpp7Nixunbtmnr37m3n0U3drVu3kjW+cubMqcaNG6tWrVpq166d3nvvPYWFhenkyZNasmSJ2rVrZ9Pjbf7+/urevbtlHwIDAzVy5EjlyJHD6q5tiRIltH79enXp0kWenp42/0G1x+rVq5WQkJDqS2aGDBmikSNHqnTp0qpcubJmzpypqKioFO/kpqZEiRKKjY3VqlWrVKlSJfn4+MjHx+euy02cOFHBwcGqXLmycuTIoW+//VYFCxa0+YU4zuTm5mbptZFSTxBH1OESJUroyJEjioqKUpEiReTv7y9PT890xZsnTx516NBBQ4YMUdOmTVWkSBG7lr906ZJOnz4ts9msgwcPavTo0QoNDb0nN6NguyFDhuixxx6zvIjnp59+0oIFC7Ry5UpLmRIlSmjVqlWqU6eOPD09lSdPHoWEhGjBggVq3bq1TCaTXn/99Qz10hs8eLC6d++uBx54QE2bNrVc7B0+fFj9+vWTJG3ZskWrVq1S06ZNFRgYqC1btujcuXOWOhUSEqIvvvhC1apV05Ur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",
      "text/plain": [
       "<Figure size 2000x2000 with 2 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Plotting The Correlations between all the features\n",
    "corrmat = final_dataset.corr()\n",
    "top_corr_features = corrmat.index\n",
    "plt.figure(figsize=(20,20))\n",
    "sns.heatmap(final_dataset[top_corr_features].corr(), annot=True, cmap='RdYlGn')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "5d814920-0aa5-4c56-aec4-8281a933faac",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Age</th>\n",
       "      <th>Churn</th>\n",
       "      <th>CustomerID</th>\n",
       "      <th>Gender_Male</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>36</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>46</td>\n",
       "      <td>0</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Age  Churn  \\\n",
       "0                          17         73.36             236   63      0   \n",
       "1                           1         48.76             172   62      0   \n",
       "2                           5         85.47             460   24      0   \n",
       "3                           3         97.94             297   36      1   \n",
       "4                          19         58.14             266   46      0   \n",
       "\n",
       "   CustomerID  Gender_Male  \n",
       "0           1            1  \n",
       "1           2            0  \n",
       "2           3            0  \n",
       "3           4            0  \n",
       "4           5            0  "
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "final_dataset.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b6fc1856-21fd-4c08-8647-bd3d4465f457",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Splitting the Dataset into Dependent and Independent Variables\n",
    "X = final_dataset.iloc[:, [0,1,2,3,4]]\n",
    "y = final_dataset.iloc[:, 1].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "2a89b9cb-1d00-42cc-ad8c-0b2806b7a01b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Subscription_Length_Months</th>\n",
       "      <th>Monthly_Bill</th>\n",
       "      <th>Total_Usage_GB</th>\n",
       "      <th>Age</th>\n",
       "      <th>Churn</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>17</td>\n",
       "      <td>73.36</td>\n",
       "      <td>236</td>\n",
       "      <td>63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>48.76</td>\n",
       "      <td>172</td>\n",
       "      <td>62</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>5</td>\n",
       "      <td>85.47</td>\n",
       "      <td>460</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>3</td>\n",
       "      <td>97.94</td>\n",
       "      <td>297</td>\n",
       "      <td>36</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>19</td>\n",
       "      <td>58.14</td>\n",
       "      <td>266</td>\n",
       "      <td>46</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Subscription_Length_Months  Monthly_Bill  Total_Usage_GB  Age  Churn\n",
       "0                          17         73.36             236   63      0\n",
       "1                           1         48.76             172   62      0\n",
       "2                           5         85.47             460   24      0\n",
       "3                           3         97.94             297   36      1\n",
       "4                          19         58.14             266   46      0"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "78fdd056-8e4b-4a15-b2f1-82cac2db2b15",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([73.36, 48.76, 85.47, ..., 96.11, 49.25, 76.57])"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "id": "a262a798-e145-4f61-8dde-48dac8f043a4",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.preprocessing import StandardScaler\n",
    "scaler = StandardScaler()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "id": "555ede1d-e8ae-4ce1-94f1-f11fc160a0d2",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "scaler.fit(final_dataset.drop(['Churn'],axis = 1))\n",
    "scaled_features = scaler.transform(final_dataset.drop('Churn',axis = 1))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "f54bd19e-ac15-4685-aad7-ce731a81dd11",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X = scaled_features\n",
    "Y = final_dataset['Churn']\n",
    "X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.3,random_state=44)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "9c2aabbd-e837-4773-a933-cbe2f56c76fd",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<style>#sk-container-id-6 {color: black;}#sk-container-id-6 pre{padding: 0;}#sk-container-id-6 div.sk-toggleable {background-color: white;}#sk-container-id-6 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-6 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-6 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-6 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-6 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-6 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-6 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-6 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-6 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-6 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-6 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-6 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-6 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-6 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-6 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-6 div.sk-item {position: relative;z-index: 1;}#sk-container-id-6 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-6 div.sk-item::before, #sk-container-id-6 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-6 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-6 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-6 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-6 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-6 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-6 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-6 div.sk-label-container {text-align: center;}#sk-container-id-6 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-6 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-6\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>LogisticRegression()</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-6\" type=\"checkbox\" checked><label for=\"sk-estimator-id-6\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">LogisticRegression</label><div class=\"sk-toggleable__content\"><pre>LogisticRegression()</pre></div></div></div></div></div>"
      ],
      "text/plain": [
       "LogisticRegression()"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.metrics import classification_report,accuracy_score ,confusion_matrix\n",
    "\n",
    "logmodel = LogisticRegression()\n",
    "logmodel.fit(X_train,Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "99fb62fe-4d70-4602-9f62-815c64eebb9f",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "predLR = logmodel.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "0c5fffea-b537-4bde-b81c-743143441794",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, ..., 0, 0, 1], dtype=int64)"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "predLR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "679735a4-3abd-4f43-a65e-ddaca4c1f23b",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "39574    0\n",
       "537      0\n",
       "99246    1\n",
       "39498    0\n",
       "24797    1\n",
       "        ..\n",
       "15067    1\n",
       "99097    1\n",
       "89572    0\n",
       "25391    0\n",
       "29677    0\n",
       "Name: Churn, Length: 30000, dtype: int64"
      ]
     },
     "execution_count": 63,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Y_test\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "46559ded-44d6-4c76-bd6a-1d0ab2b760f5",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.50      0.58      0.54     15151\n",
      "           1       0.49      0.41      0.45     14849\n",
      "\n",
      "    accuracy                           0.50     30000\n",
      "   macro avg       0.50      0.50      0.50     30000\n",
      "weighted avg       0.50      0.50      0.50     30000\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(Y_test, predLR))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "79c74642-e995-4cd7-b607-5f16f12fe35e",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA9UAAAF0CAYAAAAtlRp9AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABdwklEQVR4nO3df1xW9f3/8ecVPy4Q5VJAQAqQzIhC02EpOlMzMUrdapsWC3Phr+GPITqTrERXspoam6ZpqVRous1s/XAkrUwZaknQZjqzpoEORI0u1BQUzvcPv1yfLvkhXKL8etxvt3O7ed7ndc55H855e12v633O+5gMwzAEAAAAAAAa7LqmrgAAAAAAAC0VSTUAAAAAAA4iqQYAAAAAwEEk1QAAAAAAOIikGgAAAAAAB5FUAwAAAADgIJJqAAAAAAAcRFINAAAAAICDSKoBAAAAAHAQSTUc1rVrV40bN65B66SlpclkMunw4cNXpU4Aro1t27bJZDJp27ZttrLk5GSZTKamqxTQxDZu3KjbbrtN7u7uMplMysrKUkJCggYNGqSOHTvKZDIpLS2tqasJAJKkhQsX6q233mrqarQKJNVw2ObNm/XUU081aJ37779fO3fuVJcuXa5SrQAAuPaOHz+u2NhYdevWTRkZGdq5c6dKS0u1bt06ubq66r777mvqKgKAHZLqxuPc1BXAtXH27Fm5u7s36jZ79+7d4HU6d+6szp07N2o9gLbs+++/V7t27Zq6GkCb9+WXX+r8+fN65JFHNGjQIElSZWWljh8/Lknas2eP3njjjaasosOuxncIAE2HNt346KluQapurczNzdWDDz4oT09PWSwWPfLII7YPbenibdkjRozQm2++qd69e8vNzU3z58+XJBUVFWnSpEm64YYb5OrqqpCQEM2fP18XLlyw21dZWZkWLFigsLAwubm5ydvbW0OGDFF2drbdfn54+3dlZaWeeeYZhYaGyt3dXR07dlTPnj31xz/+0RZT2+3fa9as0e233y43Nzd5eXnpgQce0P79++1ixo0bp/bt2+urr77Sfffdp/bt2yswMFAzZ85UWVnZlf55gWav6v+Azz77TD//+c/VqVMndevWTYZhaPny5erVq5fc3d3VqVMn/fznP9d///vfatvIyMjQ0KFDZbFY1K5dO4WFhSklJcW2fM+ePXrooYfUtWtXubu7q2vXrnr44Yf1zTffXMtDBVqUcePG6cc//rEkacyYMTKZTBo8eLCuu+7Kv2Z9+OGHGjx4sLy9veXu7q6goCD97Gc/0/fff2+Lqc9n9rlz55SUlKSQkBC5urrq+uuv15QpU/Tdd9/Z7a8xvkMArcHx48c1ceJEBQYGymw2q3PnzhowYIA++OADSbU/Bjl48GANHjzYNl/1uFR6eroSExPl7+8vd3d3DRo0SLm5uXbrVn3X/eKLLzR06FB5eHioc+fOmjp1ql2bl668TZtMJp05c0avvvqqTCaT7f8tOIae6hbogQce0OjRozV58mR98cUXeuqpp7Rv3z7t3r1bLi4ukqTPPvtM+/fv15NPPqmQkBB5eHioqKhId955p6677jo9/fTT6tatm3bu3KlnnnlGhw8f1tq1ayVJFy5cUHR0tHbs2KGEhATdfffdunDhgnbt2qX8/Hz179+/xno9//zzSk5O1pNPPqm77rpL58+f13/+859qjftSKSkpeuKJJ/Twww8rJSVFJ0+eVHJysiIjI/Xpp5+qe/futtjz589r1KhRiouL08yZM7V9+3b97ne/k8Vi0dNPP904f2CgmXvwwQf10EMPafLkyTpz5owmTZqktLQ0TZ8+Xc8995y+/fZbLViwQP3799fnn38uPz8/SdLq1as1YcIEDRo0SC+99JJ8fX315Zdfau/evbZtHz58WKGhoXrooYfk5eWlwsJCrVixQnfccYf27dsnHx+fpjpsoNl66qmndOedd2rKlClauHChhgwZIk9Pzyve7uHDh3X//fdr4MCBWrNmjTp27KijR48qIyND5eXlateuXb0+sw3D0E9/+lP94x//UFJSkgYOHKh//etfmjdvnnbu3KmdO3fKbDbb9nsl3yGA1iI2NlafffaZnn32Wd1888367rvv9Nlnn+nkyZMObe+JJ57Qj370I73yyiuyWq1KTk7W4MGDlZubqxtvvNEWd/78ed13332aNGmS5syZo+zsbD3zzDP65ptv9M4770hSo7Tpn/70p7r77rs1ZMgQ2+OcjfH/VptloMWYN2+eIcmYMWOGXfm6desMSUZ6erphGIYRHBxsODk5GQcOHLCLmzRpktG+fXvjm2++sStftGiRIcn44osvDMMwjNdee82QZLz88st11ic4ONh49NFHbfMjRowwevXqVec6a9euNSQZhw4dMgzDMEpK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NUmyfX+u647PoqIiubq6qlOnTnXG1NQ55evrW+edo3RaAVdPg5JqV1dXRUREKDMz0648MzNT/fv3r3W9N954Q+PGjdP69et1//33X3Y/ZrNZnp6edhMAAADQXFVWVupHP/qRFi5cqNtvv12S9Oijj1YbzNeROz4vjakp/nLbodMKuHoafPt3YmKiXnnlFa1Zs0b79+/XjBkzlJ+fr8mTJ0u62GDHjh1ri3/jjTc0duxYLV68WP369VNRUZGKiopktVob7ygAAACAJtSlSxfdeuutdmU333yz7bWz/v7+klTnHZ/+/v4qLy9XSUlJnTHHjh2rtv/jx4/XeeconVbA1dPgpHrMmDFKTU3VggUL1KtXL23fvl1btmxRcHCwJKmwsNDundUrV67UhQsXNGXKFHXp0sU2/eY3v2m8owAAoI1avny5QkJC5ObmpoiICO3YsaPW2DfffFPDhg1T586d5enpqcjISL3//vvXsLZA6zVgwAAdOHDAruzrr7+2fUcOCQmRv7+/3R2f5eXl+vjjj213fEZERMjFxcUuprCwUHv37rXFREZGymq16pNPPrHF7N69W1artc47RwFcPQ0a/btKfHy84uPja1z2wwEZJGnbtm2O7AIAAFzGxo0blZCQoOXLl2vAgAFauXKloqOjtW/fPgUFBVWL3759u4YNG6aFCxeqY8eOWrt2rUaOHKndu3erd+/eTXAEQOsxY8YM9e/fXwsXLlR0dLSki9+LV61aJeniLdsJCQlauHChunfvru7du2vhwoVq166dYmJiJEkWi0VxcXGaOXOmvL295eXlpVmzZqlHjx62MYnCwsJ07733asKECVq5cqUkaeLEiRoxYgQjfwNNxKGkGgAANL0lS5YoLi5O48ePlySlpqbq/fff14oVK5SSklItPjU11W5+4cKF+tvf/qZ33nmHpBq4QnfccYc2b96spKQkLViwQNLFwcF++ctf2mJmz56ts2fPKj4+XiUlJerbt6+2bt2qDh062GJeeOEFOTs7a/To0Tp79qyGDh2qtLQ0OTk52WLWrVun6dOn20YJHzVqlJYtW3aNjhTApUiqAQBogcrLy5WTk6M5c+bYlUdFRdX5Wp0fqqys1KlTp+Tl5VVrTFlZmcrKymzzvIYHqN2IESM0YsQIlZaWymKxaNy4cXbLTSaTkpOTlZycXOs23NzctHTpUi1d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C9q9e7et7OTJk/ryyy8VFhZ2ratZq9Z2PqrceuutMpvNys/P10033WQ3BQYG2uI6d+6scePGKT09XampqVq1alWT1bmlaW3XDm35ouZyPqrQlq+u1nbdtPR2LLW+c1KFtnx1tbbrpqW35dZ2Pqo093bcppJqSVq+fLkqKip05513atOmTTp48KD279+vP/3pT4qMjKzXNvr27at27drpiSee0FdffaX169crLS3t6la8Fs8++6w+/PBDHThwwFbWvXt3/eQnP9GECROUlZWlzz//XI888oiuv/56/eQnP2mSetamtZ0PSerQoYNmzZqlGTNm6NVXX9XXX3+t3Nxcvfjii3r11VclSU8//bT+9re/6auvvtIXX3yhd999t1n9h9wStLZrh7bcvM6HRFu+FlrbddPS27HU+s6JRFu+FlrbddPS23JrOx9S82/HbS6pDgkJ0WeffaYhQ4Zo5syZCg8P17Bhw/SPf/xDK1asqNc2vLy8lJ6eri1btqhHjx564403muzF8DfffLMee+wxnTt3zq587dq1ioiI0IgRIxQZGSnDMLRly5Zqt2I0tdZ2Pqr87ne/09NPP62UlBSFhYVp+PDheueddxQSEiJJcnV1VVJSknr27Km77rpLTk5O2rBhQ5PWuaVpbdcObbl5nY8qtOWrq7VdNy29HUut75xUoS1fXa3tumnpbbm1nY8qzbkdm4zaHhAAAAAAAAB1anM91QAAAAAANBaS6mZk8uTJdkPE/3CaPHlyU1evzeF8wFFcO80L5wOO4LppfjgncATXTfPSWs8Ht383I8XFxSotLa1xmaenp3x9fa9xjdo2zgccxbXTvHA+4Aium+aHcwJHcN00L631fJBUAwAAAADgIG7/BgAAAADAQSTVAAAAAAA4iKQaAAAAAAAHkVQDAAAAAOAgkmoAAAAAABxEUg0AAAAAgINIqgEAAAAAcBBJNQAAAAAADvp/9qNXP4nYtU8AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 1200x400 with 4 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# calculate the classification report\n",
    "report = classification_report(Y_test, predLR, target_names=['Churn_No', 'Churn_Yes'])\n",
    "\n",
    "# split the report into lines\n",
    "lines = report.split('\\n')\n",
    "\n",
    "# split each line into parts\n",
    "parts = [line.split() for line in lines[2:-5]]\n",
    "\n",
    "# extract the metrics for each class\n",
    "class_metrics = dict()\n",
    "for part in parts:\n",
    "    class_metrics[part[0]] = {'precision': float(part[1]), 'recall': float(part[2]), 'f1-score': float(part[3]), 'support': int(part[4])}\n",
    "\n",
    "# create a bar chart for each metric\n",
    "fig, ax = plt.subplots(1, 4, figsize=(12, 4))\n",
    "metrics = ['precision', 'recall', 'f1-score', 'support']\n",
    "for i, metric in enumerate(metrics):\n",
    "    ax[i].bar(class_metrics.keys(), [class_metrics[key][metric] for key in class_metrics.keys()])\n",
    "    ax[i].set_title(metric)\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "cac5cc34-eab2-4623-bbe6-717b0307b43b",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "confusion_matrix_LR = confusion_matrix(Y_test, predLR)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "77a8cc94-1567-49de-9ed6-b198c68a133c",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "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wPWcPsLftm2bdu7c6bj/6aefqnv37ho2bJhycnJcWhwAAHANpwP/kUceUVJSkiTp4MGDuvfee+Xr66uPP/5YQ4cOdXmBAADg6jkd+ElJSYqNjZUkffzxx2rZsqUWLlyo+fPna/Hixa6uDwAAuIDTgW8Yhux2u6T8t+VdeO99ZGSkUlJSXFsdAABwCacDv1GjRho/frwWLFigb775Rp07d5aU/4E85cuXd3mBAADg6jkd+K+88oq2bdumAQMGaPjw4YqKipIkffLJJ7rllltcXiAAALh6Tr8tr27dugVm6V/w4osvys3NzSVFAQAA13I68C/H29vbVUMBAAAXczrwbTabpk+frkWLFuno0aOF3nt/+vRplxUHAABcw+lr+GPGjNHLL7+snj17KjU1VYMGDdLdd98tq9Wq0aNHl0CJAADgajkd+O+//77mzJmjZ555Ru7u7urVq5feeustjRw5Ups3by6JGgEAwFVyOvCPHz+uOnXqSJL8/f2VmpoqSbrzzjv1+eefu7Y6AADgEk4HfkREhJKTkyVJUVFRWr16tSTpxx9/lJeXl2urAwAALuF04N91111au3atJGngwIEaMWKEatSooT59+qhv374uLxAAAFw9p2fpT5482fHzPffco4iICG3cuFFRUVHq2rWrS4sDAACucdXvw2/atKmaNm3qiloAAEAJKVbgL1++vNgDcpQPAMD1p1iB371792INZrFYZLPZrqYeAABQAooV+Be+DhcAAPw9OT1LHwAA/P0UO/C//vprxcTEKC0trVBbamqqateurW+//dalxQEAANcoduC/8sor6tevnwIDAwu1BQUF6ZFHHtH06dNdWhwAAHCNYgf+jh071LFjx8u2t2/fXvHx8S4pCgAAuFaxA//333+Xh4fHZdvd3d118uRJlxQFAABcq9iBX6lSJe3cufOy7T/99JPCw8NdUhQAAHCtYgd+p06dNHLkSGVlZRVqy8zM1KhRo3TnnXe6tDgAAOAaxf5o3RdeeEFLlixRdHS0BgwYoJo1a8pisSgxMVGvv/66bDabhg8fXpK1AgCAv6jYgV++fHlt3LhRjz32mJ5//nkZhiEp/9P1OnTooFmzZql8+fIlVigAAPjrnPrynCpVquiLL77QmTNntH//fhmGoRo1aqhMmTIlVR8AAHCBv/RteWXKlNHNN9/s6loAAEAJ4aN1AQAwAQIfAAATIPABADABAh8AABMo1qS95cuXF3vArl27/uVicO0dyj0n/1xe9+Gfy5ZyqrRLAEqUzcgtVr9iBX737t2LNZjFYpHNZitWXwAAcO0UK/DtdntJ1wEAAEoQ53IBADCBv/TBOxkZGfrmm2909OhR5eTkFGh78sknXVIYAABwHacDf/v27erUqZPOnz+vjIwMhYSEKCUlRb6+vipXrhyBDwDAdcjpU/pPP/20unTpotOnT8vHx0ebN2/WkSNH1LBhQ7300kslUSMAALhKTgd+QkKCBg8eLDc3N7m5uSk7O1uRkZGaOnWqhg0bVhI1AgCAq+R04Ht4eMhisUjK/8rco0ePSpKCgoIcPwMAgOuL09fw69evr61btyo6Olpt2rTRyJEjlZKSogULFqhOnTolUSMAALhKTh/hT5w4UeHh4ZKkcePGqWzZsnrsscd04sQJ/fe//3V5gQAA4Oo5fYTfqFEjx89hYWH64osvXFoQAABwPT54BwAAE3D6CL9atWqOSXtFOXjw4FUVBAAAXM/pwH/qqacK3M/NzdX27du1cuVKDRkyxFV1AQAAF3I68AcOHFjk8tdff11bt2696oIAAIDruewa/h133KHFixe7ajgAAOBCLgv8Tz75RCEhIa4aDgAAuNBf+uCdiyftGYah48eP6+TJk5o1a5ZLiwMAAK7hdOB369atQOBbrVaFhYWpdevWqlWrlkuLAwAAruF04I8ePboEygAAACXJ6Wv4bm5uOnHiRKHlp06dkpubm0uKAgAAruV04BuGUeTy7OxseXp6XnVBAADA9Yp9Sn/GjBmSJIvForfeekv+/v6ONpvNpm+//ZZr+AAAXKeKHfjTp0+XlH+E/+abbxY4fe/p6amqVavqzTffdH2FAADgqhU78A8dOiRJatOmjZYsWaIyZcqUWFEAAMC1nJ6lv27dupKoAwAAlCCnJ+3dc889mjx5cqHlL774onr06OGSogAAgGs5HfjffPONOnfuXGh5x44d9e2337qkKAAA4FpOB/65c+eKfPudh4eH0tLSXFIUAABwLacD/6abbtJHH31UaPmHH36omJgYlxQFAABcy+lJeyNGjND//d//6cCBA2rbtq0kae3atfrggw/08ccfu7xAAABw9ZwO/K5du2rZsmWaOHGiPvnkE/n4+Khu3bpas2aNWrVqVRI1AgCAq+R0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ev7557Vx40bddNNNWrhwoaMtOjpaTz/9tFavXq27775b8+bNu2KtwOUQ+ACuWrt27dSsWTN1795dq1at0uHDh7Vx40a98MILjlnlAwcO1Ny5czV37lwlJSVp1KhR2r1792XH9Pb21rPPPquhQ4fq3Xff1YEDB7R582a9/fbbkqRy5crJx8dHK1eu1O+//67U1FRJ+UfFkyZN0quvvqqkpCTt3LlT8+bN08svvyxJuu+++2S1WvXQQw9pz549+uKLL/TSSy9dcfssFovmzZunpKQktWzZUl988YUOHjyon376SRMmTFC3bt2KfFxUVJS2bt2qVatWKSkpSSNGjNCPP/7oaD906JCef/55bdq0SUeOHNHq1auVlJSkG2+8UZmZmRowYIDWr1+vI0eOaMOGDfrxxx914403Fv8/BrhYaU8iAHB9uXTS3qVGjRpVYKLdBWlpacZ//vMfo2LFioaHh4cRGRlp9O7d2zh69Kijz4QJE4zQ0FDD39/feOCBB4yhQ4dedtKeYRiGzWYzxo8fb1SpUsXw8PAwKleubEycONHRPmfOHCMyMtKwWq1Gq1atHMvff/99IzY21vD09DTKlCljtGzZ0liyZImjfdOmTUa9evUMT09PIzY21li8ePGfTrYzDMPYu3ev0adPH6NixYqGp6enUaVKFaNXr16OyXyXTtrLysoy4uLijKCgICM4ONh47LHHjOeee86xzcePHze6d+9uhIeHO8YbOXKkYbPZjOzsbOPee+81IiMjDU9PT6NixYrGgAEDjMzMzCvWCFwOX48LAIAJcEofAAATIPABADABAh8AABMg8AEAMAECHwAAEyDwAQAwAQIfAAATIPABADABAh8AABMg8AEAMAECHwAAEyDwAQAwgf8HNe3j6a2uQ1oAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 480x480 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# create a heatmap of the matrix using matshow()\n",
    "\n",
    "plt.matshow(confusion_matrix(Y_test, predLR))\n",
    "\n",
    "# add labels for the x and y axes\n",
    "plt.xlabel('Predicted Class')\n",
    "plt.ylabel('Actual Class')\n",
    "\n",
    "for i in range(2):\n",
    "    for j in range(2):\n",
    "        plt.text(j, i, confusion_matrix_LR[i, j], ha='center', va='center')\n",
    "\n",
    "\n",
    "# Add custom labels for x and y ticks\n",
    "plt.xticks([0, 1], [\"Not Churned\", \"Churned\"])\n",
    "plt.yticks([0, 1], [\"Not Churned\", \"Churned\"])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "6324fb87-dd75-4638-9343-c71dbba964e0",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5036714285714285"
      ]
     },
     "execution_count": 68,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "logmodel.score(X_train, Y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 69,
   "id": "7ea893b1-406b-488c-9b12-d1dba90ddf50",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4999"
      ]
     },
     "execution_count": 69,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "accuracy_score(Y_test, predLR)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "b95221e6-01cb-44e0-a2b1-d2e685cb7f61",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 1, 0, ..., 0, 0, 1], dtype=int64)"
      ]
     },
     "execution_count": 79,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pickle \n",
    "  \n",
    "# Save the trained model as a pickle string. \n",
    "  \n",
    "predLR = pickle.dumps(LogisticRegression) \n",
    "  \n",
    "predLR = logmodel.predict(X_test)\n",
    "predLR"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "id": "3e885287-4e6b-47fb-950b-505416906eed",
   "metadata": {
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['customer_churn_large_dataset.csv.pkl']"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import joblib\n",
    "filename = 'customer_churn_large_dataset.csv.pkl'\n",
    "joblib.dump(LogisticRegression, filename)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4dc940e-e9c5-42c2-9700-72fbab43e896",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9ad12c8-c106-4956-9610-b0957f7d59bf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2543c125-231a-4f67-9e32-0ab0e52fc06c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3db7a1fe-0fa6-412f-b59e-d0e3b4abb66a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0b12107-8619-456f-9c5b-c4993c3b3892",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "096fa913-df85-4db1-9b73-ff17b506c0a9",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.11.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}