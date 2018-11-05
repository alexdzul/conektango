from conektango.errors import ConektangoError


class LineItem:
    """
    Store temporarely an order line item
    """

    def __init__(self):
        self.name = ""
        self.description = ""
        self.unit_price = 0
        self.quantity = 1
        self.sku = ""
        self.category = ""
        self.type = ""
        self.tags = []  # Strings

    def to_json(self):
        """
        Returns the value as JSON
        :return: json object
        """
        json_data = {
            'name': self.name,
            'description': self.description,
            'unit_price': self.unit_price,
            'quantity': self.quantity,
            'sku': self.sku,
            'category': self.category,
            'type': self.type,
            'tags': self.tags
        }
        return json_data


class OrderLineItems:
    """
    Store temporarely the order line items objects.
    """

    def __init__(self):
        self.__items = []

    def add_element(self, **kwargs):
        try:
            item = LineItem()
            item.name = kwargs['name']
            item.description = kwargs['description']
            item.unit_price = int(kwargs['unit_price'])
            item.quantity = int(kwargs['quantity'])
            item.sku = kwargs['sku']
            item.category = kwargs['category']
            item.type = kwargs['type']
            item.tags = kwargs['tags']  # Strings
            self.__items.append(item)
        except Exception as e:
            raise ConektangoError(e)

    def to_json(self):
        """
        Returns the value as JSON
        :return: json object
        """
        json_data = []
        return json_data


