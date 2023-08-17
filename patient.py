#Prepared by: Kunwar Thakur
#Class#3: Patient

class Patient:
    def __init__(self,pFileName):
        self.pFileName=pFileName

    def formatPatientInfo(self):
        self.NewValue=self.NewPatientID+"_"+self.NewPatientName+"_"+self.NewPatientDisease+"_"+self.NewPatientGender+"_"+self.NewPatientAge

    def enterPatientInfo(self):
        self.NewPatientID = input("Enter Patient id:\n")
        self.NewPatientName = input("Enter Patient Name: \n")
        self.NewPatientDisease = input("Enter Patient disease: \n")
        self.NewPatientGender = input("Enter Patient Gender: \n")
        self.NewPatientAge = input("Enter Patient age: \n")

    def readPatientsFile(self):
        self.myPatients= open(self.pFileName,'r')
        
    def searchPatientById(self,pPatientID):
        new=[]
        print("ID".ljust(5),"Name".ljust(10),"Disease".ljust(10),"Gender".ljust(10),"Age".ljust(15))
        v_Found=False
        for line in self.myPatients:
            new = line.split("_")
            if new[0]==pPatientID:
                self.displayPatientInfo(new)
                v_Found=True
                break
        if v_Found==False:
            print("Can't find the Patient with the same id on the system\n")  

    def displayPatientInfo(self,pInfo):
        print(pInfo[0].ljust(5),pInfo[1].ljust(10),pInfo[2].ljust(10),pInfo[3].ljust(10),pInfo[4].ljust(10))