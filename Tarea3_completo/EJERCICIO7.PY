class Ejercicio7:
    import requests
    from datetime import datetime
    now = datetime.now()
    url = 'https://api.apis.net.pe/v1/tipo-cambio-sunat' 

    response = requests.get(url)

    response.json() 
    dolar=response.json()
    dolar_compra = dolar['compra']
    dolar_venta = dolar['venta']

    print("Precio compra del dolar :",dolar_compra)
    print("Precio venta del dolar  :",dolar_venta)
    print("Fecha                   :", now)