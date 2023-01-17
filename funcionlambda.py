import json
import os
import mercadopago

# importar las librerias necesarias

def lambda_handler(event, context):
    sdk = mercadopago.SDK(os.environ["ACCESS_TOKEN"])
    # obteniendo el ACCESS_TOKEN de las variables de entorno
    
    bodyGet = json.loads(event["body"])
    # analizando el evento para obtener los datos del pago en formato JSON y convertirlo en un objeto Python
    
    payment_data = {
        "token": bodyGet["token"],
        "installments": int(bodyGet["installments"]),
        "payment_method_id": bodyGet["payment_method_id"],
        "transaction_amount": int(bodyGet["transaction_amount"]),
        "payer": {
            "email": bodyGet["payer"]["email"],
            "identification": {
                "type": bodyGet["payer"]["identification"]["type"], 
                "number": bodyGet["payer"]["identification"]["number"]
            }
        }
    }
    # Crear un diccionario con los datos del pago, incluyendo detalles del comprador
    
    payment_response = sdk.payment().create(payment_data)
    return{
        "statusCode": 201,
        # 201 es el status code para un recurso creado exitosamente
        "body": json.dumps(
            payment_response["response"]
        ),
    }
    # Utilizar SDK para crear el pago y devolver la respuesta con un status code 201
