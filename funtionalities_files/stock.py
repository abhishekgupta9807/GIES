import pandas as pd



def updateStock():
    import_data=pd.read_csv('import.csv')

    item_list=pd.Series(import_data['ITEM NAME']).unique()


    import_stock=[]

    for x in item_list:
        row=[]
        item=import_data[import_data['ITEM NAME']==x]
        avg_price=item['ITEMPRICE'].mean()
        item_weight=item['ITEM WEIGHT'].sum()
        item=str(x)
        row.append(item)
        row.append(item_weight)
        row.append(avg_price)
        import_stock.append(row)

    import_dataframe=pd.DataFrame(import_stock,columns=['ITEM NAME','IMPORT WEIGHT','AVG IMPORT PRICE'])

    export_data=pd.read_csv('export.csv')

    item_list=pd.Series(export_data['ITEM NAME']).unique()

    export_stock=[]

    for x in item_list:
        row=[]
        item=export_data[export_data['ITEM NAME']==x]
        avg_price=item['ITEM PRICE'].mean()
        item_weight=item['ITEM WEIGHT'].sum()
        item=str(x)
        row.append(item)
        row.append(item_weight)
        row.append(avg_price)
        export_stock.append(row)

    export_dataframe=pd.DataFrame(export_stock,columns=['ITEM NAME','EXPORT WEIGHT','AVG EXPORT PRICE'])

    stock=pd.merge(import_dataframe,export_dataframe,on='ITEM NAME')

    stock['STOCK']=stock['IMPORT WEIGHT']-stock['EXPORT WEIGHT']

    stock['profit']=stock['EXPORT WEIGHT']*stock['AVG EXPORT PRICE']-stock['EXPORT WEIGHT']*stock['AVG IMPORT PRICE']

    stock.to_csv('stock.csv',sep='\t')


