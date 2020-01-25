list_of_modules = []
module_fuel_requirements = {}
fuel_required = 0
fuel_required_pre  = 0
fuel_required_module = 0
fuel_required_post  = 0
list_fuel_required_per_module = []

class fuel_measurer:

    def fuelRequiredinTotal(self):
        global fuel_required
        fileinput = open('day1_input.txt', 'r')
        fuel_modules = fileinput.readlines()
        for module in fuel_modules:
            list_fuel_required_per_module.append(self.fuelRequiredPerModule(module))
        for modules in list_fuel_required_per_module:
            fuel_required += modules
        print(fuel_required)

    def fuelRequiredPerModule(self, s):
        global fuel_required_pre
        global fuel_required_post
        global fuel_required_module
        if (int(s) // 3 - 2) > 0:
            fuel_required_pre = (int(s) // 3 - 2)
            fuel_required_post += (int(s) // 3 - 2)
            return self.fuelRequiredPerModule(fuel_required_pre)
        else:
            return fuel_required_post

fuel_measurer().fuelRequiredinTotal()