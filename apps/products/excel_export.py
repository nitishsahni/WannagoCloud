import sqlite3

import pandas as pd

cnx = sqlite3.connect('../../db.sqlite3')


def riserva():
    df_to_export = pd.read_excel('WGC Pricing(1).xlsx', sheet_name='Data', usecols='A:E', skiprows=5)
    df_to_export['Per Month'] = round(df_to_export['Per Month'], 0).astype(int)
    df_to_export = df_to_export.rename(columns={ 'Riserva': 'name',
                                                 'Qty': 'quantity',
                                                 'Price in $': 'price_dollars',
                                                 'in AED': 'price_aed',
                                                 'Per Month': 'per_month' })
    print(df_to_export)
    df_to_export.to_sql(name='products_riserva', con=cnx, if_exists='append', index=False)
    print("Done")


def draas():
    df_to_export = pd.read_excel('WGC Pricing(1).xlsx', sheet_name='Data', usecols='I:K', nrows=5)
    df_to_export = df_to_export.rename(columns={ 'DRaaS': 'name',
                                                 'SP.1': 'selling_price',
                                                 'CP': 'cost_price' })
    df_to_export['cost_price'] = 0
    print(df_to_export)
    df_to_export.to_sql(name='products_draas', con=cnx, if_exists='append', index=False)
    print("Done")


def iaas():
    df_to_export = pd.read_excel('WGC Pricing(1).xlsx', sheet_name='Data', usecols='I:K', nrows=6, skiprows=21)
    df_to_export = df_to_export.rename(columns={ 'Unnamed: 8': 'name',
                                                 'SP': 'selling_price',
                                                 'CP': 'cost_price' })
    print(df_to_export)
    df_to_export.to_sql(name='products_iaas', con=cnx, if_exists='append', index=False)
    print("Done")


def subscriptions():
    df_to_export = pd.read_excel('WGC Pricing(1).xlsx', sheet_name='Data', usecols='A:B', nrows=2)
    df_to_export = df_to_export.rename(columns={ 'Subscriptions': 'name',
                                                 'SP': 'selling_price'})
    print(df_to_export)
    df_to_export.to_sql(name='products_subscriptions', con=cnx, if_exists='append', index=False)
    print("Done")


def hello():
    print("Sup")


if __name__ == '__main__':
    hello()

