# Junction Hackathon 2022

## Enhanced Wolt Api Endpoints
### Get order fee
- Route 'order fee' endpoint from Wolt Api

### Place order
- Route 'place order' endpoint from Wolt Api

### Get additional delivery opportunity for existing delivery
- Provide order_id
- return merchant and article for additional delivery



## Frontend workflow
Show delivery options
request api for delivery fee for chosen delivery
place order for this delivery on api
request api, if additional delivery for existing route is available
    offer this additional delivery
        place delivery order
offer the driver to take something with him
    ask destination address
    request api for delivery fee for this address
    show delivery fee, reduced.
    place delivery order
