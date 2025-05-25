
from kivymd.uix.screen import MDScreen

class NetworkProvider(MDScreen):
    def econet_next(self):
        econet = "*121*"
        self.manager.set_shared_data("cached_econet_postal_code", econet)
        self.manager.push("econet_dashboard")

    def netone_next(self):
        netone = "*133*"
        self.manager.set_shared_data("cached_netone_postal_code", netone)
        self.manager.push("netone_dashboard")
        


