class ProjectorScreen:
    warrantyPeriodInMonths = 12

    def __init__(self, heightInCentimetrs=180, widthInCentimetrs=300, mountType="floor-rising", producer="Sopar",
                 weightInKilograms=15, screenMaterial="Snow White", viewingAngleInDegrees=160,
                 countryManufacturer="China", resolution="4K"):
        self.heightInCentimetrs = heightInCentimetrs
        self.widthInCentimetrs = widthInCentimetrs
        self.mountType = mountType
        self.producer = producer
        self.weightInKilograms = weightInKilograms
        self.screenMaterial = screenMaterial
        self.viewingAngleInDegrees = viewingAngleInDegrees
        self.countryManufacturer = countryManufacturer
        self.resolution = resolution

    def __del__(self):
        print("Object deleted")

    def __str__(self):
        return "ProjectorScreen [heightInCentimetrs = " + str(self.heightInCentimetrs) + ", widthInCentimetrs = " \
               + str(self.widthInCentimetrs) + ", mountType = " + self.mountType + ", producer = " + self.producer \
               + ", weightInKilograms = " + str(self.weightInKilograms) + ", screenMaterial = " + self.screenMaterial \
               + ", viewingAngleInDegrees = " + str(self.viewingAngleInDegrees) + ", countryManufacturer = "\
               + self.countryManufacturer + ", resolution = " + self.resolution + "]"

    @staticmethod
    def getWarrantyPeriodInMonths():
        return ProjectorScreen.warrantyPeriodInMonths


def main():
    cinemaScreen = ProjectorScreen(heightInCentimetrs=400, widthInCentimetrs=800, resolution="8K")
    print(cinemaScreen)
    officeScreen = ProjectorScreen(heightInCentimetrs=180, widthInCentimetrs=180, mountType="tripod stand",
                                   countryManufacturer="USA")
    print(officeScreen)
    homeScreen = ProjectorScreen(producer="Logan", screenMaterial="Matte White")
    print(homeScreen)


if __name__ == '__main__':
    main()
