import logging

import asyncio

import azure.functions as func

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
import json 



async def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    firstString = '{"a": 1, "b": 2, "c": 3, "d": 4}'
    jsonData = json.loads(firstString) 

    producer = EventHubProducerClient.from_connection_string(conn_str="{EventHubConnectionString}", eventhub_name="{EventHubName}")
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(jsonData))


        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)
 


    return func.HttpResponse("Hello World")
 
