from underclass import UnderClass

class UberClass:
    def __init__(self):
        """
        Super cool stuff contained within the UberClass.

        Attributes
        ----------

        unc : obj
            Instance of the UnderClass class

        Returns
        -------
        None

        """
        print('This is the uberclass')
        self.unc = UnderClass()
        self.uber_method()

    def uber_method(self):
        """
        The method above all other methods.
        Hence, the uber method.

        Returns
        -------
        None

        """
        print('The uber method')
        self.run()                 

    def run(self):
        """
        The method to end all methods

        Returns
        -------
        None

        """
        running = 'Keep on running'
        self.walk(running)            

    def walk(self, running):
        """
        The mother of all methods

        Parameters
        ----------
        running : str

        Returns
        -------
        None

        """
        print(running)
        print('Slow down and walk')
        self.myout = self.unc.under_class_man()
        print(self.myout)

UberClass()
