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
        json_item = {'name': self.name, 'unit_price': self.unit_price, 'quantity': self.quantity}
        if self.description != "":
            json_item['description'] = self.description
        if self.sku != "":
            json_item['sku'] = self.sku
        if self.type != "":
            json_item['type'] = self.type
        if self.category != "":
            json_item['category'] = self.category
        if self.tags:
            json_item['tags'] = self.tags
        return json_item


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
        for item in self.__items:
            json_data.append(item.to_json())  # adding item as json.
        return json_data
