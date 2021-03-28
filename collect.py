### import dependancies ###

### declare globals ###

### define functions ###

### main logic ###

# query to get list of items
# declare result as empty dict
# for each in items
  # query to get orders for that item
  # narrow to payload.orders
  # select platinum where platform  = "PC" and order_type = "buy"
  # get mode
  # add {each.url_name: mode} to result
# return result
