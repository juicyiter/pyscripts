class VendingMachine:
    '''
    Base class
    '''

    def __init__(self):
        # track the money collected by the machine
        self.income = 0

    def dispense(self, product_code, money):
        '''
        Dispense the specified product identified by the product_code
        '''
        raise NotImplementedError('dispense() must be implemented.')


# class SnackAndDrinkVendingMachine(VendingMachine):
#     '''
#     Not proxyed class
#     '''

#     def dispense(self, product_code, money):
#         if product_code.startswith('snack'):
#             return SnackVendingMachine().dispense(product_code, money)
#         elif product_code.startswith('drink'):
#             return DrinkVendingMachine().dispense(product_code, money)

class ProxiedCall:
    def __init__(self, proxy, method_name):
        self.proxy = proxy
        self.method_name = method_name

    def __call__(self, *args, **kwargs):
        try:
            product_code = args[0]
        except IndexError:
            product_code = None

        # get the product machine
        machine = self._get_machine(product_code)

        # Look up the method and call it
        return getattr(machine, self.method_name)(*args, **kwargs)

    def _get_machine(self, product_code):
        for machine, prefix in self.proxy.machines:
            if product_code and product_code.startswith(prefix):
                return machine

        # If we don't have a product_code to go off of, default to the
        # last machine in the list on the proxy.
        return machine


class ProxyedVendingMachine:
    """
    Vending machine class which proxies to SnackVendingMachine and
    DrinkVendingMachine, defaulting to DrinkVendingMachine.
    """

    def __init__(self):
        # Existing machines
        snack_machine = SnackVendingMachine()
        drink_machine = DrinkVendingMachine()

        self.machines = [
            (snack_machine, 'snack'),
            (drink_machine, 'drink'),
        ]

    def __getattr__(self, name):
        # For each vending machine, check if the requested attribute
        # is defined. If the attr is defined on both, we take the one
        # defined for DrinkVendingMachine.
        for machine, __ in self.machines:
            try:
                attr = getattr(machine, name)
            except AttributeError:
                pass

        # The value defined for the attribute in the machines may be
        # None, which prevents us from defaulting `attr` to None.
        try:
            attr
        except NameError:
            # The attribute wasn't found on either machine.
            raise AttributeError
        else:
            # The attribute was found. If it's callable, return a
            # ProxiedCall which will route method calls to the
            # correct machine.
            if callable(attr):
                return ProxiedCall(self, name)
            else:
                return attr
